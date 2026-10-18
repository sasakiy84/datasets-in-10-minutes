# LexGLUE — 一次資料、配布、検証範囲

2026-10-18取得。著者sasakiy84、所属なし。日本語・本編29頁/全57頁、約10分の黙読・流し読みを予定（時間は未実測）。元の条件を保持し、native PPTXと最終PPTX由来PDFを制作する。

## 一次資料

- Ilias Chalkidis, Abhik Jana, Dirk Hartung, Michael Bommarito, Ion Androutsopoulos, Daniel Martin Katz, Nikolaos Aletras. 2022. LexGLUE: A Benchmark Dataset for Legal Language Understanding in English. ACL, pp.4310–4330. https://aclanthology.org/2022.acl-long.297/ 。正式ACL PDFとarXiv2110.00976のPDFを保存。正式PDFの本文/表を確認し、7課題の定義、収集と簡略化、時間分割、モデルの長さ、5seedから開発最良seedのtest値、F1の空集合処理を採用した。
- 公式リポジトリ https://github.com/coastalcph/lex-glue 。README、repo-tree、4つの評価・前処理コードを保存。ChromiumでCSS/フォント/主要画像を実際に描画して撮影し、view_imageで確認。正確なURLを冒頭に付けた。READMEとデータカードの表は現在値と論文値が混在するので、取得Parquetの件数を別に実測した。
- LEGAL-BERT: The Muppets straight out of Law School (Chalkidis et al., Findings EMNLP2020)、LEDGAR: A Large-Scale Multi-label Corpus for Text Classification of Legal Provisions in Contracts (Tuggener et al., LREC2020)、When Does Pretraining Help? Assessing Self-Supervised Learning for Law and the CaseHOLD Dataset of 53,000+ Legal Holdings (Zheng et al., ICAIL2021)はLexGLUEにおける出発点として参考文献に記載。正式タイトル・著者年・掲載先・内容説明を保ち、2件ずつ掲載する。

## 固定配布と13例

公式READMEが案内するHugging Face lex_glueの現canonical名はcoastalcph/lex_glue。revision **c23fdff1a6bf74e0e1a71cb86f1e781d37da888c**。7subsetのtest Parquetを固定revisionのresolve URLから取得し、bytes/SHAをfixed-fetch-log.jsonに記録。合計82,321,269 bytes。学習/開発件数は固定READMEのdataset_info、test件数と空ラベル件数はParquet全件実測。rows APIの先頭100件を各subsetから取得して候補探しをしたが、採用13件は必ず固定Parquetに再照合した。rows APIのHEAD取得時点だけを固定版と呼んでいない。

本編3例＋追加10例。7subsetをすべて含む。examples.jsonにはraw_record全文、原入力全文、表示原文、範囲、訳、参照の整数とClassLabel名、revision、resolve URL、位置キー、record SHAを保存。SHAはraw_recordのensure_ascii=False/sort_keys=True/separators=(',',':') JSONに対するSHA-256。位置キーはtask/test/行位置であり元の事件番号ではない。実例10/12/13は以下の抜粋で、正解は元レコード全体に付く。ほか10件は入力内容全文を保持する。

- 実例10 ecthr_b/test/26: 事実列の先頭2段落。元の事実全文は6,330文字程度で、2段落だけをHELMの全入力とは呼ばない。Task A/Bの同じ事実列が完全一致し、A=[]、B=[1]（条約3条）であることも照合。
- 実例12 eurlex/test/60: 文書冒頭からWhereas直前までの連続範囲。整数7/91/96/97に対応するEuroVoc IDは100174/100277/100282/100283。
- 実例13 case_hold/test/38: contextの「Turner concedes」から末尾まで。全5候補を省略せず保存・表示。元contextは判決からの切り出しで文頭/文末が途中になりうる。答え1は0始まり（2番目の候補）。選択肢と参照の意味の対応も確認。
- 実例11 SCOTUSは改行・連続空白だけを整理。単語・文字内容・順序は保持。訳は当事者の立場と氏名を省かない。

13件は公開された参照ラベルを紹介する。モデルが本資料のために生成した出力はなく、架空の予測を実測として示していない。UNFAIR-ToSの法律注釈は元データの注釈であり、制作者による個別の法的効力の判断ではない。

## 配布と論文の差

正式論文のCaseHOLD testは3,900、固定配布は3,600。SCOTUSは論文14分野に対し固定featuresのClassLabel名は1〜13。差が生じた特定の経緯は未確定であり、前処理コードを見つけたことだけで差の原因と決めない。testの空集合はECtHR A153/1000、B14/1000、UNFAIR-ToS1435/1607=89.30%。論文の全分割を含む説明と、固定testの独自実測を分けた。

## 採点と公表スコア

micro-F1はTP/FP/FNをラベル全体で合算、macro-F1は各クラスのF1の平均。ECtHR A/BとUNFAIR-ToSは評価時に空集合を表す追加クラスを設ける（学習時の出力を増やす処理とは別）。CaseHOLD公式実験コードも候補番号に対してmacro/micro F1を計算する。microは単一ラベル正解率と一致するが、macroと正解率を一般に同一とはしない。

本文のtest macro-F1は正式ACL論文のBERT / Legal-BERTを転記。ECtHR A63.6/64.0、B73.4/74.7、SCOTUS58.3/66.5、EURLEX57.2/57.4、LEDGAR81.8/83.0、UNFAIR-ToS81.3/83.0、CaseHOLD70.8/75.3。各課題で教師あり微調整、5 seedのうち開発成績最良seed。階層モデルは最大64段落×128token、Longformer/BigBirdは4096token。この比較をHELMの少数例提示の得点とは呼ばない。

## HELM固定版

Classic latestの固定release **v0.4.0 (2023-11-17)**。schemaにlex_glue群、主指標classification_macro_f1/testがある。release全run_specsのnameにlex_glueを含むか、scenario class_nameにLexGLUEを含むものを検索して**0 run**。元snapshot全体のSHAと母数はstats.json。実行されたモデル/試行/実提示数/切詰め率/スコアを捏造せず未観測として記す。

v0.4.0のscenarioとrun_specsを一次コードとして保存。ECtHR A/B/SCOTUSは提示上限1、ほか5。出力上限はSCOTUS/CaseHOLD5token、ほか20token。MLTCは整数idxをstrへ、SLTCはClassLabel名へ、QAは候補番号ClassLabel名へ変換。ECtHRは段落を空白で連結。CaseHOLDはcontext＋番号付き全5候補。誤参照をseed42でshuffleし最大30件に絞る。100クラスを常に全件参照として保持するとは説明しない。

SCOTUSの具体例はencoded8→ClassLabel'9'→HELM参照'9'。説明は0始まりで8=Judicial Power、9=Federalismと列挙するため意味がずれる。EURLEXの参照はEuroVoc IDそのものではなくidx文字列7/91/96/97。QAのCaseHOLDはget_lex_glue_specの分類指標を追加するMLTC/SLTCの分岐に入らない。schemaが存在することだけから全7taskに公表スコアがあると読まない。docstringのUNFAIR-ToSの終了文→変更ラベルという記述も、実際の参照生成や配布レコードと区別した。

## 帰属と権利

固定Hugging FaceカードはCC BY 4.0を表示。元の裁判所・EU機関・契約/規約の作成者等の帰属は保持し、元素材の著作権まで一律に変更されたとは扱わない。公式repo root LICENSEは取得時404、recursive treeでもlicense名ファイルが見つからなかった。コードのMIT等を推測で付けない。各引用頁で元データの作成者に帰属する旨と配布元・行位置を掲載。訳と説明は制作者による。

## 組版・校正と検査

共通マスターを使用し、native編集可能な引用/答え/本文/コード/表。ノートなし。独立答えはbold21.5pt、#B13731。長文7件のEN/JP同居を15pt・幅4.6/4.0inで実際にPPTX/PDFへ描画し、coexist-pages全7頁をview_image。成立した実例8/10/11/12を採用（11は空白整理後に最終実描画で確認、12は最終5.0/3.6inで調整）、ほか3/9/13は原文を分割せず訳を別頁へ。SCOTUSは改行・連続空白を整理すると、原文内容と訳の全文を1頁に同居できた。EUR-LEXの抜粋も段落改行だけを整理した。

master-guided-slides、dataset-introduction-slides、japanese-proofreadingを適用。method/review_mode=skill_based_codex、gemini_used=false。実際の校正・情報保持修正対と各頁最終文言を保存する。PDF/PNG/overviewから実際にview_imageした頁だけを記録。引用余白はPDF字形→PNG実画素の順に測り、余白・最終行・答えとfooterの間隔を調整する。構造・XSD・native URL-onlyリンクの監査を行い、独立レビューへ引き継ぐ。


最終検査：57頁を各1頁ずつ実際にview_image、overviewも確認。最終変更1/7/14/15/41/42/43/44/45/48/49頁を再確認。引用20枠のPNG実画素は上6.67〜8.0pt・下7.33〜8.0pt、上下差は最大1.33pt。layout326段落127セルで問題0、native表8・コード1、50URL-onlyはPDF範囲まで完全一致、新規XSD0（baseline11を分離）。日本語校正実修正6対。独立先行レビューの正式展開形・初公開年・ineffective counselの訳・頻出100の指摘を反映済み。

初公開はarXiv v1の2021-10-03。year=2021は初公開年、本文の2022はACL発表年と正式版の評価値。証拠arxiv-v1.html/citation_dateを保存。LexGLUEの正式展開形はLegal General Language Understanding Evaluation。

独立最終レビュー対応：p49の比較表に正式ACL論文と固定配布の2出典を併記。最終PPTX/PDFを同期してp49実view、layout326段落127セル0・50URL-only完全一致を確認。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/lexglue.json)、[実際の校正対](skill-proofreading/lexglue.md)、[全ページ文言](skill-proofreading/lexglue/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/lexglue/review.json)。
