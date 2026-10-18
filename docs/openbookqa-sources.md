# OpenBookQA：出典と制作・校正記録

2026-10-18作成。本編26ページ、Appendix26ページ、合計52ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Todor Mihaylov et al. (2018). Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering. EMNLP 2018.](https://aclanthology.org/D18-1260/)|paper|
|[allenai/openbookqa、改訂388097ea。2026-10-18参照。](https://huggingface.co/datasets/allenai/openbookqa)|data|
|[OpenBookQA、additional/test全500件を集計。2026-10-18取得。](https://huggingface.co/datasets/allenai/openbookqa)|stats|
|[OpenBookQA 公式公開ページ。2026-10-18参照。](https://allenai.org/data/open-book-qa)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|
|[EleutherAI. Language Model Evaluation Harness. 2026-10-18参照。](https://github.com/EleutherAI/lm-evaluation-harness)|harness|

取得日：2026-10-18。配布元 `allenai/openbookqa`、固定改訂 `388097ea7776314e93a529163e0fea805b8a6454`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/openbookqa.json)に保存した。

## 内容・実例・評価の照合

additional版test全500問を集計。科学の事実fact1、設問、四つの候補と正解を保持した。初期評価は関連事実fと追加事実kの提示条件を区別した。HELMは事実を入力しない0-shot・1試行。humanScoreは5人中の正解者の割合（1.0は5人、0.8は4人）。公式GitHubのApache 2.0とミラーのunknownを区別した。AllenAI案内はHFへ転送されたため、冒頭は公式GitHubのREADME画面を用いた。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELMのcanonical実行2件について、モデル、指標、split、提示例数、試行数と実行別statsを照合した。2023年の固定版の値であり最新順位ではない。

集計対象は `additional/test` の全500件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/openbookqa/changes.tsv)、[全ページの最終文言](skill-proofreading/openbookqa/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/openbookqa/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全52ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。
