# C³：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|3|3|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|文書から、正しい選択肢を選ぶ<br>収集と、問われる知識<br>評価と歴史的な性能<br>CLUE・CLEVAでの利用|文書から、正しい選択肢を選ぶ<br>収集と、問われる知識<br>正答率と構築時の性能<br>入手方法とCLUE・CLEVA|
|2|6|6|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / train / ID 37-153 / 質問1||
|3|7|7|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / train / ID 37-153 / 質問1||
|4|9|9|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 11-67 / 質問1||
|5|10|10|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 11-67 / 質問1||
|6|12|12|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / test / ID 9-120 / 質問1||
|7|22|21|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|3. 評価と歴史的な性能|3. 正答率と構築時の性能|
|8|23|22|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|3. 評価と歴史的な性能|3. 正答率と構築時の性能|
|9|24|23|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|3. 評価と歴史的な性能|3. 正答率と構築時の性能|
|10|25|24|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|3. 評価と歴史的な性能|3. 正答率と構築時の性能|
|11|26|25|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|3. 評価と歴史的な性能|3. 正答率と構築時の性能|
|12|27|26|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|4. CLUE・CLEVAでの利用|4. 入手方法とCLUE・CLEVA|
|13|28|27|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|4. CLUE・CLEVAでの利用|4. 入手方法とCLUE・CLEVA|
|14|30|28|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|4. CLUE・CLEVAでの利用|4. 入手方法とCLUE・CLEVA|
|15|31|29|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|4. CLUE・CLEVAでの利用|4. 入手方法とCLUE・CLEVA|
|16|32|30|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|4. CLUE・CLEVAでの利用|4. 入手方法とCLUE・CLEVA|
|17|34|32|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|追加の公開実例<br>版・原位置・再現<br>研究と参考文献|追加の公開実例<br>データの読み方<br>研究と参考文献|
|18|36|34|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 11-30 / 質問1||
|19|37|35|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 11-57 / 質問1||
|20|38|36|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 11-57 / 質問1||
|21|39|37|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 17-3 / 質問1||
|22|40|38|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 28-8 / 質問1||
|23|41|39|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 37-120 / 質問1||
|24|42|40|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Dialogue / dev / ID 37-120 / 質問1||
|25|43|41|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 8-707 / 質問1||
|26|44|42|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 8-160 / 質問1||
|27|45|43|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 9-269 / 質問1||
|28|46|44|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 11-14 / 質問1||
|29|47|45|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / dev / ID 11-14 / 質問1||
|30|48|46|追跡用のsplit・ID・質問indexは外部記録へ移す。文書・質問・選択肢は全て保持。|C³-Mixed / test / ID 8-255 / 質問1||
|31|52|50|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|版・原位置・再現|データの読み方|
|32|52|50|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|Appendix: 2. 版・原位置・再現|Appendix: 2. データの読み方|
|33|55|51|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|Appendix: 2. 版・原位置・再現|Appendix: 2. データの読み方|
|34|57|52|章名から監査・再現の語を外し、利用に関する内容を具体的に示す。|Appendix: 2. 版・原位置・再現|Appendix: 2. データの読み方|
|35|4|4|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|書かれたことと、分かることをつなぐ|文書から、正しい選択肢を選ぶ|
|36|8|8|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|似た語があっても、理由の主体は違う|父親は、会話の不足を理由に挙げている|
|37|8|8|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|父親が明言する「ほとんど会話がない」が理由。息子にかかる重圧を、父親自身の重圧と取り違えない。<br>父親が忙しいこと、会話がないこと、息子に重圧があることを、話者と因果関係に沿って結び付ける。<br>この父子会話はCLEVAの論文にも例として載る。ここでは、元C³の公開学習データにある一問として示した。|父親が理由として述べたのは、息子との会話がほとんどないこと。重圧がかかっているのは息子である。<br>父親が忙しいこと、会話がないこと、息子に重圧があることを、話者と因果関係に沿って結び付ける。<br>この父子会話は、CLEVAの論文にも読解の例として掲載されている。|
|38|17|16|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|文書と質問を分けて数える。学習・開発・テストの件数は、元の6ファイルと一致。|一つの文書に複数の質問が付くため、文書数より質問数が多い。|
|39|19|18|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|語句の照合を越えて、必要な知識を分ける|言語・専門・一般常識の知識を問う|
|40|21|20|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|正解を明示的・暗示的に支える最小の文数も注釈した。600問の36.7％は1文、62.0％は複数文、1.3％は文脈に依存しない。<br>Dialogueでは77.0％が複数文に支えられる。離れた発言、話者の関係、省略された場面をつなぐ必要がある。<br>注釈者間の一致度はCohenのκ＝0.62。86.8％などは、この600問の分析結果である。|正解を明示的・暗示的に支える最小の文数も注釈した。600問の36.7％は1文、62.0％は複数文、1.3％は文脈に依存しない。<br>Dialogueでは77.0％が複数文に支えられる。離れた発言、話者の関係、省略された場面をつなぐ必要がある。<br>注釈者間の一致度はCohenのκ＝0.62。|
|41|22|21|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|正答率を、対象と条件に沿って読む|正答率と構築時の性能|
|42|23|22|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|評価の単位は、一問の正しい選択|正しい候補を選んだ割合で評価する|
|43|23|22|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|基本指標は正答率。正しい候補を選べた質問数を、評価した質問数で割る。すべての選択肢数を4個と仮定しない。<br>BERT系は学習率0.00002、バッチ24、最大512トークン、8エポックで微調整した。長い入力は、文書・質問・候補のうち最長の列から切り詰める。<br>候補の表面上の似方にも影響される。本文に似ているだけの誤答候補があると、正解を選びにくくなる。|基本指標は正答率。正しい候補を選べた質問数を、評価した質問数で割る。<br>BERT系は学習率0.00002、バッチ24、最大512トークン、8エポックで微調整した。長い入力は、文書・質問・候補のうち最長の列から切り詰める。<br>候補の表面上の似方にも影響される。本文に似ているだけの誤答候補があると、正解を選びにくくなる。|
|44|23|22|細かな再現設定を外部記録に移し、評価の説明と入力切詰めを保持する。|基本指標は正答率。正しい候補を選べた質問数を、評価した質問数で割る。<br>BERT系は学習率0.00002、バッチ24、最大512トークン、8エポックで微調整した。長い入力は、文書・質問・候補のうち最長の列から切り詰める。<br>候補の表面上の似方にも影響される。本文に似ているだけの誤答候補があると、正解を選びにくくなる。|基本指標は正答率。正しい候補を選べた質問数を、評価した質問数で割る。<br>BERT系モデルを微調整して評価した。長い入力は、文書・質問・候補のうち最長の列から切り詰める。<br>候補の表面上の似方にも影響される。本文に似ているだけの誤答候補があると、正解を選びにくくなる。|
|45|25|24|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|人とモデルは、評価した集合を分けて読む|人は注釈付きテスト部分で、96.0％の正答率|
|46|25|24|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|人の値は全3,892問の実測ではない。モデル全体の値と、人が解いた注釈部分の値は母集団が異なる。|人の値は、知識注釈のあるテスト300問（Mixed・Dialogue各150問）で測ったもの。|
|47|25|24|表の見出しを自然で具体的な日本語にする。|人：注釈されたテスト部分|人：テストの300問|
|48|26|25|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|事前知識を使う読解に、研究上の余地を残す|事前知識の必要な問題に、モデルは苦戦する|
|49|26|25|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|構築時の最良モデルと人の差は、特に事前知識を必要とする問題で大きかった。語句の表面的一致だけでは解きにくい例が多い。<br>誤答候補のもっともらしさ、英語の関連読解データを翻訳して増やす方法なども検討された。学習量と候補の作り方が性能へ影響する。<br>C³は、知識そのものを自由回答で説明する課題ではない。文書と候補を与えた状態で、知識を使い正しい選択をする能力を測る。|構築時の最良モデルと人の差は、特に事前知識を必要とする問題で大きかった。語句の表面的一致だけでは解きにくい例が多い。<br>誤答候補のもっともらしさ、英語の関連読解データを翻訳して増やす方法なども検討された。学習量と候補の作り方が性能へ影響する。<br>C³は、文書と候補を与えた状態で、知識を使って正しい選択をする能力を測る。|
|50|27|26|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|元データと、後続の評価を分ける|入手方法とCLUE・CLEVA|
|51|28|27|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|公開C³、CLUE、CLEVAの役割|C³とCLUEは、テストの正解公開が異なる|
|52|28|27|三系列の表に示した具体的な違いと重複する禁止文を外す。|CLUEの新テストやCLEVAの採用部分を、元C³の全体と同一視しない。||
|53|28|27|表の見出しを自然で具体的な日本語にする。|CLEVA v1|CLEVA|
|54|30|28|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|CLEVAは2023年の中国語言語モデル評価基盤。読解にはC³から採った選択式問題を使い、正答率で評価すると説明する。<br>HELM v0.4.0の実装ではreading_comprehensionのデータと、train/test・prompts.json・infer_params.jsonを読み込む。<br>同梱設定にはprompt_id 0〜5の6通りがある。Classic v0.4.0の公開run索引では、CLEVAを名に含む実行は0件。|CLEVAは2023年に発表された中国語モデルの評価基盤で、読解課題にはC³から採った選択式問題を使い、正答率で評価する。<br>公開実装は、文書・質問・全選択肢をテンプレートで整形し、生成または候補の比較によって解答する。<br>CLEVAで使われた全問題や抽出範囲、詳しい推論条件は公開説明から確認できない。|
|55|31|29|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|利用する版を決め、権利条件を先に読む|公式データと知識注釈をJSONで取得する|
|56|31|29|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|元の公式repoでは、6データファイルと4注釈ファイルを公開している。文書ID、質問、候補、正解文字列を保持して取得できる。<br>license.txtは「非商用の研究目的のみ」と定める。元の試験問題が公開されていることと、利用条件が無制限であることは別である。<br>公開資料は、読解の入力、必要な知識、歴史的な比較を追う入口になる。後続利用では分割・プロンプト・評価条件も合わせて記録する。|公式リポジトリでは、文書・質問・候補・正解を含むJSONと、600問の知識注釈が公開されている。<br>各問のanswerには、choiceに並んだ候補のうち正解の文字列が入る。正答率の評価に加え、知識注釈を使った問題種別の分析にも使える。<br>license.txtに記載された利用条件は「非商用の研究目的のみ」である。|
|57|32|30|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|中国語の試験から集めた19,577問。対話と多様な単一テキストを読み、2〜4候補から唯一の正解を選ぶ。<br>語句照合だけでなく、言い換え・場面・因果・計算などが必要になる。600問の知識注釈が、その性質を具体的に示す。<br>構築時の性能、CLUEのテスト更新、CLEVAの採用部分を分けると、何をどの条件で比較しているのかが明確になる。|中国語の試験から集めた19,577問。対話と多様な単一テキストを読み、2〜4候補から唯一の正解を選ぶ。<br>語句照合だけでなく、言い換え・場面・因果・計算などが必要になる。600問の知識注釈が、その性質を具体的に示す。|
|58|36|34|保留到七点の上限時刻を保ちながら、店員の案内を自然な日本語にする。|男：今から今晩の席を予約できますか？<br>女：はい。お名前は？何名様ですか？<br>男：張と申します。2名です。6時半ごろ着きますので、窓際の席をお願いします。<br>女：承知しました。遅くとも7時までのお取り置きですので、早めにお越しください。<br>質問：男性は何をしていますか？<br>A. 救急外来を受診している<br>B. 領収書を発行している<br>C. 集まりを企画している<br>D. 席を予約している|男：今から今晩の席を予約できますか？<br>女：はい。お名前は？何名様ですか？<br>男：張と申します。2名です。6時半ごろ着きますので、窓際の席をお願いします。<br>女：承知しました。お席を確保できるのは7時までです。早めにお越しください。<br>質問：男性は何をしていますか？<br>A. 救急外来を受診している<br>B. 領収書を発行している<br>C. 集まりを企画している<br>D. 席を予約している|
|59|40|38|特别好を自然な日本語の評価表現にする。|女：昨日の公演を見に行ったそうね。どうだった？<br>男：まあ普通かな。半分見たところで帰ったよ。<br>質問：男性は公演をどう思っていますか？<br>A. よくない<br>B. とてもよい<br>C. 特によい|女：昨日の公演を見に行ったそうね。どうだった？<br>男：まあ普通かな。半分見たところで帰ったよ。<br>質問：男性は公演をどう思っていますか？<br>A. よくない<br>B. とてもよい<br>C. 非常によい|
|60|43|41|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|実例9：訪問と居住を区別する|実例9：毎週訪ねる家には、住んでいない|
|61|49|47|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|各実例で使う手掛かり|実例1〜5：答えを支える手掛かり|
|62|49|47|表の見出しを自然で具体的な日本語にする。|実例 / ID|実例|
|63|49|47|表の見出しを自然で具体的な日本語にする。|1 / 37-153|1|
|64|49|47|表の見出しを自然で具体的な日本語にする。|2 / 11-67|2|
|65|49|47|表の見出しを自然で具体的な日本語にする。|3 / 9-120|3|
|66|49|47|表の見出しを自然で具体的な日本語にする。|4 / 11-30|4|
|67|49|47|表の見出しを自然で具体的な日本語にする。|5 / 11-57|5|
|68|49|47|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|「公式注釈」は公開された知識・支持文数の分類。実例1の説明は本資料による。|表の「知識注釈」は公開注釈に基づく。その他は解答の解説。|
|69|50|48|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|各実例で使う手掛かり|実例6〜9：答えを支える手掛かり|
|70|50|48|表の見出しを自然で具体的な日本語にする。|実例 / ID|実例|
|71|50|48|表の見出しを自然で具体的な日本語にする。|6 / 17-3|6|
|72|50|48|表の見出しを自然で具体的な日本語にする。|7 / 28-8|7|
|73|50|48|表の見出しを自然で具体的な日本語にする。|8 / 37-120|8|
|74|50|48|表の見出しを自然で具体的な日本語にする。|9 / 8-707|9|
|75|50|48|前の表で説明した注記の反復を外す。|「公式注釈」は公開された知識・支持文数の分類。実例1の説明は本資料による。||
|76|51|49|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|各実例で使う手掛かり|実例10〜13：答えを支える手掛かり|
|77|51|49|表の見出しを自然で具体的な日本語にする。|実例 / ID|実例|
|78|51|49|表の見出しを自然で具体的な日本語にする。|10 / 8-160|10|
|79|51|49|表の見出しを自然で具体的な日本語にする。|11 / 9-269|11|
|80|51|49|表の見出しを自然で具体的な日本語にする。|12 / 11-14|12|
|81|51|49|表の見出しを自然で具体的な日本語にする。|13 / 8-255|13|
|82|51|49|前の表で説明した注記の反復を外す。|「公式注釈」は公開された知識・支持文数の分類。実例1の説明は本資料による。||
|83|49|47|表の見出しを自然で具体的な日本語にする。|父親が明言する「ほとんど会話がない」が理由。息子にかかる重圧を、父親自身の重圧と取り違えない。|父親が明言する「ほとんど会話がない」が理由。重圧がかかっているのは息子。|
|84|49|47|表の見出しを自然で具体的な日本語にする。|「预订」と「预订座位」が直接対応する。公式注釈はmatching／1文。|「预订」と「预订座位」が直接対応する。知識注釈は語句照合／1文。|
|85|49|47|原知識注釈と解答理由を具体的な文で伝える。|融資を受けた後に設備を更新する。公式注釈は前提条件／複数文。|融資を受けた後に設備を更新する。知識注釈は前提条件／複数文。|
|86|50|48|原知識注釈と解答理由を具体的な文で伝える。|「马上就到」と「就要到了」が対応する。公式注釈は言語知識／複数文。|「马上就到」と「就要到了」が対応する。知識注釈は言語知識／複数文。|
|87|50|48|原知識注釈と解答理由を具体的な文で伝える。|「一般吧」だけでなく、途中で帰った行動も評価の手掛かり。公式注釈は含みのある感情・語調／複数文。|「一般吧」だけでなく、途中で帰った行動も評価の手掛かり。知識注釈は含みのある感情・語調／複数文。|
|88|50|48|原知識注釈と解答理由を具体的な文で伝える。|撮影、電池、充電器からカメラだと補う。公式注釈は場面の知識／複数文。|撮影、電池、充電器からカメラだと補う。知識注釈は場面の知識／複数文。|
|89|50|48|原知識注釈と解答理由を具体的な文で伝える。|毎週の訪問と居住を区別する。公式注釈は言語知識／1文。|毎週訪ねていても、その家に住んでいるわけではない。知識注釈は言語知識／1文。|
|90|51|49|原知識注釈と解答理由を具体的な文で伝える。|経過した20日と残り10日を足す。公式注釈は算術と言語知識／1文。|経過した20日と残り10日を足す。知識注釈は算術と言語知識／1文。|
|91|51|49|原知識注釈と解答理由を具体的な文で伝える。|反語と理由のつながりを読み、「言っても仕方がない」という判断を選ぶ。公式注釈は言語知識と因果／複数文。|反語と理由のつながりを読み、「言っても仕方がない」という判断を選ぶ。知識注釈は言語知識と因果／複数文。|
|92|51|49|原知識注釈と解答理由を具体的な文で伝える。|人々の英雄視と本人の最後の発言を区別する。公式注釈は因果／複数文。|スケート靴のための救助。知識注釈は因果／複数文。|
|93|51|49|原知識注釈と解答理由を具体的な文で伝える。|スーパーは学校の東側なので、学校はスーパーの西側。公式注釈は一般常識の「その他」／1文。|スーパーは学校の東側なので、学校はスーパーの西側。知識注釈は一般常識の「その他」／1文。|
|94|55|51|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|候補数は、一律4個ではない|2〜4個の候補から、一つを選ぶ|
|95|55|51|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|固定6ファイルから再集計。2候補の真偽判定も、同じ一問一正解の読解形式に含まれる。|2候補の真偽問題も、正解を一つ選ぶ同じ形式で収録される。|
|96|57|52|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|公開元の一問を、ID付きで読み出す|JSONから、実例1の文書と設問を読む|
|97|57|52|固定配列indexの照合とassertを外し、実際の文書・設問・候補・答えを読むコードへ。|import json<br>with open('c3-d-train.json', encoding='utf-8') as f:<br>    rows = json.load(f)<br>document, questions, doc_id = rows[941]<br>question = questions[0]<br>assert doc_id == '37-153'<br>assert question['answer'] in question['choice']<br>print(document, question['question'])<br>print(question['choice'], question['answer'])|import json<br>with open("c3-d-train.json", encoding="utf-8") as f:<br>    rows = json.load(f)<br>document, questions, _ = next(r for r in rows if r[2] == "37-153")<br>question = questions[0]<br>print("\n".join(document))<br>print(question["question"])<br>print(question["choice"])<br>print(question["answer"])|
|98|57|52|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|配列の位置と元IDを併用する。正解文字列と候補の順序を保つ。|実例1の文書、質問、全選択肢、正解の文字列が得られる。|
|99|64|56|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|Kai Sun et al. · nlpdata/c3 · commit 1f41682…|Kai Sun et al. (n.d.). nlpdata/c3。参照2026-10-19。|
|100|64|56|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|CLUEbenchmark · CLUE public distribution|CLUEbenchmark (n.d.). CLUE public distribution。参照2026-10-19。|
|101|65|57|読み手に必要な事実を具体的に述べ、制作・照合用の説明を外す。|中国語モデルの多面的評価基盤。付録B.2にC³由来の選択式読解と父子会話例を示す。|中国語モデルの多面的評価基盤。C³由来の選択式読解と父子会話の実例を示す。|
|102|18|17|表の見出しを自然で具体的な日本語にする。|正解が非抜出し|正解をそのまま抜き出せない割合|
|103|1|1|副題で、文章を読んで正解を選ぶ課題を直接伝える。|free-form multiple-Choice Chinese<br>machine reading Comprehension<br>中国語の対話と文章で、知識を伴う読解を問う|free-form multiple-Choice Chinese<br>machine reading Comprehension<br>中国語の対話や文章を読み、知識で答えを選ぶ|
|104|42|40|推測を自然に訳し、読解の説明の表記を整える。|男：よし、そこに立って、笑って。あれ、急に撮れなくなったぞ？<br>女：さっきは普通に使えていたのに、急に壊れたんじゃないでしょうね？<br>男：ああ、電池切れのはずだ。予備の電池は持ってきた？<br>女：持っていないけど、バッグに充電器がある。どこかで充電しようか。<br>質問：会話から何が分かりますか？<br>A. 電池を買いに行きたい<br>B. 男性は写真を撮るのが嫌い<br>C. カメラの電池が切れた<br>D. 女性はあまりうれしくない|男：よし、そこに立って、笑って。あれ、急に撮れなくなったぞ？<br>女：さっきは普通に使えていたのに、急に壊れたんじゃないでしょうね？<br>男：ああ、たぶん電池切れだ。予備の電池は持ってきた？<br>女：持っていないけど、バッグに充電器がある。どこかで充電しようか。<br>質問：会話から何が分かりますか？<br>A. 電池を買いに行きたい<br>B. 男性は写真を撮るのが嫌い<br>C. カメラの電池が切れた<br>D. 女性はあまりうれしくない|
|105|62|54|推測を自然に訳し、読解の説明の表記を整える。|Kai Sun、Dian Yu、Dong Yu、Claire Cardieによる共同研究。中国語の自由な質問形式の選択式読解を整備し、知識が必要な問題を分類した。<br>英語のRACEとDREAMに対応する、中国語の単一テキスト・対話の両方を含む。既存の中国語データで多かった抜出し型の読解を補う位置付けを持つ。<br>公開データと注釈が分かれているため、全体を使った正答率の評価と、600問を使った知識種別の分析を組み合わせられる。|Kai Sun、Dian Yu、Dong Yu、Claire Cardieによる共同研究。中国語の自由な質問形式の選択式読解を整備し、知識が必要な問題を分類した。<br>英語のRACEとDREAMに対応する、中国語の単一テキスト・対話の両方を含む。既存の中国語データで多かった抜き出し型の読解を補う位置付けを持つ。<br>公開データと注釈が分かれているため、全体を使った正答率の評価と、600問を使った知識種別の分析を組み合わせられる。|
|106|2|2|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³ official repository. commit 1f41682e.  https://github.com/nlpdata/c3|[1] Sun et al. C³ 公式データ・実装。  https://github.com/nlpdata/c3|
|107|5|5|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/<br>[2] Sun et al. (2019). Probing Prior Knowledge Needed in Challenging Chinese Machine Reading Comprehension. arXiv:1904.09679v1.<br>https://arxiv.org/abs/1904.09679v1|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/<br>[2] Sun et al. (2019). Probing Prior Knowledge Needed in Challenging Chinese Machine Reading Comprehension.  https://arxiv.org/abs/1904.09679v1|
|108|6|6|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / train / 37-153 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-train.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|109|7|7|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / train / 37-153 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-train.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|110|8|8|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / train / 37-153 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-train.json<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data<br>[2] Li et al. (2023). CLEVA. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|
|111|9|9|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 11-67 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|112|10|10|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 11-67 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|113|11|11|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 11-67 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|114|12|12|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / test / 9-120 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-test.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|115|13|13|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / test / 9-120 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-test.json<br>[2] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data<br>[2] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|116|16|15|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|117|17|16|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|118|18|17|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|119|19|18|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|120|20|19|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|121|21|20|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|122|23|22|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|123|24|23|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|124|25|24|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|125|26|25|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|126|28|27|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] CLUEbenchmark. C3 public data, CLUE 1.0 / 1.1.  https://storage.googleapis.com/cluebenchmark/tasks/c3_public.zip<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|[1] CLUEbenchmark. C3 公開データ。  https://storage.googleapis.com/cluebenchmark/tasks/c3_public.zip<br>[2] Li et al. (2023). CLEVA. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|
|127|30|28|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/<br>[2] Stanford CRFM. CLEVAReadingComprehensionScenario / Converter. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|[1] Li et al. (2023). CLEVA. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/<br>[2] Stanford CRFM. HELM: CLEVAReadingComprehensionScenario.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|
|128|31|29|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³ official repository. commit 1f41682e.  https://github.com/nlpdata/c3<br>[2] Sun et al. C³ license.txt. Non-commercial research purpose only.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/license.txt|[1] Sun et al. C³ 公式データ・実装。  https://github.com/nlpdata/c3<br>[2] Sun et al. C³ 利用条件。  https://github.com/nlpdata/c3/blob/master/license.txt|
|129|32|30|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|130|36|34|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 11-30 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|131|37|35|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 11-57 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|132|38|36|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 11-57 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|133|39|37|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 17-3 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|134|40|38|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 28-8 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|135|41|39|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 37-120 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|136|42|40|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / dev / 37-120 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|137|43|41|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 8-707 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|138|44|42|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 8-160 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|139|45|43|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 9-269 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|140|46|44|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 11-14 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|141|47|45|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / dev / 11-14 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-dev.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|142|48|46|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-M / test / 8-255 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-m-test.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|143|49|47|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³ knowledge annotations, dev/test.  https://github.com/nlpdata/c3/tree/1f41682ebb684d63afe7c583c8f38e137fc8a826/annotation|[1] Sun et al. C³ 知識注釈。  https://github.com/nlpdata/c3/tree/master/annotation|
|144|50|48|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³ knowledge annotations, dev/test.  https://github.com/nlpdata/c3/tree/1f41682ebb684d63afe7c583c8f38e137fc8a826/annotation|[1] Sun et al. C³ 知識注釈。  https://github.com/nlpdata/c3/tree/master/annotation|
|145|51|49|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³ knowledge annotations, dev/test.  https://github.com/nlpdata/c3/tree/1f41682ebb684d63afe7c583c8f38e137fc8a826/annotation|[1] Sun et al. C³ 知識注釈。  https://github.com/nlpdata/c3/tree/master/annotation|
|146|55|51|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³ official repository. commit 1f41682e.  https://github.com/nlpdata/c3|[1] Sun et al. C³ 公式データ・実装。  https://github.com/nlpdata/c3|
|147|57|52|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun et al. C³-D / train / 37-153 / question 1.  https://github.com/nlpdata/c3/blob/1f41682ebb684d63afe7c583c8f38e137fc8a826/data/c3-d-train.json|[1] Sun et al. C³ データセット。  https://github.com/nlpdata/c3/tree/master/data|
|148|62|54|通常の出典へ整え、細かなID・commitは外部記録へ移す。|[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|[1] Sun et al. (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL.  https://aclanthology.org/2020.tacl-1.10/|
|149|14||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|一つの文書に、複数の質問が付く<br>1. 文書から、正しい選択肢を選ぶ<br><br>文書<br>対話 または 単一テキスト<br>→<br><br>質問ごとの候補<br>2〜4個から一つを選ぶ<br>→<br><br>正解<br>候補の文字列を保持<br>同じ文書に最大6問が付く。文書数と質問数は異なる。各実例は文書全文と選んだ一問の全内容を示し、同じ文書の別の質問は含めない。<br>[1] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|150|29||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|CLUEのテスト更新は、別の問題集合<br>CLUE配布ZIPの学習・開発4ファイルは、元C³の同じ4ファイルとバイト単位で一致する。<br>test1.0は2,672文書・3,892問。文書・質問・候補を照合すると、元C³のテスト全問と一致する。正解欄は除かれ、提出用IDが付く。<br>test1.1は1,080文書・1,625問。元C³全6ファイルとの同一問題は学習2問・テスト1問で、残り1,622問は一致しない。<br>4. CLUE・CLEVAでの利用<br>[1] CLUEbenchmark. C3 public data, CLUE 1.0 / 1.1.  https://storage.googleapis.com/cluebenchmark/tasks/c3_public.zip|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|151|53||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|13実例の公開位置を固定する<br>Appendix: 2. 版・原位置・再現<br>実例 / 文書ID ／ ファイル ／ 配列index / 質問index<br>1 / 37-153 ／ c3-d-train.json ／ 941 / 0<br>2 / 11-67 ／ c3-m-dev.json ／ 0 / 0<br>3 / 9-120 ／ c3-m-test.json ／ 12 / 0<br>4 / 11-30 ／ c3-d-dev.json ／ 2 / 0<br>5 / 11-57 ／ c3-d-dev.json ／ 1 / 0<br>6 / 17-3 ／ c3-d-dev.json ／ 3 / 0<br>7 / 28-8 ／ c3-d-dev.json ／ 6 / 0<br>indexは0起算。固定commit 1f41682…、各ファイルSHA256と原レコードを付属記録へ保存。<br>[1] Sun et al. C³ official repository. commit 1f41682e.  https://github.com/nlpdata/c3|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|152|54||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|13実例の公開位置を固定する<br>Appendix: 2. 版・原位置・再現<br>実例 / 文書ID ／ ファイル ／ 配列index / 質問index<br>8 / 37-120 ／ c3-d-dev.json ／ 11 / 0<br>9 / 8-707 ／ c3-m-dev.json ／ 1 / 0<br>10 / 8-160 ／ c3-m-dev.json ／ 4 / 0<br>11 / 9-269 ／ c3-m-dev.json ／ 8 / 0<br>12 / 11-14 ／ c3-m-dev.json ／ 39 / 0<br>13 / 8-255 ／ c3-m-test.json ／ 38 / 0<br>indexは0起算。固定commit 1f41682…、各ファイルSHA256と原レコードを付属記録へ保存。<br>[1] Sun et al. C³ official repository. commit 1f41682e.  https://github.com/nlpdata/c3|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|153|56||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|600問の注釈を、全19,577問へ拡張しない<br>公開注釈はDialogueとMixedそれぞれの開発・テストに150問ずつ、計600問。documentIDとquestionIndexで元質問に結び付く。<br>mは語句の照合、lは言語知識、sは専門知識。c-で始まる8種は一般常識。複数の知識は／で併記される。<br>／／の後の0は1文、1は複数文、2は文脈に依存しない問題を表す。これは正解の候補番号ではない。<br>Appendix: 2. 版・原位置・再現<br>[1] Sun et al. C³ knowledge annotations, dev/test.  https://github.com/nlpdata/c3/tree/1f41682ebb684d63afe7c583c8f38e137fc8a826/annotation|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|154|58||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|CLEVAの設定と、実際の公開実行は別<br>Converterは候補をReferenceへ変換し、labelに含まれる候補indexへCORRECTタグを付ける。テンプレートで文書・質問・候補を整形する。<br>promptのmeta.mul_as_genに応じ、生成、選択肢の一括提示、候補ごとの比較を切り替える。具体的な推論値はinfer_params.jsonから読む。<br>この調査ではCLEVA v1の変換済み読解データ全体と推論パラメータを取得できていない。元C³の分割や全問数を、そのまま実行条件に置き換えない。<br>Appendix: 2. 版・原位置・再現<br>[1] Stanford CRFM. CLEVAReadingComprehensionScenario / Converter. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py<br>[2] Stanford CRFM. CLEVA v1 run configuration. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|155|59||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|公開run索引0件の確認範囲<br>Classic v0.4.0のrun_specs公開リスト8,526件と、runs_to_run_suitesのキーを対象に、clevaを名に含む項目を照合した。該当は0件だった。<br>一方、同リリースにはCLEVA v1の実行設定が含まれ、reading_comprehensionのprompt_id 0〜5を指定している。<br>設定が存在することは、公開済みのモデル出力や集計結果があることを意味しない。CLEVA全体の論文結果と、ここで確認した公開runを区別する。<br>Appendix: 2. 版・原位置・再現<br>[1] Stanford CRFM. HELM Classic release v0.4.0, public run index.  https://crfm.stanford.edu/helm/classic/v0.4.0/<br>[2] Stanford CRFM. CLEVA v1 run configuration. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|156|60||細かな原位置・照合・設定一覧・重複する年表や注釈説明を外部記録へ移す。利用に必要な形式・版差・条件は本文に保持。|初回公開と、正式刊行を分けて記録<br>arXivの初回投稿は2019年4月21日。初期版の題名はProbing Prior Knowledge Needed in Challenging Chinese Machine Reading Comprehension。<br>正式刊行名はInvestigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension。TACL第8巻、141〜155頁、2020年に掲載された。<br>C³の公開年は2019年として扱い、正式論文は2020年、CLEVAによる後続利用は2023年として区別する。<br>Appendix: 2. 版・原位置・再現<br>[1] Sun et al. (2019). Probing Prior Knowledge Needed in Challenging Chinese Machine Reading Comprehension. arXiv:1904.09679v1.<br>https://arxiv.org/abs/1904.09679v1<br>[2] Sun, Yu, Yu & Cardie (2020). Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension. TACL 8:141–155.<br>https://aclanthology.org/2020.tacl-1.10/|詳細はbaseline-pages.json、provenance-notes.mdへ保存。|
|157|1|1|実黒字形がnative枠下端を1.603/2.264pt超える共通マスター枠。|{'height_pt': 105.45, 'margin_bottom_pt': 0.0}|{'height_pt': 113.45, 'margin_bottom_pt': 8.0}|
|158|33|31|実黒字形がnative枠下端を1.603/2.264pt超える共通マスター枠。|{'height_pt': 46.08, 'margin_bottom_pt': 0.0}|{'height_pt': 54.08, 'margin_bottom_pt': 8.0}|

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
