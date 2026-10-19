# WikiFact：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|5|5|読者が概要を理解できる自然な説明に整理する|WikiFactは、知識基盤Wikidataの「主語・関係・目的語」という三つ組を、英語の短い文に変換した事実補完データ。<br>モデルは「作品の著者は」「国の通貨は」といった文の続きを生成する。本文を検索する段階を設けず、知識を表す名前を出力できるかを測る。|WikiFactは、知識基盤Wikidataの「主語・関係・目的語」という三つ組を、英語の短い文に変換した事実補完データである。<br>モデルは「作品の著者は」「国の通貨は」といった文の続きを生成する。根拠となる文章を与えず、モデルが覚えている事実を名前として答えられるかを測る。|
|2|6|6|読者が概要を理解できる自然な説明に整理する|同じ作品に複数の著者がいるように、同じ入力から複数の対象を答えられる。また、一つの対象が複数の名前や略号を持つこともある。<br>いずれかの許容対象の、いずれかの別名に一致すれば正解とする。次の3例は、公開実行の入力と参照回答の全文を示す。|同じ作品に複数の著者がいるように、一つの入力に複数の正解がある。また、一つの対象が複数の名前や略号を持つこともある。<br>正解となる対象の名前や別名のいずれかに一致すれば正解とする。次の3例は、公開実行の入力と参照回答の全文である。|
|3|7|7|3人目ではないという禁止的補足を、別名の関係へ|2人の著者のうち1人を答えればよい。Thomas Nicholas ScortiaはThomas N. Scortiaの別名で、3人目ではない。|2人の著者のうち1人を答えればよい。Thomas Nicholas ScortiaとThomas N. Scortiaは、同じ著者の別名である。|
|4|9|9|参照1文字列という監査単位の説明を課題の意味へ|訴訟の当事者という関係を扱う。参照は1文字列。|事件名から、原告となった組織の名前を答える。|
|5|16|16|100/50/850の数値だけの見出しを分割の目的へ|通常の分割は100／50／850問|関係ごとに、学習・開発・テストへ分ける|
|6|16|16|通常設計と小規模関係の違いを自然な説明へ|1関係1,000問を標本抽出する設計。公開実行では、これより少ない関係もある。|通常は、関係ごとに1,000問を抽出して分割する。公開テストでは、問題数がこれより少ない関係もある。|
|7|17|17|試行ID照合の工程と全件実行ではないという重複否定を外部化|試行間の同一IDをまとめたtestは計7,462問。実装が対応する86関係の全件実行ではない。|公開テストは計7,462問で、86関係のうち10関係を対象とする。|
|8|19|19|問題単位と関係単位の違いを具体的に説明し、重ねた否定を削る|各関係のtestに対し、最上位候補が参照に一致した割合を計算する。その後、10関係の正答率を同じ重みで平均した値が全体の指標。<br>96問の原告も、850問の著者も、全体平均では同じ1関係として扱われる。全7,462問の正誤をそのまま平均した値ではない。|各関係のtestで、最上位候補が参照回答に一致した割合を求める。その後、10関係の正答率を同じ重みで平均する。<br>96問の原告も、850問の著者も、全体の得点には同じ重みで反映される。|
|9|20|20|モデル条件の違いを自然な見出しへ|候補数と試行数も、モデルで違っていた|モデルごとに、候補数と評価回数が異なる|
|10|20|20|設定値と全7462レコード照合という制作過程を外部化し、実際の候補数・試行数と得点への影響を保持|OPTとtext-davinci-003は、5候補から対数確率最大の候補を選び、各3試行の正答率を平均した。<br>Llama 2 70Bは1試行。設定上は5出力だが、取得した全7,462件のtestレコードには、それぞれ1候補の出力が含まれていた。<br>そのため、Llama 2の公開Accuracy@1と@5は同じ値になる。5候補を生成した条件として比較する値ではない。|OPT-175Bとtext-davinci-003は、1問につき5候補を生成し、対数確率が最大の候補を採点する。異なる提示例を使う3試行の正答率を平均した。<br>Llama 2 70Bの公開出力は1問につき1候補で、評価は1試行である。そのためAccuracy@1と@5は同じ値になる。|
|11|21|21|suite識別子とtemperatureの細部を記録へ。8token上限は旧23で説明する|v0.4.0収録・suite v0.3.0。最大5提示例、temperature 1、出力上限8トークン。|HELM Classicで2023年に公開された結果。各問に最大5例を提示。|
|12|25|25|切り分けてという読者への指示を、課題の性質へ|文脈の読解と切り分けて、事実知識を測る|根拠文を与えずに、事実知識を尋ねる|
|13|25|25|現在実装の確認日と最新モデルではないという注意を除き、実装の範囲と公表結果を明示|WikiFactは、文章に根拠が含まれる読解や、検索器が根拠を探す課題と異なり、主語と関係だけから目的語名を生成する。<br>2026-10-18確認のHELM実装にも86関係の読込がある。今回扱う公開成績は2023年のClassic固定版で、現在の知識や最新モデルを評価したものではない。|WikiFactは、主語と関係を示す短い文から、目的語となる名前を生成する。文章中の根拠を読み取る読解課題や、検索器で根拠を探す課題とは入力が異なる。<br>HELMの公開実装は86関係に対応する。ここで紹介した2023年の公開成績は、そのうち10関係に対するものである。|
|14|26|26|入手の説明を肯定的な具体文へ|配布ファイルと、実行記録への入口|公式サイトで、関係別の成績と出力を見られる|
|15|26|26|3ファイル503・30条件取得・全分布未実測という制作報告は外部化。配布先の利用上の制約を簡潔に保持 / 独立レビュー：503取得状況と紹介工程は外部記録へ、入手方法と閲覧できる範囲を説明|公式HELMページからWikiFactの条件別成績と予測へ進める。シナリオコードはCodaLabのtrain/dev/test JSONLを読み込む。<br>今回、CodaLabは3ファイルとも503となった。一方、公開runの10関係の入力・参照・生成結果と、3モデル30条件の得点は取得できた。<br>全86関係の元JSONLは未取得で、全体の総件数や全関係のデータ分布は今回の実測対象に含めていない。|公式HELMページでは、WikiFactの関係別・モデル別成績と、各問の入力・参照回答・生成結果を閲覧できる。<br>全86関係の問題は、CodaLabのtrain・dev・test JSONLとして案内されている。公式サイトでは、10関係の公開実行に含まれる入力・参照回答・出力を利用できる。|
|16|27|27|コードとデータを区別するという指示を具体的な条件へ|権利条件はコードとデータを区別する|実装コードはApache 2.0で公開される|
|17|27|27|今回確認という工程表現を除き、未確認のデータ利用条件を読者に必要な範囲で保持|HELMの実装コードはApache License 2.0で公開される。元のWikidataと、加工されたWikiFact配布物の権利条件は、コードの条件とは別に確認する。<br>今回取得したシナリオコードと論文では、WikiFactの加工済みデータ全体への専用ライセンス表示は確認できなかった。利用する配布物の条件は、配布元へ照会する必要がある。|HELMの実装コードはApache License 2.0で公開される。加工済みWikiFactデータの専用ライセンスは、公式論文と読込コードには明記されていない。<br>データを再配布・再利用する際の条件は、配布元への確認が必要である。|
|18|28|28|そろえて読むという指示を具体的なまとめへ|知識の範囲と、答え方をそろえて読む|専門領域の知識を、名前の補完で測る|
|19|28|28|読者が概要を理解できる自然な説明に整理する|WikiFactは、専門領域を含む86関係を、Wikidata由来の事実補完へ変えたデータ。複数対象と別名を参照として持つ。<br>Classicで実行された10関係では、問題数も候補数も条件によって違う。各関係を同じ重みで平均する方法と、文字列の正規化、生成候補数をそろえて、公開成績を解釈する。|WikiFactは、Wikidata由来の86関係を文の補完へ変え、一般的な事実から法律・経済・生物医学までを扱う。複数の対象や別名を正解として持つ。<br>HELM Classicの公開成績は10関係の正答率を同じ重みで平均する。候補数の違いと、参照に含まれる名前の範囲が得点に影響する。|
|20|7|7|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|21|8|8|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|22|9|9|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|23|32|32|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|24|33|33|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|25|34|34|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|26|35|35|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|27|36|36|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|28|37|37|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|29|38|38|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|30|39|39|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|31|40|40|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|32|41|41|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|33|36|36|決まった形式で答えるという曖昧な表現を具体化|実例8：発明者を、決まった形式で答える|実例8：医学的評価法の考案者を答える|
|34|36|36|配布参照のまま示すという制作報告を、データに含まれる表記の説明へ|「discovered by」というテンプレートで、医学的評価法の考案者を尋ねる。別表記と重複も配布参照のまま示す。|医学的評価法の考案者を「discovered by」というテンプレートで尋ねる。参照にはVirginia Agparという表記や、同じ名前の重複が含まれる。|
|35|37|37|入力に日付は含まれないという自明な注意を削る|役職名が参照になる。地位の就任日や退任日は、この入力には含まれない。|人物と役職の関係を尋ねる。参照回答は高等法院判事である。|
|36|40|40|現在の国を一律に尋ねないという禁止的注意を具体例の意味へ|歴史上の地域も含む。現在の国の通貨を一律に尋ねる集合ではない。|イギリス領キプロスで用いられた通貨を尋ねる。|
|37|45|45|Llamaを外した工程説明は旧20での1候補の説明と重複するため省く|10関係の単純平均、3試行平均。Llama 2は実出力が1候補なので、この5候補比較から外した。|10関係を同じ重みで平均し、3試行を平均した値。|
|38|46|46|P50等のID対照は外部記録へ。読者が実例を読み出せるコードに置換|関係<br>ID<br>関係<br>ID<br>著者<br>P50<br>部分・所属先<br>P361<br>通貨<br>P38<br>出生地<br>P19<br>発見者・発明者<br>P61<br>原告<br>P1620<br>分類<br>P31<br>役職<br>P39<br>治療対象<br>P2175<br>症状・徴候<br>P780|公開実行の入力と参照を読むコード|
|39|46|46|実装の細部を実用例に置き換える|公開実行で使う関係とWikidataのID|公開実行のJSONから、入力と参照を読む|
|40|46|46|subject引数の細部より、読むデータの意味を説明|subject引数は関係名を指定する。|scenario_state.jsonは、公式HELMの公開実行に付随するJSONファイル。各問の入力、参照回答、モデル出力を収める。|
|41|46|46|公式実行の生レコードを使う、実際に実行する読込例||import json<br>with open("scenario_state.json", encoding="utf-8") as f:<br>    state = json.load(f)<br>example = state["request_states"][0]["instance"]<br>print(example["input"]["text"])<br>print([r["output"]["text"] for r in example["references"]])|
|42|50|48|チームの工程より研究の狙いを見出しにする|HELMの知識評価として新規に構築した|専門領域まで広げた、HELMの事実知識評価|
|43|50|48|貢献者列挙を主題に関わる担当へ絞り、課題の成立と結ぶ / main校正：個人別の設計/実装/注釈/指揮の分担を外部化し、参加者と研究の意義を保持|WikiFactはHELM論文で導入されたデータセット。論文の貢献記録では、Hongyu Renが設計・実装、Lucia Zhengがデータ注釈・前処理を担当したとされる。<br>Michihiro Yasunagaが知識評価チームを率い、Neel Guhaらも設計に参加。プロジェクト全体はPercy Liangが統括した。<br>文の補完形式はLAMAを受け継ぎつつ、法律・経済・生物医学を含む幅広い関係へ対象を広げた。|WikiFactは、HELMの事実知識評価のために新しく作られた。Hongyu Ren、Lucia Zheng、Michihiro Yasunagaらが制作に参加した。<br>文の補完というLAMAの形式を受け継ぎ、法律・経済・生物医学など幅広い分野へ対象を広げた。|
|44|37|37|main校正：原templateにない過去時点を補わない|アリソン・フォスターが務めた役職は|アリソン・フォスターの役職は|
|45|45|45|main校正：許すという曖昧語を、Accuracy@5の採点条件へ|5候補を許すと、得点が上がる|5候補のどれかが合えば正解となる評価|
|46|52|50|main/独立校正：著者年と実参照日を文献情報として統一|Stanford CRFM · v0.4.0（2023-11-17）· 2026-10-18参照|Stanford CRFM (2023). v0.4.0（2023-11-17）。参照2026-10-18。|
|47|52|50|main/独立校正：著者年と実参照日を文献情報として統一|Stanford CRFM · 公開実装 · 2026-10-18確認|Stanford CRFM (n.d.). 公開実装。参照2026-10-18。|
|48|2|2|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|49|7|7|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / author/id151（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|50|8|8|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / currency/id156（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|51|9|9|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / plaintiff/id47（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|52|10|10|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM evaluate_reference_metrics. 候補の順位付け・正規化・@K採点。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|[1] Stanford CRFM. HELM evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|
|53|11|11|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|54|17|17|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|55|19|19|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|56|20|20|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|57|21|21|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|58|22|22|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|59|23|23|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM evaluate_reference_metrics. 候補の順位付け・正規化・@K採点。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|[1] Stanford CRFM. HELM evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|
|60|25|25|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM WIKIFactScenario. 86関係の辞書と配布ファイルの読込。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|61|26|26|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM WIKIFactScenario. 86関係の辞書と配布ファイルの読込。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|62|32|32|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / instance_of/id150（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|63|33|33|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / medical_condition_treated/id152（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|64|34|34|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / part_of/id151（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|65|35|35|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / place_of_birth/id150（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|66|36|36|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / discoverer_or_inventor/id154（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|67|37|37|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / position_held/id150（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|68|38|38|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / symptoms_and_signs/id156（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|69|39|39|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / author/id153（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|70|40|40|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / currency/id154（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|71|41|41|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / discoverer_or_inventor/id155（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|72|43|43|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|73|44|44|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|74|45|45|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|75|46|46|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM WIKIFactScenario. 86関係の辞書と配布ファイルの読込。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|76|30|30|監査表を実用コードへ置き換えた章構成に合わせる|関係別成績と実行条件|関係別成績とデータの読込|
|77|30|30|監査表を実用コードへ置き換えた章構成に合わせる|制作チームと参考文献|研究と参考文献|
|78|42|42|監査表を実用コードへ置き換えた章構成に合わせる|関係別成績と実行条件|関係別成績とデータの読込|
|79|42|42|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|80|43|43|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|81|44|44|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|82|45|45|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|83|46|46|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|84|49|47|監査表を実用コードへ置き換えた章構成に合わせる|制作チームと参考文献|研究と参考文献|
|85|49|47|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 3. 制作チームと参考文献|Appendix: 3. 研究と参考文献|
|86|50|48|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 3. 制作チームと参考文献|Appendix: 3. 研究と参考文献|
|87|51|49|参考文献URLまでnative編集枠に収める|107.11pt|125.11pt|
|88|51|49|参考文献URLまでnative編集枠に収める|107.11pt|125.11pt|
|89|52|50|参考文献URLまでnative編集枠に収める|87.16pt|105.16pt|
|90|52|50|参考文献URLまでnative編集枠に収める|87.16pt|105.16pt|
|91|46|46|実画素の上15.33pt/下24ptを各10ptへ、字形位置は保持|top120pt/height153pt|top125.33pt/height133.67pt|
|92|7|7|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|93|7|7|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|60.172913385826774pt|
|94|8|8|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.838582677165356pt|35.17196850393701pt|
|95|9|9|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.9436220472441pt|35.27700787401575pt|
|96|32|32|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.9436220472441pt|35.27700787401575pt|
|97|32|32|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|98|33|33|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|99|33|33|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.81157480314961pt|60.14496062992126pt|
|100|34|34|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|89.81259842519685pt|83.81259842519685pt|
|101|35|35|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.9436220472441pt|35.27700787401575pt|
|102|35|35|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|103|36|36|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|104|37|37|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|105|37|37|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|60.172913385826774pt|
|106|38|38|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.81157480314961pt|60.14496062992126pt|
|107|39|39|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|108|39|39|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.838582677165356pt|35.17196850393701pt|
|109|40|40|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|110|40|40|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|111|41|41|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|59.506220472440944pt|
|112|29|29|字形位置を保ち、章扉のnative領域を拡張|46.08|54.08|
|113|47||候補設定と実出力の照合表は旧20と重複。実候補数5/5/1・3/3/1試行と得点への影響は本編に保持。|設定の5出力と、返った候補数<br>Appendix: 2. 関係別成績と実行条件<br>Llama 2の全10関係test7,462件を取得して確認。max_tokens 8、stopは改行、最大提示例数5。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|114|48||実例選定・SHA/ID照合工程は監査記録へ。2022年1月という対象時点は本編に保持。|取得した入力と参照から再照合できる<br>Appendix: 2. 関係別成績と実行条件<br>13実例は、公開text-davinci-003のtest・第1試行から選んだ。全10関係を少なくとも1件ずつ含むが、頻度を代表する無作為標本ではない。<br>原文、全参照、全5候補、対数確率、条件内ID、固定run URL、取得SHA-256を保存した。参照に同じ名前が重複していても、原レコードでは保持した。<br>入力にある古い国・過去の役職も、2022年1月の知識基盤を基にした設計の一部として示す。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
