# APPS：出典と制作・校正記録

2026-10-18作成。本編27ページ、Appendix40ページ、合計67ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Dan Hendrycks et al. (2021). Measuring Coding Challenge Competence With APPS. NeurIPS Datasets and Benchmarks 2021.](https://arxiv.org/abs/2105.09938)|paper|
|[codeparrot/apps、改訂21e74ddf。2026-10-18参照。](https://huggingface.co/datasets/codeparrot/apps)|data|
|[APPS、train全5,000件を集計。2026-10-18取得。](https://huggingface.co/datasets/codeparrot/apps)|stats|
|[APPS 公式公開ページ。2026-10-18参照。](https://github.com/hendrycks/apps)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|

取得日：2026-10-18。配布元 `codeparrot/apps`、固定改訂 `21e74ddf8de1a21436da12e3e653065c5213e9d1`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/apps.json)に保存した。

## 内容・実例・評価の照合

train全5,000問、テストを持つ4,805問、fn_nameを持つ3,063問を集計した。13実例は問題文全文と訳を段落単位で対応させ、配布テストを各最大2件保持。解答コードは実行していない。id 323は引数の文字列に引用符自体を含むため問題文の例と入力内容が異なり、Falseを誤りと断定しない。id 2099の原文末尾の式は配布表記を保持し、訳では隣接項の差を示すと補足。every secondは2番目・4番目・6番目の1個おき。初期Top-1／Top-5とHELMの1候補、部分テスト平均と全テスト通過率を区別。MIT。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELMのcanonical実行2件について、モデル、指標、split、提示例数、試行数と実行別statsを照合した。2023年の固定版の値であり最新順位ではない。

集計対象は `train` の全5,000件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/apps/changes.tsv)、[全ページの最終文言](skill-proofreading/apps/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/apps/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全67ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。

## 2026-10-18：正解表示と出典表現の更新

全ページを点検し、正解表示0か所、出典表現1か所を変更した。正解値、引用原文、訳、評価結果、ページ数、出典URLは保持した。図表番号の照合履歴は[変更対](skill-proofreading/apps/changes.tsv)に残し、スライド内では文献単位の出典にまとめた。詳細は[今回の点検記録](skill-proofreading/apps/answer-and-citation-review.json)。Geminiは使用していない。
