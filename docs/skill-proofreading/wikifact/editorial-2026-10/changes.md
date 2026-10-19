# WikiFact：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|5|4|読者が概要を理解できる自然な説明に整理する|WikiFactは、知識基盤Wikidataの「主語・関係・目的語」という三つ組を、英語の短い文に変換した事実補完データ。<br>モデルは「作品の著者は」「国の通貨は」といった文の続きを生成する。本文を検索する段階を設けず、知識を表す名前を出力できるかを測る。|WikiFactは、知識基盤Wikidataの「主語・関係・目的語」という三つ組を、英語の短い文に変換した事実補完データである。<br>モデルは「作品の著者は」「国の通貨は」といった文の続きを生成する。根拠となる文章を与えず、モデルが覚えている事実を名前として答えられるかを測る。|
|2|6|5|読者が概要を理解できる自然な説明に整理する|同じ作品に複数の著者がいるように、同じ入力から複数の対象を答えられる。また、一つの対象が複数の名前や略号を持つこともある。<br>いずれかの許容対象の、いずれかの別名に一致すれば正解とする。次の3例は、公開実行の入力と参照回答の全文を示す。|同じ作品に複数の著者がいるように、一つの入力に複数の正解がある。また、一つの対象が複数の名前や略号を持つこともある。<br>正解となる対象の名前や別名のいずれかに一致すれば正解とする。次の3例は、公開実行の入力と参照回答の全文である。|
|3|7|6|3人目ではないという禁止的補足を、別名の関係へ|2人の著者のうち1人を答えればよい。Thomas Nicholas ScortiaはThomas N. Scortiaの別名で、3人目ではない。|2人の著者のうち1人を答えればよい。Thomas Nicholas ScortiaとThomas N. Scortiaは、同じ著者の別名である。|
|4|9|8|参照1文字列という監査単位の説明を課題の意味へ|訴訟の当事者という関係を扱う。参照は1文字列。|事件名から、原告となった組織の名前を答える。|
|5|16|13|100/50/850の数値だけの見出しを分割の目的へ|通常の分割は100／50／850問|関係ごとに、学習・開発・テストへ分ける|
|6|16|13|通常設計と小規模関係の違いを自然な説明へ|1関係1,000問を標本抽出する設計。公開実行では、これより少ない関係もある。|通常は、関係ごとに1,000問を抽出して分割する。公開テストでは、問題数がこれより少ない関係もある。|
|7|26|19|入手の説明を肯定的な具体文へ|配布ファイルと、実行記録への入口|公式サイトで、関係別の成績と出力を見られる|
|8|26|19|3ファイル503・30条件取得・全分布未実測という制作報告は外部化。配布先の利用上の制約を簡潔に保持|公式HELMページからWikiFactの条件別成績と予測へ進める。シナリオコードはCodaLabのtrain/dev/test JSONLを読み込む。<br>今回、CodaLabは3ファイルとも503となった。一方、公開runの10関係の入力・参照・生成結果と、3モデル30条件の得点は取得できた。<br>全86関係の元JSONLは未取得で、全体の総件数や全関係のデータ分布は今回の実測対象に含めていない。|公式HELMページでは、WikiFactの関係別・モデル別成績と、各問の入力・参照回答・生成結果を閲覧できる。<br>問題データの読込コードは、CodaLabで配布するtrain・dev・testのJSONLを使う。配布先は現在アクセスできないため、ここでは公式サイトで公開されている10関係の実例と成績を紹介した。|
|9|27|20|コードとデータを区別するという指示を具体的な条件へ|権利条件はコードとデータを区別する|実装コードはApache 2.0で公開される|
|10|27|20|今回確認という工程表現を除き、未確認のデータ利用条件を読者に必要な範囲で保持|HELMの実装コードはApache License 2.0で公開される。元のWikidataと、加工されたWikiFact配布物の権利条件は、コードの条件とは別に確認する。<br>今回取得したシナリオコードと論文では、WikiFactの加工済みデータ全体への専用ライセンス表示は確認できなかった。利用する配布物の条件は、配布元へ照会する必要がある。|HELMの実装コードはApache License 2.0で公開される。加工済みWikiFactデータの専用ライセンスは、公式論文と読込コードには明記されていない。<br>データを再配布・再利用する際の条件は、配布元への確認が必要である。|
|11|28|21|そろえて読むという指示を具体的なまとめへ|知識の範囲と、答え方をそろえて読む|専門領域の知識を、名前の補完で測る|
|12|28|21|読者が概要を理解できる自然な説明に整理する|WikiFactは、専門領域を含む86関係を、Wikidata由来の事実補完へ変えたデータ。複数対象と別名を参照として持つ。<br>Classicで実行された10関係では、問題数も候補数も条件によって違う。各関係を同じ重みで平均する方法と、文字列の正規化、生成候補数をそろえて、公開成績を解釈する。|WikiFactは、Wikidata由来の86関係を文の補完へ変え、一般的な事実から法律・経済・生物医学までを扱う。複数の対象や別名を正解として持つ。<br>HELM Classicの公開成績は10関係の正答率を同じ重みで平均する。候補数の違いと、参照に含まれる名前の範囲が得点に影響する。|
|13|7|6|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|14|8|7|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|15|9|8|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|16|32|25|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|17|33|26|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|18|34|27|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|19|35|28|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|20|36|29|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|21|37|30|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|22|38|31|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|23|39|32|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|24|40|33|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|25|41|34|重複を含むという各頁での制作注は省き、原参照そのものは重複も保持|参照回答（全文・重複を含む）|参照回答（全文）|
|26|36|29|決まった形式で答えるという曖昧な表現を具体化|実例8：発明者を、決まった形式で答える|実例8：医学的評価法の考案者を答える|
|27|36|29|配布参照のまま示すという制作報告を、データに含まれる表記の説明へ|「discovered by」というテンプレートで、医学的評価法の考案者を尋ねる。別表記と重複も配布参照のまま示す。|医学的評価法の考案者を「discovered by」というテンプレートで尋ねる。参照にはVirginia Agparという表記や、同じ名前の重複が含まれる。|
|28|37|30|入力に日付は含まれないという自明な注意を削る|役職名が参照になる。地位の就任日や退任日は、この入力には含まれない。|人物と役職の関係を尋ねる。参照回答は高等法院判事である。|
|29|40|33|現在の国を一律に尋ねないという禁止的注意を具体例の意味へ|歴史上の地域も含む。現在の国の通貨を一律に尋ねる集合ではない。|イギリス領キプロスで用いられた通貨を尋ねる。|
|30|46|36|P50等のID対照は外部記録へ。読者が実例を読み出せるコードに置換|関係<br>ID<br>関係<br>ID<br>著者<br>P50<br>部分・所属先<br>P361<br>通貨<br>P38<br>出生地<br>P19<br>発見者・発明者<br>P61<br>原告<br>P1620<br>分類<br>P31<br>役職<br>P39<br>治療対象<br>P2175<br>症状・徴候<br>P780|公開実行の入力と参照を読むコード|
|31|46|36|実装の細部を実用例に置き換える|公開実行で使う関係とWikidataのID|公開実行のJSONから、入力と参照を読む|
|32|46|36|subject引数の細部より、読むデータの意味を説明|subject引数は関係名を指定する。|scenario_state.jsonは、公式HELMの公開実行に付随するJSONファイル。各問の入力、参照回答、モデル出力を収める。|
|33|46|36|公式実行の生レコードを使う、実際に実行する読込例||import json<br>with open("scenario_state.json", encoding="utf-8") as f:<br>    state = json.load(f)<br>example = state["request_states"][0]["instance"]<br>print(example["input"]["text"])<br>print([r["output"]["text"] for r in example["references"]])|
|34|26|19|独立レビュー：503取得状況と紹介工程は外部記録へ、入手方法と閲覧できる範囲を説明|公式HELMページでは、WikiFactの関係別・モデル別成績と、各問の入力・参照回答・生成結果を閲覧できる。<br>問題データの読込コードは、CodaLabで配布するtrain・dev・testのJSONLを使う。配布先は現在アクセスできないため、ここでは公式サイトで公開されている10関係の実例と成績を紹介した。|公式HELMページでは、WikiFactの関係別・モデル別成績と、各問の入力・参照回答・生成結果を閲覧できる。<br>全86関係の問題は、CodaLabのtrain・dev・test JSONLとして案内されている。公式サイトでは、10関係の公開実行に含まれる入力・参照回答・出力を利用できる。|
|35|37|30|main校正：原templateにない過去時点を補わない|アリソン・フォスターが務めた役職は|アリソン・フォスターの役職は|
|36|52|39|main/独立校正：著者年と実参照日を文献情報として統一|Stanford CRFM · v0.4.0（2023-11-17）· 2026-10-18参照|Stanford CRFM (2023). v0.4.0（2023-11-17）。参照2026-10-18。|
|37|52|39|main/独立校正：著者年と実参照日を文献情報として統一|Stanford CRFM · 公開実装 · 2026-10-18確認|Stanford CRFM (n.d.). 公開実装。参照2026-10-18。|
|38|7|6|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / author/id151（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|39|8|7|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / currency/id156（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|40|9|8|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / plaintiff/id47（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|41|10|15|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM evaluate_reference_metrics. 候補の順位付け・正規化・@K採点。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|[1] Stanford CRFM. HELM evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|
|42|11|16|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|43|23|17|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM evaluate_reference_metrics. 候補の順位付け・正規化・@K採点。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|[1] Stanford CRFM. HELM evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|
|44|26|19|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM WIKIFactScenario. 86関係の辞書と配布ファイルの読込。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|45|32|25|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / instance_of/id150（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|46|33|26|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / medical_condition_treated/id152（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|47|34|27|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / part_of/id151（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|48|35|28|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / place_of_birth/id150（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|49|36|29|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / discoverer_or_inventor/id154（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|50|37|30|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / position_held/id150（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|51|38|31|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / symptoms_and_signs/id156（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|52|39|32|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / author/id153（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|53|40|33|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / currency/id154（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|54|41|34|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。 test / discoverer_or_inventor/id155（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|55|46|36|run内ID・参照日・固定版識別・処理監査の説明を出典から外部記録へ|[1] Stanford CRFM, HELM WIKIFactScenario. 86関係の辞書と配布ファイルの読込。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|56|30|23|監査表を実用コードへ置き換えた章構成に合わせる|関係別成績と実行条件|関係別成績とデータの読込|
|57|30|23|監査表を実用コードへ置き換えた章構成に合わせる|制作チームと参考文献|研究と参考文献|
|58|42|35|監査表を実用コードへ置き換えた章構成に合わせる|関係別成績と実行条件|関係別成績とデータの読込|
|59|42|35|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|60|46|36|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 2. 関係別成績と実行条件|Appendix: 2. 関係別成績とデータの読込|
|61|49|37|監査表を実用コードへ置き換えた章構成に合わせる|制作チームと参考文献|研究と参考文献|
|62|49|37|監査表を実用コードへ置き換えた章構成に合わせる|Appendix: 3. 制作チームと参考文献|Appendix: 3. 研究と参考文献|
|63|51|38|参考文献URLまでnative編集枠に収める|107.11pt|125.11pt|
|64|51|38|参考文献URLまでnative編集枠に収める|107.11pt|125.11pt|
|65|52|39|参考文献URLまでnative編集枠に収める|87.16pt|105.16pt|
|66|52|39|参考文献URLまでnative編集枠に収める|87.16pt|105.16pt|
|67|46|36|実画素の上15.33pt/下24ptを各10ptへ、字形位置は保持|top120pt/height153pt|top125.33pt/height133.67pt|
|68|7|6|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|69|7|6|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|60.172913385826774pt|
|70|8|7|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.838582677165356pt|35.17196850393701pt|
|71|9|8|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.9436220472441pt|35.27700787401575pt|
|72|32|25|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.9436220472441pt|35.27700787401575pt|
|73|32|25|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|74|33|26|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|75|33|26|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.81157480314961pt|60.14496062992126pt|
|76|34|27|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|89.81259842519685pt|83.81259842519685pt|
|77|35|28|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.9436220472441pt|35.27700787401575pt|
|78|35|28|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|79|36|29|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|80|37|30|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|81|37|30|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|60.172913385826774pt|
|82|38|31|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.81157480314961pt|60.14496062992126pt|
|83|39|32|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|84|39|32|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|39.838582677165356pt|35.17196850393701pt|
|85|40|33|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.94456692913386pt|59.61125984251969pt|
|86|40|33|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|58.83952755905512pt|
|87|41|34|実画素の上下余白差を解消。原文/訳の文字・字形位置は保持|64.83952755905511pt|59.506220472440944pt|
|88|29|22|字形位置を保ち、章扉のnative領域を拡張|46.08|54.08|
|89|5|4|元作成主体を一度示し、データの課題を主題にする|WikiFactは、知識基盤Wikidataの「主語・関係・目的語」という三つ組を、英語の短い文に変換した事実補完データである。<br>モデルは「作品の著者は」「国の通貨は」といった文の続きを生成する。根拠となる文章を与えず、モデルが覚えている事実を名前として答えられるかを測る。|WikiFactは、知識基盤Wikidataの「主語・関係・目的語」という三つ組を、英語の短い文に変換した事実補完データである。<br>モデルは「作品の著者は」「国の通貨は」といった文の続きを生成する。根拠となる文章を与えず、モデルが覚えている事実を名前として答えられるかを測る。<br>Stanford CRFMを中心とする研究チームが2022年に設計した。|
|90|6|5|公開実行という制作単位を外し、実際の問題と参照の意味を述べる|同じ作品に複数の著者がいるように、一つの入力に複数の正解がある。また、一つの対象が複数の名前や略号を持つこともある。<br>正解となる対象の名前や別名のいずれかに一致すれば正解とする。次の3例は、公開実行の入力と参照回答の全文である。|同じ作品に複数の著者がいるように、一つの入力に複数の正解がある。また、一つの対象が複数の名前や略号を持つこともある。<br>正解となる対象の名前や別名のいずれかに一致すれば正解とする。次の3例は、公開されている入力と参照回答の全文である。|
|91|10|15|基盤の候補生成設定でなく、データの答え方と評価の意味へ|候補を五つ作り、対数確率で順位を付ける|参照のいずれかに一致すれば正解になる|
|92|10|15|一般の採点条件と実例を説明し、5出力固定/対数確率順位という基盤設定は外部化|HELMでは、1問当たり5候補を生成する設定を使う。出力の対数確率の和で並べ、最上位の候補をAccuracy@1で採点する。<br>Accuracy@5では、最大5候補のどれかが参照回答に一致すれば正解。文字列を小文字化し、冠詞・句読点・余分な空白を除いて照合する。|生成した名前が、参照回答のいずれかに一致した割合で正答率を求める。照合では英字の大小、冠詞、句読点、余分な空白をならす。<br>一つの答えだけを見るAccuracy@1と、複数候補のどれかが合えばよいAccuracy@Kでは、正解とする条件が変わる。次の出力例では、先頭候補と5候補全体を比べる。|
|93|11|16|公開モデル採点監査という見出しを、実例が示すデータの性質へ|実例3の公開モデル出力と採点|略称が、参照回答に含まれない場合|
|94|11|16|真正な既存生成5候補を識別し、試行番号と数値監査を外部化|text-davinci-003、第1試行。@1は0、@5は1（USLは参照にない）。|2023年の公開出力例（text-davinci-003）。先頭候補は不一致、5候補の中には一致する答えがある。|
|95|13|10|基盤の紹介でなく、元課題の着想と設計の貢献を説明|2019年のLAMAは、文の穴埋めを通して言語モデルの事実知識を調べる方法を広めた。<br>HELMではより幅広い知識を対象にするため、法律・経済・生物医学などの関係とテンプレートを手で選び、WikiFactを作った。|2019年のLAMAは、文の穴埋めを通して言語モデルの事実知識を調べる方法を広めた。<br>WikiFactでは対象を法律・経済・生物医学などへ広げ、関係と英語テンプレートを人手で選んだ。|
|96|18|14|モデル別runの結果から、課題の採点へ章を再構成|HELMの採点と公開成績|参照回答に一致するかを評価する|
|97|23|17|参照集合による評価上の限界を保持し、特定runの8トークン出力上限は外部化|実例3ではUSLという略称は参照に含まれず、会社名の全文が必要だった。正規化は略語の展開や、意味の同一性の推論を行わない。<br>出力上限は8トークンなので、長い固有名や複数の答えをまとめる出力は途中で切れる場合がある。参照のいずれか一つに合う短い補完を求める評価となる。|実例3のUSLという略称は、参照回答に含まれていない。人が同じ組織を思い浮かべても、参照に一致する名前でなければ正解にならない。<br>知識基盤の名前や別名の収録範囲が、評価に影響する。複数の参照を持つ場合は、そのうち一つに合う補完を求める。|
|98|23|17|本文から外した生成トークン制限を見出しにも残さず、参照名による採点の特徴を示す|短い補完でも、参照と生成形式が効く|参照に含まれる名前が、正誤を左右する|
|99|26|19|入手と利用できるデータの形式へ|公式サイトで、関係別の成績と出力を見られる|配布JSONLと、公開例から利用を始める|
|100|26|19|データの入手と実用の範囲を示し、プラットフォームの成績閲覧手順を外部化|公式HELMページでは、WikiFactの関係別・モデル別成績と、各問の入力・参照回答・生成結果を閲覧できる。<br>全86関係の問題は、CodaLabのtrain・dev・test JSONLとして案内されている。公式サイトでは、10関係の公開実行に含まれる入力・参照回答・出力を利用できる。|全86関係の問題は、CodaLabのtrain・dev・test JSONLとして案内されている。データの読込実装は、関係を指定して文章と参照回答を取り出す。<br>公式サイトでは、10関係の公開入力・参照回答・出力を閲覧できる。問題の形を調べたり、名前の照合を試したりするために使える。|
|101|27|20|基盤を主語にせず、利用するものごとの条件へ|実装コードはApache 2.0で公開される|読込コードと、加工済みデータの利用条件|
|102|27|20|ライセンス不確実性という実用条件を保ち、基盤名の反復を外す|HELMの実装コードはApache License 2.0で公開される。加工済みWikiFactデータの専用ライセンスは、公式論文と読込コードには明記されていない。<br>データを再配布・再利用する際の条件は、配布元への確認が必要である。|公開されている読込実装はApache License 2.0で提供される。加工済みWikiFactデータの専用ライセンスは、論文と読込コードには明記されていない。<br>データを再配布・再利用する際の条件は、配布元への確認が必要である。|
|103|28|21|元課題の知識範囲・入力・答えをまとめ、特定10関係のrun集計説明は外部化|WikiFactは、Wikidata由来の86関係を文の補完へ変え、一般的な事実から法律・経済・生物医学までを扱う。複数の対象や別名を正解として持つ。<br>HELM Classicの公開成績は10関係の正答率を同じ重みで平均する。候補数の違いと、参照に含まれる名前の範囲が得点に影響する。|WikiFactは、Wikidata由来の86関係を文の補完へ変え、一般的な事実から法律・経済・生物医学までを扱う。複数の対象や別名を正解として持つ。<br>根拠文を与えず、モデルが事実を表す名前を答えられるかを調べる。入力の関係や知識の時点、参照に含まれる名前の範囲が評価の意味を決める。|
|104|46|36|取得可能な本物のレコードの実用読込として示す|公開実行のJSONから、入力と参照を読む|公開例のJSONから、入力と参照を読む|
|105|46|36|基盤解説でなく、実コードが読む形式と内容を明示|scenario_state.jsonは、公式HELMの公開実行に付随するJSONファイル。各問の入力、参照回答、モデル出力を収める。|scenario_state.jsonは、公開された評価記録のJSON。各問の入力、参照回答、モデル出力を収める。|
|106|3|2|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|HELMの採点と公開成績|参照回答に一致するかを評価する|
|107|3|2|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|利用の位置付けと入手方法|データの入手と利用条件|
|108|18|14|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|3. HELMの採点と公開成績|3. 参照回答に一致するかを評価する|
|109|23|17|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|3. HELMの採点と公開成績|3. 参照回答に一致するかを評価する|
|110|24|18|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|利用の位置付けと入手方法|データの入手と利用条件|
|111|24|18|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|4. 利用の位置付けと入手方法|4. データの入手と利用条件|
|112|26|19|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|4. 利用の位置付けと入手方法|4. データの入手と利用条件|
|113|27|20|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|4. 利用の位置付けと入手方法|4. データの入手と利用条件|
|114|28|21|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|4. 利用の位置付けと入手方法|4. データの入手と利用条件|
|115|30|23|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|関係別成績とデータの読込|公開例のデータ形式|
|116|42|35|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|関係別成績とデータの読込|公開例のデータ形式|
|117|42|35|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|Appendix: 2. 関係別成績とデータの読込|Appendix: 2. 公開例のデータ形式|
|118|46|36|モデル成績の章を課題の評価/データ形式へ再構成し、目次と帯を同期|Appendix: 2. 関係別成績とデータの読込|Appendix: 2. 公開例のデータ形式|
|119|10|15|真正出力例を採点章へ配置|1. 事実を文の続きで答える|3. 参照回答に一致するかを評価する|
|120|11|16|真正出力例を採点章へ配置|1. 事実を文の続きで答える|3. 参照回答に一致するかを評価する|
|121|7|6|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|122|8|7|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|123|9|8|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|124|10|15|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|[1] Stanford CRFM. evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|
|125|11|16|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。   https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|126|23|17|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|[1] Stanford CRFM. evaluate_reference_metrics。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py|
|127|26|19|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|128|27|20|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM, HELM. Apache License 2.0（コード）。  https://github.com/stanford-crfm/helm/blob/main/LICENSE|[1] Stanford CRFM. Apache License 2.0（読込コード）。   https://github.com/stanford-crfm/helm/blob/main/LICENSE|
|129|32|25|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|130|33|26|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|131|34|27|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|132|35|28|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|133|36|29|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|134|37|30|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|135|38|31|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|136|39|32|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|137|40|33|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|138|41|34|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM Classic v0.4.0 — WikiFact（2023）。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|139|46|36|実例の原出典と正式実装名を保持し、不要な基盤名の反復を除く|[1] Stanford CRFM. HELM WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM. WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|140|52|39|基盤文献の解説をデータ例の入口へ。URLはそのまま保持|HELM Classic — WikiFact<br>Stanford CRFM (2023). v0.4.0（2023-11-17）。参照2026-10-18。<br>関係別・モデル別の公開成績と予測記録をまとめる。<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|WikiFact<br>Stanford CRFM (2023). 公開入力・参照回答。参照2026-10-18。<br>関係ごとの入力、参照回答、既存モデル出力を閲覧できる。<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|141|52|39|データ形式・読込の一次資料を示し、基盤の一般解説を削除|HELM WIKIFactScenario<br>Stanford CRFM (n.d.). 公開実装。参照2026-10-18。<br>86関係のIDと、問題・参照回答をJSONLから読み込む手順を定義する。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|WIKIFactScenario<br>Stanford CRFM (n.d.). 公開読込実装。参照2026-10-18。<br>86関係のIDと、問題・参照回答をJSONLから読み込む手順を定義する。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|
|142|46|36|実際に読む公開scenario_state.jsonの出所へ出典を合わせる|[1] Stanford CRFM. WIKIFactScenario。 <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py|[1] Stanford CRFM (2023). WikiFact — 公開入力・参照回答。 <br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact|
|143|2||一般のHELM公式成績画面は課題そのものの紹介に不要なため外部化。データ例へのURLは文献に保持。|公式HELMサイト：WikiFactの公開結果<br>WikiFact<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|144|17||特定公開runの10関係/7462件の集計表は基盤固有の取得・評価範囲。入手説明に10関係公開を簡潔に保持。|Classicの公開実行は10関係を含む<br>2. 知識基盤から問題を作る<br>試行間の同一IDをまとめたtestは計7,462問。実装が対応する86関係の全件実行ではない。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|145|19||10関係runの均等平均/試行集計は特定公開成績の条件として外部記録へ。|公開結果は、関係ごとの正答率を平均する<br>3. HELMの採点と公開成績<br>各関係のtestに対し、最上位候補が参照に一致した割合を計算する。その後、10関係の正答率を同じ重みで平均した値が全体の指標。<br>96問の原告も、850問の著者も、全体平均では同じ1関係として扱われる。全7,462問の正誤をそのまま平均した値ではない。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|146|20||モデルごとの候補数/試行数の比較は基盤の実行条件のため外部化。|候補数と試行数も、モデルで違っていた<br>3. HELMの採点と公開成績<br>OPTとtext-davinci-003は、5候補から対数確率最大の候補を選び、各3試行の正答率を平均した。<br>Llama 2 70Bは1試行。設定上は5出力だが、取得した全7,462件のtestレコードには、それぞれ1候補の出力が含まれていた。<br>そのため、Llama 2の公開Accuracy@1と@5は同じ値になる。5候補を生成した条件として比較する値ではない。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|147|21||特定3モデルの公開Accuracyは元課題の概要より実行結果を主題にしているため外部化。|HELM ClassicのAccuracy@1<br>3. HELMの採点と公開成績<br>v0.4.0収録・suite v0.3.0。最大5提示例、temperature 1、出力上限8トークン。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|148|22||特定4関係のモデル比較値も実行記録へ保持。|関係によって正答率は大きく違う<br>3. HELMの採点と公開成績<br>Accuracy@1（%）。各関係を独立に評価。候補数は5／5／1、試行数は3／3／1。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|149|25||根拠なし補完と知識範囲の説明は旧5/28と重複、プラットフォーム対応範囲の確認は外部へ。|文脈の読解と切り分けて、事実知識を測る<br>4. 利用の位置付けと入手方法<br>WikiFactは、文章に根拠が含まれる読解や、検索器が根拠を探す課題と異なり、主語と関係だけから目的語名を生成する。<br>2026-10-18確認のHELM実装にも86関係の読込がある。今回扱う公開成績は2023年のClassic固定版で、現在の知識や最新モデルを評価したものではない。<br>[1] Stanford CRFM, HELM WIKIFactScenario. 86関係の辞書と配布ファイルの読込。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py||
|150|43||特定モデル別10関係の全成績表は評価基盤の実行記録へ。|10関係のAccuracy@1（前半）<br>Appendix: 2. 関係別成績と実行条件<br>単位は%。候補数は5／5／1、試行数は3／3／1。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|151|44||同上。元入力/参照は13実例を全文保持。|10関係のAccuracy@1（後半）<br>Appendix: 2. 関係別成績と実行条件<br>単位は%。候補数は5／5／1、試行数は3／3／1。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|152|45||特定モデルの@1/@5集計は外部へ。@Kの意味と真正5出力例は旧10/11へ保持。|5候補を許すと、得点が上がる<br>Appendix: 2. 関係別成績と実行条件<br>10関係の単純平均、3試行平均。Llama 2は実出力が1候補なので、この5候補比較から外した。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|153|50||作成チーム役割・基盤紹介の重複。作成主体/年は旧5へ一度、元LAMAと設計の拡張は旧13へ。|HELMの知識評価として新規に構築した<br>Appendix: 3. 制作チームと参考文献<br>WikiFactはHELM論文で導入されたデータセット。論文の貢献記録では、Hongyu Renが設計・実装、Lucia Zhengがデータ注釈・前処理を担当したとされる。<br>Michihiro Yasunagaが知識評価チームを率い、Neel Guhaらも設計に参加。プロジェクト全体はPercy Liangが統括した。<br>文の補完形式はLAMAを受け継ぎつつ、法律・経済・生物医学を含む幅広い関係へ対象を広げた。<br>[1] Liang et al. (2023), Holistic Evaluation of Language Models. Transactions on Machine Learning Research.  https://arxiv.org/abs/2211.09110||
|154|47||候補設定と実出力の照合表は旧20と重複。実候補数5/5/1・3/3/1試行と得点への影響は本編に保持。|設定の5出力と、返った候補数<br>Appendix: 2. 関係別成績と実行条件<br>Llama 2の全10関係test7,462件を取得して確認。max_tokens 8、stopは改行、最大提示例数5。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||
|155|48||実例選定・SHA/ID照合工程は監査記録へ。2022年1月という対象時点は本編に保持。|取得した入力と参照から再照合できる<br>Appendix: 2. 関係別成績と実行条件<br>13実例は、公開text-davinci-003のtest・第1試行から選んだ。全10関係を少なくとも1件ずつ含むが、頻度を代表する無作為標本ではない。<br>原文、全参照、全5候補、対数確率、条件内ID、固定run URL、取得SHA-256を保存した。参照に同じ名前が重複していても、原レコードでは保持した。<br>入力にある古い国・過去の役職も、2022年1月の知識基盤を基にした設計の一部として示す。<br>[1] Stanford CRFM, HELM Classic v0.4.0, WikiFact. 2023-11-17の固定版。2026-10-18参照。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
