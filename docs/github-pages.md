# スライドギャラリーの公開と更新

## 現在の容量

2026-10-16時点の9資料は、PPTX・PDF合計30,757,302 bytes（29.33 MiB）。表紙画像・HTML・CSSなどを含む公開サイトは約29.60 MiBです。最大ファイルはUCF101のPPTX、8,441,287 bytes（8.05 MiB）。容量が原因で公開できない資料はありません。

GitHub公式の制限は公開サイト1 GB、ソースリポジトリ推奨1 GB、帯域のソフト上限100 GB/月です。通常のGitへの単一ファイル追加は100 MiB未満にします。ビルドは公開サイト1,000,000,000 bytes以上またはスライド1ファイル100 MiB以上で失敗させます。サイト容量とリポジトリ履歴の容量は別なので、大きなファイルの改訂が蓄積した場合は履歴側も確認してください。

- [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)（2026-10-16に公式ソースを取得して確認）
- [About large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

## 手元でビルドする

Python 3.12を使います。PowerPoint、LibreOffice、Node.jsはサイトのビルドには不要です。公開するPDFはPPTXと同じ改訂を用意してください。

```sh
python -m pip install -r site/requirements.txt
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

`http://localhost:8000/`で確認できます。生成物は`_site/`に入り、Git管理しません。PDFから表紙サムネイルを生成し、PPTX・PDFは元のままコピーします。相対リンクなので、リポジトリ名付きURLとカスタムドメインのどちらでも動きます。タイトル検索は大文字・小文字と全角・半角を区別せず、部分一致で絞り込みます。種別・タスク・公開年とも併用でき、公開年の新しい順・古い順でも並び替えられます。初期表示は新しい順で、リセットは検索文字と選択条件を消去し、並び順も新しい順に戻します。同じ年の資料はCSVの掲載順を維持します。JavaScriptが無効でも全資料とリンクを表示できます。カードは表紙・タイトル・種別／タスク／公開年ラベルだけを表示し、カード全体からPDFを開きます。説明文やPPTXのパスなどはCSVと`catalog.json`に保持します。

## 公開を開始する（ユーザーの操作）

1. この変更とスライドをGitHubの`main`へ反映します。
2. リポジトリの **Settings → Pages → Build and deployment → Source** を **GitHub Actions** にします。リポジトリやプランでPagesが利用可能なこともここで確認できます。
3. **Actions → Build and deploy slide gallery → Run workflow** を実行します。以後は対象ファイルを`main`で更新すると自動公開します。PRではビルドのみ行います。
4. 公開URLはワークフローの`github-pages` environmentに表示されます。カスタムドメイン未設定なら、通常は `https://sasakiy84.github.io/codex-cloud-workspace/` です。

`main`への反映に加えて、GitHub PagesのSource設定と、以下のCustom domain・DNS設定が必要です。これらの設定が完了すると、公開ワークフローから配信できます。

## カスタムドメイン

公開先は **`https://datasets-in-10-minutes.sasakiy84.net/`** です。`site/config.json`には設定済みです。ビルドでcanonical・構造化データ・`CNAME`を生成します。DNSとGitHub Pagesの設定はユーザー側で行ってください。

1. GitHubアカウントの **Settings → Pages** でドメインを検証します。GitHubが表示するTXTレコードをDNSに登録してください。すでに親ドメインを検証済みなら、その状態を確認します。
2. リポジトリの **Settings → Pages → Custom domain** に **`datasets-in-10-minutes.sasakiy84.net`** を設定します。DNSを向ける前に設定してください。GitHub Actionsでの公開では、生成した`CNAME`だけではこの設定の代わりになりません。
3. `sasakiy84.net`のDNSに次のレコードを登録します。同じ名前に既存のA・AAAA・CNAMEがある場合は、競合しないよう更新してください。

   |項目|設定値|
   |---|---|
   |種類|`CNAME`|
   |名前・ホスト|`datasets-in-10-minutes`|
   |宛先・値|`sasakiy84.github.io`|
   |TTL|DNS事業者の既定値|

   DNS事業者が完全なホスト名を要求する場合は、名前を`datasets-in-10-minutes.sasakiy84.net`にします。宛先に`https://`やリポジトリ名は含めません。
4. DNSチェックと証明書発行の完了後、**Enforce HTTPS** を有効にします。DNS反映には最大24時間ほどかかる場合があります。
5. 公開先でギャラリーとPDF・PPTXのリンクを確認します。

[GitHubのカスタムドメイン設定案内](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

独自ドメインを使わずにcanonicalを付ける場合は、`custom_domain`を空にし、`canonical_url`を`https://sasakiy84.github.io/codex-cloud-workspace/`にします。

## 資料を追加・更新する

1. `slides/`に同じ改訂のPDF・PPTXを追加します。
2. `site/datasets.csv`に1行追加します。ギャラリーは初公開年の新しい順で表示し、同じ年の資料はCSVの掲載順を使います。
3. ビルドして表示を確認し、GitHubに反映します。サムネイル・ページ数・ファイル容量は自動生成されます。

表紙の書体・太字は共通SKILLとSlideMaster.pptxの指定に揃え、制作時にPDFとサムネイルの見た目を確認してください。フォントの違いを理由に公開ビルドを止める検査は行いません。

|列|内容|
|---|---|
|`slug`|重複しない半角英小文字・数字・ハイフン。例：`new-dataset`|
|`title`|ギャラリーに表示する名前|
|`description`|短い紹介文|
|`modality`|`画像`・`動画`・`言語`のいずれか|
|`tasks`|下記の共通タスク。複数の場合は`|`区切り|
|`year`|データセットの初公開年。スライド制作年ではない|
|`pdf`・`pptx`|リポジトリ基準の`slides/`内のパス|

タスクの共通ラベルは **画像分類・物体認識・行動認識・自然言語推論・質問応答・言語モデル学習・エージェント操作** の7種類です。物体検出・領域分割は「物体認識」にまとめています。COCOの画像説明などの副次タスクは説明文で補います。分類が必要になった時だけ、`scripts/build_site.py`の`MODALITIES`・`TASKS`に共通ラベルを追加してください。未定義ラベルや重複slug、存在しないファイルはビルドで検出します。

公開年はデータセット系列の最初の公開年に統一しています。ImageNetは2009年（ILSVRC 2012版の年ではない）、SQuADは2016年（2.0は2018年）です。CSVはサイトからも取得でき、ページ数・ファイル容量を加えた`catalog.json`も生成します。スライド内の出典・権利表記は元の資料に含まれます。
