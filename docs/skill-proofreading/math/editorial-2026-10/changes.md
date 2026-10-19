# MATH：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|3|3|評価基盤固有の比較から、元データの採点と登場時の評価へ構成を戻す|競技数学の問題と解答<br>採点とHELMの比較条件<br>収集とデータの全体像<br>利用の変化と入手方法|競技数学の問題と解答<br>最終解答の採点と2021年の成績<br>収集とデータの全体像<br>公開配布と利用方法|
|2|12|11|読者に必要な説明へ整理|採点とHELMの比較条件|最終解答の採点と2021年の成績|
|3|12|11|読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|4|13|12|読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|5|14||読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|6|15||読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|7|16||読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|8|17|13|読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|9|18||読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|10|19||読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|11|20||読者に必要な説明へ整理|2. 採点とHELMの比較条件|2. 最終解答の採点と2021年の成績|
|12|26|19|読者に必要な説明へ整理|利用の変化と入手方法|公開配布と利用方法|
|13|26|19|読者に必要な説明へ整理|4. 利用の変化と入手方法|4. 公開配布と利用方法|
|14|27|20|読者に必要な説明へ整理|4. 利用の変化と入手方法|4. 公開配布と利用方法|
|15|28|21|読者に必要な説明へ整理|4. 利用の変化と入手方法|4. 公開配布と利用方法|
|16|29|22|読者に必要な説明へ整理|4. 利用の変化と入手方法|4. 公開配布と利用方法|
|17|30|23|読者に必要な説明へ整理|4. 利用の変化と入手方法|4. 公開配布と利用方法|
|18|31|24|読者に必要な説明へ整理|4. 利用の変化と入手方法|4. 公開配布と利用方法|
|19|33|26|読者に必要な説明へ整理|分野と難度が異なる追加例<br>実行条件と配布の補足<br>研究と参考文献|分野と難度が異なる追加例<br>解答と人手評価の補足<br>研究と参考文献|
|20|45|38|読者に必要な説明へ整理|実行条件と配布の補足|解答と人手評価の補足|
|21|45|38|読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|22|46||読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|23|47||読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|24|48||読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|25|49||読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|26|50|39|読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|27|51|40|読者に必要な説明へ整理|Appendix: 2. 実行条件と配布の補足|Appendix: 2. 解答と人手評価の補足|
|28|5|5|作成主体を示し、最終解答の形式と用途を元研究から説明する|MATHは、競技数学の12,500問に、途中の解説と最終解答を付けたデータセット。<br>AMCやAIMEなど、米国の数学競技から問題を集めた。入力は英語の問題文で、数式や図の記述も含む。<br>最終解答はLaTeXのboxedに入る。解答だけを出す条件と、解説を含めて出す条件の両方で使われる。|MATHは、競技数学の12,500問に、途中の解説と最終解答を付けたデータセット。Dan Hendrycksらが2021年に公開した。<br>AMCやAIMEなど、米国の数学競技から問題を集めた。入力は英語の問題文で、数式や図の記述も含む。<br>解説の最後には、LaTeXのboxed命令で囲んだ最終解答がある。問題から解答を生成する学習や評価に使える。|
|29|13|12|採用先の条件ではなく、MATH本来の最終解答抽出と正規化・正解率を説明する|生成した最終解答を、参照解答と照合する。空白やLaTeXの一部を整え、分数や平方根などの表記をそろえる。<br>各問を正解1・不正解0で採点し、評価集合の正解率を求める。<br>chain-of-thought条件でも、採点するのは最後のboxedから取り出した解答。途中の推論を個別には採点しない。|生成した最終解答を、参照解答と照合する。解説を生成する場合は、最後のboxedの中から解答を取り出す。<br>空白やLaTeXの一部を整え、分数や平方根などの表記をそろえて比較する。例えば1/2と\frac{1}{2}は同じ答えとして扱う。<br>各問を正解1・不正解0で採点し、正解した問題の割合をAccuracy（正解率）として求める。|
|30|13|12|読者に必要な説明へ整理|[1] Stanford CRFM. MATHScenario v0.3.0. 参照解答の抽出と表記正規化。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/math_scenario.py|[1] Hendrycks et al. (2021). Measuring Mathematical Problem Solving With the MATH Dataset. NeurIPS Datasets and Benchmarks.<br>https://arxiv.org/abs/2103.03874|
|31|17|13|評価対象を保持し、AMPSの役割を簡潔に説明する|MATH test全5,000問、全7分野・全難度。AMPSは別の数学事前学習データで、MATHとは区別される。|MATH test全5,000問、全7分野・難度1〜5を評価。AMPSは、数学の基礎を学ぶために同時公開された別の事前学習データ。|
|32|24|17|基盤固有のLevel1抽出説明を外部化する|test全5,000問の件数。HELMの公開評価はLevel 1の437問。|test全5,000問の、難度ごとの件数。|
|33|25|18|AoPSを初出で導入し、難度の意味を具体的に示す|難度は各分野の中で1〜5を付ける。1が易しく、5が難しい。<br>AoPSの難度を使い、AMC 8の序盤の問題はLevel 1、AIMEの問題はLevel 5に当たることが多い。<br>分野と難度は別の注釈。例えば複素数の絶対値や三角関数も、Level 1に含まれる。|各分野の中で、難度を1〜5で表す。1が易しく、5が難しい。<br>Art of Problem Solving（AoPS）の難度を使い、AMC 8の序盤の問題はLevel 1、AIMEの問題はLevel 5に当たることが多い。<br>複素数の絶対値や三角関数も、分野内で易しい問題ならLevel 1に含まれる。|
|34|27|20|読者に必要な説明へ整理|数学の学習と、汎用モデルの評価に使われる|数学の基礎学習と、競技問題の追加学習をつなぐ|
|35|27|20|不要な採用先の利用紹介を外し、元研究の学習資源と公開利用へつなぐ|2021年は、解説付きデータでの学習と、別途AMPSでの数学事前学習を組み合わせて評価した。<br>HELMでは、学習例をプロンプトに入れる方法で複数の汎用言語モデルを比較した。<br>2026-10-18時点で公式リポジトリ、固定した公開配布、HELMの実装を取得できる。|2021年の研究では、数学の事前学習データAMPSも公開した。Khan Academyの練習問題と、Mathematicaで生成した問題・解説からなる約23 GBのデータである。<br>GPT-2はAMPSで事前学習してから、MATHの問題と解説・最終解答で追加学習した。解法を学ぶことが、答えだけを学ぶ場合より役立つかも調べた。<br>公式リポジトリは、MATHとAMPSの取得先、データを読むコード、解答の評価コードを案内している。|
|36|27|20|読者に必要な説明へ整理|[1] Dan Hendrycks et al. MATH. 公式リポジトリ。2026-10-18参照。  https://github.com/hendrycks/math|[1] Hendrycks et al. (2021). Measuring Mathematical Problem Solving With the MATH Dataset.<br>https://arxiv.org/abs/2103.03874<br>[2] Hendrycks et al. MATH. https://github.com/hendrycks/math|
|37|28|21|読者に必要な説明へ整理|分野、分割、バージョンを固定して読む|分野と分割を選び、問題と解説を読み出す|
|38|28|21|公開Parquetを読む最小コードを載せ、40文字の固定revisionは外部記録へ移す|from datasets import load_dataset<br>data = load_dataset(<br>    'EleutherAI/hendrycks_math', 'algebra',<br>    revision='21a5633873b6a120296cce3e2df9d5550074f4a3',<br>    split='test',<br>)<br>print(data[372]['problem'])<br>print(data[372]['solution'])|import pyarrow.parquet as pq<br>data = pq.read_table("algebra-test.parquet").to_pylist()<br>print(data[0]["problem"])<br>print(data[0]["solution"])<br>print(data[0]["level"], data[0]["type"])|
|39|28|21|読者に必要な説明へ整理|problem、solution、level、typeを持つ。元のLaTeXも含めて保存される。|algebraのtest Parquetをalgebra-test.parquetとして保存する。problemが問題文、solutionが解説。levelとtypeが難度と分野を表す。|
|40|29|22|読者に必要な説明へ整理|公式リンクと、分割を保つ配布を照合した|公式リンク先と、分野・分割を選べる配布がある|
|41|29|22|全件照合の制作過程を外部へ移し、読者が配布を選ぶための違いを残す|公式READMEが案内する配布では、12,500問を1つの集合として取得できた。<br>今回の実例には、学習・testと7分野の分割を保つEleutherAIの公開配布を使った。<br>両方の配布を全件取得し、問題・解説・分野・難度の12,500レコードが、重複数も含めて一致することを確認した。|公式READMEは、Hugging Faceのqwedsacf/competition_mathを案内する。この配布は12,500問を一つのtrain集合に収めている。<br>EleutherAI/hendrycks_mathでは、7分野と学習・testの分割を選べる。モデルの学習や評価には、使う集合の構成を確認して選ぶ。|
|42|29|22|読者に必要な説明へ整理|[1] MATH. 公式READMEのリンク先配布。12,500件を1集合で公開。  https://huggingface.co/datasets/qwedsacf/competition_math|[1] MATH. 公式READMEのリンク先配布。https://huggingface.co/datasets/qwedsacf/competition_math<br>[2] EleutherAI. hendrycks_math. https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|43|30|23|検証用hash・取得手順・細かな配布容量比較を外部化し、利用条件を残す|公式コードと公開データカードのライセンス表示はMIT。元の競技問題やAoPS上の解説の著者・出所も保持する。<br>今回取得した分割付きParquetは合計約4.9 MB。公式リンク先の統合Parquetは約4.8 MBで、どちらも取得実測。<br>実例の問題全文・解説全文・最終解答・固定revision・レコードhashを検証記録に保存した。|公式コードと公開データカードのライセンス表示はMIT。元の競技問題やArt of Problem Solving上の解説の著者・出所も保持して利用する。|
|44|30|23|コードとデータカードの利用条件を直接出典へ対応付ける|[1] Dan Hendrycks et al. MATH. 公式リポジトリ。2026-10-18参照。  https://github.com/hendrycks/math|[1] Hendrycks et al. MATH. https://github.com/hendrycks/math<br>[2] EleutherAI. hendrycks_math. https://huggingface.co/datasets/EleutherAI/hendrycks_math<br>[3] MATH. 統合配布。https://huggingface.co/datasets/qwedsacf/competition_math|
|45|31|24|固有基盤の部分集合比較を外し、元データの目的と特徴をまとめる|MATHは12,500問の競技数学データで、7分野・5段階の難度と解説付きの解答を持つ。<br>最終解答の採点と、途中の推論の正しさは別に検討する。<br>HELMのregularと解説付き条件は、Level 1の437問を、異なる提示例と出力条件で比べる。|MATHは、12,500問の競技数学データ。7分野・5段階の難度と、解説付きの解答を持つ。<br>問題を読み、解法を組み立てて最終解答を出す能力を評価する。解説付きの学習データは、途中の解き方を学ぶ材料にもなる。<br>2021年のモデルは全難度のテストで低い正解率を示した。数学の基礎学習と、競技問題の解法学習をつなぐ研究資源である。|
|46|51|40|読者に必要な説明へ整理|解説の符号も、最終解答とは別に確かめる|配布解説には、途中の式の誤りもある|
|47|51|40|解説の実際の誤りという利用上の特徴を残し、制作側の保存説明を削る|実例13の配布解説では、sin x = 4/5、cos x = −3/5を導いた後、最後の分数で符号の位置が入れ替わっている。<br>最終解答−4/3は変わらないが、途中の式は、(4/5) ÷ (−3/5)と書くのが導出に対応する。<br>資料の解説はこの対応を保って説明し、配布解説の原文は変更せず検証記録へ保存した。|実例13の配布解説は、sin x = 4/5、cos x = −3/5を導いた後、最後の分数で符号の位置を入れ替えている。<br>最終解答−4/3は変わらないが、導出に対応する式は、(4/5) ÷ (−3/5)である。|
|48|53|42|著者位置の説明を外し、作成主体と研究の意義を紹介する|第一著者はDan Hendrycks、最終著者はJacob Steinhardt。計8人の著者による研究としてNeurIPS 2021 Datasets and Benchmarksに発表された。<br>競技数学の問題、段階的な解説、難度と分野の注釈を組み合わせ、数学的な問題解決を測る資源を作った。<br>同時にAMPSを公開し、数学に特化した事前学習データが性能に与える影響も調べた。|Dan Hendrycks、Collin Burnsら8人が構築し、NeurIPS 2021のDatasets and Benchmarks Trackで発表した。<br>競技数学の問題、段階的な解説、難度と分野の注釈を組み合わせ、数学的な問題解決を測る資源を作った。<br>同時にAMPSを公開し、数学に特化した事前学習データが性能に与える影響も調べた。|
|49|54|43|基盤論文の文献を元データ公式配布の案内へ置き換える|Holistic Evaluation of Language Models|MATH Dataset|
|50|54|43|基盤論文の文献を元データ公式配布の案内へ置き換える|Percy Liang et al. · 2023 · TMLR|Hendrycks et al. · n.d. · 公式リポジトリ（2026-10-19参照）|
|51|54|43|基盤論文の文献を元データ公式配布の案内へ置き換える|共通の適応方法と複数の指標を使い、MATHを含む多数の課題で言語モデルを比較する。|データの取得先、データを読むコード、解答の評価コード、AMPSを案内する。|
|52|54|43|基盤論文の文献を元データ公式配布の案内へ置き換える|https://arxiv.org/abs/2211.09110|https://github.com/hendrycks/math|
|53|28|21|コード枠の余白をそろえ、説明と出典の間隔を確保する|長い旧コード用の170pt枠と下部の説明|5行の実コードに合わせて背景と上下実字形余白を調整し、説明を直下へ置く|
|54|1|1|独立レビュー：全text_frame実画素境界への収容|実字形が外枠を約1.6〜2.3pt超える|heightとmargin_bottomを各8pt拡張し、文字位置を維持|
|55|32|25|独立レビュー：全text_frame実画素境界への収容|実字形が外枠を約1.6〜2.3pt超える|heightとmargin_bottomを各8pt拡張し、文字位置を維持|
|56|28|21|独立レビュー：全text_frame実画素境界への収容|説明の字形が下枠を約3.3pt超える|top−4/height＋12/margin_top＋4/margin_bottom＋8pt、文字位置を保持|
|57|6|6|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 algebra / test row 372<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|58|8|7|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 intermediate_algebra / test row 457<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|59|10|9|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 counting_and_probability / test row 445<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|60|11|10|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。  https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|61|23|16|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。  https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|62|24|17|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。  https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|63|28|21|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。  https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|64|35|28|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 prealgebra / test row 134<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|65|36|29|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 geometry / test row 235<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|66|37|30|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 number_theory / test row 345<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|67|38|31|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 precalculus / test row 235<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|68|39|32|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 algebra / test row 195<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|69|40|33|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 counting_and_probability / test row 156<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|70|41|34|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 prealgebra / test row 190<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|71|42|35|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 geometry / test row 167<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|72|43|36|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 number_theory / test row 89<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|73|44|37|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。 precalculus / test row 541<br>https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|74|51|40|固定revision・行番号・反復する帰属説明は外部記録へ|[1] MATH, EleutherAI/hendrycks_math. 固定revisionのtest分割。元の競技問題・解説の著者に帰属。  https://huggingface.co/datasets/EleutherAI/hendrycks_math|[1] Hendrycks et al. MATH. 公開データ。 https://huggingface.co/datasets/EleutherAI/hendrycks_math|
|75|7||基盤固有の生成比較を外部化|同じ問題でも、モデルの出力は異なる<br>式に値を代入すれば、(15 + 5)(15 − 5) = 20 × 10で200になる。<br>HELMの公開実行では、text-davinci-003が解答だけの条件で100、解説を出す条件で200と答えた。<br>二つの条件では提示する例も変わる。具体的な入力条件と採点は次の章で扱う。<br>1. 競技数学の問題と解答<br>[1] HELM Classic v0.4.0. MATH、Level 1の固定評価。2023-11-17公開版。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_regular||
|76|14||基盤固有の解答抽出条件表を外部化|HELMの解答抽出は条件で変わる<br>2. 最終解答の採点と2021年の成績<br>正規化した文字列の一致。一般の代数式を記号計算で同値判定する採点ではない。<br>[1] Stanford CRFM. MATHScenario v0.3.0. 参照解答の抽出と表記正規化。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/math_scenario.py||
|77|15||基盤固有の生成出力と採点を外部化。原記録は旧版に保持|同じ問題の、実際に生成された二つの出力<br>2. 最終解答の採点と2021年の成績<br>text-davinci-003 / trial 0 / x = 15, y = 5の問題<br>regular: 100<br>採点：0（参照解答は200）<br>chain-of-thought: Plugging in the given values for x and y, we get (15 + 5)(15 − 5) = \boxed{200}.<br>訳：xとyに与えられた値を代入すると、(15 + 5)(15 − 5) = 200。<br>採点：1（最後のboxedから200を抽出）<br>[1] HELM Classic v0.4.0. MATH、Level 1の固定評価。2023-11-17公開版。 regular id8 / CoT id178。本文は全文、数式は組版。<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_regular||
|78|16||生成比較の繰り返しと一般的な注意書きを外部化|正しい最終解答と、正しい推論を分ける<br>公開実行のregularは100を出したため不正解。chain-of-thoughtは最後のboxedから200を抽出できるため正解。<br>この採点は、途中の各等式や説明が正しいかを証明するものではない。<br>解説付きの学習データは、最終解答だけでは見えない解法や誤りを調べる材料にもなる。<br>2. 最終解答の採点と2021年の成績<br>[1] Stanford CRFM. MATHScenario v0.3.0. 参照解答の抽出と表記正規化。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/math_scenario.py||
|79|18||基盤固有Level1抽出と再集計を外部化|HELMはLevel 1の437問を評価する<br>HELM Classicの二つの条件は、7分野のLevel 1に絞った437問を評価する。<br>全testの5,000問のうち8.74%。Level 2〜5の4,563問は、この二つの公開グループの評価には入らない。<br>以下は各分野の実行値から、評価問題数で重み付けして再集計した正解率。各分野の値は3試行平均。<br>2. 最終解答の採点と2021年の成績<br>[1] HELM Classic v0.4.0. MATH、Level 1の固定評価。2023-11-17公開版。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_regular||
|80|19||基盤固有のモデル比較を外部化|解説付き条件の正解率はモデルで異なる<br>2. 最終解答の採点と2021年の成績<br>437問の件数重み付き再集計、各3試行。異なる提示例と出力条件を含む比較。2023年の固定版。<br>[1] HELM Classic v0.4.0. MATH、Level 1の固定評価。2023-11-17公開版。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_regular||
|81|20||生成パラメータの細目を外部化|提示例と生成条件も同時に変わる<br>2. 最終解答の採点と2021年の成績<br>二つの条件では、提示例の内容、出力上限、停止文字列も異なる。<br>[1] Stanford CRFM. HELM v0.3.0 run_specs.py, get_math_spec. 生成・適応条件。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py||
|82|46||基盤固有の分野別抽出数を外部化|Level 1の分野別評価対象数<br>Appendix: 2. 解答と人手評価の補足<br>[1] HELM Classic v0.4.0. MATH、Level 1の固定評価。2023-11-17公開版。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_regular||
|83|47||基盤固有の分野別得点を外部化|text-davinci-003の分野別正解率<br>Appendix: 2. 解答と人手評価の補足<br>[1] HELM Classic v0.4.0. MATH、Level 1の固定評価。2023-11-17公開版。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_regular||
|84|48||提示例数と処理監査を外部化|実際の提示例数はモデルと分野で異なる<br>regularでは今回の3モデルとも8例。解説付き条件でも、text-davinci-003とAnthropicは全分野で8例だった。<br>OPTの解説付き条件は、中級代数5.16例、幾何5.88例、解析の基礎6.88例が平均。ほかは8例。<br>入力を切り詰めた割合prompt_truncatedは、今回の42実行すべて0。提示例を減らして収めた場合も、この値は0になる。<br>Appendix: 2. 解答と人手評価の補足<br>[1] HELM Classic v0.4.0. MATH chain-of-thought、Level 1の固定評価。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/math_chain_of_thought||
|85|49||基盤固有採点の説明を外部化。元データの採点説明は本編へ|表記の正規化を、数学の同値判定と区別する<br>例えば1/2とLaTeXの\frac{1}{2}は、表記をそろえて一致と判定される。<br>一方で、(x + 1)²とx² + 2x + 1を一般に展開して比較する記号計算器は使わない。<br>chain-of-thought条件では、生成と参照解説の最後のboxedを取り出してから、同じ正規化を行う。<br>Appendix: 2. 解答と人手評価の補足<br>[1] Stanford CRFM. MATHScenario v0.3.0. 参照解答の抽出と表記正規化。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/math_scenario.py||
|86|55||基盤固有実装文献を外部化。公式配布文献は前頁に統合|参考文献<br>Appendix: 3. 研究と参考文献<br>MATH Dataset<br>Dan Hendrycks et al. · 公式リポジトリ<br>データの取得先、解答抽出と正規化、評価コード、AMPSの配布を案内する。<br>https://github.com/hendrycks/math<br>MATHScenario<br>Stanford CRFM · HELM v0.3.0<br>Level 1の抽出、公式提示例、解説付き条件の参照、解答の比較関数を実装する。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/math_scenario.py||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
