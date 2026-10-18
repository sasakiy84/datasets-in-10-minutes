# BLiMP：出典と制作・校正記録

2026-10-18作成。本編23ページ、Appendix21ページ、合計44ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.](https://aclanthology.org/2020.tacl-1.25/)|paper|
|[nyu-mll/blimp、改訂877fba08。2026-10-18参照。](https://huggingface.co/datasets/nyu-mll/blimp)|data|
|[BLiMP、67 configurations/train全67,000件を集計。2026-10-18取得。](https://huggingface.co/datasets/nyu-mll/blimp)|stats|
|[BLiMP 公式公開ページ。2026-10-18参照。](https://github.com/alexwarstadt/blimp)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|
|[EleutherAI. Language Model Evaluation Harness. 2026-10-18参照。](https://github.com/EleutherAI/lm-evaluation-harness)|harness|

取得日：2026-10-18。配布元 `nyu-mll/blimp`、固定改訂 `877fba0801ffb7cbd8c39c1ff314a46f053f6036`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/blimp.json)に保存した。

## 内容・実例・評価の照合

全67ファイル各1,000対、計67,000対を取得。linguistics_termは13値だがs-selection 2,000対をargument_structureに合算して公式12分類に集約した。英語の許容／非許容文を保持し、訳は意味と英語の文法上の対比を示す。singular theyや自動詞seeを一般に誤りとはせず生成設定に範囲を限定。人の直接判断88.6%と多数決一致96.4%を区別。HELMは4現象のみ、表はbindingの1,000対・0-shot・1試行。初期公開2019年、TACL発表2020年。CC BY 4.0。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELMのcanonical実行2件について、モデル、指標、split、提示例数、試行数と実行別statsを照合した。2023年の固定版の値であり最新順位ではない。

集計対象は `67 configurations/train` の全67,000件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/blimp/changes.tsv)、[全ページの最終文言](skill-proofreading/blimp/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/blimp/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全44ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。

## 2026-10-18：正解表示と出典表現の更新

全ページを点検し、正解表示13か所、出典表現1か所を変更した。正解値、引用原文、訳、評価結果、ページ数、出典URLは保持した。図表番号の照合履歴は[変更対](skill-proofreading/blimp/changes.tsv)に残し、スライド内では文献単位の出典にまとめた。詳細は[今回の点検記録](skill-proofreading/blimp/answer-and-citation-review.json)。Geminiは使用していない。

## 2026-10-18：正解表示の色

ユーザー個人の好みに合わせ、正解表示13か所をテーマaccent1（#B13731、えんじ系の赤）に変更。文章・値・書体・大きさ・座標は旧版と一致。変更記録は[こちら](skill-proofreading/blimp/answer-color-review.json)。
