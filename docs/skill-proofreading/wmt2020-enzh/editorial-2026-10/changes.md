# WMT2020（英中）：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|1|1|読者に必要な説明へ整理|News Translation Task<br>newstest2020: English to/from Chinese<br>ニュースの原入力と参照訳で、英中の翻訳を評価する|News Translation Task<br>newstest2020: English to/from Chinese<br>ニュースの原文と参照訳で、英中の翻訳を評価する|
|2|1|1|全subtitle本文がnative枠内に収まる高さへ、位置・内容を保持|baseline subtitle height|height +12pt|
|3|3|3|見出しの原入力を自然な日本語にする|原入力から、別の言語へ訳す<br>ニュース文書と参照訳の構成<br>BLEUと、2020年の人手評価<br>CLEVAでの採用と利用条件|ニュースを、別の言語へ訳す<br>ニュース文書と参照訳の構成<br>BLEUと、2020年の人手評価<br>CLEVAでの採用と利用条件|
|4|4|4|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|5|5|5|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|6|6|6|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|7|7|7|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|8|8|8|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|9|9|9|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|10|10|10|見出しの原入力を自然な日本語にする|1. 原入力から、別の言語へ訳す|1. ニュースを、別の言語へ訳す|
|11|5|5|読者に必要な説明へ整理|WMT2020のニュース翻訳では、入力の内容を別の言語で表す。本資料は公開テストnewstest2020の英→中と中→英を扱う。<br>入力と対応する参照訳が公開されている。参照訳は比較のための訳文であり、同じ内容を表す唯一の正解ではない。<br>二つの翻訳方向は、それぞれ原言語の異なるニュース文書から作られた。同じ対を逆向きにして、独立した例を増やしていない。|WMT2020のニュース翻訳では、入力の内容を別の言語で表す。この資料は、公開テストnewstest2020の英語→中国語と中国語→英語を扱う。<br>入力に対応する参照訳が公開されている。参照訳は比較のために人が作った訳文で、同じ内容を表すほかの訳もあり得る。<br>英語→中国語は英語のニュース、中国語→英語は中国語のニュースを原文にしている。|
|12|7|7|読者に必要な説明へ整理|Houseは下院、rebukesは非難。対立するbut節と、plansが示す意向を保つ。<br>主節の非難と、but節の反対の動きを一つの見出しに保つ。plansは実行済みの拒否ではなく、行使する意向を表す。<br>この原入力と参照訳は、CLEVAの紙面例と一致する。ここでは、WMT2020の公開テストにある一つの区間として示した。|Houseは下院、rebukesは非難を表す。下院の動きに対し、butの後にはトランプ氏の反対の動きが続く。plansは、拒否権を行使する意向を表す。<br>この見出しと中国語の参照訳は、CLEVA論文の翻訳例にも掲載されている。|
|13|10|10|読者に必要な説明へ整理|単語の対応と、文の役割を保つ|関係節や役職を読み取り、誰が何をしたかを訳す|
|14|10|10|読者に必要な説明へ整理|長い関係節がthe manを説明する。女性への抑圧に反対したことと、再婚の推進を両方保つ。<br>人名や機関名のある文では、誰がどの役職で、何をしたのかを読み分ける。長い列挙でも、受賞者へ賞を贈ったという動作を保つ。<br>表示したのは各SGMの1区間の全文と、その区間に対応する参照訳の全文。記事全体を入力にした実行結果ではない。|実例2では、長い関係節がthe manを説明する。女性への抑圧と闘ったことと、寡婦の再婚を推進したことが、この人物の活動として述べられている。<br>実例3では、人名・機関名・役職が列挙され、受賞者へ賞を贈ったという動作につながる。原文と参照訳には、役職をまとめる表現の違いもある。|
|15|12|12|読者に必要な説明へ整理|WMT20のニュース翻訳は11言語対、22方向を含む国際共有タスク。本資料はそのうちの英語・中国語の二方向に絞る。<br>ニュースサイトの原文を収集し、評価用の翻訳を作成した。入力が翻訳文になることを避けるため、各方向の原言語の文書を使う。<br>学習用の対訳・単言語コーパス、開発データ、公開テストは別の資源。WMT14など、別年のテストも同じ集合とは扱わない。|WMT20のニュース翻訳は、11言語対・22方向を含む国際共有タスク。この資料は、そのうち英語・中国語の二方向を扱う。<br>ニュースサイトから各言語の原文を収集し、評価用の参照訳を作成した。<br>参加者向けには、学習用の対訳・単言語コーパスや開発データも配布された。公開テストは、学習後の翻訳品質を比べるために使う。|
|16|13|13|再集計・重複検査等の制作監査は外部記録へ|SGMのdocidとseg idを再集計。区間数と記事数は異なる。各方向で原入力の重複・空欄は0。||
|17|14|14|読者に必要な説明へ整理|英→中では、翻訳者へ文単位ではなく段落の区切りを保った文章を渡した。翻訳時に文を結合・分割する自由度を持たせている。<br>公式サイトも、一つの区間が通常より長く、複数の文を含む場合があると説明する。segを一律に一文と数えない。<br>公開SGMは、文書のdocidと区間のidを持つ。同じseg idが別の記事にも現れるため、二つを組にして対応付ける。|英語→中国語では、翻訳者へ段落の区切りを保った文章を渡し、翻訳時に文を結合・分割する自由度を持たせた。評価の1区間に、複数の文が入る場合もある。<br>公開ファイルのSGM形式では、文書にdocid、区間にidが付く。この二つを組にして、原文と参照訳を対応付ける。|
|18|15|15|読者に必要な説明へ整理|入力が同じなので、B配布を追加の独立した入力例として数えない。本資料の13例は通常配布の参照を使用。|実例では、newstest2020の通常参照を示す。|
|19|16|16|読者に必要な説明へ整理|上：newstest2020、下：newstestB2020。「边境城」はB配布の原形を保持。|上：newstest2020、下：newstestB2020。B参照には「边境城」（国境の都市）という表記がある。|
|20|17|17|読者に必要な説明へ整理|共有タスクでは、提供された学習資源に従うconstrained条件と、それを超える資源を使う条件を区別する。テストの対だけで学習条件は決まらない。<br>ニュース翻訳のシステムは、対訳データ、単言語データ、逆翻訳、モデルの組合せなどを利用した。個別のシステム構成は参加論文で説明される。<br>ここで示す13例は公開テストの原入力と参照訳。実際のモデル出力や、未取得のCLEVAの学習・提示データではない。|共有タスクには、公式に提供された学習資源の範囲で参加するconstrained条件と、それを超える資源を使う条件がある。<br>参加システムは、対訳データや単言語データ、逆翻訳、複数モデルの組合せなどを用いた。個別のシステム構成は、各参加論文で説明されている。|
|21|18|18|読者に必要な説明へ整理|語句の一致と、人の判断を分ける|語句の一致と、人による意味の評価|
|22|19|19|読者に必要な説明へ整理|BLEUは、翻訳内容の正答率ではない|BLEUは、参照訳と語句が重なる程度を測る|
|23|19|19|読者に必要な説明へ整理|BLEUは、出力と参照のn-gramの重なりを数える。通常は1〜4-gramの修正適合率を幾何平均し、短い出力へ長さのペナルティを掛ける。<br>修正適合率は、出力中の全n-gramに対する、参照と一致するn-gramの割合。一致数は参照の出現回数を上限とし、繰り返しによる水増しを抑える。<br>n-gramはn個のトークンの連続列。複数区間の一致数と長さをまとめてコーパスのBLEUを求め、区間ごとのBLEUの単純平均とは区別する。|BLEUは、翻訳出力と参照訳のn-gramの重なりを数える。通常は1〜4-gramの修正適合率を幾何平均し、短い出力へ長さのペナルティを掛ける。<br>修正適合率は、出力中のn-gramのうち参照と一致するものの割合。一致数は参照の出現回数を上限とするため、同じ語を繰り返しても得点は伸びにくい。<br>n-gramは、n個のトークンの連続列。各区間の一致数と長さを合計して、コーパス全体のBLEUを求める。|
|24|20|20|読者に必要な説明へ整理|言語の区切り方と、版を明示する|中国語の文字の区切り方が、BLEUに影響する|
|25|20|20|読者に必要な説明へ整理|中国語の分割方法は得点に影響する。この計算のzh分割は漢字などを1字ずつに分け、非漢字部分にも区切り処理を行う。<br>SacreBLEUは、参照や分割方法などの条件を再現しやすくする評価ツール。版、大小文字、参照数、tokenizerをそろえて値を読む。<br>次の計算例はSacreBLEU 2.5.1、参照1本、大小文字を保持、zh分割。WMT2020や、未取得のCLEVA実行の採点条件を再現した値ではない。|中国語の分割方法は、得点に影響する。SacreBLEUのzh分割は、漢字などを1字ずつに分け、非漢字部分にも区切り処理を行う。<br>SacreBLEUは、参照や分割方法をそろえてBLEUを計算する評価ツール。<br>次の参照訳同士の比較では、このzh分割でBLEUを計算した。|
|26|22|22|読者に必要な説明へ整理|2020年の人手評価は、別の尺度を使う|2020年の人手評価は、意味の伝わり方を採点する|
|27|22|22|読者に必要な説明へ整理|英→中。HUMAN-A/Bは評価した人手訳、3システムは資源制約内。DA評点（0〜100）は正答率ではない。|英→中の人手評点（0〜100）。HUMAN-A/Bは人手訳、3システムは公式の学習資源内で参加。|
|28|23|23|読者に必要な説明へ整理|英語からの翻訳では、原文と翻訳を示し、文書全体を見ながら個々の区間や文書を評価する方式を使った。意味がどれほど適切に伝わるかを人が判断する。<br>採点者ごとの評点の傾向を平均と標準偏差で標準化し、平均z得点を求める。生の平均評点と、標準化後の並び順が同じになるとは限らない。<br>会議の公式順位は統計的な同順位群も持つ。上の小数点の差を、すべて有意な性能差と扱わない。|英語からの翻訳では、原文を理解できる評価者に原文と翻訳を示し、文書の文脈を見ながら意味の伝わり方を評価してもらった。<br>採点者ごとの評点を、その人の平均と標準偏差で標準化し、平均z得点を求める。標準化した値で評価対象を並べるため、生の平均評点とは順位が入れ替わることがある。<br>公式順位では、統計的に差があるとはいえないシステムを同順位の群にまとめている。|
|29|24|24|読者に必要な説明へ整理|公開例の出所と、実行の範囲を追う|CLEVAでも、ニュース翻訳を評価する|
|30|25||読者に必要な説明へ整理|CLEVAの公開例は、2020年の配布へ一致|CLEVAは、過去のWMTデータで翻訳を評価する|
|31|25||読者に必要な説明へ整理|CLEVAは、過去のWMT大会から英中翻訳データを集め、SacreBLEUで評価すると説明する。紙面自体は、採用データの年を一つに限定していない。<br>紙面の下院見出しと、HELMの二つの翻訳説明例は、WMT2020通常配布の原入力・参照訳へ完全一致する。<br>この一致が示すのは、公開例の出所。CLEVAの全翻訳集合がWMT2020だけであることや、B配布を使わないことまで証明するものではない。|CLEVAは、過去のWMT大会から英中翻訳データを集め、SacreBLEUで評価する。採用した年ごとの問題数は、公表されていない。<br>CLEVA論文の下院の見出しと、HELMの二つの翻訳例は、WMT2020通常配布の原文・参照訳と一致する。|
|32|28|25|読者に必要な説明へ整理|研究利用と、ニュース本文の権利を分ける|研究目的で利用でき、引用と権利の条件がある|
|33|28|25|読者に必要な説明へ整理|公式タスクページは、WMT20のデータを研究目的で自由に使えるとし、概要論文と各集合の追加引用条件を守るよう求める。<br>それ以外の用途は元データの権利者へ相談するという条件。公開ダウンロードが、ニュース本文の権利の放棄を意味するわけではない。<br>本資料は識別可能な短い13区間を、出所と参照訳とともに示す。ニュースの原記事全体や、データ全量の追加配布は作っていない。|公式タスクページは、WMT20のデータを研究目的で自由に使えるとし、概要論文と各集合の追加引用条件を守るよう求める。<br>それ以外の用途については、元データの権利者へ相談する条件になっている。|
|34|29|26|読者に必要な説明へ整理|入力・参照・方向・尺度をそろえて読む|英中のニュース翻訳を、BLEUと人手で評価する|
|35|29|26|読者に必要な説明へ整理|WMT2020英中は、原言語の異なるニュース文書を二方向へ翻訳する公開テスト。文章区間と文書の単位を分け、対応する参照を使う。<br>BLEUは参照の表現や分割条件で変わり、人の意味判断と同じ尺度ではない。2020年の会議の評価と、説明用の再計算も区別する。<br>CLEVAの公開例は出所を追跡できる一方、選定集合全体と推論条件は未確定。元WMTデータの全件数を、そのままCLEVAの実行数へ置き換えない。|WMT2020の英中公開テストは、英語→中国語が1,418区間、中国語→英語が2,000区間。ニュースの原文に、人が作った参照訳が付く。<br>BLEUは参照訳との語句の一致を測り、人手評価は文脈の中で意味が伝わるかを調べる。同じ入力にも異なる参照訳があり、語句の選び方がBLEUに影響する。<br>後にCLEVAでも、WMTのデータが言語モデルの翻訳評価へ取り込まれた。|
|36|31|28|読者に必要な説明へ整理|追加の公開翻訳例<br>原位置・計算・公開実装<br>研究と参考文献|追加の公開翻訳例<br>データの読み方と評価の具体例<br>参考文献|
|37|6|6|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / foxnews.100085 / seg 1 / 全体index 910|英語から中国語へ|
|38|8|8|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / en.ndtv.com.13041 / seg 8 / 全体index 1411|英語から中国語へ|
|39|9|9|出所ID・区間番号・全体indexは外部記録へ移す|中→英 / chinanews.com.102568 / seg 3 / 全体index 18|中国語から英語へ|
|40|33|30|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / cnn.385674 / seg 1 / 全体index 24|英語から中国語へ|
|41|34|31|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / rte.en.ie.5333 / seg 1 / 全体index 101|英語から中国語へ|
|42|35|32|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / upi.205660 / seg 1 / 全体index 114|英語から中国語へ|
|43|36|33|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / seattle_times.7657 / seg 1 / 全体index 164|英語から中国語へ|
|44|37|34|出所ID・区間番号・全体indexは外部記録へ移す|英→中 / standard.co.uk.14676 / seg 2 / 全体index 230|英語から中国語へ|
|45|38|35|出所ID・区間番号・全体indexは外部記録へ移す|中→英 / international_times-zh.151 / seg 4 / 全体index 30|中国語から英語へ|
|46|39|36|出所ID・区間番号・全体indexは外部記録へ移す|中→英 / hunan_ribao-zh.186 / seg 2 / 全体index 96|中国語から英語へ|
|47|40|37|出所ID・区間番号・全体indexは外部記録へ移す|中→英 / nikkei-.108 / seg 1 / 全体index 146|中国語から英語へ|
|48|41|38|出所ID・区間番号・全体indexは外部記録へ移す|中→英 / xinhua-zh-01.6415 / seg 2 / 全体index 228|中国語から英語へ|
|49|42|39|出所ID・区間番号・全体indexは外部記録へ移す|中→英 / chinanews.com.102714 / seg 1 / 全体index 238|中国語から英語へ|
|50|46|41|読者に必要な説明へ整理|原位置・計算・公開実装|データの読み方と評価の具体例|
|51|46|41|読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|52|47||読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|53|48||読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|54|49|42|読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|55|50||読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|56|51|43|読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|57|52|44|読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|58|53||読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|59|54|45|読者に必要な説明へ整理|Appendix: 2. 原位置・計算・公開実装|Appendix: 2. データの読み方と評価の具体例|
|60|44|40|読者に必要な説明へ整理|各実例で、何を保って訳すか|参照訳にも、具体化や語句の違いがある|
|61|44|40|番号・検査用表現を自然な説明へ整理|引用符付きのlikesはSNSの反応。参照訳は点赞数と、数であることを明示する。|英語のlikesに対し、中国語の参照訳は点赞数と「数」であることを明示する。|
|62|44|40|番号・検査用表現を自然な説明へ整理|固有名詞とカテゴリー4、east ofが示す位置を保つ。|英語のeast of Caribbeanはカリブ海の東。中国語の参照訳は加勒比海东部（カリブ海の東部）と表す。|
|63|44|40|番号・検査用表現を自然な説明へ整理|参照訳は教皇の名前を補う。原入力の明示語と、参照訳の具体化を分けて読む。|英語はPope（教皇）と記し、中国語の参照訳は「教皇フランシスコ」と名前を具体化する。|
|64|44|40|番号・検査用表現を自然な説明へ整理|has been set upは設立済みであることを示す。to recognise以下は表彰する目的。|英語は表彰制度が設けられたことと、その目的を述べる。中国語の参照訳は目的を中心に表す。|
|65|44|40|番号・検査用表現を自然な説明へ整理|只能／onlyが機器を限定する。IR-1という型式を、そのまま保つ。|只能とonlyは、使用できる機器を第1世代のIR-1型に限定する。|
|66|44|40|訳を無理に同一化しないという制作方針を本文から除く|説明は本資料による。原入力と参照訳を同じ意味の日本語へ無理にそろえていない。||
|67|49|42|読者に必要な説明へ整理|SacreBLEU2.5.1 / nrefs1 / case mixed / smooth exp / eff no。モデル出力を使った評価ではない。|通常参照を出力側、B参照を比較の参照側に置いて計算。SacreBLEU 2.5.1、参照1本、大小文字を保持。|
|68|51|43|読者に必要な説明へ整理|import re, tarfile, html<br>with tarfile.open('test.tgz') as archive:<br>    raw = archive.extractfile(<br>        'sgm/newstest2020-enzh-src.en.sgm'<br>    ).read().decode('utf-8')<br>segments = re.findall(r'<seg id="[^"]+">(.*?)</seg>', raw)<br>print(html.unescape(segments[910]))|import tarfile<br>from lxml import etree<br>with tarfile.open("test.tgz") as t:<br>    raw = t.extractfile(<br>        "sgm/newstest2020-enzh-src.en.sgm").read()<br>data = etree.HTML(raw)<br>seg = data.xpath('//doc[@docid="foxnews.100085"]//seg')[0]<br>print("".join(seg.itertext()))|
|69|54|45|読者に必要な説明へ整理|二方向の人手評価は、同一の方式ではない|翻訳方向ごとに、原文や参照を使って人が評価する|
|70|54|45|読者に必要な説明へ整理|2020年の英語からの翻訳は、原文を理解できる評価者によるsource-based評価。英語への翻訳は、英語の参照を使うreference-based評価を中心とする。<br>文書の文脈を示す方法も評価方向で異なる。複数の区間をまとめて見せる構成と、区間を順に評価しながら全文書へアクセスする構成を区別する。<br>したがって、英→中の平均zと中→英の平均zを、そのまま同じ絶対尺度の翻訳品質として比較しない。|英語からの翻訳は、原文を理解できる評価者が原文と訳文を見るsource-based評価。英語への翻訳は、英語の参照訳と照らすreference-based評価が中心となる。<br>文書の文脈を示す方法も方向によって異なる。得点は、それぞれの翻訳方向・評価方式の中で比較する。|
|71|55|46|読者に必要な説明へ整理|研究と参考文献|参考文献|
|72|55|46|読者に必要な説明へ整理|Appendix: 3. 研究と参考文献|Appendix: 3. 参考文献|
|73|56||読者に必要な説明へ整理|Appendix: 3. 研究と参考文献|Appendix: 3. 参考文献|
|74|57|47|読者に必要な説明へ整理|Appendix: 3. 研究と参考文献|Appendix: 3. 参考文献|
|75|58|48|読者に必要な説明へ整理|Appendix: 3. 研究と参考文献|Appendix: 3. 参考文献|
|76|59||読者に必要な説明へ整理|Appendix: 3. 研究と参考文献|Appendix: 3. 参考文献|
|77|60||読者に必要な説明へ整理|Appendix: 3. 研究と参考文献|Appendix: 3. 参考文献|
|78|6|6|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / foxnews.100085 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|79|7|7|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / foxnews.100085 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|
|80|8|8|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / en.ndtv.com.13041 / seg 8.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|81|9|9|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / zhen / chinanews.com.102568 / seg 3.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|82|10|10|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / en.ndtv.com.13041 / seg 8.  https://data.statmt.org/wmt20/translation-task/test.tgz<br>[2] WMT20. newstest2020 / zhen / chinanews.com.102568 / seg 3.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz<br>[2] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|83|33|30|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / cnn.385674 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|84|34|31|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / rte.en.ie.5333 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|85|35|32|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / upi.205660 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|86|36|33|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / seattle_times.7657 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|87|37|34|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / standard.co.uk.14676 / seg 2.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|88|38|35|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / zhen / international_times-zh.151 / seg 4.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|89|39|36|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / zhen / hunan_ribao-zh.186 / seg 2.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|90|40|37|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / zhen / nikkei-.108 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|91|41|38|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / zhen / xinhua-zh-01.6415 / seg 2.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|92|42|39|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / zhen / chinanews.com.102714 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|93|51|43|出典のdocid/seg番号は原記録へ移す|[1] WMT20. newstest2020 / enzh / foxnews.100085 / seg 1.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|94|10|10|同じ出典を二度列挙しない|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz<br>[2] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|95|20|20|独立レビュー：文献名に残った制作計算説明を削除|[2] Post et al. SacreBLEU 2.5.1. Local reference-to-reference calculation, fixed tokenization.|[2] Post et al. SacreBLEU 2.5.1. |
|96|21|21|独立レビュー：文献名に残った制作計算説明を削除|[2] Post et al. SacreBLEU 2.5.1. Local reference-to-reference calculation, fixed tokenization.|[2] Post et al. SacreBLEU 2.5.1. |
|97|49|42|独立レビュー：文献名に残った制作計算説明を削除|[2] Post et al. SacreBLEU 2.5.1. Local reference-to-reference calculation, fixed tokenization.|[2] Post et al. SacreBLEU 2.5.1. |
|98|50||独立レビュー：文献名に残った制作計算説明を削除|[1] Post et al. SacreBLEU 2.5.1. Local reference-to-reference calculation, fixed tokenization.|[1] Post et al. SacreBLEU 2.5.1. |
|99|52|44|独立レビュー：文献名に残った制作計算説明を削除|[2] Post et al. SacreBLEU 2.5.1. Local reference-to-reference calculation, fixed tokenization.|[2] Post et al. SacreBLEU 2.5.1. |
|100|52|44|メインレビュー：利用コードから監査用署名出力を除く|import re, tarfile, html<br>from sacrebleu.metrics import BLEU<br>def refs(name):<br>    with tarfile.open('test.tgz') as t:<br>        raw = t.extractfile(name).read().decode('utf-8')<br>    return [html.unescape(s) for s in re.findall(<br>        r'<seg id="[^"]+">(.*?)</seg>', raw)]<br>a = refs('sgm/newstest2020-enzh-ref.zh.sgm')<br>b = refs('sgm/newstestB2020-enzh-ref.zh.sgm')<br>metric = BLEU(tokenize='zh', lowercase=False)<br>print(metric.corpus_score(a, [b]).score)<br>print(metric.get_signature())|import re, tarfile, html<br>from sacrebleu.metrics import BLEU<br>def refs(name):<br>    with tarfile.open('test.tgz') as t:<br>        raw = t.extractfile(name).read().decode('utf-8')<br>    return [html.unescape(s) for s in re.findall(<br>        r'<seg id="[^"]+">(.*?)</seg>', raw)]<br>a = refs('sgm/newstest2020-enzh-ref.zh.sgm')<br>b = refs('sgm/newstestB2020-enzh-ref.zh.sgm')<br>metric = BLEU(tokenize='zh', lowercase=False)<br>print(metric.corpus_score(a, [b]).score)|
|101|52|44|署名出力1行の削除後、実描画の下余白24ptを8ptへ調整。字形位置は保持|height 205.333 pt|height 189.333 pt|
|102|51|43|独立レビュー：実字形位置を保ってコード背景の上余白を2.67pt拡張|上7.33pt/下10pt|上10pt/下10pt|
|103|26||公開索引件数・prompt設定・取得状況の制作監査|HELMの設定と、公開された実行を分ける<br>4. CLEVAでの採用と利用条件<br>設定の数はモデル数や生成候補数ではない。実際の得点・提示例数・温度は補っていない。<br>[1] Stanford CRFM. CLEVA v1 run settings, translation en2zh / zh2en. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf<br>[2] Stanford CRFM. HELM Classic v0.4.0 public run index.  https://crfm.stanford.edu/helm/classic/v0.4.0/||
|104|27||未取得実装の再現性に関する細かな制作報告|公開実装から分かることにも限界がある<br>HELM v0.4.0は、変換済みデータとテンプレートから翻訳入力と参照を作る。生成条件はinfer_params.jsonから読む。<br>採点設定は翻訳用のCLEVAMachineTranslationMetricクラスを指定する。しかし、その配置先のmachine_translation_metrics.pyは、同版の公開metrics一覧にない。<br>そのため、固定公開版だけからCLEVAの分割方法や集約を再現できたとは述べない。前の参照同士の計算は、条件を明示した別の説明用計算である。<br>4. CLEVAでの採用と利用条件<br>[1] Stanford CRFM. get_cleva_spec / get_cleva_machine_translation_metric_specs. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/run_specs.py<br>[2] Stanford CRFM. Public metrics directory at HELM v0.4.0.  https://github.com/stanford-crfm/helm/tree/v0.4.0/src/helm/benchmark/metrics||
|105|43||本編と同じ例の読み方と、取り違えを禁じる反復説明|各実例で、何を保って訳すか<br>Appendix: 1. 追加の公開翻訳例<br>説明は本資料による。原入力と参照訳を同じ意味の日本語へ無理にそろえていない。<br>[1] WMT20. Official test.tgz: newstest2020 / newstestB2020, English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz||
|106|45||既存例の数字を取り違えない等の注意書きと制作方針|各実例で、何を保って訳すか<br>Appendix: 1. 追加の公開翻訳例<br>説明は本資料による。原入力と参照訳を同じ意味の日本語へ無理にそろえていない。<br>[1] WMT20. Official test.tgz: newstest2020 / newstestB2020, English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz||
|107|47||原位置・0起算index・SHA保存の監査表|原文書と区間を、組で固定する<br>Appendix: 2. データの読み方と評価の具体例<br>全体indexは0起算、seg idは配布原形。SGM行番号、行SHA256、byte offset、対応参照を原記録へ保存。<br>[1] WMT20. Official test.tgz: newstest2020 / newstestB2020, English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz||
|108|48||原位置の監査表|原文書と区間を、組で固定する<br>Appendix: 2. データの読み方と評価の具体例<br>全体indexは0起算、seg idは配布原形。SGM行番号、行SHA256、byte offset、対応参照を原記録へ保存。<br>[1] WMT20. Official test.tgz: newstest2020 / newstestB2020, English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz||
|109|50||細かなn-gram件数。概念は19頁、割合は21頁に保持|英→中の計算例で、何を数えたか<br>Appendix: 2. データの読み方と評価の具体例<br>通常配布参照を出力側へ置く。参照側は78,915 token、出力側が長いためBP=1。<br>[1] Post et al. SacreBLEU 2.5.1.   https://github.com/mjpost/sacrebleu/tree/v2.5.1||
|110|53||生成既定値・取得失敗・条件を補わない等の制作監査|固定版の実行と、説明用計算の条件<br>get_cleva_specには、生成の既定値として提示例上限5、出力1候補、最大20 token、温度0などがある。実際にはinfer_paramsの値で上書きされる。<br>CLEVAの変換済みtranslation.zipを取得できていないため、この既定値を公開実行の条件とはみなさない。公開索引からも実際の翻訳runは得られない。<br>SacreBLEU2.5.1による参照比較は、使用した参照、tokenizer、大小文字、全区間数を固定した独立の計算例。CLEVAの未公開条件とは分けて再現する。<br>Appendix: 2. データの読み方と評価の具体例<br>[1] Stanford CRFM. get_cleva_spec / get_cleva_machine_translation_metric_specs. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/run_specs.py<br>[2] Stanford CRFM. CLEVA v1 run settings, translation en2zh / zh2en. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf||
|111|56||本編と繰り返す研究概要。著者と刊行は参考文献に保持|国際共有タスクで、翻訳を比較する<br>WMT20はLoïc Barrault、Magdalena Biesialska、Ondřej Bojarらによる国際共有タスク。第5回Conference on Machine Translationとして2020年に開催された。<br>ニュース翻訳の共通テスト、参加システム、人手評価、同順位群を整備し、多言語の翻訳を比較する。英中はその一部である。<br>CLEVAはこのような過去のWMTデータを、言語モデルの翻訳課題へ取り込む。原データの単位と後続評価の条件を分けて読む必要がある。<br>Appendix: 3. 参考文献<br>[1] Barrault et al. (2020). Findings of the 2020 Conference on Machine Translation (WMT20). WMT, pp.1–55.  https://aclanthology.org/2020.wmt-1.1/<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/||
|112|60||実行仕様・prompt設定だけの参考文献|参考文献<br>Appendix: 3. 参考文献<br>get_cleva_spec and get_cleva_machine_translation_metric_specs<br>Stanford CRFM · 2023 · HELM v0.4.0 run specification<br>推論パラメータの読取、生成条件、翻訳用metricへの接続先を定義する。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/run_specs.py<br>run_specs_cleva_v1.conf<br>Stanford CRFM · 2023 · HELM v0.4.0 configuration<br>翻訳en2zhとzh2enに、それぞれ0〜2の三つのprompt_idを登録する。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf||
|113|3|3|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|ニュースを、別の言語へ訳す<br>ニュース文書と参照訳の構成<br>BLEUと、2020年の人手評価<br>CLEVAでの採用と利用条件|ニュースを、別の言語へ訳す<br>ニュース文書と参照訳の構成<br>BLEUと、2020年の人手評価<br>入手と利用条件|
|114|24|24|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. CLEVAでの採用と利用条件|4. 入手と利用条件|
|115|25||元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. CLEVAでの採用と利用条件|4. 入手と利用条件|
|116|28|25|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. CLEVAでの採用と利用条件|4. 入手と利用条件|
|117|29|26|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|4. CLEVAでの採用と利用条件|4. 入手と利用条件|
|118|24|24|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|CLEVAでも、ニュース翻訳を評価する|公開データの入手と利用条件|
|119|29|26|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|WMT2020の英中公開テストは、英語→中国語が1,418区間、中国語→英語が2,000区間。ニュースの原文に、人が作った参照訳が付く。<br>BLEUは参照訳との語句の一致を測り、人手評価は文脈の中で意味が伝わるかを調べる。同じ入力にも異なる参照訳があり、語句の選び方がBLEUに影響する。<br>後にCLEVAでも、WMTのデータが言語モデルの翻訳評価へ取り込まれた。|WMT2020の英中公開テストは、英語→中国語が1,418区間、中国語→英語が2,000区間。ニュースの原文に、人が作った参照訳が付く。<br>BLEUは参照訳との語句の一致を測り、人手評価は文脈の中で意味が伝わるかを調べる。同じ入力にも異なる参照訳があり、語句の選び方がBLEUに影響する。|
|120|29|26|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|[1] Barrault et al. (2020). Findings of the 2020 Conference on Machine Translation (WMT20). WMT, pp.1–55.  https://aclanthology.org/2020.wmt-1.1/<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|[1] Barrault et al. (2020). Findings of the 2020 Conference on Machine Translation (WMT20). WMT, pp.1–55. https://aclanthology.org/2020.wmt-1.1/|
|121|7|7|元データセットの目的・作成・評価・使い方を中心へ戻し、評価基盤固有の説明を外部記録へ移す|Houseは下院、rebukesは非難を表す。下院の動きに対し、butの後にはトランプ氏の反対の動きが続く。plansは、拒否権を行使する意向を表す。<br>この見出しと中国語の参照訳は、CLEVA論文の翻訳例にも掲載されている。|Houseは下院、rebukesは非難を表す。下院の動きに対し、butの後にはトランプ氏の反対の動きが続く。plansは、拒否権を行使する意向を表す。|
|122|7|7|原データ配布元だけで裏付けられる意味説明から、採用先の紙面引用を外部へ移す|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz<br>[2] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/|[1] WMT20 (2020). newstest2020 — English–Chinese.  https://data.statmt.org/wmt20/translation-task/test.tgz|
|123|25||CLEVAへの採用・HELM紙面との照合は外部記録へ移す|CLEVAは、過去のWMTデータで翻訳を評価する<br>CLEVAは、過去のWMT大会から英中翻訳データを集め、SacreBLEUで評価する。採用した年ごとの問題数は、公表されていない。<br>CLEVA論文の下院の見出しと、HELMの二つの翻訳例は、WMT2020通常配布の原文・参照訳と一致する。<br>4. 入手と利用条件<br>[1] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/<br>[2] Stanford CRFM. CLEVATranslationScenario / Converter. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py||
|124|59||評価基盤論文と変換実装の文献は外部記録へ移す|参考文献<br>Appendix: 3. 参考文献<br>CLEVA: Chinese Language Models EVAluation Platform<br>Li et al. · 2023 · EMNLP System Demonstrations<br>過去のWMTから英中翻訳を採用。公開見出し例とSacreBLEUの使用を記す。<br>https://aclanthology.org/2023.emnlp-demo.17/<br>CLEVATranslationScenario and Converter<br>Stanford CRFM · 2023 · HELM v0.4.0 implementation<br>変換済みデータとテンプレートから入力と参照を構成し、二方向の翻訳例を示す。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
