# TwitterAAE：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|5|5|読者に必要な説明へ整理|TwitterAAEは、Twitter上のAfrican-American English（AAE）に関連する言語を、地域の人口統計と言葉の共起から分析する資源。|TwitterAAEは、Twitter上のアフリカ系米国人英語（AAE）に関連する表現を調べる言語資源。投稿の位置に対応する地域の人口構成と、使われる言葉の関係から分析する。|
|2|6||読者に必要な説明へ整理|HELMは、AA寄り・white寄りの言語混合比で抽出した二つの投稿集合に、言語モデルが付ける確率を測る。|HELMでは、AA系・white系の言語的特徴が多い投稿をそれぞれ集め、言語モデルがどれだけ予測できるかを比べる。|
|3|7|6|読者に必要な説明へ整理|実例はHELMの公開実行入力から示す|AA・whiteは、言語の特徴に基づく抽出条件|
|4|7|6|読者に必要な説明へ整理|以下の3例とAppendixの10例は、公開されたscenario_stateから選んだ別々の投稿。元の大文字・つづり・句読点を保って全文を示す。|本編3例と追加10例は、HELMの公開評価に使われた13件の投稿全文。大文字や独自のつづり、句読点にも会話の特徴が現れる。|
|5|7|6|読者に必要な説明へ整理|aa／whiteはデータの抽出条件名。元の推定値は、人口統計に関連付けられた言語が文中で占める割合であり、話者の自己申告人種ではない。|aa／whiteは抽出条件の名前。地域の人口構成に関連する言語の混合比を使っており、投稿者の自己申告による人種を表すラベルではない。|
|6|8|7|読者に必要な説明へ整理|OOMFはone of my followersの略。大文字やつづりの工夫も、実際に採点された文字列の一部。|OOMFはone of my followers（フォロワーの一人）の略。FONEやJUSなど、発音に近づけたつづりも使う。|
|7|9|8|読者に必要な説明へ整理|bruhという呼びかけとwannaの縮約を含む。語りかけの調子を保って訳した。|bruhはくだけた呼びかけ。wannaはwant toの縮約で、短い投稿でも会話の調子が伝わる。|
|8|10|9|読者に必要な説明へ整理|実例3：white側にもくだけた会話がある|実例3：white側にも語りかけの表現がある|
|9|13|12|読者に必要な説明へ整理|これは近隣地域の人口構成を介した遠隔教師信号。個人に人種を尋ねた注釈は付けていない。|近隣地域の人口構成を、投稿の言語的特徴を推定する手掛かりにする。|
|10|14|13|読者に必要な説明へ整理|同じ人が投稿ごとに異なる表現を使える設計。特定のキーワードを一度使っただけで、その人の全投稿を同じ言語に固定しない。|同じ人でも、投稿によって使う表現は変わる。ユーザー単位と投稿単位の混合比で、その変化を表現する。|
|11|15|14|読者に必要な説明へ整理|言語的特徴との対応を確かめた|AAEに特徴的な文法が多く現れる|
|12|16||読者に必要な説明へ整理|2016年の集合とHELMの集合は作り方が違う|HELMは、投稿ごとの言語的特徴で集合を作る|
|13|16||読者に必要な説明へ整理|HELMの公開コードが記載する二段階の抽出。2016年の解析集合をそのまま5万件にしたものではない。|2016年の分析はユーザーごとに選び、HELMは投稿ごとの混合比で選ぶ。|
|14|18||読者に必要な説明へ整理|低いbits per byteほど投稿を予測できる|BPBが低いほど、投稿を予測しやすい|
|15|19||読者に必要な説明へ整理|BPB、低いほど良い。Classic v0.4.0収録・suite v0.3.0、各条件1,000投稿、提示例0、各1試行。|BPB（低いほど良い）。2022年公開の2モデルを、AA・white各1,000投稿で比較。提示例なし。|
|16|20||読者に必要な説明へ整理|得点差は、二つの抽出集合での予測の差|AA側の投稿では、両モデルとも予測が難しい|
|17|20||読者に必要な説明へ整理|集合にはつづり、話題、長さ、会話の形式などの違いも含まれる。同じ内容だけを方言で書き換えた対訳実験ではない。|二つの集合には、つづり・話題・長さ・会話の形式などの違いがある。得点差には、こうした内容や表現の違いが含まれる。|
|18|20||モデル公開年と評価対象を直前の表で示しており、現在順位でないという重複注意を削除|この値が示すのは公開実行時の投稿集合での差であり、2026年のモデルの順位ではない。||
|19|23|17|読者に必要な説明へ整理|HELM Classicは別途抽出した投稿を言語モデリングに用いる。2026-10-18確認の公開実装にもAA／whiteの両条件が残る。|HELM Classicでは、同じ元コーパスから投稿を別途抽出し、言語モデルの予測しやすさを比べる評価へ広がった。|
|20|24|18|読者に必要な説明へ整理|公式配布とHELMの公開記録を使い分ける|研究用コーパスと評価結果を公式サイトで入手する|
|21|24|18|読者に必要な説明へ整理|HELMの5万件CSVはCodaLabのURLを参照する。今回の取得では双方503となったが、公開実行の1,000投稿ずつと得点は取得できた。|HELMはAA・white各5万投稿のCSVを案内し、Classicの評価ページで、実際に使った投稿とモデルの得点を公開している。|
|22|24|18|読者に必要な説明へ整理|推定モデルのコードにはMITライセンスがある。投稿本文の権利や再配布範囲は、コードのMITライセンスとは別に扱う。|推定モデルのコードはMITライセンス。投稿本文の利用は、公式サイトの研究目的という条件と、元投稿の権利を確認する。|
|23|25|19|読者に必要な説明へ整理|元の集合の作り方と公開実行の範囲を押さえると、投稿の予測しにくさと、既存NLP処理の取りこぼしを具体的に捉えられる。|言語モデルの予測しやすさと、言語同定による取りこぼしを調べることで、NLPが扱える会話の範囲を見直せる。|
|24|27|21|読者に必要な説明へ整理|追加の投稿例<br>版・実行条件の補足<br>研究と参考文献|追加の投稿例<br>入力と指標の補足<br>研究と参考文献|
|25|39||読者に必要な説明へ整理|版・実行条件の補足|入力と指標の補足|
|26|39||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|27|40||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|28|41||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|29|42||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|30|43||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|31|44||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|32|45||読者に必要な説明へ整理|Appendix: 2. 版・実行条件の補足|Appendix: 2. 入力と指標の補足|
|33|29|23|読者に必要な説明へ整理|何を数えているかは、この投稿だけでは分からない。|終わった数と残りの数を、短い対比で伝える。|
|34|30|24|読者に必要な説明へ整理|afの強調を、日本語でも強い話し言葉で表した。|afは強い強調を加える俗語。hungryと組み合わせ、空腹の強さを伝える。|
|35|32|26|読者に必要な説明へ整理|ndはandに相当する。反復と感嘆符も表現の一部。|ndはandの略。writenの反復と感嘆符が、書き続ける調子を作る。|
|36|36|30|読者に必要な説明へ整理|thisの指す内容は公開された一文からは特定できない。|thisの具体的な内容は省かれ、続けることへの迷いを短く伝える。|
|37|37|31|読者に必要な説明へ整理|I cannot even.は文脈に依存する口語表現として訳した。|I cannot even.は、驚きやあきれなどで言葉が続かないことを表す口語表現。|
|38|38|32|読者に必要な説明へ整理|時間の数値と疑問の調子を保った。|3時間という長さと、まだ疲れているという疑問を一息に伝える。|
|39|40||読者に必要な説明へ整理|公開実行入力の長さを確かめた|HELMの投稿は、AA側が平均約40文字|
|40|40||読者に必要な説明へ整理|Unicodeコードポイント数。エスケープ文字列は入力のまま数えた。元の2013年ツイート表示上の文字数ではない。|HELMで使われた各1,000投稿の文字数。Unicodeの文字単位で、エスケープ表現も入力のつづりどおり数えた。|
|41|41||読者に必要な説明へ整理|文字の表現も、評価入力の一部になる|絵文字のエスケープ表現も入力に含む|
|42|41||読者に必要な説明へ整理|公開入力には、絵文字を文字列のまま表した「\ud83d\ude02」のようなエスケープ表現もある。|HELMの入力には、絵文字を「\ud83d\ude02」のようなエスケープ表現にした投稿もある。|
|43|41||読者に必要な説明へ整理|本資料の実例はそれらを復号・訂正せず、公開実行で使われたinput.textを保存する。短い自然文だけを選び、本文の実例で表記を追いやすくした。|モデルは、この表現を含む文字列に確率を付ける。画面で絵文字として表示した場合とは、入力の長さやトークンの分割が変わる。|
|44|41||HELM内IDとTwitter IDの照合説明は制作記録へ移す|HELM内のid11841などは投稿のTwitter IDではなく、条件内のインスタンスID。同じ番号でもAAとwhiteで本文が異なる。||
|45|42||読者に必要な説明へ整理|公開実行の設定は両モデルで共通|公開実行のJSONから、投稿全文を読み出す|
|46|42||再現設定の列挙を、実際の投稿本文を読むコードへ置換|設定 ／ 値<br>method ／ language_modeling<br>max_eval_instances ／ 1,000（test）<br>max_train_instances / 試行数 ／ 0 / 1<br>temperature / max_tokens ／ 0 / 0<br>prompt_truncated ／ 0（両モデル・両条件）|import json<br>with open("scenario_state.json", encoding="utf-8") as f:<br>    state = json.load(f)<br>post = state["request_states"][0]["instance"]<br>print(post["input"]["text"])|
|47|42||読者に必要な説明へ整理|生成した回答の採点ではなく、echo_promptで既存の投稿の確率を取得する。|公開されたscenario_state.jsonには、評価に使った投稿とリクエストを収める。最初の投稿のinput.textを取り出す。|
|48|43||読者に必要な説明へ整理|BPBは投稿ごとの比を単純平均しない|BPBは、全投稿の総byte数で割って求める|
|49|43||読者に必要な説明へ整理|投稿ごとの長さで重みが変わる、総byte数による集約。トークン単位のperplexityとは分母が異なる。|すべての投稿の対数確率とbyte数を合計してから計算するため、長い投稿ほど大きな重みを持つ。|
|50|12|11|メインレビュー：収集対象を示す条件を簡潔に説明し、閾値は記録へ|フォロワー1,000人以上の著者、3個以上のハッシュタグ、http・follow・mentionを含む投稿、リツイートなどを除いた。|フォロワーの多いアカウントや、ハッシュタグの多い投稿、リンク・宣伝語を含む投稿、リツイートなどを除いた。|
|51|16||番号・検査用表現を自然な説明へ整理|ユーザーの対応言語比率80%以上、他2成分の合計5%未満。AA約83万／white約730万投稿。|ユーザーの対応言語成分80%以上、ヒスパニック系・アジア系は計5%未満。AA約83万／white約730万投稿。|
|52|25|19|メインレビュー：言語抽出集合という不自然な語を具体化|HELMは、同じコーパスから二つの言語抽出集合を作り、それぞれの投稿に対するBPBを比べる。|HELMは、同じコーパスから言語的特徴で選んだ二つの投稿集合を作り、それぞれの投稿に対するBPBを比べる。|
|53|18||メインレビュー：BPBの負符号を明示|言語モデルは、先行する文字列を条件に各トークンの確率を付ける。予測対象の対数確率を合計し、そのbyte数で割ってbitsへ換算する。|言語モデルは、先行する文字列を条件に各トークンの確率を付ける。予測対象の負の対数確率を合計し、そのbyte数で割ってbitsへ換算する。|
|54|16||文言自然化後のセル・表注重複を実描画で修正|2行想定の行高・表注位置|割合の説明3行に合わせ行高と表注を再配置|
|55|2|2|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. 2026-10-18参照。  https://slanglab.cs.umass.edu/TwitterAAE/|[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. https://slanglab.cs.umass.edu/TwitterAAE/|
|56|6||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM TwitterAAEScenario. AA／whiteの抽出とtestインスタンス。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|[1] Stanford CRFM, HELM TwitterAAEScenario. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|
|57|7|6|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Blodgett et al. (n.d.), twitteraae. 人口統計と言語を結ぶ混合モデルのREADME。2026-10-18参照。  https://github.com/slanglab/twitteraae|[1] Blodgett et al. (n.d.), twitteraae. 人口統計と言語を結ぶ混合モデルのREADME。https://github.com/slanglab/twitteraae|
|58|8|7|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id19602（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|59|9|8|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id15055（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|60|10|9|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: white/id12363（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|61|16||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM TwitterAAEScenario. AA／whiteの抽出とtestインスタンス。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|[1] Stanford CRFM, HELM TwitterAAEScenario. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|
|62|18||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM BasicMetrics. 対数確率・byte数からの集約。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py|[1] Stanford CRFM, HELM BasicMetrics. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py|
|63|19||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|64|20||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|65|23|17|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Blodgett, Wei & O’Connor (2018), Twitter Universal Dependency Parsing for African-American and Mainstream American English. ACL, 1415–1425.<br>https://aclanthology.org/P18-1131/<br>[2] Stanford CRFM, HELM TwitterAAEScenario. AA／whiteの抽出とtestインスタンス。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|[1] Blodgett, Wei & O’Connor (2018), Twitter Universal Dependency Parsing for African-American and Mainstream American English. ACL, 1415–1425.<br>https://aclanthology.org/P18-1131/<br>[2] Stanford CRFM, HELM TwitterAAEScenario. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|
|66|24|18|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. 2026-10-18参照。  https://slanglab.cs.umass.edu/TwitterAAE/|[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. https://slanglab.cs.umass.edu/TwitterAAE/|
|67|29|23|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id42642（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|68|30|24|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id8369（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|69|31|25|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id46250（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|70|32|26|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id24647（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|71|33|27|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: aa/id29079（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|72|34|28|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: white/id32104（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|73|35|29|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: white/id46712（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|74|36|30|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: white/id42460（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|75|37|31|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: white/id19412（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|76|38|32|照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。 instance: white/id5140（HELM内ID）<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|77|40||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|78|41||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|79|42||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|80|43||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM BasicMetrics. 対数確率・byte数からの集約。2026-10-18確認。<br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py<br>[2] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM BasicMetrics.  https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py<br>[2] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|81|44||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] Stanford CRFM, HELM Classic v0.4.0, TwitterAAE. 公開実行suite v0.3.0。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae|
|82|45||照合情報・原行ID・取得日を外部記録へ移し、通常の引用に整理|[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. 2026-10-18参照。  https://slanglab.cs.umass.edu/TwitterAAE/|[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. https://slanglab.cs.umass.edu/TwitterAAE/|
|83|48|35|文献URLがnative文字枠内に収まる高さを確保。字形位置は保持|height 128.200 pt|height 146.200 pt|
|84|48|35|文献URLがnative文字枠内に収まる高さを確保。字形位置は保持|height 108.250 pt|height 126.250 pt|
|85|49|36|文献URLがnative文字枠内に収まる高さを確保。字形位置は保持|height 107.110 pt|height 125.110 pt|
|86|49|36|文献URLがnative文字枠内に収まる高さを確保。字形位置は保持|height 87.160 pt|height 105.160 pt|
|87|8|7|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上14.24pt/下16.50pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|88|9|8|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|89|10|9|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|90|29|23|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|91|30|24|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|92|31|25|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下16.46pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|93|32|26|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|94|33|27|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|95|34|28|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下16.46pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|96|35|29|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|97|36|30|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|98|37|31|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上14.91pt/下16.46pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|99|38|32|実描画の字形を基準に引用背景を均等化。原文の字形位置・全文は保持|上13.57pt/下11.13pt|上7pt/下7pt、訳と注記を下辺調整に合わせ移動|
|100|42||実字形位置を保持してコード背景を8–12ptへ合わせる|上14pt/下18.51pt|上10pt/下10.01pt|
|101|45||全体ZIP未取得・SHA保存・原票照合などの制作監査。研究目的と権利条件は本編24頁に保持|公開範囲と取得できた範囲<br>Appendix: 2. 入力と指標の補足<br>公式の全体ZIP（5.5 GB）は未取得。公式UD配布ZIPと公開HELM入力2,000件を取得し、13実例は後者から選定した。<br>公式サイトは研究目的での利用と論文の引用を求めている。投稿本文についての包括的な再配布許諾は確認できなかった。<br>原文、訳、条件内ID、固定実行URL、原レコード、取得ファイルのSHA-256を制作記録へ保存した。<br>[1] UMass SLANG Lab (n.d.), TwitterAAE: Research on African-American English on Twitter. https://slanglab.cs.umass.edu/TwitterAAE/||
|102|1|1|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|African-American English on Twitter<br>会話の言語的多様性と言語モデルの評価|African-American English on Twitter<br>会話の言語的多様性を捉えるコーパス|
|103|3|3|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|投稿の実例と言語モデルの課題<br>人口統計と言語を結ぶ構築方法<br>HELMの評価条件と結果<br>利用の変化と公開範囲|投稿の実例と言語的特徴<br>人口統計と言語を結ぶ構築方法<br>HELMの評価条件と結果<br>利用の変化と公開範囲|
|104|4|4|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|投稿の実例と言語モデルの課題|投稿の実例と言語的特徴|
|105|4|4|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|106|5|5|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|107|6||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|108|7|6|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|109|8|7|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|110|9|8|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|111|10|9|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|1. 投稿の実例と言語モデルの課題|1. 投稿の実例と言語的特徴|
|112|22|16|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. 利用の変化と公開範囲|3. 公開データと解析への利用|
|113|23|17|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. 利用の変化と公開範囲|3. 公開データと解析への利用|
|114|24|18|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. 利用の変化と公開範囲|3. 公開データと解析への利用|
|115|25|19|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. 利用の変化と公開範囲|3. 公開データと解析への利用|
|116|22|16|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|利用の変化と公開範囲|公開データと解析への利用|
|117|3|3|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|投稿の実例と言語的特徴<br>人口統計と言語を結ぶ構築方法<br>HELMの評価条件と結果<br>利用の変化と公開範囲|投稿の実例と言語的特徴<br>人口統計と言語を結ぶ構築方法<br>公開データと解析への利用|
|118|7|6|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|AA・whiteは、言語の特徴に基づく抽出条件|AA・whiteは、言語的特徴に基づく名前|
|119|7|6|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|本編3例と追加10例は、HELMの公開評価に使われた13件の投稿全文。大文字や独自のつづり、句読点にも会話の特徴が現れる。|本編3例と追加10例では、異なる13件の投稿全文を示す。大文字や独自のつづり、句読点にも会話の特徴が現れる。|
|120|7|6|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|aa／whiteは抽出条件の名前。地域の人口構成に関連する言語の混合比を使っており、投稿者の自己申告による人種を表すラベルではない。|aa／whiteは、地域の人口構成に関連する言語の混合比に基づく名前。投稿者の自己申告による人種を表すラベルではない。|
|121|21|15|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|3. HELMの評価条件と結果|2. 人口統計と言語を結ぶ構築方法|
|122|23|17|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|会話の解析から、言語モデルの格差測定へ|構文解析のための注釈も公開されている|
|123|23|17|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM Classicでは、同じ元コーパスから投稿を別途抽出し、言語モデルの予測しやすさを比べる評価へ広がった。||
|124|23|17|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|[1] Blodgett, Wei & O’Connor (2018), Twitter Universal Dependency Parsing for African-American and Mainstream American English. ACL, 1415–1425.<br>https://aclanthology.org/P18-1131/<br>[2] Stanford CRFM, HELM TwitterAAEScenario. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py|[1] Blodgett, Wei & O’Connor (2018). Twitter Universal Dependency Parsing for African-American and Mainstream American English. ACL, 1415–1425.<br>https://aclanthology.org/P18-1131/|
|125|24|18|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|研究用コーパスと評価結果を公式サイトで入手する|公式サイトで、コーパスと解析用資源を入手する|
|126|24|18|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELMはAA・white各5万投稿のCSVを案内し、Classicの評価ページで、実際に使った投稿とモデルの得点を公開している。|言語混合比の推定モデルと、2018年の構文解析用注釈も、公式ページから入手できる。|
|127|25|19|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELMは、同じコーパスから言語的特徴で選んだ二つの投稿集合を作り、それぞれの投稿に対するBPBを比べる。|2016年の研究は、既知のAAEの文法との対応や、言語同定・構文解析ツールによる扱いの差を調べた。|
|128|25|19|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|言語モデルの予測しやすさと、言語同定による取りこぼしを調べることで、NLPが扱える会話の範囲を見直せる。|方言を含む意見や会話も扱えるNLPのために、言語的な多様性を研究する資源となる。|
|129|25|19|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|[1] Liang et al. (2023), Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110|[1] Blodgett, Green & O’Connor (2016). Demographic Dialectal Variation in Social Media: A Case Study of African-American English. EMNLP, 1119–1130.<br>https://aclanthology.org/D16-1120/|
|130|27|21|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|追加の投稿例<br>入力と指標の補足<br>研究と参考文献|追加の投稿例<br>投稿の表記の補足<br>研究と参考文献|
|131|39||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|入力と指標の補足|投稿の表記の補足|
|132|39||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 2. 入力と指標の補足|Appendix: 2. 投稿の表記の補足|
|133|40||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 2. 入力と指標の補足|Appendix: 2. 投稿の表記の補足|
|134|41||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 2. 入力と指標の補足|Appendix: 2. 投稿の表記の補足|
|135|42||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 2. 入力と指標の補足|Appendix: 2. 投稿の表記の補足|
|136|43||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 2. 入力と指標の補足|Appendix: 2. 投稿の表記の補足|
|137|44||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 2. 入力と指標の補足|Appendix: 2. 投稿の表記の補足|
|138|41||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|絵文字のエスケープ表現も入力に含む|絵文字が文字列として記された投稿もある|
|139|41||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELMの入力には、絵文字を「\ud83d\ude02」のようなエスケープ表現にした投稿もある。|ここに示す投稿には、絵文字を「\ud83d\ude02」のような文字列で記したものもある。|
|140|41||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|モデルは、この表現を含む文字列に確率を付ける。画面で絵文字として表示した場合とは、入力の長さやトークンの分割が変わる。|大文字・つづり・絵文字の表記も、元の投稿例どおりに読む。|
|141|49|36|評価基盤HELMの文献は外部記録へ移し、元2016/2018研究と公式配布を案内|Holistic Evaluation of Language Models<br>Percy Liang et al. · 2023 · Transactions on Machine Learning Research<br>多様なシナリオと指標をそろえ、言語モデルの能力と格差を測るHELMの評価設計。<br>https://arxiv.org/abs/2211.09110||
|142|8|7|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|143|9|8|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|144|10|9|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / white抽出条件・投稿全文|投稿全文 / white群（言語的特徴で抽出）|
|145|29|23|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|146|30|24|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|147|31|25|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|148|32|26|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|149|33|27|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / aa抽出条件・投稿全文|投稿全文 / aa群（言語的特徴で抽出）|
|150|34|28|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / white抽出条件・投稿全文|投稿全文 / white群（言語的特徴で抽出）|
|151|35|29|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / white抽出条件・投稿全文|投稿全文 / white群（言語的特徴で抽出）|
|152|36|30|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / white抽出条件・投稿全文|投稿全文 / white群（言語的特徴で抽出）|
|153|37|31|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / white抽出条件・投稿全文|投稿全文 / white群（言語的特徴で抽出）|
|154|38|32|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|HELM test / white抽出条件・投稿全文|投稿全文 / white群（言語的特徴で抽出）|
|155|27|21|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|追加の投稿例<br>投稿の表記の補足<br>研究と参考文献|追加の投稿例<br>研究と参考文献|
|156|46|33|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 3. 研究と参考文献|Appendix: 2. 研究と参考文献|
|157|47|34|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 3. 研究と参考文献|Appendix: 2. 研究と参考文献|
|158|48|35|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 3. 研究と参考文献|Appendix: 2. 研究と参考文献|
|159|49|36|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Appendix: 3. 研究と参考文献|Appendix: 2. 研究と参考文献|
|160|5|5|構築方法の主述と対象が伝わる日本語へ自然化|TwitterAAEは、Twitter上のアフリカ系米国人英語（AAE）に関連する表現を調べる言語資源。投稿の位置に対応する地域の人口構成と、使われる言葉の関係から分析する。|TwitterAAEは、Twitter上のアフリカ系米国人英語（AAE）に関連する表現を調べる言語資源。投稿位置に対応する地域の人口構成と言葉の使い方を結び付けて構築した。|
|161|6||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|HELMでは、投稿の予測しやすさを比べる<br>1. 投稿の実例と言語的特徴<br>HELMでは、AA系・white系の言語的特徴が多い投稿をそれぞれ集め、言語モデルがどれだけ予測できるかを比べる。<br>入力は投稿全文で、直前までの文字列から次のトークンを予測する。参照回答の代わりに、実際に書かれた文字列の確率を評価する。<br>[1] Stanford CRFM, HELM TwitterAAEScenario. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py||
|162|16||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|HELMは、投稿ごとの言語的特徴で集合を作る<br>2. 人口統計と言語を結ぶ構築方法<br>2016年の分析はユーザーごとに選び、HELMは投稿ごとの混合比で選ぶ。<br>[1] Stanford CRFM, HELM TwitterAAEScenario. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py||
|163|17||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|HELMの評価条件と結果<br>3. HELMの評価条件と結果||
|164|18||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|BPBが低いほど、投稿を予測しやすい<br>3. HELMの評価条件と結果<br>言語モデルは、先行する文字列を条件に各トークンの確率を付ける。予測対象の負の対数確率を合計し、そのbyte数で割ってbitsへ換算する。<br>bits per byte（BPB）は、1 byteを表すために必要な平均情報量。低いほど、その文字列に高い確率を与えている。<br>トークンの区切りがモデル間で異なるため、HELMの主要指標にはbyteで正規化したBPBを使う。<br>[1] Stanford CRFM, HELM BasicMetrics. <br>https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py||
|165|19||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|HELMではAA側のBPBが高かった<br>3. HELMの評価条件と結果<br>BPB（低いほど良い）。2022年公開の2モデルを、AA・white各1,000投稿で比較。提示例なし。<br>[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae||
|166|20||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|AA側の投稿では、両モデルとも予測が難しい<br>3. HELMの評価条件と結果<br>byte数で正規化した予測の難しさは、両モデルともAA抽出条件の投稿で大きかった。<br>二つの集合には、つづり・話題・長さ・会話の形式などの違いがある。得点差には、こうした内容や表現の違いが含まれる。<br>[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae||
|167|40||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|HELMの投稿は、AA側が平均約40文字<br>Appendix: 2. 投稿の表記の補足<br>HELMで使われた各1,000投稿の文字数。Unicodeの文字単位で、エスケープ表現も入力のつづりどおり数えた。<br>[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae||
|168|42||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|公開実行のJSONから、投稿全文を読み出す<br>Appendix: 2. 投稿の表記の補足<br>公開されたscenario_state.jsonには、評価に使った投稿とリクエストを収める。最初の投稿のinput.textを取り出す。<br>[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae<br>import json<br>with open("scenario_state.json", encoding="utf-8") as f:<br>    state = json.load(f)<br>post = state["request_states"][0]["instance"]<br>print(post["input"]["text"])||
|169|43||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|BPBは、全投稿の総byte数で割って求める<br>Appendix: 2. 投稿の表記の補足<br>予測対象トークンの対数確率の総和をL、予測対象のbyte数の総和をBとすると、BPB = −L / (B × ln 2)。<br>すべての投稿の対数確率とbyte数を合計してから計算するため、長い投稿ほど大きな重みを持つ。<br>実例1のtext-davinci-003では、対数確率の和は−101.668、52 byte。1投稿のBPBは約2.821となる。<br>[1] Stanford CRFM. HELM BasicMetrics.  https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py<br>[2] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae||
|170|44||HELM固有の投稿抽出・予測タスク・BPB/PPL成績・指標計算・保存実行JSONの説明を外部へ移す。元2016年の構築/文法/言語同定を中心に構成|perplexityでは分母がトークンになる<br>Appendix: 2. 投稿の表記の補足<br>同じ公開実行のperplexity。モデル間ではトークンの分割が異なるため、主要な比較にはBPBを用いた。<br>[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae||
|171|39||保存入力の文字列表記の補足は元データセット紹介から外部記録へ移す|投稿の表記の補足<br>Appendix: 2. 投稿の表記の補足||
|172|41||保存入力のUnicodeエスケープ監査を外部化。選定13投稿の原文/訳は保持|絵文字が文字列として記された投稿もある<br>Appendix: 2. 投稿の表記の補足<br>ここに示す投稿には、絵文字を「\ud83d\ude02」のような文字列で記したものもある。<br>大文字・つづり・絵文字の表記も、元の投稿例どおりに読む。<br>[1] Stanford CRFM. HELM Classic v0.4.0 — TwitterAAE.  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
