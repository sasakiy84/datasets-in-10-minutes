# WMT14：出典と制作・校正記録

2026-10-18作成。本編23ページ、Appendix24ページ、合計47ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと、その最終版から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Ondřej Bojar et al. (2014). Findings of the 2014 Workshop on Statistical Machine Translation. WMT 2014.](https://aclanthology.org/W14-3302/)|paper|
|[wmt/wmt14、改訂b199e406。2026-10-18参照。](https://huggingface.co/datasets/wmt/wmt14)|data|
|[WMT14、five language pairs/test全14,519件を集計。2026-10-18取得。](https://huggingface.co/datasets/wmt/wmt14)|stats|
|[WMT14 公式公開ページ。2026-10-18参照。](https://www.statmt.org/wmt14/translation-task.html)|page|
|[Liang et al. Holistic Evaluation of Language Models. TMLR 2023. Classic v0.4.0（2023-11-17）。](https://crfm.stanford.edu/helm/classic/v0.4.0/)|helm|
|[Stanford CRFM. HELM Classic v0.4.0. 公開run_specs。2023-11-17のリリース。](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.4.0/run_specs.json)|config|
|[Wu et al. (2016). Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation. arXiv:1609.08144.](https://arxiv.org/abs/1609.08144)|gnmt|
|[Vaswani et al. (2017). Attention Is All You Need. NeurIPS.](https://arxiv.org/abs/1706.03762)|transformer|
|[Matt Post (2018). A Call for Clarity in Reporting BLEU Scores. WMT.](https://aclanthology.org/W18-6319/)|sacrebleu|

取得日：2026-10-18。配布元 `wmt/wmt14`、固定改訂 `b199e406369ec1b7634206d3ded5ba45de2fe696`。冒頭はCSSとフォントを読み込んだブラウザ画面。取得URL、ファイルのbytes・SHA-256、13実例の識別子・原文・訳・元レコード・ハッシュを[検証データ](data-audits/wmt14.json)に保存した。

## 内容・実例・評価の照合

5言語組のtest全14,519対訳レコードを取得。de/fr/cs/ru各3,003件、hi 2,507件。英語を共有するため14,519件の異なる記事とはしない。13例は英語と参照訳を保持し、それぞれの意味訳を添えた。ヒンディー語文字のPDF欠落なし。10翻訳方向、newstest2013と2014、コーパスBLEUと文ごとの平均を区別。GNMT Table 5とTransformer Table 2を別々に照合。HELM v0.4.0の定義はあるがrun_specsは0件のため、HELM得点を創作しない。コードのtrain最大20,000件・翻訳先重複除去を説明。著者13名と最終著者Ales Tamchynaを論文で確認。言語組を横断した一律のライセンスを推定しない。

本編3件、追加10件の13公開レコードを掲載。長い実例は文・段落単位で分割し、同じレコードは1件と数えた。原文と訳は同じページで読める配置。HELM v0.4.0のrun_specsに実行が0件だった。定義と評価コードを説明し、HELMの得点は掲載していない。

集計対象は `five language pairs/test` の全14,519件。データの構造に合わせた全件集計を示した。取得した容量と、未取得分を含めた配布全体の容量は区別して扱った。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)を1ページずつ適用した。[実際の修正前後の対](skill-proofreading/wmt14/changes.tsv)、[全ページの最終文言](skill-proofreading/wmt14/pages.jsonl)、[検査とレイアウト変更の記録](skill-proofreading/wmt14/review.json)を保存。削除ページは最終pageをnull、初稿番号をdraft_pageとして記録した。

全47ページを描画して一覧を確認し、引用・コード・表・参考文献・公式画面・グラフは個別に拡大した。最終変更ページは再出力して再確認。文字欠落、原文・訳の保持、表セルと引用のはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査。最終PPTX・PDFのSHA-256を記録した。

OOXMLはマスター、レイアウト、表、内部参照、図形IDも検査し、新規の標準XSD構造エラー0件。元のマスター由来の既存11件とbuSzPctの整数字句表記の差は分離した。整数値25000–400000を別に検査し、XSD自体は変更していない。[定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照。PowerPointでの手動開封は実施せず、LibreOffice変換とネイティブ編集構造を検証した。
