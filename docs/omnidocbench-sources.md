# OmniDocBench 制作・出典記録

2026-10-17（Asia/Tokyo）。本編28ページ、全63ページ。日本語の黙読・流し読み約10分を想定、未実測。著者sasakiy84。表紙は正式な固有名OmniDocBenchを使用し、論文タイトルを略語の展開形と混同していない。

## 一次資料・取得改訂

- Linke Ouyang et al., **OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations**, CVPR 2025。https://arxiv.org/abs/2412.07626 。取得PDFはarXiv v2（2025-03-25）。第一著者Linke Ouyang、最終著者Conghui He。Shanghai AI Laboratory、Abaka AI、2077 AI。
- 公式リポジトリ https://github.com/opendatalab/OmniDocBench 。取得改訂 `f133a71e9e91c3621c7ce8994200a7b394a06eb3`（2026-09-11）。README、更新履歴、モデル比較表、評価の照合・指標、推論スクリプト、LICENSEを確認した。
- 公式配布 https://huggingface.co/datasets/opendatalab/OmniDocBench 。取得改訂 `aa1ee96d106dbe53d0ae59474d75c6e6d9b53fec`。現行READMEと全件の `OmniDocBench.json`（42,208,096 bytes）、実例13枚の元画像を取得。JSONのSHA256は `a45cd84b04ad8b793e775089640e6b681209abea33ead54c1828ddca35fae496`。
- 公式の汎用モデル向け推論指示 https://github.com/opendatalab/OmniDocBench/blob/main/tools/model_infer/gpt_5.2_img2md.py 。画像の本文をMarkdown、数式をLaTeX、表をHTMLとして出力。図の内容の記述を求めない。ページ内の作文などの指示は文書の内容であり、制作側の指示として実行していない。
- CDMの公式実装・解説 **Image Over Text: Transforming Formula Recognition Evaluation with Character Detection Matching** https://github.com/opendatalab/OmniDocBench/tree/main/metrics/cdm 。LaTeXの文字列一致ではなく、描画した画像から文字と位置を対応させる。

データは2024年12月初出のため、ギャラリー公開年は2024。CVPRの発表年2025やデータ更新年2026を初出年へ使っていない。公式のモデル表にはGemini 3 Pro、Gemini 3 Flash、GPT-5.2があり、現在のプロプライエタリモデルを評価するデータという選定条件を満たす。

## バージョンと現行の対象

- 1.0：981ページ、9文書種別。初期制作の収集・注釈工程を論文から説明。
- 1.5（2025-09-25）：374ページ追加で1,355ページ。新聞・ノートの画像解像度を改善、本文・表・数式の注釈を修正。本文と数式の対応付けを改善。Overallを本文・表・数式の3成分の平均に変更。
- 1.6（リポジトリ2026-04-10、配布カード2026-04-09）：296の難しいページを追加し1,651ページ。複雑な表、密な数式、特殊な配置を追加、注釈修正。Multi-Granularity Adaptive Matchingは正解の分割を固定し、予測側だけ分割の粒度を調整する。CDMの依存環境も改修。
- 1.7（2026-04-30）：評価用スキルなどを追加。取得時の比較表は引き続き `v1.6_full` と表示。1.7を追加ページ数のあるデータ更新だと推測していない。

配布JSONの1,651ページを全件集計。`page_info.page_attribute` の各ラベルをページごとに1回数えた。HFの自動画像ビューアの行数を、正解JSONの評価対象数に流用していない。

|切り口|配布ラベルとページ数|
|---|---|
|文書種別|book 276、PPT2PDF 253、academic_literature 215、exam_paper 193、colorful_textbook 159、newspaper 151、magazine 149、research_report 132、note 118、historical_document 5|
|言語|simplified_chinese 765、english 755、en_ch_mixed 116、traditional_chinese 13、other 2|
|配置|single_column 887、other_layout 372、double_column 184、1andmore_column 155、three_column 53|
|サブセット|v1.5 1,355、equation_hard 100、layout_hard 99、table_hard 97|

初期制作は20万件超のPDFからResNet-50の画像特徴とFaissのクラスタリングで候補6,000ページを選び、人手で属性を付け、構成を調整して981ページにした。事前注釈はLayoutLMv3、PaddleOCR、UniMERNet、GPT-4o。人手で位置、文字、読む順番、領域の関係を修正。表・数式を描画して確認し、描画不能な要素を3人の研究者が確認・修正した。未公表の総作業者数・作業時間は推測していない。

## 採点と公式比較

ページのMarkdownを本文・数式・表へ分解し、正解領域と対応させる。本文の正規化編集距離は小さいほどよい。表TEDSはHTMLの木の構造とセル内容、TEDS-Sは構造を比較。数式CDMは描画した文字と位置を比較する。読む順番の編集距離はOverallには含まれない。

`Overall = ((1 - Text Edit Distance) * 100 + Table TEDS + Formula CDM) / 3`。
説明用のabc/adcは1置換÷最大長3。説明用90・80・100の平均は90点。公式モデルの実測と同じ表には混ぜていない。

次の値は取得改訂の公式 `v1.6_full` 表から選び、HTMLの行を直接読んで照合した。列はOverall、本文ED、数式CDM、表TEDS。

|モデル|種類|Overall ↑|本文ED ↓|数式CDM ↑|表TEDS ↑|
|---|---|---:|---:|---:|---:|
|TeleOCR|文書専用|96.91|0.0267|96.5895|96.8183|
|Gemini 3 Pro|汎用|92.91|0.064|95.99|89.15|
|Gemini 3 Flash|汎用|92.62|0.066|95.16|89.29|
|GPT-5.2|汎用|86.59|0.114|88.21|82.95|

現行表の結果であり、初期981ページでの成績を同条件の順位へ混ぜていない。公式比較への掲載を、各提供会社のモデルカードでの採用確認へ言い換えていない。重いモデル推論や全評価・CDMの実行はしていない。

## 13独立ページの実例

本編3ページ＋追加10ページ。全例、公式配布の元画像と正解JSONを取得し、画像と注釈を目視照合。PPTXに元画像のバイト列を保持し、編集可能な赤枠を座標から重ねた。次のページに、選択領域の正解注釈と日本語の内容要約を示す。入力画像全体の完全なMarkdownを示しているとはしていない。画像は生成・再描画していない。

|画像ページ|注釈ページ|JSON行（0始まり）|注釈ID|文書の内容|
|---:|---:|---:|---|---|
|7|8|433|`22`|2段組みの論文|
|9|10|300|`1`|講義スライドの表|
|11|12|8|`box_id_9`|数値計算の数式|
|32|33|23|`box-6s09k9l9`|カラー教材|
|34|35|107|`box_id_2`|雑誌の身体性AI|
|36|37|1011|`11`|新聞の種子供給記事|
|38|39|895|`2`|手書き地理ノート|
|40|41|202|`box_id_3`|表の下の箇条書き|
|42|43|111|`box-a1va37rw`|縦書きの古典資料|
|44|45|126|`box_id_9`|見開きの作文問題|
|46|47|465|`4`|結合セルを持つ表|
|48|49|10|`box_id_3`|表と数式の間の本文|
|50|51|543|`1`|コードを含む技術書|

本編の表は配布HTMLの全セルを編集可能なネイティブ表へ再構成し、全5行×4列を照合。追加例8は、結合セルを持つ最上段の表から先頭の見出し行を抜粋。3セルすべての文字列とcolspan=2を照合した。その他の本文・数式の正解引用は選択領域の全文と一致。各ページ下部にJSON行・注釈IDと配布URLを記載する。

## 利用条件・制作確認

配布カードはPDFの出所を公開オンライン資料・コミュニティの提供とし、データを研究目的・非商用の利用に限定する。コードのApache 2.0を、収録された各文書の包括的なライセンスとは扱わない。実例の元文書にある著作権表記を画像内に残し、資料の研究紹介・注釈の説明に必要なページを引用した。コードのライセンス全文は [omnidocbench-code-Apache-2.0.txt](licenses/omnidocbench-code-Apache-2.0.txt)。

公式配布ページのスクリーンショットはChromiumで取得。CSS3枚とSource Sans Proの適用、document.fonts.readyを確認し、データカード本文へスクロールして撮影した。アバター等の周辺リクエストにCONNECTエラーがあったが、本文とCSSは読み込まれ、実画像を確認した。

共通マスターと2つのスキルを使用。全63ページの一覧、その後で全引用、全10表、コード2ページ、参考文献2ページ、表紙を拡大表示して確認。修正後も再描画し、変更ページを再確認した。表紙・転換の文字群の縦中心は約221.4pt。タイトルの一行表示、表セルの文字・余白・数値と見出しの右揃え、booktabs形式の罫線、引用ボックスの実際の文字からの上下余白、本文と出典、参考文献のまとまりと間隔、URLのみのリンクを確認した。

PPTXとPDFの全テキスト対応、13枚の埋め込み画像のバイト一致、全件集計、実例注釈、公式モデル表の値、掲載PythonのJSON読み取りを検証。OOXMLの78部品をスキーマ確認し、既存マスターのbuSzPct字句差異127件以外の不整合、ノート、壊れた参照はなし。制作・調査・検証スクリプトは一時領域に置き、スキルやリポジトリにはコミットしない。

ギャラリーは25資料。分類は画像／文書解析／2024。OCR・表・数式を別々のラベルへ増やさず、「文書解析」一つでまとめた。デスクトップ・モバイル、名前の検索と全角正規化、フィルター、公開年順、サムネイル、PDF・PPTX配布、JSON-LD、コンソールエラーを確認して公開する。
