# CCPM：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|5|5|読者に必要な説明へ整理|CCPMは、中国古典詩の意味理解を調べる四択データセット。現代中国語で書かれた説明を読み、意味が最も対応する古典詩句を選ぶ。古典詩句と現代語訳の対を、正解の根拠として使う。<br>候補には、正解に似た語や表現を持つ別の詩句を含める。詩を新しく書く課題ではなく、与えられた候補の意味の違いを識別する。|CCPMは、中国古典詩の意味理解を調べる四択データセット。現代中国語の説明を読み、意味が最も対応する古典詩句を選ぶ。古典詩句と現代語訳の対が、正解の根拠になる。<br>候補には、正解に似た語や表現を持つ別の詩句も含まれる。似た言葉の中から、意味の違いを読み取ることが求められる。|
|2|11|11|単純な順序を読める文章にする|四つの箱と矢印による直列の手順|約6,000段落の古典文と現代語訳をWebから収集する。<br>句読点やWeb上の行境界で分割し、五言・七言の詩型に合う27,218の対訳を残す。二行の対も含む。<br>正解に似た別の詩句を三つ選び、正解と混ぜて四択問題にする。|
|3|12|12|読者に必要な説明へ整理|収集した古典文には、詩以外の文学も含まれていた。そこで、よく使われる五言・七言の詩型に合う長さの詩句を残した。<br>二行で連続した意味を持つ対は、そのまま二行単位で扱う。ここでいう27,218件は問題数であり、詩の作品数や作者数ではない。|収集した古典文には、詩以外の文学も含まれていた。そこで、よく使われる五言・七言の詩型に合う長さの詩句を残した。<br>二行で連続した意味を持つ対は、そのまま二行単位で扱う。|
|4|15|15|読者に必要な説明へ整理|件数は配布ファイルの全行と一致。論文のテスト正解率と、公開テストの正解なし配布を区別する。|学習・検証には正解が付く。公開テストの正解は非公開。|
|5|16|16|読者に必要な説明へ整理|全27,218問。形式別の件数は構築時の集計。配布文字列には特殊な表記を含む少数の例もある。|全27,218問。形式別の件数は、データ構築時の集計。|
|6|17|17|読者に必要な説明へ整理|answerは0始まりの位置。表示上のA/B/C/Dは、元の候補順へ対応させる。元JSONLには問題ID・詩題・作者の欄はない。|translationが問題文、choicesが四候補。answer=0は先頭の候補Aを指す。|
|7|20|19|読者に必要な説明へ整理|指標はAccuracy（正解率）。各問題で予測した選択肢が元のanswerと一致したかを数え、評価した問題数で割る。四つの候補から一つを選ぶため、各問の正誤は0か1になる。<br>2021年の実験は、学習分割でBERTを微調整し、テスト分割で評価した。公開テストの正解は非公開で、比較表には2021年の報告値を示す。|選んだ候補が正解と一致した問題の割合を、Accuracy（正解率）で評価する。<br>2021年の実験では、学習21,778問でBERTを微調整し、テスト2,720問で評価した。|
|8|21|20|読者に必要な説明へ整理|CCPMの同じテスト2,720問を対象とする、構築時の報告値。BERTの基盤はbert-base-chinese。|2021年の報告値。同じテスト2,720問で評価。両方式の基盤はbert-base-chinese。|
|9|25|23|読者に必要な説明へ整理|2023年のCLEVAは、中国語モデルを多様な課題で評価するプラットフォーム。古典中国語理解の課題としてCCPMから四択問題を抽出し、現代語と古典候補の意味の対応を正解率で評価する。<br>掲載例は実例2の「山間の雨が晴れ始める」問題で、公式trainの18,823行と四候補・正解Dが一致する。同じ説明文に別候補が付く問題もある。|2023年のCLEVAは、中国語モデルを多様な課題で評価するプラットフォーム。CCPMの四択問題を、古典中国語理解の評価に用いる。<br>現代語の説明と四候補を提示し、選んだ候補の正誤を正解率で評価する。実例2の雨の問題は、CLEVA論文にも掲載されている。<br>HELMにも同課題の評価実装が公開されている。CLEVAで評価した問題の総数は、公開説明には記されていない。|
|10|28|24|読者に必要な説明へ整理|公式JSONLを取得でき、再利用条件は確認が必要|公式GitHubで問題と技術報告を公開する|
|11|28|24|読者に必要な説明へ整理|公式GitHubはtrain.jsonl、valid.jsonl、test_public.jsonlと技術報告を公開し、利用時にはCCPMの引用を求める。2021年8月21日の更新版には、これらを含む五つのファイルがある。<br>取得したリポジトリにはライセンスファイルがなく、元Web素材の個別出所・作者も各レコードには含まれない。古典詩の原句、現代語説明、収集データの利用条件を同じものとして推定せず、配布元を確認して利用する。|公式GitHubは、学習・検証・公開テストのJSONLと技術報告を公開している。利用時にはCCPMの論文を引用する。<br>リポジトリにはライセンスが明示されていない。再利用・再配布の条件は、配布元へ確認する。|
|12|29|25|読者に必要な説明へ整理|CCPMは現代中国語の説明と古典詩句の対応を問う27,218問の四択データ。正解との対訳に、似た詩句を検索した三つの負例を組み合わせる。<br>2021年のBERT二方式はテスト正解率84.96%と82.60%。後にCLEVAの古典中国語理解へ採用された。公開元データ・掲載例・未取得の後利用集合を対応させて読む。|CCPMは、現代中国語の説明と古典詩句の対応を問う27,218問の四択データ。正解との対訳に、似た詩句を検索した三つの負例を組み合わせる。<br>2021年のBERT二方式は、テストで84.96%と82.60%の正解率を示した。後にCLEVAの古典中国語理解にも採用され、中国語モデルの意味理解を調べる課題となった。|
|13|31|27|読者に必要な説明へ整理|追加10問の原文と日本語訳<br>分割・重複・入力形式の補足<br>参考文献|追加10問の原文と日本語訳<br>入力形式と詩句の読み方<br>参考文献|
|14|42|38|読者に必要な説明へ整理|分割・重複・入力形式の補足|入力形式と詩句の読み方|
|15|42|38|読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|16|43|39|読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|17|44||読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|18|45|40|読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|19|46||読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|20|47|41|読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|21|48|42|読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|22|49|43|読者に必要な説明へ整理|Appendix: 2. 分割・重複・入力形式の補足|Appendix: 2. 入力形式と詩句の読み方|
|23|43|39|読者に必要な説明へ整理|同じ雨の説明でも、候補と正解位置が変わる|同じ説明に、異なる候補の組が付く|
|24|43|39|番号・検査用表現を自然な説明へ整理|train 18,823行|候補の組1|
|25|43|39|番号・検査用表現を自然な説明へ整理|train 21,287行|候補の組2|
|26|43|39|番号・検査用表現を自然な説明へ整理|D（answer=3）|D|
|27|43|39|番号・検査用表現を自然な説明へ整理|A（answer=0）|A|
|28|43|39|読者に必要な説明へ整理|両方の説明は「山间连绵阴雨刚刚有了一点停止的意思。」。CLEVA掲載例は18,823行。|共通の説明：「山间连绵阴雨刚刚有了一点停止的意思。」<br>候補の組1が、実例2とCLEVA論文に掲載された問題。|
|29|45|40|番号・検査用表現を自然な説明へ整理|answer / 表示|正解の候補|
|30|45|40|番号・検査用表現を自然な説明へ整理|0 / A|A|
|31|45|40|番号・検査用表現を自然な説明へ整理|1 / B|B|
|32|45|40|番号・検査用表現を自然な説明へ整理|2 / C|C|
|33|45|40|番号・検査用表現を自然な説明へ整理|3 / D|D|
|34|45|40|独立レビュー：見出しと表から分かる正解位置の均等さの重複注を除く|公開テストにはanswerがない。候補順を維持し、0始まりの番号をA〜Dへ対応させた。||
|35|47|41|読者に必要な説明へ整理|配布文字列には、空の説明や特殊な表記もある|一部の問題には、説明の欠落や形式の例外がある|
|36|47|41|読者に必要な説明へ整理|公開テスト2,026行のtranslationは空文字列で、四候補は残っている。正解が非公開のため、意図した説明や答えは補っていない。<br>学習6,518行には「公曰：勿杀」という五言・七言に収まらない正解文字列がある。別の行には拡張漢字や文字コードを表すような文字列もあり、配布物を一律に標準漢字だけへ直していない。|公開テストには、説明が空の問題が1問ある。四候補は残っているが、説明との意味対応を評価するための入力が欠けている。<br>五言・七言の詩型に当てはまらない文や、特殊な漢字表記を含む問題もある。<br>学習と公開テストで、説明と四候補が一致する問題が1問ある。|
|37|48|42|読者に必要な説明へ整理|一つのJSONL行から四候補と参照位置を読む|JSONLから問題文・候補・正解を読み出す|
|38|48|42|読者に必要な説明へ整理|record = json.loads(line)<br>modern = record["translation"]<br>choices = record["choices"]<br># train / valid<br>answer_index = record["answer"]  # 0, 1, 2, 3<br>answer_text = choices[answer_index]|import json<br>with open("train.jsonl", encoding="utf-8") as f:<br>    question = json.loads(next(f))<br>print(question["translation"])<br>for i, verse in enumerate(question["choices"]):<br>    print(f"{chr(65+i)}. {verse}")<br>print("正解:", chr(65 + question["answer"]))|
|39|48|42|読者に必要な説明へ整理|CCPM配布の読み方。CLEVAの実際のpromptは、別途配布されるテンプレートで組み立てる。|train.jsonlは1行に1問のJSONを収める。最初の問題の説明、四候補、正解記号を表示する。|
|40|35|31|独立レビュー：不自然な主述関係を原詩の景色と音の描写に沿って自然化|現代語：大雨が水煙を巻き上げ、辺りはかすみ、天地はもの寂しい景色になった。<br>A. 村の煙が途切れる所を渡り、野の景色が眺めの中で開ける。<br>B. 立ちこめる煙が雨の景色をかすませ、もの寂しさが視界に迫る。<br>C. 幾重もの山は煙る雨の向こう。眺めようとしても青々とした姿を見失う。<br>D. かすみが遠くの眺めを覆い、もの寂しい様子が寒々しい音を送る。|現代語：大雨が水煙を巻き上げ、辺りはかすみ、天地はもの寂しい景色になった。<br>A. 村の煙が途切れる所を渡り、野の景色が眺めの中で開ける。<br>B. 立ちこめる煙が雨の景色をかすませ、もの寂しさが視界に迫る。<br>C. 幾重もの山は煙る雨の向こう。眺めようとしても青々とした姿を見失う。<br>D. かすみが遠くの眺めを覆い、寒々しい物音がもの寂しく響く。|
|41|40|36|独立レビュー：寒蝉を日本語で伝わる季節の蝉として訳す|現代語：初秋の寒蝉が、野の朝風の中で、声をからして鳴いている。<br>A. 猿が、秋の野風の中で叫ぶ。<br>B. 蝉が、風の前でせわしなく鳴く。<br>C. 蝉が、秋の野風の中で鳴く。<br>D. 蛍が、秋の野風の中で散る。|現代語：初秋の蝉が、野の朝風の中で、声をからして鳴いている。<br>A. 猿が、秋の野風の中で叫ぶ。<br>B. 蝉が、風の前でせわしなく鳴く。<br>C. 蝉が、秋の野風の中で鳴く。<br>D. 蛍が、秋の野風の中で散る。|
|42|2|2|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|43|6|6|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 train.jsonl:14行 / answer=0<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|44|7|7|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 train.jsonl:18823行 / answer=3<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|45|8|8|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 train.jsonl:14876行 / answer=1<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|46|15|15|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] Li, Qi, Sun, Yi & Zhang (2021). CCPM: A Chinese Classical Poetry Matching Dataset. arXiv:2106.01979v1.  https://arxiv.org/abs/2106.01979<br>[2] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] Li, Qi, Sun, Yi & Zhang (2021). CCPM: A Chinese Classical Poetry Matching Dataset. arXiv:2106.01979v1.  https://arxiv.org/abs/2106.01979<br>[2] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|47|17|17|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|48|18||出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|49|28|24|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|50|32|28|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:1行 / answer=3<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|51|33|29|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:5行 / answer=2<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|52|34|30|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:14行 / answer=1<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|53|35|31|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:24行 / answer=1<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|54|36|32|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:25行 / answer=0<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|55|37|33|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:35行 / answer=0<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|56|38|34|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:47行 / answer=1<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|57|39|35|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:52行 / answer=3<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|58|40|36|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:60行 / answer=2<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|59|41|37|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。 valid.jsonl:65行 / answer=3<br>https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|60|43|39|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|61|45|40|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|62|46||出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|63|47|41|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|64|48|42|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|65|49|43|出典行からコミット・行番号・正解番号などの監査情報を除く|[1] THUNLP-AIPoet. CCPM. 公式配布、commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5、2026-10-18参照。  https://github.com/THUNLP-AIPoet/CCPM|[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM|
|66|51|45|読者に必要な説明へ整理|CCPM — Official Dataset Repository<br>THUNLP-AIPoet · 2021 · commit e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5<br>学習・検証・正解非公開テストのJSONLと技術報告、データ形式、正解率による評価方法を公開する。<br>https://github.com/THUNLP-AIPoet/CCPM|CCPM — Official Dataset Repository<br>THUNLP-AIPoet · 2021<br>学習・検証・正解非公開テストのJSONLと技術報告、データ形式、正解率による評価方法を公開する。<br>https://github.com/THUNLP-AIPoet/CCPM|
|67|51|45|独立レビュー：文献URL全文がnative文字枠内に収まる高さへ。位置・本文・URL・書式は保持|height 105.970 pt|height 123.970 pt|
|68|51|45|独立レビュー：文献URL全文がnative文字枠内に収まる高さへ。位置・本文・URL・書式は保持|height 105.970 pt|height 123.970 pt|
|69|52|46|独立レビュー：文献URL全文がnative文字枠内に収まる高さへ。位置・本文・URL・書式は保持|height 105.970 pt|height 123.970 pt|
|70|52|46|独立レビュー：文献URL全文がnative文字枠内に収まる高さへ。位置・本文・URL・書式は保持|height 105.970 pt|height 123.970 pt|
|71|53|47|独立レビュー：文献URL全文がnative文字枠内に収まる高さへ。位置・本文・URL・書式は保持|height 105.970 pt|height 123.970 pt|
|72|3|3|メインレビュー：不自然な後利用を利用へ自然化|現代語の説明から古典詩句を選ぶ<br>対訳と似た詩句から問題を作る<br>正解率で意味の対応を評価する<br>CLEVAでの後利用と公開配布|現代語の説明から古典詩句を選ぶ<br>対訳と似た詩句から問題を作る<br>正解率で意味の対応を評価する<br>CLEVAでの利用と公開配布|
|73|24|22|メインレビュー：不自然な後利用を利用へ自然化|CLEVAでの後利用と公開配布|CLEVAでの利用と公開配布|
|74|24|22|メインレビュー：不自然な後利用を利用へ自然化|4. CLEVAでの後利用と公開配布|4. CLEVAでの利用と公開配布|
|75|25|23|メインレビュー：不自然な後利用を利用へ自然化|4. CLEVAでの後利用と公開配布|4. CLEVAでの利用と公開配布|
|76|26||メインレビュー：不自然な後利用を利用へ自然化|4. CLEVAでの後利用と公開配布|4. CLEVAでの利用と公開配布|
|77|27||メインレビュー：不自然な後利用を利用へ自然化|4. CLEVAでの後利用と公開配布|4. CLEVAでの利用と公開配布|
|78|28|24|メインレビュー：不自然な後利用を利用へ自然化|4. CLEVAでの後利用と公開配布|4. CLEVAでの利用と公開配布|
|79|29|25|メインレビュー：不自然な後利用を利用へ自然化|4. CLEVAでの後利用と公開配布|4. CLEVAでの利用と公開配布|
|80|18||問題・説明の文字列一意数の監査|説明文だけでは、問題を一意に特定できない<br>2. 対訳と似た詩句から問題を作る<br>2026-10-18、配布全件の文字列を加工せず集計。学習と公開テストには、説明と四候補が同じ問題が1件ある。<br>[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM||
|81|23||細かな最適化設定は外部記録へ移し、基盤モデル・学習回数は結果頁に保持|両方式を同じ学習設定で微調整した<br>3. 正解率で意味の対応を評価する<br>BERT-CCPoemは負例の検索に使うモデルで、ここで評価した二方式の基盤とは区別する。<br>[1] Li, Qi, Sun, Yi & Zhang (2021). CCPM: A Chinese Classical Poetry Matching Dataset. arXiv:2106.01979v1.  https://arxiv.org/abs/2106.01979||
|82|26||公開実行件数と未取得の制作状況|HELMにも課題の実装があり、公開実行は0件<br>HELM v0.4.0にはCLEVAClassicalChineseUnderstandingScenarioがあり、実例1と同じ説明・候補・正解Aを記す。データとテンプレートを外部ZIPから読み、候補の番号を正解参照へ変換する。<br>Classic v0.4.0の公開run_specs全8,526件にはCLEVA実行がない。CLEVA用評価ZIPも取得できていないため、HELMでの得点、実際の学習例数や生成条件は示さない。<br>4. CLEVAでの利用と公開配布<br>[1] Stanford CRFM. CLEVAClassicalChineseUnderstandingScenario / Converter. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py||
|83|27||確認範囲の監査表|元のCCPM配布と、後利用の集合を区別する<br>4. CLEVAでの利用と公開配布<br>[1] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP 2023: System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/<br>[2] Stanford CRFM. CLEVAClassicalChineseUnderstandingScenario / Converter. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py||
|84|44||詩型ごとの分割別詳細は外部記録へ移し、全体分布は本編に保持|形式別件数の内訳<br>Appendix: 2. 入力形式と詩句の読み方<br>[1] Li, Qi, Sun, Yi & Zhang (2021). CCPM: A Chinese Classical Poetry Matching Dataset. arXiv:2106.01979v1.  https://arxiv.org/abs/2106.01979||
|85|46||分割間の文字列共通要素の監査。完全一致1問の制約は残す|分割間の一致は、比較する単位で異なる<br>Appendix: 2. 入力形式と詩句の読み方<br>全行の説明文と四候補を、表記を変えずに比較した共通要素数。説明＋候補の一致1件はtrain14,734行とtest_public1,020行。<br>[1] THUNLP-AIPoet (2021). CCPM.  https://github.com/THUNLP-AIPoet/CCPM||
|86|54||評価設定ファイルだけの参考文献|参考文献<br>Appendix: 3. 参考文献<br>run_specs_cleva_v1.conf<br>Stanford CRFM · HELM v0.4.0 · CLEVA設定<br>古典中国語理解を含む課題とprompt IDを設定し、同課題には0〜5の六つのIDを登録する。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)
