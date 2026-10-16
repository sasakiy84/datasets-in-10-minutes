# FACTS Grounding 制作・出典記録

2026-10-17（Asia/Tokyo）。本編27ページ、全60ページ。日本語の黙読・流し読み約10分を想定、未実測。著者sasakiy84。

## 一次資料とバージョン

- Alon Jacovi et al., **The FACTS Grounding Leaderboard: Benchmarking LLMs’ Ability to Ground Responses to Long-Form Input**, 2024-12-17のGoogle技術報告。第一著者Alon Jacovi、最終著者Dipanjan Das。https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf
- Aileen Cheng et al., **The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality**, 2025-12-11の技術報告。第一著者Aileen Cheng、最終著者Dipanjan Das。https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf
- Google, **FACTS Grounding 1.0 Public Examples**。配布改訂 `11b6961370aa0ac73c91d58e35317e724b2ac765`。https://huggingface.co/datasets/google/FACTS-grounding-public
- The FACTS team, **FACTS Benchmark Suite: Systematically evaluating the factuality of large language models**, 2025-12-09。https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/
- 現行Grounding順位表 https://www.kaggle.com/benchmarks/google/facts-grounding/leaderboard 。この制作環境ではKaggleへのCONNECTが403となったため、ライブ順位の確認済みとはせず、取得できた公式技術報告の日時・数値を使う。

正式名はFACTS Grounding。一次資料で対象名の展開形は確認できず、論文名を略語の展開形として作っていない。公開問題の初出は2024年、採点更新v2は2025年。v2の入力問題はv1と同じであることをスイート論文6.1で確認。v1はGemini 1.5 Pro・GPT-4o・Claude 3.5 Sonnet、v2はGemini 2.5 Flash・GPT-5を判定に使用し、採点指示も変更した。

## 作成・規模・結果

初期報告は公開860問、非公開859問。人がウェブの文書・レビュー群と依頼を作成し、文書限定のシステム指示を加える。全件を人が確認し、創作、外部知識や複雑な推論を要する依頼、OCRで読めない文書などを除外する。文書長は原著のトークン計測で平均約2.5K、最大32K。作業者数など未公表の値は推測していない。

領域・依頼の構成比は原著の全体集計。医療29.0、法律22.2、技術19.2、金融18.1、小売・製品11.4%。依頼は事実抽出31.6、抽出と要約29.7、影響分析8.9、説明・定義7.5、概念比較6.1、利点・欠点4.4、要約と形式4.4、要約3.8、平易な要約3.7%。元の丸め値を保つ。

v2の得点は2025年12月のスイート報告による、公開・非公開を平均したGrounding成績。Gemini 2.5 Pro 74.2±2.0、GPT-5 69.6±2.1、Gemini 3 Pro 69.0±2.1、Claude 4.5 Opus 62.1±3.3、Grok 4 54.7±2.3（%・95%信頼区間）。Gemini 3 Proのスイート総合68.8%を、Grounding単独の値に置き換えない。

人の判定との照合320件で、採用したモデル・指示のMacro-F1はGemini 2.5 Flash 65.33、GPT-5 65.18。回答モデルの成績と判定モデルの一致度を分けて説明する。判定器の採用理由の説明はAppendixにも置く。

## 実例と利用条件

examples.csv全860行、evaluation_prompts.csv、READMEを取得。full_promptは860件とも異なる。各実例は文書原文の連続抜粋またはラベルで示した複数箇所の抜粋、依頼の全文、日本語訳と回答要点。空白・改行は組版用に正規化し、原文の綴りを保つ。複数の引用間は[…]で区切る。

配布CSVに固定の正解回答列はない。「回答に含める要点」は制作側の日本語の解説で、公開された正解文章・実モデル出力とはしていない。全文・訳・要点は根拠となる該当文書と照合。本編3件＋別の追加10件、計13問。同じ問の文書・依頼の2ページは1件と数える。

|CSV行（0始まり）|文書ページ|依頼ページ|題材|
|---:|---:|---:|---|
|6|7|8|赤外線センサーの最大距離|
|94|9|10|9 gのカートリッジに合う重り|
|103|11|12|ハッシュとnonceを説明する|
|18|31|32|海藻抽出物と魚乳剤を比較する|
|40|33|34|需要とコストから物価上昇を説明|
|70|35|36|ガンマ線と赤外線の望遠鏡|
|99|37|38|C型肝炎の感染を自覚する割合|
|128|39|40|パンフレット内のテーマパーク|
|823|41|42|無線ネット接続を妨げる地形|
|826|43|44|ファイアウォールの動作|
|853|45|46|緊急地震速報の通知経路|
|105|47|48|型番に対応するスピーカー価格|
|747|49|50|行政命令の発効日を探す|

コード欄のcsv.DictReaderによる読み込みを実行し、860行・行94の依頼とカウンターウェイトの範囲を確認。採点モデルAPIの呼び出しや、独自のモデル性能測定は行っていない。

データカードのライセンスは **CC BY 4.0**。https://creativecommons.org/licenses/by/4.0/ 。転載した文書・依頼と訳にも同ライセンスを適用し、Googleと公式配布先を各ページに記載。原文抜粋・空白の正規化・日本語訳を加えたことをここに明記する。ライセンス本文の直接取得はこの環境では403で、データカードの明示と公式ライセンスURLを記録した。

evaluation_prompts.csvは2024年の初期採点用で、v2の採点指示と取り違えない。Kaggleの画面は取得できなかったため、Hugging Faceの公式配布ページを実ブラウザで撮影し、見出しとURLを画面に合わせた。CSS4枚とSource Sans Pro適用を確認し、実画面を目視。アバターなど補助リソースの取得失敗は本文に影響しないことを確認した。

## 最終確認

全60ページを一覧で確認。引用13・依頼13ページ、全7表、コード、参考文献2ページ、表紙・導入画面を個別に拡大して確認。全引用の上下余白各8pt、本文と出典の最小間隔11.89pt、文献項目間25.91pt以上、コード上下10.88/11.19pt。PPTXとPDFの全文照合、文字欠落・ページ外文字・タイトル折り返しなし、全セル内収容と罫線を確認。ZIP・内部参照・ノートなし、XML75部品を検証し、共通マスターの既知のbuSzPct字句差124件以外に予期しないエラーなし。

最終修正はp.38の分母を明確にした訳文。他58ページは確認済み版とピクセル一致。p.44はテキスト一致のまま577成分に描画差があり、拡大して再確認した。制作・調査・検査のスクリプトはscratchのみ。

|成果物|bytes|SHA-256|
|---|---:|---|
|PDF|1,111,272|`7907a87a3c6b2637eab40cb1af06e37384f57d7ed5ad4f5be20c1893b13e6e93`|
|PPTX|319,752|`ea84dcd301badd56bd9064f305750367516b63822283f53e784f00f55c89eba8`|

23件のギャラリーを実ブラウザで確認。全サムネイル、大小・全角のタイトル検索、言語・質問応答・2024年の併用、年順、PDFカードリンク・PPTX取得、390px表示の横はみ出しなし。確認済みscratch・リポジトリ・公開ビルドのPPTX・PDFはSHA-256一致。
