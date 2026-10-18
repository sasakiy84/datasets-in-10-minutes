# MMMLU：出典と制作記録

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

2026-10-17制作。正式名称は **Multilingual Massive Multitask Language Understanding**。本編31枚＋Appendix26枚、計57枚。約10分の黙読・流し読み向けの日本語資料で、閲覧時間は未実測。編集可能なPPTXと同じ最終版から出力したPDFを保存した。

## 一次資料とバージョン

|資料|確認内容|
|---|---|
|[MMMLU公式データカード](https://huggingface.co/datasets/openai/MMMLU)|OpenAI。2024-09-13公開。正式名称、専門翻訳者による14言語への翻訳、設定名、MITライセンス。|
|[公式ファイル・変更履歴](https://huggingface.co/datasets/openai/MMMLU/commits/main)|参照バージョン `325a01dc3e173cac1578df94120499aaca2e2504`（2024-10-16）。14 CSVを全件取得。10月3日に分割名をtestへ統一、10月16日に中国語設定名の誤記を修正した。|
|[Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)|Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, Jacob Steinhardt。2020年初稿、ICLR 2021。学生による設問収集、57科目、難度と分割の設計。|
|[OpenAI MMLU評価実装](https://github.com/openai/simple-evals/blob/652c89d/mmlu_eval.py)|参照リポジトリのバージョン `652c89d0ca9df547706735883097e9537d40dc47`。英語の入力テンプレート、回答記号の抽出、正解との一致、問題単位の平均、科目と4領域の対応を確認。|
|[Multilingual MMLU Benchmark Results](https://github.com/openai/simple-evals/blob/652c89d/multilingual_mmlu_benchmark_results.md)|同じバージョンのOpenAI公開比較。14言語、o3-high、GPT-4.1-2025-04-14、GPT-4o-2024-11-20などの言語別正答率。|
|[Gemini 3.1 Pro: Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)|2026-10-17に公式HTMLと、そこからリンクされたPDFの両方を取得。2026年2月のMMMLU比較を照合した。PDFは [Gemini-3-1-Pro-Model-Card.pdf](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Pro-Model-Card.pdf)。|
|[Gemini 3.1 Pro: Evaluation Methodology](https://deepmind.google/models/evals-methodology/gemini-3-1-pro/)|公式PDFを取得。Geminiの自社評価と他社の公表値の採用、モデルID・思考設定などの条件を確認。|
|[Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation](https://arxiv.org/abs/2412.03304v2)|Shivalika Singh et al.。2024年初稿・2025年2月改訂。42言語への展開と、文化依存の知識を要する設問の分析。MMMLUのバージョン番号として扱っていない。|

## 作成方法・規模・科目

元のMMLUの問題は、大学生・大学院生がオンラインの教材や練習問題から人手で収集した。初等・高校・大学・専門職向けの科目を含む。MMMLUはそのテスト集合を専門翻訳者が14言語へ訳したもの。データカードにない翻訳者数や作業量は推定していない。

14ファイルはすべて14,042行、計196,588翻訳レコード。取得したCSVの合計は124,869,536 bytes（119.09 MiB）。英語の原著が記した初期の分割数を、そのまま今回の配布ファイルの実数として使っていない。

日本語CSVは57種類のSubjectを持つ。科目別件数の合計は14,042。上位5科目は専門法律学1,534、道徳的状況判断895、その他の知識783、専門心理学612、高校心理学545。全57科目と件数をAppendixの3ページに掲載し、日本語の表示名は本資料で付けた。

OpenAI実装のsubject2categoryを用いた日本語全件の4領域集計は、人文系4,705、その他3,242、社会科学3,077、STEM 3,018。言語によってSubject列にファイル名風の表記などの差があるため、この集計の対象を日本語へ限定している。

日本語CSVのSHA-256は `b2daf62034489b88411af91ad955e8ec513bd7d3129c9eb0319036160bd18032`。元ファイル名は `test/mmlu_JA-JP.csv`。

## 実例の選定と照合

独立した問題13問を、本編3問＋追加10問で掲載。同じ問題のスペイン語・スワヒリ語版を本編に2ページ追加し、問題数には重ねて数えていない。設問・選択肢は配布原文の全文。正解記号もその言語の配布値と照合した。日本語も公式の翻訳文であり、本資料が新たに訳したものではない。下段の説明は本資料で付記した。

先頭の無名列は科目ごとに番号が戻るため、単独のグローバルIDとして使っていない。ページ下部には言語・科目・科目内番号と、公式viewerの行URLを示す。

|ページ|言語|科目|科目内番号|viewerの行|内容|
|---|---|---|---:|---:|---|
|8|日本語|machine_learning|95|6930|教師あり学習とPCA|
|9|日本語|high_school_statistics|101|5533|カイ二乗検定の自由度|
|10|日本語|international_law|70|6513|欧州人権条約|
|11–12|スペイン語・スワヒリ語|machine_learning|95|6930|上記と同じ機械学習問題|
|35|日本語|astronomy|79|314|火星の公転周期|
|36|日本語|computer_security|34|1505|認証方式|
|37|日本語|nutrition|155|9563|ヒストン|
|38|日本語|high_school_biology|48|2717|受精が起こる場所|
|39|日本語|college_mathematics|94|1190|複素数の累乗|
|40|日本語|world_religions|66|13937|『女誡』の著者|
|41|日本語|high_school_microeconomics|76|4574|独占的競争|
|42|日本語|professional_accounting|168|10517|現在価値|
|43|日本語|logical_fallacies|44|6716|帰謬法|
|44|日本語|high_school_geography|91|3538|化石燃料|

全言語で行番号・正解記号が一致すると仮定せず、実物を比較した。例えば高校世界史の行5853・科目内番号1は、日本語では火薬兵器、簡体字中国語ではダリオの詩、韓国語では古代の死後世界という別の設問であり、その事実をAppendixに掲載した。本編の並行比較には、本文と選択肢の対応を確認した機械学習の問題を使った。

## 採点・モデル成績

OpenAIの公開実装は、QuestionとA〜Dを入力テンプレートへ入れ、回答末尾を `Answer: A` などの形式にするよう指示する。各言語の回答表現も対象とする正規表現、文字の正規化、正解記号との一致、問題ごとの得点の平均を確認した。

公式の正規化関数と抽出ロジックを使い、正解Aに対する説明用の応答 `Answer: A` → 1、`Answer: B` → 0、`A` → 0を実行して照合した。モデルAPIの呼び出しは行っていない。科目を均等に平均する方法と、公開実装の問題単位の平均を混同せず、科目別件数が持つ重みを専門法律学1,534問・抽象代数学100問で示した。

Googleの2026年2月の公式比較は、Gemini 3.1 Pro 92.6%、Gemini 3 Pro 91.8%、Claude Sonnet 4.6 89.3%、Claude Opus 4.6 91.1%、GPT-5.2 89.6%。モデルカードの表頭にある思考設定も転記し、評価手順書にある自社評価・他社公表値の採用を説明した。今回の取得時点で読める公式資料として採用し、2026年10月の独自再評価や未確認の最新順位と呼んでいない。

OpenAIの公開比較は別ページに分け、モデルの日付・設定を付記した。日本語／スペイン語／スワヒリ語／ヨルバ語のGPT-4oは83.5／84.3／77.9／62.1%、GPT-4.1は85.6／87.6／79.5／64.7%、o3-highは89.0／91.1／86.0／78.0%。全14言語の3モデルの値もAppendixへ掲載した。

## 表示・構造・公開

共通マスターを使用。Noto Sans / Noto Sans CJK JP、コードはLiberation Mono。表紙主題52pt太字、正式名称20pt、緑帯14pt太字。15個の表、2個のグラフは編集可能で、発表者ノートは含めない。横罫線は上下1.2pt・見出し下0.6pt、縦罫線なし。参考文献は2件ずつ3ページへまとめた。

全57枚を一覧で確認し、引用15枚、表15枚、コード1枚、参考文献3枚を1枚ずつ拡大確認した。表紙とグラフ、変更ページも確認。タイトル・表セルの短い折り返しを確認し、本文の短い最終行は許容する方針を適用した。

全段落のPPTX・PDF照合で文字欠落・ページ外文字・通常タイトルの想定外の折り返しなし。文字のある表323セルを実文字境界で検査し、セル内の収まりと表注との12pt以上の間隔を確認した。本文と出典の最小間隔は約8.7pt、コード背景の上下余白は約11pt、参考文献間は最小約27.3pt。URLのみのリンク52件を確認した。

PPTXのZIP・内部参照、74 XMLパーツを検査。既知のbuSzPct整数表記の字句差113件以外のスキーマエラーなし。最終修正後のPDFを旧版と描画比較し、変更11ページを拡大確認、ほか46ページが同じ描画であることを確認した。検査済みの同じPPTX・PDFを納品先へコピーした。

公式配布ページはCSS4件・Source Sans Proの適用を確認して撮影した。ギャラリーへ「言語 / 質問応答 / 2024」で登録し、ラベルは増やしていない。表紙からサムネイルを再生成し、タイトル検索では略称と正式名称を検索できるようにした。制作・集計・検証の一時スクリプトと、取得した全CSVはコミットしていない。

データカードはMITを指定する。引用元を実例ページへ対応させ、評価コードのMIT表記は既存の [simple-evals-MIT.txt](licenses/simple-evals-MIT.txt) で保持している。

PC 1440px・モバイル390pxのブラウザーで、19件の表紙、MMMLUの略称・全角表記・正式名称の検索、複合フィルター、公開年ソート、タイトルの1行省略、PDF/PPTXリンク、JSON-LDを確認した。ブラウザーエラー・モバイルの横はみ出しは0件。公開用ファイルが検査済みのPPTX・PDFと同じbytesであることも確認した。

## 2026-10-18：正解表示と出典表現の再確認

正解の読みやすさ・個人の好みのえんじ色と、本文の図表番号を確認した。原文・訳・正解値・統計値・評価条件・ページ数を保持。Codexによるスキル適用、Gemini使用なし。[変更対と最終版の検査](skill-proofreading/mmmlu/answer-style-review.json)。
