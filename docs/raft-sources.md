# RAFT：出典と制作・校正記録

2026-10-18作成。本編23ページ、Appendix25ページ、合計48ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Neel Alex et al. (2021). RAFT: A Real-World Few-Shot Text Classification Benchmark. NeurIPS Datasets and Benchmarks 2021.](https://arxiv.org/abs/2109.14076)|paper|
|[ought/raft、改訂9ee50172。2026-10-18参照。](https://huggingface.co/datasets/ought/raft)|data|
|[RAFT、11 tasks/train全550件を集計。2026-10-18取得。](https://huggingface.co/datasets/ought/raft)|stats|
|[RAFT 公式公開ページ。2026-10-18参照。](https://github.com/oughtinc/raft-baselines)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|

取得日：2026-10-18。配布元 `ought/raft`、固定改訂 `9ee50172ea9afda2f1033c6f1b986e568b862fb3`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/raft.json)に保存した。

## 内容・実例・評価の照合

11課題の公開train各50件、計550件とtask.jsonを取得。記事難易度は冒頭段落のみ、影響声明と変革的AIも入力（抜粋）と明示。レビュー採否はTitle・Abstract・Labelを表示し、Authors・Journalを含む元レコードは監査データに保持した。制作記録だけを述べる3ページを削除し、課題名を短い日本語に変更。公式のmacro-F1の11課題平均とHELM twitter_complaints再分割40件の正解率を分けた。HELMは公開50件の10／40分割で、正解非公開の公式testではない。基礎データ全体のライセンスをMITと一括しない。公式サイト403のため公式baselines GitHubの画面を使用。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELMのcanonical実行2件について、モデル、指標、split、提示例数、試行数と実行別statsを照合した。2023年の固定版の値であり最新順位ではない。

集計対象は `11 tasks/train` の全550件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/raft/changes.tsv)、[全ページの最終文言](skill-proofreading/raft/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/raft/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全48ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。

## 2026-10-18：正解表示と出典表現の更新

全ページを点検し、正解表示0か所、出典表現1か所を変更した。正解値、引用原文、訳、評価結果、ページ数、出典URLは保持した。図表番号の照合履歴は[変更対](skill-proofreading/raft/changes.tsv)に残し、スライド内では文献単位の出典にまとめた。詳細は[今回の点検記録](skill-proofreading/raft/answer-and-citation-review.json)。Geminiは使用していない。
