# MMMU-Pro：出典と確認範囲

2026-10-16作成。日本語「datasets in 10 minutes」。本編35枚＋Appendix31枚、計66枚。作成者sasakiy84、所属欄なし。大学水準の図表・画像を使う質問応答について、実例、採点、作成方法、構成、MMMUからの発展、公開後の修正を紹介する。本編の黙読・流し読みは、入口30秒、課題と実例200秒、評価150秒、作成と構成140秒、発展と利用80秒、計600秒を想定する。閲覧時間は未実測。

## 選定と現行モデルでの利用

[Google DeepMind, Gemini 3.1 Pro](https://deepmind.google/models/gemini/pro/)の公式Performance表を今回ライブ取得し、MMMU-Pro / No tools欄を確認した。Gemini 3.1 Pro Highは80.5%、GPT-5.2 xhighは79.5%、Claude Opus 4.6 Maxは73.9%。推論設定とツール条件を表に添えた。公式MMMUサイトの公開リポジトリにあるleaderboard_data.jsonでも、Gemini 3.1 Proのpro.overall 80.5を照合した。モデルのAPI評価は実施していない。

## 一次資料と改訂

- Xiang Yue, Tianyu Zheng, Yuansheng Ni, Yubo Wang, Kai Zhang, Shengbang Tong, Yuxuan Sun, Botao Yu, Ge Zhang, Huan Sun, Yu Su, Wenhu Chen, Graham Neubig. *MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark*. ACL 2025。参照PDFは[arXiv:2409.02813v3](https://arxiv.org/abs/2409.02813v3)、2025-05-22、53ページ。共同第一著者は冒頭3名。データ初公開は2024-09-05。
- Xiang Yue, Yuansheng Ni et al. *MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI*. CVPR 2024。[arXiv:2311.16502](https://arxiv.org/abs/2311.16502)。初公開年は2023年。正式タイトル・著者・発表先は公式のBibTeXとも照合した。
- [公式コード](https://github.com/MMMU-Benchmark/MMMU)：固定コミット`268471d0d488258990025331c7528359c324aa25`。MMMU-Proのevaluate.py、推論コード、prompts.yaml、公開GPT-4o評価レコードを参照。
- [公式配布データ](https://huggingface.co/datasets/MMMU/MMMU_Pro)：今回APIで確認した改訂`0d7426df4ccb3d8704a992fe6850abee7c262127`。データカードも今回再取得し、2026-10-04までの更新履歴を確認した。
- 公式サイトの公開ソース：MMMU-Benchmark/mmmu-benchmark.github.io、コミット`9092d1bda95bd2f957c323fc8957c89db6944c5a`。leaderboard_data.jsonを補助照合に使った。

論文とGitHub公開リポジトリは同日の先行調査で取得した保存版を参照した。公式サイト本体とdatasets-server、およびParquetの配布ストレージは、この環境の経路でCONNECT 403となった。全配布画像の取得・全データ実行はしていない。実例画像は論文の実際のVision入力画像を抽出し、課題文・選択肢・正解・科目は固定した公式公開評価レコードと対応させた。分布集計も同レコードを対象とし、取得できていない現行Parquetを全件検査したとは扱わない。

冒頭は公式Hugging Face配布ページの実スクリーンショット。CSS 2件とSource Sans Proの本文スタイル、表・見出しの描画をブラウザで確認した。アバターやデータプレビューの外部画像には接続できないものがあるが、掲載画面の主要な見出しと表はスタイルが反映されている。見出し・URLも「公式配布ページ」に対応させた。

## 掲載した13実例

画像は論文内に埋め込まれたVision入力そのものを抽出して使用した。架空の画面や対話を生成していない。3例を本編、10例をAppendixに掲載し、日本語の課題内容と正解を編集可能な文字で添えた。数学と計算機科学の図の拡大はPPTXの画像クロップで作り、元の入力画像も同じ実例に掲載している。

|掲載ページ|科目|課題ID|正解|画像の出所（論文ページ）|
|---|---|---|---|---|
|8|Economics|`test_Economics_47`|D|29|
|10|Math|`validation_Math_16`|A|36|
|12|Computer_Science|`validation_Computer_Science_29`|A|49|
|39|Art|`test_Art_227`|G|24|
|40|Art_Theory|`test_Art_Theory_19`|E|25|
|41|Music|`test_Music_209`|G|27|
|42|Biology|`validation_Biology_30`|C|33|
|43|Geography|`test_Geography_90`|B|35|
|44|Physics|`validation_Physics_9`|B|37|
|45|Basic_Medical_Science|`test_Basic_Medical_Science_72`|E|38|
|46|Electronics|`test_Electronics_76`|B|50|
|47|Materials|`test_Materials_423`|F|52|
|48|Mechanical_Engineering|`test_Mechanical_Engineering_409`|B|53|

全13件のID・正解は公式公開レコードと一致し、課題はすべて異なる。図・入力内の文字・候補の順序も目視確認した。地理のBはimage_5、音楽のGは画像内の2番目、計算機科学のAは`([1-9][0-9]*)|0`に対応する。材料の順序C,A,B,D、電子工学の−8,−10,20 V、機械工学の196.9,166.7 psiも論文のGround Truthと対応する。

経済の購入費用は2014年58,280ドル、2015年40,820ドルで、比率×100を四捨五入すると143。数学の制約はx₁²−x₂−3≤0、x₂≤1、x₁≥0で、目的は点(3,2)への距離の二乗の最小化。正解(2,1)との対応を確認した。

## 構成・作成方法・統計

論文の作成手順は、4モデルに画像なしで各10回解かせ、6回以上正解したモデルが3つ以上の問題を除外する。その後30科目から60問ずつ1,800問を抽出。GPT-4oによる候補生成、Claude 3.5による候補選別、2回の人手確認を経て70問を除き、1,730問となる。背景・文字サイズ・書体を変えた画面の写真／スクリーンショットを作る。

配布構成はstandard (4 options)、standard (10 options)、visionの3つで、同じ1,730問題に対応する。構成名の10 optionsを、すべての問題が厳密に10択であるという意味にはしていない。本編に8択の計算機科学の実例を置き、問題により選択肢数が異なることを具体的に示した。

統計の対象は固定コミットの`mmmu-pro/output/gpt-4o_standard(10 options)_cot.jsonl`にある1,730件・1,730種類のID。モデルのresponseを集計するのではなく、公開されたsubjectフィールドを集計した。6分野への対応は公式evaluate.pyのDOMAIN_CAT2SUB_CATを用いた。

- 芸術・デザイン228、ビジネス286、科学291、健康・医学286、人文・社会科学222、技術・工学417問。合計1,730問。
- 科目は30種類、各50〜60問。最少のManageは50問。Appendixの7ページで全30科目を掲載。
- Proの配布splitはtest。IDに含まれるtest／validationは元MMMUの識別子に由来する。
- 元のMMMUは開発150、検証900、テスト10,500。2026-02-12のテスト正解公開は公式READMEを出典とした。

2025-03-08の画像ラベルと選択肢の対応修正、2026-05-30の診断・検査医学の選択肢修正、2026-07-10のデザイン・芸術理論の正解修正、2026-10-04の化学の選択肢と金融の不足条件の修正を説明した。元のMMMU、Proの初公開、Pro公開後の修正を本編でつなげた。

## 評価と初期結果

公式evaluate.pyのparse_multi_choice_response、eval_multi_choiceを読み、モデルAPIを呼ばずに同ファイルの関数定義を抽出して実行した。全13実例で`Answer: 正解記号`が正解となり、別の記号が不正解となることを確認した。各形式は問題単位の正解率で、科目をまとめるときは問題数で重み付けする。総合はStandardの拡張選択肢版とVisionの平均という論文の定義に従った。

初期結果はYueらの論文に対応させた。

|モデル|元の選択肢|拡張選択肢|Vision|総合|
|---|---:|---:|---:|---:|
|GPT-4o (0513)|64.7|54.0|49.7|51.9|
|Claude 3.5 Sonnet|63.7|55.0|48.0|51.5|
|Gemini 1.5 Pro (0801)|60.6|49.4|44.4|46.9|

Direct／CoTの高い方を報告する論文の設定を表注に示した。OCR指示の有無の別表はGPT-4o 49.7／49.4、Gemini 1.5 Pro 44.4／43.6、GPT-4o mini 35.2／35.6%。誤答の原因は論文のGPT-4o Vision誤答60件の分析を使い、推論46%、知覚27%、知識不足25%、注釈2%を示した。手元でモデルの誤答を再分類した値ではない。

## 制作・検査・公開

共通SlideMaster.pptxを使用。表紙52 pt太字、Noto Sans／Noto Sans CJK JP、帯14 pt太字、コードLiberation Mono。編集可能な表18個・グラフ2個。上端・下端1.2 pt、見出し下0.6 pt、縦罫なし。発表者ノートなし。

全66ページを描画し、6枚のコンタクトシートを目視確認した。全190セル、本文と出典の間隔、56件のURLリンク範囲、文字欠落・ページ外要素・タイトル改行を検査し、問題なし。本文と出典の最小間隔9.40 pt。PDFで数式記号の抽出順序が変わる箇所は、描画位置順の文字抽出と目視を併用して、表示上の欠落と区別した。

PPTXのZIP・内部参照・83 XML部品を検証。既知のbuSzPct字句判定130件以外にスキーマエラーなし。buSzPctの値はOpen XML SDKの25000〜400000の範囲内。最終PPTXから出力したPDFを納品する。

ギャラリーの12件目としてCSVに登録。種別「画像」、タスク「質問応答」、公開年2024。新しい分類ラベルは増やしていない。タイトル検索、複合フィルタ、年順、12件の表紙とリンク、JSON-LD、390 px幅の表示をブラウザで検査し、全項目を通過した。

## 権利表記

データカードと公式リポジトリはApache License 2.0を指定する。論文とデータの著者・出所を各実例の脚注に記し、日本語の説明と図の拡大を加えた。公式リポジトリのライセンス全文を[mmmu-Apache-2.0.txt](licenses/mmmu-Apache-2.0.txt)に保持する。

## コード枠のレイアウト再点検

57ページのコード最終行が背景からはみ出していた。全ページを見直した結果、33ページのコード枠にも同じ問題を確認した。倍率で指定した行間の実描画と、文字サイズ×倍率で見積もった背景高が一致せず、上揃えも明示されていなかった。前回の検査は文字欠落・ページ外・出典間隔を中心としており、コードと背景の包含関係を見落としていた。

両ページの行送りをptで指定して上揃えにし、57ページは空行を1行除いて、背景と後続説明の位置を調整した。33ページのコード実文字の上下余白は10.66／11.27 pt、57ページは10.79／11.02 pt。修正前の背景外はみ出し（33ページ5.55 pt、57ページ7.86 pt）を検出できる検査で、修正後の背景内への収まりも確認した。

全66ページの275テキスト枠について、実文字領域同士と画像との重なりを検査し、問題なし。全190セル、本文と出典の最小間隔9.40 pt、56件のURLリンク、PPTX構造も再検査した。全ページのコンタクトシートを目視し、コード2ページは拡大画像でも確認した。旧版とPDFの文字・描画を比較し、変更ページが33・57のみであることを確認。共通スキルのコード配置手順にも、倍率指定の行間を文字サイズだけで見積もらず、描画した最初と最後の行の境界を確認する手順を追記した。
