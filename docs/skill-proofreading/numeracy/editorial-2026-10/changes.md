# Numeracy（多項式の規則推論）：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|1|1|評価プラットフォーム名でなく、何を推論する課題かを表紙に示す|HELMの多項式帰納シナリオ<br>入出力の例から数の規則を推測する|多項式の規則推論<br>入出力の例から、未知の値を予測する|
|2|5|4|元研究の作成主体を一度自然に示し、固定配布文章集でなく生成課題として定義|Numeracyは、HELMで導入された人工生成の数値推論課題。入力と出力の組から式を推測する。<br>モデルには数値の組を示し、新しい入力に対応する値を出力させる。式そのものは入力に書かない。<br>ここでは、公開コードv0.3.0の生成器をseed=0で実行し、生成された実際のレコードを使う。|Numeracyは、入力と出力の数値の組から多項式の規則を推測し、新しい入力に対応する値を答える人工生成課題である。<br>Stanford CRFMを中心とする研究チームが2022年に設計した。公開生成器で式の係数と入力点を選び、学習用・評価用の数値を作る。<br>モデルには数値の対応を見せる。式そのものは示さず、新しい入力に対する数値を予測させる。|
|3|6|5|訓練レコード/プロンプトの内部語より入力出力の意味を説明|訓練レコードをプロンプトの例に使う|数値の対応を見せ、別の入力の答えを尋ねる|
|4|6|5|1試行や内部adapterの設定を外部化。表示範囲/100組/正解の意味を保持|数値の対応を見せるtrainと、予測対象にするtestを生成する。関数を推測するための例をプロンプトに示す。<br>standard／exampleの設定では、訓練例は最大100件、評価は100件、1試行。<br>以下のページには、訓練100件の連続した冒頭4〜6件と、test入力1件の全文を示す。|学習用の数値の組と、予測対象にする評価用の入力を生成する。モデルは、提示された入出力例を手掛かりに規則を推測する。<br>次の実例では、学習用100組から抜粋した4〜6組と、評価用の入力1件を示す。各例の正解は、生成時に保存された式から計算できる。|
|5|8|7|参照メタデータの保存という工程を、規則推論の意味へ|この生成例の参照式はy=4x+4。x=15なら、4×15+4=64になる。<br>入力として渡すのは、−82→−324、70→284などの値の組で、参照式は採点・検証用のメタデータに保存される。<br>数字の並びから規則を推測し、新しい点へ適用することを測る。|この例を生成した式はy=4x+4。x=15なら、4×15+4=64になる。<br>モデルに見せるのは、−82→−324、70→284などの数値の対応である。例の間で共通する規則を見つけ、新しい入力へ適用する。|
|6|12|11|文字列形式を繰り返す説明を、変数を増やした推論の意味へ|この例はz=4x+4y+1。x=6、y=7を代入すると53になる。<br>入力の文字列は「6, 7」、正解の文字列は「53」。モデルは出力する数値だけを生成する。<br>二つの変数を持つ一次式と、二次式までの4種類を用意している。|この例を生成した式はz=4x+4y+1。x=6、y=7を代入すると53になる。<br>一つの入力が二つの値を持つため、xとyが出力にどう影響するかを、数値の組から推測する。<br>一次・二次、1変数・2変数を組み合わせた4種類の式を用意している。|
|7|15|14|乱数初期化の細部より、規則と数値の組を作る設計へ|各関数型に係数の範囲を決め、PythonとNumPyの乱数を同じseedで初期化する。<br>最高次数、変数の数、非ゼロの定数項を満たす式ができるまで抽選する。<br>生成した式に入力点を代入し、出力の整数値と、参照式・関数型をレコードへ保存する。|式の種類ごとに、整数の係数を選ぶ範囲を決める。必要な次数と変数の数を持ち、定数項が0でない式を作る。<br>式に整数の入力点を代入し、対応する出力を計算する。学習用と評価用は同じ式から作る。<br>係数を固定した式で試す方法と、範囲内から係数を抽選して別の式を作る方法がある。|
|8|16|15|overlapの内部引数名を外し、入力領域と分割条件の意味を保持|linearは−100〜100、parabolaは0〜200の整数を使う。二次式の入力は非負にしている。<br>planeはx・yが−10〜10、paraboloidは0〜20。さらに2変数ではx≤yの点だけを残す。<br>overlap=Trueは訓練とtestの入力範囲を共通にする設定。訓練用と評価用の点は重複しない。|公開生成器の標準設定では、linearは−100〜100、parabolaは0〜200の整数を使う。二次式の入力は非負にしている。<br>planeは二つの変数が−10〜10、paraboloidは0〜20の整数を使う。どちらもxがy以下となる点を選ぶ。<br>学習用と評価用を同じ領域から選び、同じ入力点が両方に入らないようにする。|
|9|17|16|seed/modeの監査ラベルを外部化し、散布図の対象を自然に説明|plane／standard／seed=0。訓練100点、test 100点。候補は231点。|planeの生成例。学習100点、評価100点を、231候補点から選ぶ。|
|10|19|17|TODOや4型実行照合の工程を外部化。利用上の未実装条件は簡潔に保持|各型・seed=0を実行して確認。function内の生成処理はTODOとreturn []が残る。|公開生成器v0.3.0。functionモードの生成処理は未実装である。|
|11|21|19|HELMの指標キー/文字正規化/整数変換の細部を外部化し、正答率と数値誤差の意味へ|既定ではexact_match、正規化してから比べるquasi_exact_match、絶対誤差を測るabsolute_value_differenceを使う。<br>exact_matchは正解文字列と一致すれば1、違えば0。absolute_value_differenceは、整数として解釈した予測値と正解値の差の絶対値。<br>入力ごとの値を集計する。絶対誤差は小さいほどよく、完全に一致する予測なら0になる。|予測した整数が正解と一致する割合で、規則を正しく適用できたかを見る。数値としてどれほど近いかは、予測値と正解値の差の絶対値で測れる。<br>絶対誤差 = ／予測値 − 正解値／<br>実例1の正解64に対して65を出力すると、一致せず、絶対誤差は1になる。出力の大きさが式ごとに異なるため、式の種類や入力範囲と合わせて評価する。|
|12|21|19|内部metric名でなく数値予測の評価を説明|正解の文字列と数値のずれを採点する|正答率と、予測値のずれで評価する|
|13|28|21|切り分けるという読者への指示を、実験で変えられる条件へ|規則の推測と適用を切り分けて調べる|例の数や入力範囲を変えて、推論を調べる|
|14|28|21|対象の使い方を具体的に示し、実行監査ではなく実験設計へつなげる|一つの式に多くの入出力例を与え、未知の入力点へ適用できるかを調べる。<br>入力範囲、係数範囲、訓練例の数、表示順序を固定すると、数値の規則への適合を比較する評価を組める。<br>答えの規模によって、同じ割合のずれでも絶対誤差が変わる。関数型と出力範囲も結果と対応させる。|一つの式について、学習用の例を何組見せれば、新しい入力に正しく答えられるかを調べられる。<br>係数の範囲、入力の範囲、例の数や並び順を決めると、モデルを同じ条件で比較できる。<br>1変数から2変数へ、一次式から二次式へと、規則の形を変えて推論の違いを見ることもできる。|
|15|29|22|200件の長さを確認するだけのコードを、実際の入力と正解を読む生成例へ|scenario = NumeracyScenario(<br>    relation_type="linear",<br>    mode="standard", seed=0<br>)<br>records = scenario.get_instances("output")<br>len(records)  # 200|task = NumeracyScenario(<br>    relation_type="linear", mode="standard", seed=0<br>)<br>records = task.get_instances("output")<br>example = next(r for r in records if r.split == "test")<br>print(example.input.text)<br>print(example.references[0].output.text)|
|16|29|22|プラットフォーム名でなく、実行前提とコードの役割を説明|HELM v0.3.0のNumeracyScenarioを読み込んだ後の例。train 100件とtest 100件が返る。|公開生成器のNumeracyScenarioを読み込んだ後の例。学習用・評価用の数値を作り、最初の評価入力と正解を表示する。|
|17|31|23|固定文章データではないという重ねた否定を外し、生成器の利用方法と再現条件を簡潔に示す|HELMのコードはApache License 2.0で公開されている。Numeracyの入力と正解は、このコードが人工的に生成する。<br>人が書いた問題文や既存Web文章のコレクションをダウンロードする課題ではない。<br>公式リポジトリのv0.3.0を選び、生成器と採点実装を同じバージョンでそろえて使う。|公開生成器はApache License 2.0で提供される。式の種類、係数を選ぶ方法、乱数のseedを指定して、数値の組と正解を作れる。<br>同じ数値を再現するときは、生成器のバージョンと実行環境も記録する。ここで示す実例はv0.3.0の生成器を使っている。|
|18|32|24|公開run有無/指標実装の細部を外し、課題の目的と使い方をまとめる|Numeracyは、一次・二次、1変数・2変数の多項式を使い、例から規則を推測して新しい入力へ適用する課題。<br>既定の採点には文字列一致と絶対誤差があり、整数として読めない出力の扱いも得点に影響する。<br>Classic v0.4.0には公開モデル成績がない。動作するexample／standardの生成器から、条件を固定して評価を組み立てられる。|Numeracyは、多項式から作った入出力の例を見せ、未知の入力に対応する数値を予測させる課題である。<br>一次・二次、1変数・2変数の式を使い、既知の計算式を直接与えずに、数の対応から規則を見つけられるかを調べる。<br>生成器の条件をそろえることで、正答率や数値誤差を使った比較実験を組み立てられる。|
|19|48|38|独自IDやメタデータ混入禁止文を外し、実レコードを読むための構造を説明|referencesの先頭は数値の正解で、correctタグが付く。次にsolutionタグの参照式、classタグの関数型が入る。<br>モデルの入力はinput.textにある整数の列。採点と検証に使う参照式は、通常の入出力例の文章に混ぜない。<br>実例のIDは、関数型・モード・seed・test配列内の位置を組み合わせた、この資料での識別子。|生成した各問題には、入力の整数列と、数値の正解が含まれる。参照式と式の種類も、正解を確かめるために保存される。<br>入力はinput.text、参照はreferencesに入る。correctタグは数値の正解、solutionは参照式、classは式の種類を表す。|
|20|7|6|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|21|7|6|seed/配列位置/内部modeの監査ラベルを外部記録へ|linear / mode=standard / seed=0 / test[0]|式の種類：linear|
|22|7|6|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|23|7|6|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|24|9|8|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|25|9|8|seed/配列位置/内部modeの監査ラベルを外部記録へ|parabola / mode=standard / seed=0 / test[0]|式の種類：parabola|
|26|9|8|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|27|9|8|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|28|11|10|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭6件（連続）|学習用100組から6組を抜粋|
|29|11|10|seed/配列位置/内部modeの監査ラベルを外部記録へ|plane / mode=standard / seed=0 / test[0]|式の種類：plane|
|30|11|10|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|31|11|10|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|32|35|27|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭6件（連続）|学習用100組から6組を抜粋|
|33|35|27|seed/配列位置/内部modeの監査ラベルを外部記録へ|paraboloid / mode=standard / seed=0 / test[0]|式の種類：paraboloid|
|34|35|27|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|35|35|27|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|36|36|28|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|37|36|28|seed/配列位置/内部modeの監査ラベルを外部記録へ|linear / mode=example / seed=0 / test[0]|式の種類：linear|
|38|36|28|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|39|36|28|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|40|37|29|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|41|37|29|seed/配列位置/内部modeの監査ラベルを外部記録へ|parabola / mode=example / seed=0 / test[0]|式の種類：parabola|
|42|37|29|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|43|37|29|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|44|38|30|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭6件（連続）|学習用100組から6組を抜粋|
|45|38|30|seed/配列位置/内部modeの監査ラベルを外部記録へ|plane / mode=example / seed=0 / test[0]|式の種類：plane|
|46|38|30|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|47|38|30|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|48|39|31|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭6件（連続）|学習用100組から6組を抜粋|
|49|39|31|seed/配列位置/内部modeの監査ラベルを外部記録へ|paraboloid / mode=example / seed=0 / test[0]|式の種類：paraboloid|
|50|39|31|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|51|39|31|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|52|40|32|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|53|40|32|seed/配列位置/内部modeの監査ラベルを外部記録へ|linear / mode=standard / seed=0 / test[1]|式の種類：linear|
|54|40|32|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|55|40|32|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|56|41|33|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|57|41|33|seed/配列位置/内部modeの監査ラベルを外部記録へ|parabola / mode=standard / seed=0 / test[1]|式の種類：parabola|
|58|41|33|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|59|41|33|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|60|42|34|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭6件（連続）|学習用100組から6組を抜粋|
|61|42|34|seed/配列位置/内部modeの監査ラベルを外部記録へ|plane / mode=standard / seed=0 / test[1]|式の種類：plane|
|62|42|34|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|63|42|34|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|64|43|35|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭6件（連続）|学習用100組から6組を抜粋|
|65|43|35|seed/配列位置/内部modeの監査ラベルを外部記録へ|paraboloid / mode=standard / seed=0 / test[1]|式の種類：paraboloid|
|66|43|35|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|67|43|35|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|68|44|36|先頭/連続の照合手順は外部記録へ。学習用の母集団と表示数を簡潔に保持|原データ：訓練100件の先頭4件（連続）|学習用100組から4組を抜粋|
|69|44|36|seed/配列位置/内部modeの監査ラベルを外部記録へ|linear / mode=standard / seed=0 / test[2]|式の種類：linear|
|70|44|36|testレコードという実装語を自然なラベルへ|予測対象：testレコードの入力（全文）|予測する入力|
|71|44|36|参照メタデータ/入力に含めないという反復を具体的な役割へ|参照メタデータ（入力には含めない）|正解の計算に使う式|
|72|5|4|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110<br>[2] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110<br>[2] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|73|6|5|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. get_numeracy_spec, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. get_numeracy_spec（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py|
|74|7|6|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|75|8|7|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|76|9|8|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|77|10|9|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|78|11|10|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|79|12|11|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|80|14|13|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|81|15|14|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|82|16|15|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|83|17|16|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|84|19|17|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|85|21|19|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. get_numeracy_spec, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py<br>[2] Stanford CRFM. BasicMetric, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py|[1] Stanford CRFM. get_numeracy_spec（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py<br>[2] Stanford CRFM. BasicMetric（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py|
|86|28|21|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110<br>[2] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110<br>[2] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|87|29|22|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|88|31|23|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. HELM v0.3.0, Apache License 2.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/LICENSE|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. Apache License 2.0。  https://github.com/stanford-crfm/helm/blob/v0.3.0/LICENSE|
|89|32|24|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. HELM Classic v0.4.0 (2023-11-17).  https://crfm.stanford.edu/helm/classic/v0.4.0/|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. HELM Classic v0.4.0 (2023-11-17).  https://crfm.stanford.edu/helm/classic/v0.4.0/|
|90|35|27|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|91|36|28|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|92|37|29|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|93|38|30|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|94|39|31|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|95|40|32|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|96|41|33|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|97|42|34|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|98|43|35|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|99|44|36|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。 <br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|100|45|37|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|101|48|38|出典は通常の文献・コード情報とし、プラットフォーム名の反復と実行環境監査を外部化|[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|[1] Stanford CRFM. NumeracyScenario（v0.3.0）。  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py|
|102|32|24|本文から外した公開runの出典も外部化|[2] Stanford CRFM. HELM Classic v0.4.0 (2023-11-17).  https://crfm.stanford.edu/helm/classic/v0.4.0/||
|103|51|39|Web文献の著者年・バージョン・実参照日を統一|Stanford CRFM (2023). HELM v0.3.0, Python implementation.|Stanford CRFM (n.d.). NumeracyScenario v0.3.0（2026-10-18参照）。|
|104|51|39|URLまでnative編集枠に収める|105.54|123.54|
|105|51|39|URLまでnative編集枠に収める|105.54|123.54|
|106|3|2|課題中心の内容へ章名/目次/帯を対応|数値の採点と公開実行|予測値と正解を比べる|
|107|3|2|課題中心の内容へ章名/目次/帯を対応|再現方法と利用の範囲|生成器を使って試す|
|108|20|18|課題中心の内容へ章名/目次/帯を対応|3. 数値の採点と公開実行|3. 予測値と正解を比べる|
|109|20|18|課題中心の内容へ章名/目次/帯を対応|3. 数値の採点と公開実行|3. 予測値と正解を比べる|
|110|21|19|課題中心の内容へ章名/目次/帯を対応|3. 数値の採点と公開実行|3. 予測値と正解を比べる|
|111|27|20|課題中心の内容へ章名/目次/帯を対応|4. 再現方法と利用の範囲|4. 生成器を使って試す|
|112|27|20|課題中心の内容へ章名/目次/帯を対応|4. 再現方法と利用の範囲|4. 生成器を使って試す|
|113|28|21|課題中心の内容へ章名/目次/帯を対応|4. 再現方法と利用の範囲|4. 生成器を使って試す|
|114|29|22|課題中心の内容へ章名/目次/帯を対応|4. 再現方法と利用の範囲|4. 生成器を使って試す|
|115|31|23|課題中心の内容へ章名/目次/帯を対応|4. 再現方法と利用の範囲|4. 生成器を使って試す|
|116|32|24|課題中心の内容へ章名/目次/帯を対応|4. 再現方法と利用の範囲|4. 生成器を使って試す|
|117|34|26|課題中心の内容へ章名/目次/帯を対応|生成と採点の詳細|式とデータ形式の補足|
|118|45|37|課題中心の内容へ章名/目次/帯を対応|Appendix: 2. 生成と採点の詳細|Appendix: 2. 式とデータ形式の補足|
|119|48|38|課題中心の内容へ章名/目次/帯を対応|Appendix: 2. 生成と採点の詳細|Appendix: 2. 式とデータ形式の補足|
|120|33|25|MIDDLE字形位置を保持してnative枠を広げる|46.08|54.08|
|121|2||HELM Classic一般画面は多項式課題の概要に不要。生成器の直接URLを参考文献と各頁へ保持。|公式サイト：HELM Classic<br>HELM Classic<br>[1] Stanford CRFM. HELM Classic v0.4.0 (2023-11-17).  https://crfm.stanford.edu/helm/classic/v0.4.0/||
|122|18||1600件の生成/再計算の制作監査は外部記録へ。100学習/100評価と入力領域は16/19へ保持。|100点を見せ、別の100点で確かめる<br>各関数について、訓練用とtest用に異なる100点ずつを選ぶ。1変数では201候補点、2変数ではx≤yを満たす231候補点がある。<br>今回は各型でseed=0を使い、exampleとstandardの8組、計1,600レコードを生成した。<br>全1,600件の正解を参照式へ別途代入して再計算し、生成器の出力と一致することを確認した。<br>2. 多項式と入力点を生成する<br>[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py||
|123|22||特定metricの句読点除去/整数変換4例は実装監査。一般的な正答率と絶対誤差は21へ。|同じ正解64に対する出力の採点<br>3. 数値の採点と公開実行<br>出力 ／ 完全一致 ／ 正規化後の一致 ／ 絶対誤差<br>64 ／ 1 ／ 1 ／ 0<br>65 ／ 0 ／ 0 ／ 1<br>64.0 ／ 0 ／ 0 ／ 64<br>-64 ／ 0 ／ 1 ／ 128<br>正規化後の一致はquasi_exact_match。符号も句読点として除かれ、-64と64が一致する。<br>[1] Stanford CRFM. BasicMetric, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py||
|124|23||errorを0として扱う実装の細部は外部監査記録へ。|整数として読めない出力の扱い<br>absolute_value_differenceの実装では、整数として解釈できない出力は、0として採点される。<br>たとえば正解が0のとき、出力がerrorでも絶対誤差は0になる。exact_matchは0で、正解文字列とは一致しない。<br>数値のずれと出力形式を合わせて確認できるよう、exact matchと実際の出力を併せて保存する。<br>3. 数値の採点と公開実行<br>[1] Stanford CRFM. BasicMetric, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py||
|125|24||任意ソルバーの幾何距離は中心的な数値予測の解説に不要な実装詳細。|曲線・曲面からの距離も定義される<br>run_solver=Trueなら、予測した点から参照曲線・曲面までの最短距離と、整数として読めた出力の割合を追加できる。<br>実例1で65を予測すると、点(15, 65)は直線y=4x+4から1/√17、約0.243だけ離れる。<br>これは任意の追加指標。既定の指標は数値の絶対誤差であり、Classicの表示設定でも主指標になっている。<br>3. 数値の採点と公開実行<br>[1] Stanford CRFM. get_numeracy_spec, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py<br>[2] Stanford CRFM. DistanceMetric, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/numeracy_metrics.py||
|126|25||公開run索引0件の確認表は対象リスト由来の監査であり、課題概要から外部化。|Classic v0.4.0の公開実行は0件<br>3. 数値の採点と公開実行<br>確認した対象 ／ 公開内容<br>シナリオ定義 ／ numeracyが登録されている<br>主指標 ／ absolute_value_difference / test<br>公開run_specs ／ 該当runは0件<br>モデル別の成績 ／ 掲載された値はない<br>2026-10-18にlatest設定とv0.4.0の配布JSONを確認した。<br>[1] Stanford CRFM. HELM Classic v0.4.0 (2023-11-17).  https://crfm.stanford.edu/helm/classic/v0.4.0/||
|127|26||run0/未生成function/未実行モデルという注意の反復。function未実装は19に簡潔に保持。|生成できる設定と公開成績を区別する<br>公開runは0件だった。0点というモデル成績が記録されているのではない。<br>v0.3.0のexample／standardはレコードを生成する一方、既定のfunctionは空のリストを返す。<br>この資料では、動作する生成器の出力と採点実装を説明する。未実行のモデル得点を補っていない。<br>3. 数値の採点と公開実行<br>[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py<br>[2] Stanford CRFM. HELM Classic v0.4.0 (2023-11-17).  https://crfm.stanford.edu/helm/classic/v0.4.0/||
|128|30||SHA/実行環境/実例位置の監査。生成器のバージョン・seed再現条件は31へ保持。|再現にはバージョンと乱数を保存する<br>再現にはseedに加えて実行環境も保存する。ここではPython 3.12、NumPy 2.3.5、SymPy 1.14.0で公式の生成処理を実行した。<br>seed、関数型、モードに加え、overlap=True、sort_vals=Falseを固定した。<br>公式ソースのSHA-256、全生成レコード、13実例の位置とハッシュを保存した。<br>4. 再現方法と利用の範囲<br>[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py||
|129|46||axis-alignedコメントと係数実装の照合は外部監査。交差項xyの存在は実例4の原式と45係数表に保持。|2変数の二次式には交差項も現れる<br>v0.3.0の係数範囲では、paraboloidのxyの係数は0または1。xとyに関する一次項は0に固定される。<br>standard／seed=0の参照式はz=2x²+xy+y²+4となり、交差項xyを含む。<br>コードのコメントにはaxis-alignedのみとあるが、実際の係数範囲と生成結果には交差項がある。<br>Appendix: 2. 生成と採点の詳細<br>[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py||
|130|47||単一seedの全生成件数の出力極値は対象全体の分布ではなく細かな制作集計。原数値は外部記録へ。|seed=0のstandard出力の範囲<br>Appendix: 2. 生成と採点の詳細<br>型 ／ train＋testの最小値 ／ 最大値<br>linear ／ -396 ／ 404<br>parabola ／ 1 ／ 80,201<br>plane ／ -79 ／ 81<br>paraboloid ／ 4 ／ 1,604<br>各型の200件を実測した範囲。係数と入力点の全組み合わせの極値ではない。<br>[1] HELM v0.3.0の公式生成器をseed=0で実行。Python 3.12 / NumPy 2.3.5。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py||
|131|49||未実装functionとTODO/1000関数を重ねて警告する頁。19の利用条件に集約。|functionモードは生成処理が止まっている<br>functionは、問題ごとに式を抽選し直す設計として説明される。MODE_INFOには訓練・評価の関数を各1,000個とする設定がある。<br>しかしv0.3.0のgenerate_datasetsはTODOとともに空リストを返す。4型をseed=0で実行して、いずれも0件だった。<br>設定上の1,000関数と、実際に生成・公開評価された件数を同じ数量として扱わない。<br>Appendix: 2. 生成と採点の詳細<br>[1] Stanford CRFM. NumeracyScenario, HELM v0.3.0.  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/numeracy_scenario.py||
|132|50||同名データ/論文とコードの名称対応の監査を外部出自記録へ。表紙/定義で多項式課題と明示。|Numeracy-600Kは別の自然言語データ<br>Numeracy-600Kは、ニュース見出しや市況コメントに現れる数値の大きさを扱う、2019年の別データセット。<br>HELMのNumeracyは、人工生成した入出力の組から多項式の値を推測する。質問・文章や利用する指標が異なる。<br>HELMの論文では数値関係を推測する課題をnumeracy_predictionと呼び、公開コードではnumeracyとして実装している。<br>Appendix: 2. 生成と採点の詳細<br>[1] Chen, Huang, Takamura & Chen (2019). Numeracy-600K. ACL.  https://aclanthology.org/P19-1635/<br>[2] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110||
|133|52||run_spec/BasicMetric実装の細部の2文献は外部監査へ。元研究と公開生成器を保持。|参考文献<br>Appendix: 3. 研究と参考文献<br>get_numeracy_spec<br>Stanford CRFM (2023). HELM v0.3.0, run_specs.py.<br>モード別の提示例数、評価件数、生成方法と既定・任意の指標を設定する。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py<br>BasicMetric: absolute_value_difference<br>Stanford CRFM (2023). HELM v0.3.0, basic_metrics.py.<br>出力の整数変換と絶対誤差、文字列一致などの基本的な採点処理を実装する。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py||
|134|53||任意ソルバーと同名別データの文献は多項式課題の概要に不要、外部記録へ。|参考文献<br>Appendix: 3. 研究と参考文献<br>DistanceMetric<br>Stanford CRFM (2023). HELM v0.3.0, numeracy_metrics.py.<br>予測点と曲線・曲面の最短距離、および整数として読める出力の割合を計算する。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/numeracy_metrics.py<br>Numeracy-600K: Learning Numeracy for Detecting Exaggerated Information in Market Comments<br>Chung-Chi Chen, Hen-Hsen Huang, Hiroya Takamura, Hsin-Hsi Chen (2019). ACL.<br>ニュース見出しと市況コメントの数値を集め、数の大きさの理解と誇張表現の検出を扱う。<br>https://aclanthology.org/P19-1635/||
|135|7|6|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|136|7|6|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|
|137|9|8|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|138|9|8|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|
|139|11|10|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=181.48,margin=5.00|top=156.80,height=180.81,margin=3.00|
|140|11|10|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=43.32,margin=5.00|
|141|29|22|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=121.00,height=157.00,margin=5.00|top=119.00,height=157.67,margin=7.00|
|142|35|27|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=181.48,margin=5.00|top=156.80,height=180.81,margin=3.00|
|143|35|27|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=43.32,margin=5.00|
|144|36|28|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|145|36|28|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|
|146|37|29|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|147|37|29|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|
|148|38|30|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=181.48,margin=5.00|top=156.80,height=180.81,margin=3.00|
|149|38|30|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=43.32,margin=5.00|
|150|39|31|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=181.48,margin=5.00|top=156.80,height=180.81,margin=3.00|
|151|39|31|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=43.32,margin=5.00|
|152|40|32|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|153|40|32|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|
|154|41|33|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|155|41|33|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|
|156|42|34|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=181.48,margin=5.00|top=156.80,height=180.81,margin=3.00|
|157|42|34|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=43.32,margin=5.00|
|158|43|35|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=181.48,margin=5.00|top=156.80,height=180.81,margin=3.00|
|159|43|35|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=43.32,margin=5.00|
|160|44|36|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=133.89,margin=5.00|top=156.80,height=133.22,margin=3.00|
|161|44|36|字形位置を保ち、数値と実用コードの背景実余白を上下12ptへ整える|top=154.80,height=42.65,margin=5.00|top=154.80,height=39.32,margin=5.00|

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
