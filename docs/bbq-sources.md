# BBQ：出典と制作・校正記録

2026-10-18作成。本編26ページ、Appendix33ページ、合計59ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.](https://aclanthology.org/2022.findings-acl.165/)|paper|
|[BBQ 公式配布データ。2026-10-18取得。](https://github.com/nyu-mll/BBQ/tree/bea11bd97d79/data)|data|
|[BBQ、official GitHub data 11 files全58,492件を集計。2026-10-18取得。](https://github.com/nyu-mll/BBQ/tree/bea11bd97d79/data)|stats|
|[BBQ 公式公開ページ。2026-10-18参照。](https://github.com/nyu-mll/BBQ)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|
|[Stanford CRFM. BBQMetric. HELM v0.3.0. 2026-10-18参照。](https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/bbq_metrics.py)|bbqcode|

取得日：2026-10-18。配布元 `nyu-mll/BBQ`、固定改訂 `bea11bd97d79217245b5871acd247b9d6eb24598`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/bbq.json)に保存した。

## 内容・実例・評価の照合

公式nyu-mll/BBQのコミットbea11bd97d79217245b5871acd247b9d6eb24598の11ファイルをGit blob SHA-1で照合した。全58,492件＝単一属性9分類31,372件＋交差属性2分類27,120件。曖昧／情報十分は各29,246件。同一テンプレートの条件対を含む13公開レコードであり、13種の独立テンプレートではない。三つの候補と不明という正解を保持。論文の曖昧条件バイアス式と、HELM v0.3.0が全体正解率を使う実装差をAppendixで説明。初期公開2021年、ACL Findings発表2022年。CC BY 4.0。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELMのcanonical実行2件について、モデル、指標、split、提示例数、試行数と実行別statsを照合した。2023年の固定版の値であり最新順位ではない。

集計対象は `official GitHub data 11 files` の全58,492件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/bbq/changes.tsv)、[全ページの最終文言](skill-proofreading/bbq/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/bbq/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全59ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。
