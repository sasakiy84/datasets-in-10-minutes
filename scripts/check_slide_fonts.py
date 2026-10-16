#!/usr/bin/env python3
"""Check cover font families and main-title weight before publishing slides."""
import argparse
import posixpath
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

NS = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
REL = '{http://schemas.openxmlformats.org/package/2006/relationships}'
ROOT = Path(__file__).resolve().parents[1]


def linked_part(archive, source, relation_type=None, relation_id=None):
    relpath = posixpath.join(posixpath.dirname(source), '_rels', posixpath.basename(source) + '.rels')
    for rel in ET.fromstring(archive.read(relpath)).findall(REL + 'Relationship'):
        if ((relation_type and rel.get('Type', '').endswith('/' + relation_type))
                or (relation_id and rel.get('Id') == relation_id)):
            return posixpath.normpath(posixpath.join(posixpath.dirname(source), rel.attrib['Target'])).lstrip('/')
    raise ValueError(f'Missing relationship from {source}: {relation_type or relation_id}')


def placeholder(shape):
    node = shape.find('p:nvSpPr/p:nvPr/p:ph', NS)
    return node


def inherited_shape(root, ph):
    if ph is None:
        return None
    for shape in root.findall('.//p:sp', NS):
        candidate = placeholder(shape)
        if candidate is not None and candidate.get('idx', '0') == ph.get('idx', '0'):
            return shape
    return None


def defaults(shape, level):
    if shape is None:
        return []
    return [shape.find('p:txBody/a:p/a:pPr/a:defRPr', NS),
            shape.find(f'p:txBody/a:lstStyle/a:lvl{level + 1}pPr/a:defRPr', NS)]


def check_presentation(path):
    errors, runs = [], []
    with ZipFile(path) as archive:
        presentation = ET.fromstring(archive.read('ppt/presentation.xml'))
        first_id = presentation.find('p:sldIdLst/p:sldId', NS).get('{' + NS['r'] + '}id')
        slide_path = linked_part(archive, 'ppt/presentation.xml', relation_id=first_id)
        layout_path = linked_part(archive, slide_path, 'slideLayout')
        master_path = linked_part(archive, layout_path, 'slideMaster')
        theme_path = linked_part(archive, master_path, 'theme')
        slide, layout, master, theme = [ET.fromstring(archive.read(p)) for p in (slide_path, layout_path, master_path, theme_path)]
        for shape in slide.findall('.//p:sp', NS):
            ph = placeholder(shape)
            layout_shape = inherited_shape(layout, ph)
            master_shape = inherited_shape(master, placeholder(layout_shape) if layout_shape is not None else ph)
            kind = ph.get('type', 'obj') if ph is not None else 'obj'
            style = 'titleStyle' if kind in ('title', 'ctrTitle') else 'bodyStyle' if kind == 'body' else 'otherStyle'
            for paragraph in shape.findall('p:txBody/a:p', NS):
                ppr = paragraph.find('a:pPr', NS)
                level = int(ppr.get('lvl', '0')) if ppr is not None else 0
                for run in paragraph.findall('a:r', NS):
                    text = run.findtext('a:t', '', NS)
                    if not text.strip():
                        continue
                    chain = [run.find('a:rPr', NS), paragraph.find('a:pPr/a:defRPr', NS),
                             *defaults(shape, level), *defaults(layout_shape, level), *defaults(master_shape, level),
                             master.find(f'p:txStyles/p:{style}/a:lvl{level + 1}pPr/a:defRPr', NS),
                             presentation.find(f'p:defaultTextStyle/a:lvl{level + 1}pPr/a:defRPr', NS)]
                    chain = [node for node in chain if node is not None]
                    def value(name, default=None):
                        return next((node.get(name) for node in chain if name in node.attrib), default)
                    for script, expected in [('latin', 'Noto Sans'), ('ea', 'Noto Sans CJK JP')]:
                        font = next((node.find('a:' + script, NS).get('typeface') for node in chain if node.find('a:' + script, NS) is not None), '')
                        if font.startswith('+'):
                            family = 'majorFont' if font.startswith('+mj') else 'minorFont'
                            base = theme.find(f'a:themeElements/a:fontScheme/a:{family}', NS)
                            node = base.find('a:' + script, NS)
                            font = node.get('typeface', '') if node is not None else ''
                            if not font and script == 'ea':
                                font = next((n.get('typeface') for n in base.findall('a:font', NS) if n.get('script') == 'Jpan'), '')
                        if font != expected:
                            errors.append(f'{text!r}: {script}={font!r}, expected {expected!r}')
                    size = int(value('sz', '0'))
                    if not size:
                        errors.append(f'{text!r}: font size cannot be resolved')
                    runs.append((size, value('b', '0') in ('1', 'true'), text))
        if not runs:
            errors.append('Cover contains no editable text')
        else:
            largest = max(size for size, _, _ in runs)
            for size, bold, text in runs:
                if size == largest and not bold:
                    errors.append(f'{text!r}: main cover title must be bold')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='*', type=Path)
    args = parser.parse_args()
    files = args.files or sorted((ROOT / 'slides').glob('*.pptx'))
    if not files:
        parser.error('No PPTX files found')
    failed = False
    for path in files:
        errors = check_presentation(path)
        if errors:
            failed = True
            for error in errors:
                print(f'{path.name}: {error}', file=sys.stderr)
        else:
            print(f'PASS: {path.name} cover fonts and title weight')
    sys.exit(1 if failed else 0)
