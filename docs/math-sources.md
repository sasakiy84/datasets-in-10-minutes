# MATH — 出典・実データ・検証記録

2026-10-18取得。日本語、sasakiy84、所属なし。共通SlideMaster由来のnative PPTXと、その最終PPTXから専用LibreOffice profileで出力したPDF。本編31頁・全55頁。本編の黙読・流し読み約10分を予定し、閲覧時間は未実測。

## 一次資料

- Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, Jacob Steinhardt. 2021. **Measuring Mathematical Problem Solving With the MATH Dataset.** NeurIPS Datasets and Benchmarks. https://arxiv.org/abs/2103.03874
  - §3.1の正式名称Mathematics Aptitude Test of Heuristics、12,500問・学習7,500/test5,000、7分野・Level1〜5、AMC/AIMEとAoPS由来、LaTeX/Asymptote、boxed解答を使用。
  - Table2のGPT-2 1.5B 6.9%（AMPS事前学習と微調整）、GPT-3 175B 5.2%（8例提示）。全testの値で、HELMのLevel1評価と区別した。
  - 人の成績はtestから20問、6人の大学生、1時間・手計算という条件。正解数8/13/14/15/18/18を保存。全5,000問に対する人の成績へ拡張しない。
- 公式リポジトリ https://github.com/hendrycks/math — README、MIT LICENSE、取得先リンク。公式READMEが案内する取得先は https://huggingface.co/datasets/qwedsacf/competition_math 。GitHub画面をCSS・フォントが読み込まれたChromiumで撮影し、実際に目視。主要リポジトリ内容とREADME見出しを表示し、正確なURLを掲載。スクリーンショットログ保存。
- Percy Liang et al. 2023. **Holistic Evaluation of Language Models.** TMLR. https://arxiv.org/abs/2211.09110
- 固定実装 https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/math_scenario.py — 原実行の問題抽出、公式提示8問、参照解説、get_answer、is_equiv、is_equiv_chain_of_thought。
- 2026-10-18取得のmain実装も保存した。現mainはhendrycks/competition_mathのrevision71b758ecc688b2822d07ffa7f8393299f1dc7cacを読み、問題でsortした後seed42でshuffleする。2023年の公開runを現mainで再実行した値として扱っていない。

## 固定した配布と実例

分割付き配布: https://huggingface.co/datasets/EleutherAI/hendrycks_math 、revision **21a5633873b6a120296cce3e2df9d5550074f4a3**。7分野×train/testの14 Parquetを全件取得、合計 **4,883,857 bytes**。学習7,500・test5,000件。公式READMEリンク先のqwedsacf/competition_mathはrevision **e839825f9ec5c6cfa585c654a59610969ec13993**、1つのtrain Parquetに12,500件（**4,848,345 bytes**）。双方のproblem/solution/level/typeの4フィールドを、重複数も含むCounterで照合し、12,500件すべて一致した。

実例はtestから本編3件＋追加10件、全7分野とLevel1〜5を含める。固定revision・subject・testの行番号が再現可能な位置。`algebra/test/372`のようなIDはこの資料の位置キーであり、元の競技問題番号とは呼んでいない。raw problem/solution/answer、分野・難度、表示原文、訳、説明、SHA-256をexamples.jsonへ保存。原文は各問題全文で、訳の同居のために分割していない。図が問題文に必須な例を選んでいない。LaTeXの数式は、意味を保ったnative Unicode文字・上付きrunで組版し、元のLaTeXを別途保持する。問題・答え・解説は画像化していない。OfficeMathの試作はLibreOfficeで欠落したため採用せず、最終PPTXは編集可能なnativeテキストを使用する。

13最終解答は、元solutionの最後のboxedから取り出して照合。さらにSymPyと整数の総当たりで13件を独立に確認した（mathematical-answer-check.json）。例3は正の偶数a,b,cを直接列挙して35。例13はsin=4/5、cos=−3/5、和1/5、二乗和1、正弦正、tan=−4/3を確認。配布解説の最後の分数に符号配置の誤りがある点をAppendixで具体的に説明し、原レコードは修正していない。

## HELMの範囲と採点

Classic latest固定版v0.4.0（2023-11-17）のmath_regular / math_chain_of_thoughtを統合し、別資料として水増ししない。966 runすべてlevel=1。今回の3モデル×7分野×2条件は42 run、元suiteはv0.3.0。各run3試行、num_outputs=1、temperature=0、max_eval_instances=1000。

各分野のLevel1 test件数は、Algebra135、Counting39、Geometry38、IntermediateAlgebra52、NumberTheory30、Prealgebra86、Precalculus57。合計**437問**で、全MATH test5,000問の**8.74%**。Level2〜5を評価した成績と混同しない。

regular: use_official_examples=True、use_chain_of_thought=False。コード内の公式8問と最終解答を提示、max_tokens20、stop `$`。CoT: use_official_examples=False、use_chain_of_thought=True。同じsubject/Level1のtrain問題と解説を提示、max_tokens400、stop `###`。両条件とも最大提示数8、候補1。

実提示数はregularでは3モデルとも全分野8、CoTのtext-davinci-003とAnthropicも8。OPT CoTはgeometry5.87719、intermediate_algebra5.16026、precalculus6.87719、残り8。prompt_truncatedは42 runすべて0。設定上の8例を一律に実提示数と呼ばない。

本文のモデル比較は**独自の件数重み付き再集計**。各分野で3試行平均したaccuracyを、評価問題数で重み付けして437問にまとめる。公式画面の集約をそのまま転記したと称していない。regular/CoTの順に、OPT 6.2548%/1.9069%、text-davinci-003 38.2914%/47.5210%、Anthropic 17.6201%/16.0946%。各subjectの値と計算条件はstats.json、exact adapter/scenario specsはevidence/selected-run-specs.json、42URL/bytes/SHAはfetch-log.json。

数学の同値判定は、一般のCASではなく、空白・単位・分数・平方根などの文字列表記を正規化して一致を取る。CoTは生成と参照の最後のboxedを取り出してから同じ正規化を行う。途中の各等式や推論を個別採点しない。

実際の生成はAlgebra/Level1の同一問題（x=15,y=5、HF test row372）。regular trial0/id8は100、CoT trial0/id178はboxed{200}を出力。参照解答200に対して歴史実装の比較関数をそのまま使い、0/1を再現した。元request、8提示例、出力全文はhelm-generation-{regular,cot}.jsonに保存。両run各405 request（135問×3試行）を全件再採点し、公開値28.148148%と50.370370%に完全一致。さらにAlgebra Level1の135問題全文が固定Parquetと一致することを確認した。

## 帰属と利用条件

公式コードはMIT（Copyright 2021 Dan Hendrycks）。両Hugging FaceデータカードもMITを表示する。収録された競技問題とAoPS上の解説の著者・出所の帰属は保持し、これらの元素材の著作権をコードのライセンスにより移転されたものと扱わない。各引用頁にMATH・配布元・分野/行位置を付け、元の問題・解説・元のLaTeXを保存した。日本語訳・説明は本資料制作者による。

## 校正・描画・構造

master-guided-slides、dataset-introduction-slides、japanese-proofreadingを適用。method/review_mode=skill_based_codex、gemini_used=false。実際の修正対6件と全55頁の最終文言・ページ別校正記録を保存。数式・原文・数値は勝手に自然化せず、訳と表示組版の対応を確認。本文中に「原著」「論文Table番号」を繰り返していない。

全55頁のoverviewと、**各55頁を実際に1頁ずつview_image**。引用15枠、13問題、8native表、1native chart、コード、公式画面、参考文献を拡大して確認。表のa/b列を中央揃えにし、隣の範囲列との間隔を確保した。生成例の引用・採点・訳の間隔を調整。コードの最終行からfooterのgapを修正。LaTeXのfrac命令のバックスラッシュを訂正し、変更頁も再確認。数式の上付き、平方根、負号、π、≤、終行とfooter間隔を目視。編集後のPPTXからPDFを再出力し、最終版を一致させた。

package-audit: ZIP、内部参照、shape ID、標準XSDを検査。マスター由来11件と整数buSzPctの字句形式差を分離し、新規XSDエラー0。native tables8/charts1、数式はnative text、notesSlideなし。layout/textは319段落・87セルをPDF字形と照合し問題0。46個のnative URL-only runとPDFリンクの実文字範囲も完全一致。独立レビューはメインへ引き継ぐ。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/math.json)、[実際の校正対](skill-proofreading/math.md)、[全ページ文言](skill-proofreading/math/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/math/review.json)。
