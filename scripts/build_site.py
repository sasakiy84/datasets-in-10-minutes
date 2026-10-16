#!/usr/bin/env python3
"""Build a portable GitHub Pages gallery from CSV and the published PDFs."""
import argparse
import csv
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

import fitz
from check_slide_fonts import check_presentation

ROOT = Path(__file__).resolve().parents[1]
MODALITIES = ('画像', '動画', '言語')
TASKS = ('画像分類', '物体認識', '行動認識', '自然言語推論', '質問応答', '言語モデル学習')
SITE_LIMIT = 1_000_000_000
GIT_FILE_LIMIT = 100 * 1024 * 1024


def esc(value):
    return html.escape(str(value), quote=True)


def read_catalog(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        required = {'slug', 'title', 'description', 'modality', 'tasks', 'year', 'pdf', 'pptx'}
        if set(reader.fieldnames or []) != required:
            raise ValueError(f'CSV columns must be {sorted(required)}')
        rows = list(reader)
    if not rows:
        raise ValueError('Catalog must contain at least one dataset')
    seen = set()
    for row in rows:
        slug = row['slug']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in seen:
            raise ValueError(f'Invalid or duplicate slug: {slug}')
        seen.add(slug)
        if not row['title'].strip() or not row['description'].strip():
            raise ValueError(f'Missing title or description: {slug}')
        if row['modality'] not in MODALITIES:
            raise ValueError(f'Unknown modality: {slug}')
        tasks = row['tasks'].split('|')
        if any(task not in TASKS for task in tasks) or len(set(tasks)) != len(tasks):
            raise ValueError(f'Unknown or duplicate task: {slug}')
        if not re.fullmatch(r'(19|20)\d{2}', row['year']):
            raise ValueError(f'Invalid year: {slug}')
        for kind in ('pdf', 'pptx'):
            rel = Path(row[kind])
            source = (ROOT / rel).resolve()
            if rel.is_absolute() or not source.is_relative_to(ROOT / 'slides') or source.suffix != '.' + kind:
                raise ValueError(f'Invalid {kind} path: {slug}')
            if not source.is_file():
                raise ValueError(f'Missing file: {source}')
            if source.stat().st_size >= GIT_FILE_LIMIT:
                raise ValueError(f'{source.name} reaches GitHub’s 100 MiB Git file limit')
        font_errors = check_presentation(ROOT / row['pptx'])
        if font_errors:
            raise ValueError(f'{slug}: cover typography check failed: ' + '; '.join(font_errors))
    return rows


def options(values):
    return ''.join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in values)


def build(output):
    if output.exists() and not (output / '.gallery-build').exists():
        raise ValueError(f'Refusing to overwrite an unmanaged directory: {output}')
    if output == ROOT or ROOT.is_relative_to(output) or output.is_relative_to(ROOT / 'slides'):
        raise ValueError('Output must be a separate build directory')
    rows = sorted(read_catalog(ROOT / 'site/datasets.csv'), key=lambda row: int(row['year']), reverse=True)
    config = json.loads((ROOT / 'site/config.json').read_text())
    domain = config.get('custom_domain', '')
    if domain and not re.fullmatch(r'(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}', domain):
        raise ValueError('custom_domain must be a lowercase hostname, without scheme or path')
    canonical = config.get('canonical_url', '')
    if canonical and (urlparse(canonical).scheme != 'https' or not urlparse(canonical).netloc):
        raise ValueError('canonical_url must be an absolute HTTPS URL')
    if domain and canonical.rstrip('/') != f'https://{domain}':
        raise ValueError('Set canonical_url to https://custom_domain/ when using a custom domain')
    if output.exists():
        shutil.rmtree(output)
    (output / 'thumbnails').mkdir(parents=True)
    (output / 'slides').mkdir()
    (output / '.gallery-build').touch()
    (output / '.nojekyll').touch()
    if domain:
        (output / 'CNAME').write_text(domain + '\n')
    cards = []
    public_rows = []
    for row in rows:
        files = {}
        for kind in ('pdf', 'pptx'):
            src = ROOT / row[kind]
            target = output / 'slides' / src.name
            shutil.copyfile(src, target)
            files[kind] = {'url': f'slides/{src.name}', 'bytes': src.stat().st_size}
        with fitz.open(ROOT / row['pdf']) as doc:
            if not len(doc) or doc.is_encrypted:
                raise ValueError(f'Unreadable PDF: {row["slug"]}')
            page = doc[0]
            page.get_pixmap(matrix=fitz.Matrix(960 / page.rect.width, 960 / page.rect.width), alpha=False).save(output / 'thumbnails' / f'{row["slug"]}.png')
            pages = len(doc)
        tasks = row['tasks'].split('|')
        tags = ''.join(f'<span class="tag">{esc(t)}</span>' for t in [row['modality'], *tasks, row['year'] + '年'])
        pdf = esc(files['pdf']['url'])
        cards.append(f'''<a class="card" href="{pdf}" aria-labelledby="title-{row['slug']}" data-modality="{esc(row['modality'])}" data-tasks="{esc(row['tasks'])}" data-year="{row['year']}">
<div class="cover"><img src="thumbnails/{row['slug']}.png" alt="" width="960" height="540" loading="lazy"></div>
<div class="card-body"><h2 id="title-{row['slug']}">{esc(row['title'])}</h2><div class="tags">{tags}</div></div></a>''')
        public_rows.append({**row, 'tasks': tasks, 'pages': pages, 'files': files, 'thumbnail': f'thumbnails/{row["slug"]}.png'})
    canon_meta = ''
    if canonical:
        canon_meta = f'<link rel="canonical" href="{esc(canonical)}"><meta property="og:url" content="{esc(canonical)}">'
    structured = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': config['title'], 'description': config['description'], 'inLanguage': 'ja', 'author': {'@type': 'Person', 'name': config['author']}, 'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(rows), 'itemListElement': [{'@type': 'ListItem', 'position': i, 'item': {'@type': 'CreativeWork', 'name': r['title'], 'description': r['description'], 'keywords': [r['modality'], *r['tasks'].split('|')], 'encodingFormat': 'application/pdf', **({'url': canonical.rstrip('/') + '/' + r['pdf']} if canonical else {})}} for i, r in enumerate(rows, 1)]}}
    markup = f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(config['title'])} | データセットを知るスライド集</title><meta name="description" content="{esc(config['description'])}"><meta name="author" content="{esc(config['author'])}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(config['title'])}"><meta property="og:description" content="{esc(config['description'])}"><meta property="og:locale" content="ja_JP">{canon_meta}
<link rel="stylesheet" href="assets/style.css"><script src="assets/gallery.js" defer></script>
<script type="application/ld+json">{json.dumps(structured, ensure_ascii=False).replace('<', '\\u003c')}</script></head>
<body><a class="skip" href="#gallery">スライド一覧へ</a>
<main><section class="intro"><h1>{esc(config['title'])}</h1><p class="note">LLMで生成した資料であり、内容は保証していません。</p><p class="note">公開年はデータセットの初公開年です。ImageNet-1kなどの派生版や改訂版の公開年とは異なる場合があります。</p></section>
<section aria-label="スライド一覧"><div class="gallery-tools"><p id="result-count" role="status" aria-live="polite"><strong>{len(rows)}</strong> datasets</p><div class="filters" hidden><label class="title-search">タイトル検索<input id="title-search" type="search" placeholder="データセット名" autocomplete="off" spellcheck="false"></label><label>データの種類<select id="modality"><option value="">すべて</option>{options(MODALITIES)}</select></label><label>タスク<select id="task"><option value="">すべて</option>{options(TASKS)}</select></label><label>データセット公開年<select id="year"><option value="">すべて</option>{options(sorted({r['year'] for r in rows}, reverse=True))}</select></label><label>並び順<select id="sort-order"><option value="year-desc">公開年：新しい順</option><option value="year-asc">公開年：古い順</option></select></label><button id="reset" type="button">リセット</button></div></div>
<div id="gallery" class="gallery">{''.join(cards)}</div><p id="empty" hidden>該当する資料がありません。条件を変えてお試しください。</p></section>
</main>
<footer><span>{esc(config['title'])} / {esc(config['author'])}</span></footer></body></html>'''
    (output / 'index.html').write_text(markup, encoding='utf-8')
    shutil.copytree(ROOT / 'site/assets', output / 'assets')
    shutil.copyfile(ROOT / 'site/datasets.csv', output / 'datasets.csv')
    (output / 'catalog.json').write_text(json.dumps(public_rows, ensure_ascii=False, indent=2) + '\n')
    size = sum(p.stat().st_size for p in output.rglob('*') if p.is_file())
    if size >= SITE_LIMIT:
        raise ValueError(f'Site is {size} bytes; GitHub Pages limit is {SITE_LIMIT}')
    print(f'Built {len(rows)} datasets, {size:,} bytes ({size/1024/1024:.2f} MiB), {size/SITE_LIMIT:.1%} of Pages 1 GB limit → {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    args = parser.parse_args()
    build(args.output.resolve())
