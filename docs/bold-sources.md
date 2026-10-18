# BOLD：出典と制作・校正記録

2026-10-18作成。本編23ページ、Appendix21ページ、合計44ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Jwala Dhamala et al. (2021). BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation. FAccT 2021.](https://arxiv.org/abs/2101.11718)|paper|
|[BOLD 公式配布データ。2026-10-18取得。](https://github.com/amazon-science/bold/tree/3ad652c773f5d1e30d5f6f61657ed934d768ecad/prompts)|data|
|[BOLD、official prompts, all items in lists全23,679件を集計。2026-10-18取得。](https://github.com/amazon-science/bold/tree/3ad652c773f5d1e30d5f6f61657ed934d768ecad/prompts)|stats|
|[BOLD 公式公開ページ。2026-10-18参照。](https://github.com/amazon-science/bold)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|

取得日：2026-10-18。配布元 `amazon-science/bold`、固定改訂 `3ad652c773f5d1e30d5f6f61657ed934d768ecad`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/bold.json)に保存した。

## 内容・実例・評価の照合

公式amazon-science/boldのコミット3ad652c773f5d1e30d5f6f61657ed934d768ecadの5ファイルをGit blob SHA-1で照合した。23,679書き出し、5ドメイン43グループ。HELMは各topicの最初の書き出しを使い、候補は7,201件。canonical実行1,000入力すべてが実際にこの候補に対応（adapter末尾空白を除去して照合、重複を除くと994文）。13例は未完の書き出しを保持し、続きや唯一の正解を創作しない。重複する注意の本文3ページを削除。初期の定性的比較に数値を補わない。HELMは20トークン・温度0.9・各1生成のPerspective指標。公式CC BY-SA 4.0とHFカードCC BY 4.0の違いを明記。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELMのcanonical実行2件について、モデル、指標、split、提示例数、試行数と実行別statsを照合した。2023年の固定版の値であり最新順位ではない。

集計対象は `official prompts, all items in lists` の全23,679件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/bold/changes.tsv)、[全ページの最終文言](skill-proofreading/bold/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/bold/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全44ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。

## 2026-10-18：正解表示と出典表現の更新

全ページを点検し、正解表示0か所、出典表現0か所を変更した。正解値、引用原文、訳、評価結果、ページ数、出典URLは保持した。図表番号の照合履歴は[変更対](skill-proofreading/bold/changes.tsv)に残し、スライド内では文献単位の出典にまとめた。詳細は[今回の点検記録](skill-proofreading/bold/answer-and-citation-review.json)。Geminiは使用していない。
