# LexGLUE：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|3|3|元の7課題と元研究の評価・実利用を中心へ構成する|法律の文章で何を当てるか<br>七つのデータと作り方<br>採点方法と到達水準<br>HELMでの位置付けと入手方法|法律の文章で何を当てるか<br>七つのデータと作り方<br>採点方法と2022年の成績<br>公開配布と利用方法|
|2|18|18|読者に必要な説明へ整理|採点方法と到達水準|採点方法と2022年の成績|
|3|18|18|読者に必要な説明へ整理|3. 採点方法と到達水準|3. 採点方法と2022年の成績|
|4|19|19|読者に必要な説明へ整理|3. 採点方法と到達水準|3. 採点方法と2022年の成績|
|5|20|20|読者に必要な説明へ整理|3. 採点方法と到達水準|3. 採点方法と2022年の成績|
|6|21|21|読者に必要な説明へ整理|3. 採点方法と到達水準|3. 採点方法と2022年の成績|
|7|22|22|読者に必要な説明へ整理|3. 採点方法と到達水準|3. 採点方法と2022年の成績|
|8|23|23|読者に必要な説明へ整理|HELMでの位置付けと入手方法|公開配布と利用方法|
|9|23|23|読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|10|24||読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|11|25||読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|12|26||読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|13|27|24|読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|14|28|25|読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|15|29|26|読者に必要な説明へ整理|4. HELMでの位置付けと入手方法|4. 公開配布と利用方法|
|16|31|28|読者に必要な説明へ整理|追加の公開実例<br>配布・実装の詳しい条件<br>制作研究と参考文献|追加の公開実例<br>条約ラベルの対応<br>制作研究と参考文献|
|17|31|28|読者に必要な説明へ整理|追加の公開実例<br>条約ラベルの対応<br>制作研究と参考文献|追加の公開実例<br>条約ラベルの対応<br>研究と参考文献|
|18|46|43|読者に必要な説明へ整理|配布・実装の詳しい条件|条約ラベルの対応|
|19|46|43|読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|20|47|44|読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|21|48||読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|22|49||読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|23|50||読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|24|51||読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|25|52||読者に必要な説明へ整理|Appendix: 2. 配布・実装の詳しい条件|Appendix: 2. 条約ラベルの対応|
|26|53|45|読者に必要な説明へ整理|制作研究と参考文献|研究と参考文献|
|27|53|45|読者に必要な説明へ整理|Appendix: 3. 制作研究と参考文献|Appendix: 3. 研究と参考文献|
|28|54|46|読者に必要な説明へ整理|Appendix: 3. 制作研究と参考文献|Appendix: 3. 研究と参考文献|
|29|55|47|読者に必要な説明へ整理|Appendix: 3. 制作研究と参考文献|Appendix: 3. 研究と参考文献|
|30|56|48|読者に必要な説明へ整理|Appendix: 3. 制作研究と参考文献|Appendix: 3. 研究と参考文献|
|31|57|49|読者に必要な説明へ整理|Appendix: 3. 制作研究と参考文献|Appendix: 3. 研究と参考文献|
|32|5|5|作成主体・初公開と正式発表の年を直接説明する|LexGLUEは、英語の法律文書を使う7つのデータセットを、共通の評価枠組みにまとめたベンチマーク。2022年のACLで発表された。<br>欧州人権裁判所の事件、米国最高裁の判決、EU法令、契約条項、利用規約、判例の引用を扱う。<br>入力に応じて、条項や争点のラベルを付けたり、引用に入る判旨を5候補から選んだりする。|LexGLUEは、英語の法律文書を使う7つのデータセットを、共通の評価枠組みにまとめたベンチマーク。Ilias Chalkidisらが2021年に公開し、2022年のACLで発表した。<br>欧州人権裁判所の事件、米国最高裁の判決、EU法令、契約条項、利用規約、判例の引用を扱う。<br>入力に応じて、条項や争点のラベルを付けたり、引用に入る判旨を5候補から選んだりする。|
|33|9|9|参照を自然なラベル説明へ戻し、繰り返す一般的な免責を除く|UNFAIR-ToSは、欧州の消費者法の観点で問題になりうる条項を、8種類で注釈したデータ。1文に複数の種類が付くこともある。<br>実例2の参照は一方的変更。どの種類にも当たらない文には、空のラベル集合が付く。<br>これはデータセットの注釈を予測する課題であり、個別契約の法的効力を確定する判断とは区別される。|UNFAIR-ToSは、欧州の消費者法の観点で問題になりうる条項を、8種類で注釈したデータ。1文に複数の種類が付くこともある。<br>実例2には「一方的変更」のラベルが付く。どの種類にも当たらない文には、空のラベル集合が付く。|
|34|12|12|作業上の区別指示を、二つの課題の具体的な違いと公開形式へ整理する|ECtHR Aは、事実の段落列から、裁判所が違反を認定した条項を予測する。ECtHR Bは、違反が主張され、裁判所が検討した条項を予測する。<br>どちらも欧州人権条約の10条項に絞った複数ラベル分類。第6条などの条項名と、配布中の0始まりの整数は対応表で区別する。<br>Task Bのラベルが付いていても、Task Aで違反が認定されるとは限らない。|ECtHR Aは、事実の段落列から、裁判所が違反を認定した条項を予測する。ECtHR Bは、違反が主張され、裁判所が検討した条項を予測する。<br>どちらも欧州人権条約の10条項を対象とする複数ラベル分類である。条番号と、配布データ中の整数ラベルとの対応は補足に示す。|
|35|15|15|読者に必要な説明へ整理|既存データを、比較しやすい形へ整える|法律データを七つの課題に整える|
|36|15|15|正式論文§3.2に基づき、SCOTUSの新規構築主体と元の判決文/SCDBを明確にする|公開され、論文で説明された法律データを選び、分割、入力とラベル、評価方法へのアクセスをそろえた。<br>EUR-LEXは7,000以上のEuroVoc概念から第2階層の頻出100概念に整理。LEDGARは頻出100テーマを対象に、単一の主題を持つ条項へ絞った。<br>法律の専門性を必要とする課題も対象にし、文書が長い課題も残した。|既存の法律データを整理し、SCOTUSは判決文とSCDBの争点情報を組み合わせて新たに構築した。分割、入力とラベル、評価方法へのアクセスをそろえた。<br>EUR-LEXは7,000以上のEuroVoc概念から第2階層の頻出100概念に整理。LEDGARは頻出100テーマを対象に、単一の主題を持つ条項へ絞った。<br>法律の専門性を必要とする課題も対象にし、文書が長い課題も残した。|
|37|15|15|一般的な特徴の反復を、残る主要課題の作り方と時間分割の例外へ置き換える|既存の法律データを整理し、SCOTUSは判決文とSCDBの争点情報を組み合わせて新たに構築した。分割、入力とラベル、評価方法へのアクセスをそろえた。<br>EUR-LEXは7,000以上のEuroVoc概念から第2階層の頻出100概念に整理。LEDGARは頻出100テーマを対象に、単一の主題を持つ条項へ絞った。<br>法律の専門性を必要とする課題も対象にし、文書が長い課題も残した。|既存の法律データを整理し、SCOTUSは判決文とSCDBの争点情報を組み合わせて新たに構築した。分割、入力とラベル、評価方法へのアクセスをそろえた。<br>EUR-LEXは7,000以上のEuroVoc概念から第2階層の頻出100概念に整理。LEDGARは頻出100テーマを対象に、単一の主題を持つ条項へ絞った。<br>CaseHOLDでは、米国判例の引用にある判旨を隠して5択を作る。年代情報がないため、ほかの課題のような時系列の分け直しは行わない。|
|38|16|16|元評価と配布の範囲に関わる差を1箇所へ集約する|固定配布の件数。CaseHOLD testは論文3,900、現配布3,600。|配布の件数。CaseHOLD testは2022年の論文が3,900問、配布が3,600問。SCOTUSも、論文は14分野、配布のラベル名は13種類である。|
|39|16|16|論文の件数と現配布をそれぞれ直接出典へ対応付ける|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. (2022). LexGLUE. https://aclanthology.org/2022.acl-long.297/<br>[2] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|40|17|17|禁止・注意の形から、時間分割の役割を肯定的に説明する|ECtHRは2001〜2016年を学習、2016〜2017年を開発、2017〜2019年をtestとする。<br>SCOTUSは1946〜1982年、1982〜1991年、1991〜2016年の順に分ける。EUR-LEX、LEDGAR、UNFAIR-ToSも時系列の分割を使う。<br>後の時期の文書を予測する条件を保つため、学習とtestを混ぜず、公開された分割で比較する。|ECtHRは2001〜2016年を学習、2016〜2017年を開発、2017〜2019年をtestとする。<br>SCOTUSは1946〜1982年、1982〜1991年、1991〜2016年の順に分ける。EUR-LEX、LEDGAR、UNFAIR-ToSも時系列の分割を使う。<br>後の時期の文書を、以前の文書で学習したモデルが予測する条件で評価できる。|
|41|19|19|F1を初出で短く定義してから、二つの集計方法と課題をつなぐ|micro-F1は、全クラスの正解・誤りをまとめて計算する。出現が多いラベルの影響を受けやすい。<br>macro-F1は、クラスごとに計算したF1の平均。出現の少ないクラスも、多いクラスと同じ重みで数える。<br>単一ラベル分類やCaseHOLDの5択では、全クラスを含めたmicro-F1は正解率と一致する。|F1は、予測ラベルの正しさを表す適合率と、正解ラベルをどれだけ拾えたかを表す再現率を合わせた指標。micro-F1は、全ラベルの正解・誤りをまとめて計算する。<br>macro-F1は、クラスごとに計算したF1の平均。出現の少ないクラスも、多いクラスと同じ重みで数える。<br>単一ラベル分類やCaseHOLDの5択では、全クラスを含めたmicro-F1は正解率と一致する。|
|42|20|20|採点に必要な空集合の扱いと偏りを残し、内部処理の対比を省く|ECtHRとUNFAIR-ToSでは、どのラベルも付かない文書や文がある。すべて0の予測と参照は、通常のラベルだけのF1には正例として数えられない。<br>そこで評価時には「どの種類にも当たらない」という追加ラベルを設け、空集合を正しく予測した場合も数える。学習時の出力クラスを増やす処理とは区別する。<br>固定配布のtestでは、UNFAIR-ToSの空集合は1,607文中1,435文、89.30%。|ECtHRとUNFAIR-ToSでは、どのラベルも付かない文書や文がある。通常のラベルだけでF1を計算すると、空集合を正しく予測しても正例として数えられない。<br>評価時には「どの種類にも当たらない」という追加ラベルを設け、空集合の正しい予測も数える。<br>公開testでは、UNFAIR-ToSの空集合は1,607文中1,435文、約89.3%を占める。|
|43|20|20|公開testの集計の直接出典も併記する|[1] Chalkidis et al. (2022). LexGLUE: A Benchmark Dataset for Legal Language Understanding in English. ACL.  https://aclanthology.org/2022.acl-long.297/|[1] Chalkidis et al. (2022). LexGLUE. https://aclanthology.org/2022.acl-long.297/<br>[2] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|44|21|21|seedを読者が意味を理解できる日本語へ置き換える|2022年のtest macro-F1（%）。各課題で微調整、5 seedから開発最良を採用。|2022年のtest macro-F1（%）。各課題で微調整し、初期化を変えた5回の実験のうち開発得点が最良の結果を採用。|
|45|22|22|長文処理という意味ある比較条件を残し、採用基盤への注意とseed反復を除く|ECtHR A/BとSCOTUSでは、BERT系の階層モデルが最大64段落×128トークンを読む。段落を個別に符号化し、上位のTransformerで文書にまとめる。<br>LongformerとBigBirdは疎な注意を使い、最大4,096トークンを扱う。モデル名だけでなく、読める範囲も条件の一部となる。<br>成績は各課題で微調整し、5 seedのうち開発成績が最良のseedを採用。HELMの少数例提示の成績とは区別する。|ECtHR A/BとSCOTUSでは、BERT系の階層モデルが最大64段落×128トークンを読む。段落を個別に符号化し、上位のTransformerで文書にまとめる。<br>LongformerとBigBirdは疎な注意を使い、最大4,096トークンを扱う。長い文書のどこまで読めるかが、方式ごとの評価条件に含まれる。|
|46|27|24|読者に必要な説明へ整理|subsetとrevisionを指定して取得する|契約条項を読み、整数ラベルを主題名へ変換する|
|47|27|24|固定hashの取得コードを、公開Parquetから原文とラベル名を読む実利用コードへ置き換える|from datasets import load_dataset<br>data = load_dataset(<br>    'coastalcph/lex_glue', 'ledgar',<br>    revision='c23fdff1a6bf74e0e1a71cb86f1e781d37da888c',<br>    split='test',<br>)<br>print(data[52]['text'], data[52]['label'])|import json<br>import pyarrow.parquet as pq<br>table = pq.read_table("ledgar-test.parquet")<br>info = json.loads(table.schema.metadata[b"huggingface"])<br>labels = info["info"]["features"]["label"]["names"]<br>row = table.to_pylist()[0]<br>print(row["text"])<br>print(labels[row["label"]])|
|48|27|24|読者に必要な説明へ整理|整数ラベルの意味は、そのsubsetのfeaturesにあるClassLabelと対応させる。|ledgarのtest Parquetをledgar-test.parquetとして保存する。textが条項、labelが主題の整数番号。ClassLabelのnamesから主題名を取り出す。|
|49|28|25|読者に必要な説明へ整理|共通カードと、元素材の権利を確認する|共通の配布先から、七つの課題を選べる|
|50|28|25|制作側の取得・保存記録を外し、入手方法と利用条件を説明する|Hugging FaceのデータカードはCC BY 4.0を表示する。裁判所、EU機関、契約や規約の作成者など、元素材の出所と帰属も保つ。<br>本資料では、固定revisionの7つのtest Parquetを取得し、13件の原レコードと参照ラベルを保存した。長い原入力の抜粋には範囲を明示する。<br>コードと収録文書では利用条件の出所が異なるため、再配布時は各出所を確認する。|公式GitHubは、7課題の説明、データ取得先、微調整と評価のコードを案内する。Hugging Faceでは課題名とtrain・validation・testを選んで取得できる。<br>データカードはCC BY 4.0を表示する。裁判所、EU機関、契約や規約の作成者など、元素材の出所と帰属も保って利用する。<br>コードと収録文書では利用条件の出所が異なるため、再配布時はそれぞれの出所を確認する。|
|51|28|25|読者に必要な説明へ整理|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE. https://github.com/coastalcph/lex-glue<br>[2] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|52|29|26|元の対象と具体的な使い方をまとめ、採用先の公開run監査を外す|LexGLUEは、英語の法律文書に対する分類と5択を、7課題にまとめる。単一ラベル、複数ラベル、候補番号の違いを保つ。<br>長文の扱い、空集合の採点、少数クラス、時系列の分割が成績の読み方に関わる。<br>HELM固定版では公開runを確認できなかった。教師あり学習の公開成績と、実装上の少数例提示条件を区別して利用する。|LexGLUEは、英語の法律文書に対する分類と5択を、7課題にまとめたベンチマーク。裁判・法令・契約など、文書ごとに異なる言語理解を扱う。<br>長文の扱い、空集合の採点、少数クラス、時系列の分割が、成績を読むための重要な特徴である。<br>法律向け事前学習を使うLegal-BERTなどを、共通のデータ分割と指標で比較できる。|
|53|39|36|facts as submitted by the partiesを、当事者が述べた事件経緯として自然な日本語にする|5. 申立人は1989年生まれで、マニサに住む。<br>6. 当事者が提出した事実は、以下のとおり要約できる。<br>7. 2009年7月7日、申立人は規律違反を理由に専門憲兵学校から退学処分を受けた。<br>8. 7月28日、最高軍事行政裁判所に処分の取消しを求めて提訴した。<br>9. 2010年1月6日、同裁判所は国防省が提出した「秘密文書」を考慮して請求を退けた。この文書は申立人に開示されなかった。<br>10. 5月5日、同裁判所は申立人の訂正の申立ても退けた。|5. 申立人は1989年生まれで、マニサに住む。<br>6. 当事者から示された事件の経緯は、以下のように要約できる。<br>7. 2009年7月7日、申立人は規律違反を理由に専門憲兵学校から退学処分を受けた。<br>8. 7月28日、最高軍事行政裁判所に処分の取消しを求めて提訴した。<br>9. 2010年1月6日、同裁判所は国防省が提出した「秘密文書」を考慮して請求を退けた。この文書は申立人に開示されなかった。<br>10. 5月5日、同裁判所は申立人の訂正の申立ても退けた。|
|54|38|35|混入した不自然な題名を内容に即して自然化する|実例9：秘密文書を使った手続きを読む|実例9：秘密文書を用いた審理|
|55|39|36|混入した不自然な題名を内容に即して自然化する|実例9：秘密文書を使った手続きを読む（訳）|実例9：秘密文書を用いた審理（訳）|
|56|42|39|公式EuroVoc英語名称に対応する日本語概念名を主表示にし、整数IDと公式英語名は次頁で保持する|正解：EuroVoc：100174 / 100277 / 100282 / 100283|正解：EU機関・欧州公務員制度／欧州／経済地理／政治地理|
|57|40|37|元課題のラベル定義を肯定的な題名で伝える|実例10：主張された違反と認定を区別する|実例10：検討対象となった条項を予測する|
|58|45|42|候補は0〜4と表示されるため、重複する0始まりの補足を省く|正解：選択肢1（0始まり）|正解：選択肢1|
|59|47|44|読者に必要な説明へ整理|条約の条番号と、配布の整数は別の値|配布の整数ラベルを、条約の条番号へ対応付ける|
|60|54|46|著者位置を省き、作成主体と元研究の意義を紹介する|第一著者はIlias Chalkidis、最終著者はNikolaos Aletras。計7人の著者による研究として、ACL 2022で発表された。<br>法域や文書の形式が異なる公開データに、統一した取得方法と基準モデルを用意した。<br>Legal-BERTなどの法律向け事前学習、長文処理、ラベルの不均衡が、どの課題で役立つかを比較する基盤になっている。|Ilias Chalkidis、Abhik Janaら7人による研究で、2021年に初公開され、ACL 2022で発表された。<br>法域や文書の形式が異なる公開データに、統一した取得方法と基準モデルを用意した。<br>Legal-BERTなどの法律向け事前学習、長文処理、ラベルの不均衡が、どの課題で役立つかを比較する基盤になっている。|
|61|57|49|読者に必要な説明へ整理|Ilias Chalkidis et al. · Hugging Face|Ilias Chalkidis et al. · n.d. · Hugging Face（2026-10-18参照）|
|62|57|49|採用先固有の変換コードを、元データの公式利用案内へ置き換える|LexGLUEScenario / get_lex_glue_spec|LexGLUE official repository|
|63|57|49|採用先固有の変換コードを、元データの公式利用案内へ置き換える|Stanford CRFM · HELM v0.4.0|Ilias Chalkidis et al. · n.d. · GitHub（2026-10-18参照）|
|64|57|49|採用先固有の変換コードを、元データの公式利用案内へ置き換える|七つのsubsetの入力、参照、少数例提示と指標の登録を実装する。|7課題の構成、データ取得先、微調整と評価のコードを案内する。|
|65|57|49|採用先固有の変換コードを、元データの公式利用案内へ置き換える|https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/lex_glue_scenario.py|https://github.com/coastalcph/lex-glue|
|66|21|21|実描画で見つかった重なりを解消|2行の表注と出典が接触|出典を12pt下へ置き、表注との間隔を確保|
|67|27|24|実コード全文の背景と上下実字形余白をそろえる|8行目のコードが背景下端から出る|字形位置を維持して背景のtop/height/余白を調整|
|68|1|1|全text_frameの実画素境界への収容|字形の下端が外枠を少し超える|heightとmargin_bottomを各8pt拡張、字形位置不変|
|69|30|27|全text_frameの実画素境界への収容|字形の下端が外枠を少し超える|heightとmargin_bottomを各8pt拡張、字形位置不変|
|70|6|6|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ledgar/test/52  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|71|8|8|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 unfair_tos/test/15  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|72|10|10|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ecthr_a/test/34  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|73|11|11|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ecthr_a/test/34  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|74|27|24|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|75|33|30|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ledgar/test/86  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|76|34|31|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ledgar/test/22  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|77|35|32|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 unfair_tos/test/57  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|78|36|33|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 unfair_tos/test/56  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|79|37|34|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 unfair_tos/test/67  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|80|38|35|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ecthr_a/test/12  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|81|39|36|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ecthr_a/test/12  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|82|40|37|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 ecthr_b/test/26  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|83|41|38|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 scotus/test/18  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|84|42|39|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 eurlex/test/60  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|85|44|41|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 case_hold/test/38  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|86|45|42|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。 case_hold/test/38  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|87|47|44|行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|88|49||行位置・hash・繰り返す権利文言を検証記録へ移す|[1] Chalkidis et al. (2022). LexGLUE: A Benchmark Dataset for Legal Language Understanding in English. ACL.  https://aclanthology.org/2022.acl-long.297/<br>[2] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|89|52||行位置・hash・繰り返す権利文言を検証記録へ移す|[1] coastalcph/lex_glue. 固定revision c23fdff… / 元の裁判・法令・契約の作成者に帰属。  https://huggingface.co/datasets/coastalcph/lex_glue|[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue|
|90|24||採用先の公開run0と取得監査を外部化|HELMには実装があり、固定版の公開runはない<br>HELM Classic v0.4.0のschemaにはLexGLUE群があり、7つのsubsetを読み込む実装もある。<br>一方、固定releaseの全run_specsを名前とscenarioクラスで調べると、LexGLUEに対応する公開runは0件だった。<br>このため、ここではHELMの得点やモデル順位を示さず、公開されている入力・参照・生成設定の設計を説明する。<br>4. 公開配布と利用方法<br>[1] Stanford CRFM. HELM Classic v0.4.0, LexGLUE群。  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/lex_glue||
|91|25||採用先固有の提示上限・生成パラメータを外部化|実装上の提示上限と出力上限<br>4. 公開配布と利用方法<br>v0.4.0の設定値。実際の提示数・試行数・切詰め率は公開runなし。<br>[1] Stanford CRFM. LexGLUEScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/lex_glue_scenario.py||
|92|26||採用先固有のラベル変換を外部化。元ラベルの対応は保持|配布のラベルと、出力文字列を区別する<br>HELMの複数ラベル課題は、配布の整数インデックスを文字列化する。ECtHRの第6条は3、EUR-LEXのEuroVoc ID 100174は7となる。<br>LEDGARはClassLabelの名前を参照とし、CaseHOLDは0〜4の候補番号を使う。<br>SCOTUSには説明中の番号と参照文字列のずれがある。固定配布・実装を照合した対応をAppendixに示す。<br>4. 公開配布と利用方法<br>[1] Stanford CRFM. LexGLUEScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/lex_glue_scenario.py||
|93|48||採用先の番号ずれを調べた実装監査を外部化|SCOTUSの番号は三つの層で読む<br>Appendix: 2. 条約ラベルの対応<br>v0.4.0実装と固定配布を照合。実行成績への影響は、公開runがないため観測していない。<br>[1] Stanford CRFM. LexGLUEScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/lex_glue_scenario.py||
|94|49||細かな論文対配布の照合表を外部化。評価範囲の差は本編の件数頁へ集約|論文と固定配布の差を記録する<br>Appendix: 2. 条約ラベルの対応<br>固定配布の空集合はtest実測。論文の記載比率と区別する。差が生じた経緯は未確定。<br>[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue||
|95|50||採用先固有の不正解参照生成処理を外部化|HELMは不正解の参照を最大30件に絞る<br>単一・複数ラベル分類では、全クラスから正解を除いて不正解の参照を作り、seed42の乱数で順序を変える。<br>不正解が30件を超えると、先頭30件だけを保持する。LEDGARやEUR-LEXでは、全100クラスを参照として毎回並べる実装ではない。<br>入力本文はECtHRの段落列を空白で連結し、CaseHOLDはcontextと番号付きの5候補を連結する。<br>Appendix: 2. 条約ラベルの対応<br>[1] Stanford CRFM. LexGLUEScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/lex_glue_scenario.py||
|96|51||採点登録とdocstring照合の監査を外部化|参照を作る処理と、採点の登録を照合する<br>複数ラベル分類はカンマと空白を区切りとして分類指標を登録し、単一ラベル分類も分類指標を登録する。<br>CaseHOLDのタスク型はQAで、同じ関数の分類指標を追加する分岐には入らない。schemaの主指標名だけから、7課題すべての採点結果があると解釈しない。<br>UNFAIR-ToSのdocstring例には、終了を述べる文に変更ラベルを示す記述がある。参照ラベルは、説明例の文言ではなく配布レコードと生成処理で確かめた。<br>Appendix: 2. 条約ラベルの対応<br>[1] Stanford CRFM. get_lex_glue_spec, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/run_specs.py||
|97|52||表示範囲の制作説明を外部化。各真正例の抜粋範囲表示は保持|長い入力を抜粋した範囲を明示する<br>実例10はECtHR Bの事実列の先頭2段落、実例12はEU法令の冒頭からWhereas直前までを表示する。参照ラベルは元の全文に付く。<br>実例13はCaseHOLD contextの末尾の連続範囲を示し、5つの候補はすべて全文を保持する。元のcontextと全候補は原記録に保存する。<br>ほかの10例は入力全文を表示する。SCOTUSの空行は整理し、内容と順序は保った。<br>Appendix: 2. 条約ラベルの対応<br>[1] Chalkidis et al. LexGLUE公開データ。https://huggingface.co/datasets/coastalcph/lex_glue||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
