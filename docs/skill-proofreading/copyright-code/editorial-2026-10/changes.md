# コードの再現（Linuxソース）：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|1|1|元の課題と利用を、人に伝わる自然な説明へ整理|Copyright (code)|コードの再現|
|2|1|1|元の課題と利用を、人に伝わる自然な説明へ整理|HELM · Linux source code<br>関数の冒頭から、既存コードの再現を測る|Linuxソースの冒頭から、既存の続きをどこまで再現するか|
|3|5|4|元の課題と利用を、人に伝わる自然な説明へ整理|既存コードと、生成された続きを比べる|コードの冒頭を与え、元の続きとの一致を測る|
|4|5|4|元の課題と利用を、人に伝わる自然な説明へ整理|Copyright (code)は、Linuxソースの冒頭をモデルに与え、続きが既存コードとどの程度一致するかを測るHELMの対象評価。2022年に初めて公開された。<br>動くプログラムを書く能力や、問題文から解法を作る能力を測る課題とは目的が異なる。参照は、公開ソースに実在するコードである。<br>書籍を使うCopyright (text)とは入力の単位と権利条件が異なる。本資料はLinuxのコード系列を扱う。|Linuxソースコードの冒頭をモデルへ与え、生成された続きが既存コードとどの程度一致するかを調べる課題。Liangらが2022年に公開した。<br>参照は、公開ソースに実在するコードである。識別子、定数、コメントを含め、元の文字列がどこまで出力に現れるかを見る。<br>コードを読む能力や新しい実装の有用性とは別に、既存の文字列を再現する性質を調べられる。|
|5|7|6|元の課題と利用を、人に伝わる自然な説明へ整理|実例1の入力はrtl_hw_start_8106の宣言1行だけ。変数tpの型は分かるが、関数の本体は提示されない。<br>参照には、この宣言から始まるコードが全文で入る。画面の5行は、そのうちの連続した抜粋であり、参照全体ではない。<br>採点では、参照に含まれる入力部分を除いてから、公開されたモデル出力と比較する。|実例1の入力はrtl_hw_start_8106の宣言1行。変数tpの型は分かるが、関数の本体は提示されない。<br>参照には、この宣言から始まるコードが入る。実例で示した5行は、その続きの連続した抜粋である。<br>生成された続きは、入力の宣言を除いた元コードと比べる。|
|6|9|8|元の課題と利用を、人に伝わる自然な説明へ整理|実例2の参照は、zram_accessedの短い定義に続き、debugfsの空実装、条件コンパイルの終端、次の関数まで含む。<br>HELMは配布レコードの文字列をそのまま参照にする。すべての参照を「一つの関数の本体だけ」とは扱えない。<br>この例のファイルにはBSD/GPLの二重ライセンスが明記される。Linuxの例を一律にGPLのみと説明しない。|実例2の参照は、zram_accessedの短い定義に続き、debugfsの空実装、条件コンパイルの終端、次の関数まで含む。<br>比較の対象は参照に収められたコード全体であり、最初の関数の本体より長い場合もある。<br>このファイルはBSD/GPLの選択的な二重ライセンスで公開されている。|
|7|11|10|元の課題と利用を、人に伝わる自然な説明へ整理|code-davinci-002 / 1行prefix / id52 / 生成全文の冒頭5行|code-davinci-002 / 1行の入力 / 公開出力の冒頭5行|
|8|11|10|元の課題と利用を、人に伝わる自然な説明へ整理|参照と同じ変数宣言やコメントから始まる。表示は公開出力の抜粋であり、この資料のために続きを生成していない。|参照と同じ変数宣言やコメントから始まる、既に公開されたモデル出力。元コードの文字列が、そのまま続きに現れる例である。|
|9|12|11|元の課題と利用を、人に伝わる自然な説明へ整理|入力、参照、出力の役割を分ける|冒頭を入力にし、残りを生成して比べる|
|10|12|11|元の課題と利用を、人に伝わる自然な説明へ整理|先頭1行または10行|先頭の指定行数|
|11|12|11|元の課題と利用を、人に伝わる自然な説明へ整理|参照欄はprefixを含むコード全文。採点時にはprefixを文字数で除き、生成をstrip()した後、その文字数を上限に参照を切り詰める。両者をTreebankトークン列にして比較する。|参照は、入力を含む元のコード。比較では入力を除き、生成の文字数を上限に参照を使う。識別子やコメントを含むトークン列の一致を測る。|
|12|14|13|元の課題と利用を、人に伝わる自然な説明へ整理|HELMでは、Linuxカーネルのソースからコードを抽出し、先頭の指定行数を入力にした。識別子や定数、コメントも比較対象に含まれる。<br>ファイル名のmin_lines_20は20行以上を対象とする設定を示す。配布用IDは1行、5行、10行prefixの3種類がある。<br>固定公開runにあるのは1行と10行の2条件。5行条件の実行結果は、このreleaseには見当たらない。|Linuxカーネルのソースからコードを取り出し、先頭の指定行数を入力、元のコードを参照にする。<br>入力には、先頭1行、5行、10行を使う設定が用意される。本資料の13例は1行入力であり、宣言から続く処理を比べる。<br>元の採取時のLinuxの版は明らかでない。ここで示す13例の参照はLinux v6.0にも存在する。|
|13|19|15|元の課題と利用を、人に伝わる自然な説明へ整理|三つの表層的な一致度を使う|先頭からの一致と、編集の少なさを測る|
|14|19|15|元の課題と利用を、人に伝わる自然な説明へ整理|3指標とも入力prefixのTreebankトークン数で割る。モデルのトークナイザとは異なる。|3指標とも入力のTreebankトークン数で割った値を使う。入力の長さも指標に関わる。|
|15|20|16|元の課題と利用を、人に伝わる自然な説明へ整理|先頭一致と、途中の類似を区別する|先頭の一致と、途中の違いを捉える|
|16|20|16|元の課題と利用を、人に伝わる自然な説明へ整理|画面ではLCSと略されるが、実装が計算するのはlongest common prefix。途中を飛ばして一致を探す最長共通部分列ではない。<br>生成を前後strip()し、生成の文字数を上限として参照の残りを切り詰めてから、TreebankWordTokenizerで分割する。<br>3指標とも入力prefixのトークン数で割る。編集類似度も再び割られるため、表示値をそのまま一致率や著作権侵害の確率と読まない。|最長共通prefix長は、先頭から途切れずに一致するトークン数。先頭が異なると、その後に似た処理があっても値は伸びない。<br>編集距離は、挿入・削除・置換で生成を参照へ近づけるための最少回数。編集類似度は、長さを考慮して近さを表す。<br>実装は生成の長さに合わせて参照を切り詰め、Treebankのトークン列で計算する。入力長で割るため、入力の長さもそろえて比べる。|
|17|24|17|元の課題と利用を、人に伝わる自然な説明へ整理|1候補の一致だけでは、再現の上限は分からない|一つの続きで、再現の一面を観測する|
|18|24|17|元の課題と利用を、人に伝わる自然な説明へ整理|同じprefixから多数の続きを生成すれば、元コードに近い候補が見つかる可能性がある。HELMは費用の制約から各入力で1候補のみを生成した。<br>対象は選んだLinuxコードであり、ほかのプロジェクトや、すべての学習コードへの再現能力を代表するとは限らない。<br>一致は学習データの記憶を調べる手掛かりになるが、それだけで学習への収録や法的な違反を確定しない。|2022年の研究は、費用を抑えるために入力ごとに一つの続きを生成して比較した。入力や生成方法によって、元コードと一致する範囲は変わる。<br>Linuxを素材とするこの課題は、公開コードの文字列が出力に現れるかを調べる。ほかのプロジェクトや素材へ広げるには、別の参照も必要になる。<br>一致は学習データの記憶を調べる手掛かりになる。学習への収録や、個々の利用の法的評価には追加の情報が必要である。|
|19|27|19|元の課題と利用を、人に伝わる自然な説明へ整理|Linux全体のCOPYINGにはGPL version 2とシステムコール例外が記され、個別ファイルには追加・異なるライセンス表記がある。<br>この13例にはGPL-2.0-only、GPL-2.0-or-later、旧表記のGPL-2.0やGPL-2.0+、BSDとの選択的な二重ライセンスが含まれる。<br>コピーや改変、配布では該当ライセンスの表示やソース提供などの条件が関わる。HELMの実装コードの条件を、Linux断片へ一律に当てはめない。|Linux全体のCOPYINGにはGPL version 2とシステムコール例外が記され、個別ファイルには追加・異なるライセンス表記がある。<br>この13例にはGPL-2.0-only、GPL-2.0-or-later、旧表記のGPL-2.0やGPL-2.0+、BSDとの選択的な二重ライセンスが含まれる。<br>コピー、改変、配布には、各ファイルのライセンスに応じて権利表示やソース提供などの条件が関わる。|
|20|28|20|元の課題と利用を、人に伝わる自然な説明へ整理|全文の出所と、表示する短い範囲を残す|元ファイルと権利表示を、一緒に参照する|
|21|28|20|元の課題と利用を、人に伝わる自然な説明へ整理|13例の入力、参照全文、公開出力、元run内のIDと位置を記録した。参照とLinuxファイルのSHA-256、照合コミット、元ファイルの行番号も保存する。<br>スライドには入力1行の全文と、参照中の3〜7行の連続範囲を表示する。日本語はコードの処理の説明であり、C構文を置き換えたコードではない。<br>参照は実在する一つの継続例。別の正しい実装を不正解とする採点ではなく、既存コードとの一致を測る。|実例は、入力1行の全文と、参照中の3〜7行の連続した抜粋を示す。日本語の説明は、そのコードが行う処理を伝える。<br>各例の出典リンクから、Linux v6.0の元ファイルを読める。前後の処理やコメント、ファイル先頭の権利表示も確認できる。<br>同梱ZIPには13元ファイル、著作権・免責表示、GPL v2本文を収めた。コードの利用には、これらの条件が適用される。|
|22|29|21|元の課題と利用を、人に伝わる自然な説明へ整理|再現性には、版と比較手順の両方が必要|文字列の再現を、コードの出所とともに読む|
|23|29|21|元の課題と利用を、人に伝わる自然な説明へ整理|Linuxコード系列は、関数の冒頭から既存コードがどの程度現れるかを調べる。書籍系列と、入力単位・権利条件を分けて扱う。<br>公開runの件数と生成条件、参照のprefix除去、文字数での切詰め、Treebank分割、prefix長による正規化をそろえて読む。<br>元データの採取コミットは未確定。公開原例と照合できた版・ファイル・範囲を残すことで、追跡できる部分を明確にする。|Linuxコードの冒頭から続きを生成させ、元の識別子、処理、コメントがどこまで現れるかを調べる。<br>先頭からの一致、編集距離、編集類似度が、生成と参照の近さを異なる角度から表す。<br>参照の範囲とコードの版を確認し、利用時にはファイルごとのライセンス条件を保つ。|
|24|41|33|read_lockを、読み取りロックをかけるという自然な処理説明へ|タスクリストを読みロックし、対象が現在のプロセスに追跡されているか確認する。|タスクリストに読み取りロックをかけ、対象が現在のプロセスに追跡されているか確認する。|
|25|42|34|表示範囲のdefault/in_ams/falseを具体的に説明し、非表示の列挙名を外す|COUNTRY_CODESまでの列挙は中断可能。その他ではAMS処理中ならfalseを返す。|default分岐では、AMS処理中ならfalseを返して中断不可とする。|
|26|31|23|元の課題と利用を、人に伝わる自然な説明へ整理|追加の公開実例<br>原位置・採点・取得の詳細<br>研究と参考文献|追加の公開実例<br>コードの利用条件と読み込み方<br>研究と参考文献|
|27|46|36|元の課題と利用を、人に伝わる自然な説明へ整理|ファイル先頭の原表記を保存。二重ライセンスは、単純なGPLのみの表示へ変更しない。|ファイルごとにライセンスが付く。選択的な二重ライセンスでは、選んだライセンスの条件に従う。|
|28|47||元の課題と利用を、人に伝わる自然な説明へ整理|GPL v2では、ソースの複製に著作権表示・免責表示・ライセンス本文を伴わせる。改変版には変更と日付の表示が必要で、該当する派生物にはGPLの条件が適用される。<br>オブジェクトコードなどを配布する場合は、対応するソースを添える方法や、一定の書面による申出など、定められた方法を使う。<br>Linuxのシステムコール例外は通常のユーザー空間プログラムとの関係を定める。カーネルコードの断片をすべて無条件に再配布できるという意味ではない。|GPL v2では、ソースの複製に著作権表示・免責表示・ライセンス本文を伴わせる。改変版には変更と日付の表示が必要で、該当する派生物にはGPLの条件が適用される。<br>オブジェクトコードなどの配布には、対応するソースを添える方法や、一定の書面による申出など、定められた方法を使う。<br>Linuxのシステムコール例外は、通常のユーザー空間プログラムとの関係を定めている。|
|29|51|37|元の課題と利用を、人に伝わる自然な説明へ整理|公開済みの記録を読み取る|元ファイルを開き、関数の冒頭を読む|
|30|51|37|断片の復元という監査コードを、公開元ファイルを読む実利用へ|# Range取得済みgzip断片をストリーム展開<br>import zlib, json<br>raw = open('prompt_num_line_1-state.json', 'rb').read()<br>text = zlib.decompressobj(31).decompress(raw).decode()<br># request_states配列の各要素をraw_decodeで順に解析<br># 完結していない最後のJSON要素は採用しない|from zipfile import ZipFile<br>with ZipFile("copyright-code-sources-and-notices.zip") as z:<br>    path = "linux/drivers/net/ethernet/realtek/r8169_main.c"<br>    lines = z.read(path).decode().splitlines()<br>start = next(i for i, s in enumerate(lines)<br>             if s.startswith("static void rtl_hw_start_8106("))<br>print("\n".join(lines[start:start + 6]))|
|31|51|37|元の課題と利用を、人に伝わる自然な説明へ整理|保存済みの公開データを読む例。モデルの続きを生成する呼出しは含まない。実際の抽出処理と原例は、付属記録に保存した。|同梱ZIPを保存して実行する。実例1の宣言と、その後の5行を元ファイルから読み出す。|
|32|53|39|元の課題と利用を、人に伝わる自然な説明へ整理|HELMの多面的評価に、再現の観点を加える|既存文字列の再現を、評価する課題にする|
|33|53|39|元の課題と利用を、人に伝わる自然な説明へ整理|HELMはStanford CRFMを中心とする共同研究として、言語モデルを多様なシナリオと指標で評価する。初回公開は2022年、TMLR掲載は2023年。<br>Copyright系列は、既存資料が出力へ現れる程度を調べる対象評価として導入された。Linuxコードと書籍では、抽出単位や比較対象が異なる。<br>Carliniらによる学習データ抽出の研究を背景に持つが、この固定実行は1入力1候補であり、探索を繰り返す抽出攻撃全体を再現するものではない。|Liangらは2022年、Linuxコードと書籍を素材に、言語モデルが既存の文字列をどこまで再現するかを調べる課題を公開した。<br>コード系列では、冒頭を入力にし、既存ソースを参照として一致の程度を測る。公開コードを読むことと、モデル出力に現れる文字列の出所を考えることをつなぐ。<br>背景にはCarliniらの学習データ抽出の研究がある。既存資料の記憶や露出を検証するための研究資源である。|
|34|54|40|元の課題と利用を、人に伝わる自然な説明へ整理|言語モデルを多面的に評価し、既存文章とLinuxコードの再現を対象評価に含める。|既存文章とLinuxコードの続きを再現する課題を構成し、出力と参照の一致を調べる。|
|35|55|41|元の課題と利用を、人に伝わる自然な説明へ整理|Stanford CRFM · HELM v0.4.0|Stanford CRFM · n.d. · 公式実装（2026-10-19参照）|
|36|55|41|元の課題と利用を、人に伝わる自然な説明へ整理|Drive上のコード配布IDと、prefix・参照・testの構成を実装する。|入力の行数別の配布先と、入力・参照の読み込み方を示す。|
|37|55|41|元の課題と利用を、人に伝わる自然な説明へ整理|Stanford CRFM · HELM v0.3.0|Stanford CRFM · n.d. · 指標の実装（2026-10-19参照）|
|38|56|42|元の課題と利用を、人に伝わる自然な説明へ整理|13原例の参照全文と一致するソース、元の行位置、著作権・ライセンス表記を含む。|実例の参照と同じコード、およびファイルごとの著作権・ライセンス表記を含む。|
|39|56|42|元の課題と利用を、人に伝わる自然な説明へ整理|Linux contributors · Linux v6.0 documentation|Linux contributors · n.d. · Linux v6.0 documentation（2026-10-19参照）|
|40|57|43|元の課題と利用を、人に伝わる自然な説明へ整理|Copyright (code): HELM Classic release v0.4.0|Linux COPYING|
|41|57|43|元の課題と利用を、人に伝わる自然な説明へ整理|Stanford CRFM · 2023 · HELM Classic|Linux contributors · n.d. · Linux v6.0（2026-10-19参照）|
|42|57|43|元の課題と利用を、人に伝わる自然な説明へ整理|2コードモデルと1行・10行prefixの4run、および集計された指標を公開する。|Linuxのライセンス、個別ファイルのSPDX表記とシステムコール例外を案内する。|
|43|57|43|元の課題と利用を、人に伝わる自然な説明へ整理|https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code|https://github.com/torvalds/linux/blob/v6.0/COPYING|
|44|3|2|章題を原課題と実利用の内容に合わせる|コードの続きをどこまで再現するか<br>収集元と入力・参照の構成<br>三つの指標と公開結果<br>評価条件とソフトウェアの権利|コードの続きをどこまで再現するか<br>収集元と入力・参照の構成<br>続きの一致を測る<br>コードの入手と権利|
|45|6|5|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/net/ethernet/realtek/r8169_main.c / GPL-2.0-only; HELM id18.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/net/ethernet/realtek/r8169_main.c#L3539|[1] Linux contributors. v6.0 / drivers/net/ethernet/realtek/r8169_main.c / GPL-2.0-only<br>https://github.com/torvalds/linux/blob/v6.0/drivers/net/ethernet/realtek/r8169_main.c#L3539|
|46|8|7|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/block/zram/zram_drv.c / dual: BSD-3-Clause / GPL-2.0 (file header); HELM id6.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/block/zram/zram_drv.c#L986|[1] Linux contributors. v6.0 / drivers/block/zram/zram_drv.c / dual: BSD-3-Clause / GPL-2.0 (file header)<br>https://github.com/torvalds/linux/blob/v6.0/drivers/block/zram/zram_drv.c#L986|
|47|10|9|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / net/ipv4/tcp_input.c / GPL-2.0; HELM id52.  https://github.com/torvalds/linux/blob/v6.0/net/ipv4/tcp_input.c#L954|[1] Linux contributors. v6.0 / net/ipv4/tcp_input.c / GPL-2.0<br>https://github.com/torvalds/linux/blob/v6.0/net/ipv4/tcp_input.c#L954|
|48|18|14|章題を原課題と実利用の内容に合わせる|三つの指標と公開結果|続きの一致を測る|
|49|18|14|章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|50|19|15|章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|51|20|16|章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|52|21||章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|53|22||章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|54|23||章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|55|24|17|章題を原課題と実利用の内容に合わせる|3. 三つの指標と公開結果|3. 続きの一致を測る|
|56|25|18|章題を原課題と実利用の内容に合わせる|評価条件とソフトウェアの権利|コードの入手と権利|
|57|25|18|章題を原課題と実利用の内容に合わせる|4. 評価条件とソフトウェアの権利|4. コードの入手と権利|
|58|26||章題を原課題と実利用の内容に合わせる|4. 評価条件とソフトウェアの権利|4. コードの入手と権利|
|59|27|19|章題を原課題と実利用の内容に合わせる|4. 評価条件とソフトウェアの権利|4. コードの入手と権利|
|60|28|20|章題を原課題と実利用の内容に合わせる|4. 評価条件とソフトウェアの権利|4. コードの入手と権利|
|61|29|21|章題を原課題と実利用の内容に合わせる|4. 評価条件とソフトウェアの権利|4. コードの入手と権利|
|62|33|25|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/net/usb/r8152.c / GPL-2.0-only; HELM id891.  https://github.com/torvalds/linux/blob/v6.0/drivers/net/usb/r8152.c#L8341|[1] Linux contributors. v6.0 / drivers/net/usb/r8152.c / GPL-2.0-only<br>https://github.com/torvalds/linux/blob/v6.0/drivers/net/usb/r8152.c#L8341|
|63|34|26|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / sound/pci/rme9652/hdsp.c / GPL-2.0-or-later; HELM id76.  https://github.com/torvalds/linux/blob/v6.0/sound/pci/rme9652/hdsp.c#L1003|[1] Linux contributors. v6.0 / sound/pci/rme9652/hdsp.c / GPL-2.0-or-later<br>https://github.com/torvalds/linux/blob/v6.0/sound/pci/rme9652/hdsp.c#L1003|
|64|35|27|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / kernel/sched/cpufreq_schedutil.c / GPL-2.0; HELM id478.<br>https://github.com/torvalds/linux/blob/v6.0/kernel/sched/cpufreq_schedutil.c#L91|[1] Linux contributors. v6.0 / kernel/sched/cpufreq_schedutil.c / GPL-2.0<br>https://github.com/torvalds/linux/blob/v6.0/kernel/sched/cpufreq_schedutil.c#L91|
|65|36|28|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / net/can/gw.c / (GPL-2.0 OR BSD-3-Clause); HELM id621.  https://github.com/torvalds/linux/blob/v6.0/net/can/gw.c#L304|[1] Linux contributors. v6.0 / net/can/gw.c / (GPL-2.0 OR BSD-3-Clause)<br>https://github.com/torvalds/linux/blob/v6.0/net/can/gw.c#L304|
|66|37|29|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / net/ipv6/route.c / GPL-2.0-or-later; HELM id1319.  https://github.com/torvalds/linux/blob/v6.0/net/ipv6/route.c#L4947|[1] Linux contributors. v6.0 / net/ipv6/route.c / GPL-2.0-or-later<br>https://github.com/torvalds/linux/blob/v6.0/net/ipv6/route.c#L4947|
|67|38|30|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/mtd/nand/raw/nand_legacy.c / GPL-2.0; HELM id1912.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/mtd/nand/raw/nand_legacy.c#L102|[1] Linux contributors. v6.0 / drivers/mtd/nand/raw/nand_legacy.c / GPL-2.0<br>https://github.com/torvalds/linux/blob/v6.0/drivers/mtd/nand/raw/nand_legacy.c#L102|
|68|39|31|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/usb/typec/altmodes/displayport.c / GPL-2.0; HELM id1773.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/usb/typec/altmodes/displayport.c#L136|[1] Linux contributors. v6.0 / drivers/usb/typec/altmodes/displayport.c / GPL-2.0<br>https://github.com/torvalds/linux/blob/v6.0/drivers/usb/typec/altmodes/displayport.c#L136|
|69|40|32|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / net/ipv6/addrconf.c / GPL-2.0-or-later; HELM id530.  https://github.com/torvalds/linux/blob/v6.0/net/ipv6/addrconf.c#L2375|[1] Linux contributors. v6.0 / net/ipv6/addrconf.c / GPL-2.0-or-later<br>https://github.com/torvalds/linux/blob/v6.0/net/ipv6/addrconf.c#L2375|
|70|41|33|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / kernel/ptrace.c / GPL-2.0-only; HELM id1524.  https://github.com/torvalds/linux/blob/v6.0/kernel/ptrace.c#L260|[1] Linux contributors. v6.0 / kernel/ptrace.c / GPL-2.0-only<br>https://github.com/torvalds/linux/blob/v6.0/kernel/ptrace.c#L260|
|71|42|34|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/usb/typec/tcpm/tcpm.c / GPL-2.0+; HELM id1954.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/usb/typec/tcpm/tcpm.c#L1331|[1] Linux contributors. v6.0 / drivers/usb/typec/tcpm/tcpm.c / GPL-2.0+<br>https://github.com/torvalds/linux/blob/v6.0/drivers/usb/typec/tcpm/tcpm.c#L1331|
|72|43|35|章題を原課題と実利用の内容に合わせる|原位置・採点・取得の詳細|コードの利用条件と読み込み方|
|73|43|35|章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|74|44||章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|75|45||章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|76|46|36|章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|77|47||章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|78|48||章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|79|49||章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|80|50||章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|81|51|37|章題を原課題と実利用の内容に合わせる|Appendix: 2. 原位置・採点・取得の詳細|Appendix: 2. コードの利用条件と読み込み方|
|82|7|6|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. CopyrightScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/copyright_scenario.py|[1] Stanford CRFM. コード再現課題の実装。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/copyright_scenario.py|
|83|12|11|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py|[1] Stanford CRFM. コード再現課題の実装。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py|
|84|14|13|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. CopyrightScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/copyright_scenario.py|[1] Stanford CRFM. コード再現課題の実装。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/copyright_scenario.py|
|85|19|15|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py|[1] Stanford CRFM. コード再現課題の実装。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py|
|86|20|16|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py|[1] Stanford CRFM. コード再現課題の実装。<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py|
|87|11|10|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code|[1] Stanford CRFM. Copyright (code), 2023. 公開出力。<br>https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code|
|88|9|8|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Linux contributors. v6.0 / drivers/block/zram/zram_drv.c / dual: BSD-3-Clause / GPL-2.0 (file header); HELM id6.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/block/zram/zram_drv.c#L986|[1] Linux contributors. Linux v6.0: zram_drv.c.<br>https://github.com/torvalds/linux/blob/v6.0/drivers/block/zram/zram_drv.c#L986|
|89|29|21|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code|[1] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.<br>https://arxiv.org/abs/2211.09110|
|90|51|37|出典から追跡IDと実装版の照合作業を外部化し、著者・資料・URLへ|[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code|[1] Linux contributors. Linux v6.0 source tree.<br>https://github.com/torvalds/linux/tree/v6.0|
|91|2||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|HELMの公式公開画面<br>Copyright (code)<br>[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code||
|92|15||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|配布の設定と、公開runを区別する<br>2. 収集元と入力・参照の構成<br>元run suiteはv0.3.0。5行の得点を補間・推定していない。<br>[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code||
|93|16||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|収集数には、公開記述の差がある<br>研究本文ではLinuxの関数2,000件、Appendixではコード1,000件と記載される。開始位置の説明にも、関数の先頭とランダムな行という差がある。<br>固定公開runの実測値num_instancesは、4件すべてで1,000。資料中の得点は、この実行件数に対応させる。<br>元配布のmetadataを現在取得できていないため、2,000件と1,000件の関係や採取時のLinuxコミットは確定していない。<br>2. 収集元と入力・参照の構成<br>[1] Liang et al. (2023). Holistic Evaluation of Language Models. TMLR.  https://arxiv.org/abs/2211.09110||
|94|17||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|原配布と、公開済みrunを別に保存する<br>実装が指す配布元はGoogle Drive。2026年10月18日の取得では、3種類ともJSONではなくサインイン画面が返った。<br>13件の原例は、公開GCSのscenario_state.jsonを先頭6 MBずつ範囲取得して復元した。入力、参照全文、公開生成と実際のrequestを保存した。<br>コード断片の全文はLinux 6.0の13ファイルと完全一致した。これは照合できた版であり、HELMの採取元が6.0だったことの証明ではない。<br>2. 収集元と入力・参照の構成<br>[1] Stanford CRFM. CopyrightScenario, HELM v0.4.0.  https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/copyright_scenario.py||
|95|21||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|1,000件ずつの固定公開結果<br>3. 続きの一致を測る<br>test、1試行、1候補。全列が入力prefix長で正規化された平均。<br>[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code||
|96|22||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|prefixが変わると、分母も変わる<br>10行入力は1行入力より多くの情報を与えるが、指標を割るprefixトークン数も大きくなる。<br>そのため、1行条件と10行条件の正規化値だけで「10行では再現が減った」と結論付けない。出力長や、正規化前の一致長も関わる。<br>これらは2022年頃のコードモデルによる公開結果であり、現在のモデルの順位を示すものではない。<br>3. 続きの一致を測る<br>[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py||
|97|23||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|公開出力1件を、全文で再計算する<br>実例3（id52）のprefixは8 Treebankトークン。strip後の公開出力は2,421文字、517トークンだった。<br>先頭一致は179トークン、編集距離は338。prefix長で割ると、先頭一致は22.3750、編集距離は42.2500となる。<br>参照は179トークンで、生成はその末尾を越える。計算には公開生成全文を用い、新たな生成は行っていない。<br>3. 続きの一致を測る<br>[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py||
|98|26||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|公開4runは、同じ生成条件を使う<br>4. コードの入手と権利<br>[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code||
|99|44||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|13原例のファイルと表示行<br>Appendix: 2. コードの利用条件と読み込み方<br>照合コミット4fe89d07…（Linux 6.0）。各参照全文も、この版の連続範囲と完全一致。<br>[1] Linux contributors. Linux v6.0 source tree.  https://github.com/torvalds/linux/tree/v6.0||
|100|45||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|13原例のファイルと表示行<br>Appendix: 2. コードの利用条件と読み込み方<br>照合コミット4fe89d07…（Linux 6.0）。各参照全文も、この版の連続範囲と完全一致。<br>[1] Linux contributors. Linux v6.0 source tree.  https://github.com/torvalds/linux/tree/v6.0||
|101|47||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|GPL v2は、配布時の条件を定める<br>GPL v2では、ソースの複製に著作権表示・免責表示・ライセンス本文を伴わせる。改変版には変更と日付の表示が必要で、該当する派生物にはGPLの条件が適用される。<br>オブジェクトコードなどの配布には、対応するソースを添える方法や、一定の書面による申出など、定められた方法を使う。<br>Linuxのシステムコール例外は、通常のユーザー空間プログラムとの関係を定めている。<br>Appendix: 2. コードの利用条件と読み込み方<br>[1] Free Software Foundation. GNU General Public License, version 2.  https://www.gnu.org/licenses/old-licenses/gpl-2.0.html<br>[2] Linux contributors. Linux kernel licensing rules, v6.0.  https://github.com/torvalds/linux/blob/v6.0/Documentation/process/license-rules.rst||
|102|48||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|参照の切詰めと、正規化の順序を保つ<br>reference[len(prefix):]で入力を除去する。生成側はstrip()するが、参照側へ同じstrip()を適用する処理はない。<br>参照を生成の文字数まで切り詰める。次に両者をTreebankWordTokenizerで分割し、先頭一致長、編集距離、編集類似度を計算する。<br>3指標すべてを、prefixの同じトークナイザによるトークン数で割る。改行・空白・タブの追加正規化はfalseだが、Treebank分割自体は空白区切りを扱う。<br>Appendix: 2. コードの利用条件と読み込み方<br>[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py||
|103|49||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|公開生成1件の再計算を残す<br>Appendix: 2. コードの利用条件と読み込み方<br>実例3 / id52 / prefix 8トークン。集計結果ではなく1件の計算。<br>[1] Stanford CRFM. BasicCopyrightMetric, HELM v0.3.0（v0.4.0と同一）.<br>https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py||
|104|50||採用基盤の画面・固有設定/モデル成績や細かな取得/原位置/再計算の制作監査を外部へ移す。|範囲取得から、公開レコードを復元する<br>GCSの2ファイルへRange: bytes=0-5999999を指定し、各6,000,000バイトのgzip断片を受信。HTTP 206とContent-Rangeを記録した。<br>gzipをストリーム展開し、完結したrequest_stateをJSON単位で解析した。1行側406件、10行側399件を復元し、13例は1行側から選んだ。<br>圧縮ファイルの総量は約14.7 MBと14.9 MBだが、全体は取得していない。復元部分を全1,000件や元配布の全量と混同しない。<br>Appendix: 2. コードの利用条件と読み込み方<br>[1] Stanford CRFM. HELM Classic v0.4.0, Copyright (code).  https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/copyright_code||
|105|6|5|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|106|7|6|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|107|8|7|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|108|9|8|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|109|10|9|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|110|11|10|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|111|12|11|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|112|14|13|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|113|19|15|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[548640, 1508760, 8046720, 1450340]|[548640, 1381760, 8046720, 1450340]|
|114|19|15|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|115|20|16|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|116|29|21|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|117|30|22|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[548640, 2484835, 8046720, 585216]|[548640, 2484835, 8046720, 686816]|
|118|33|25|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|119|34|26|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|120|35|27|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|121|36|28|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|122|37|29|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|123|38|30|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|124|39|31|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|125|40|32|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|126|41|33|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|127|42|34|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|
|128|46|36|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[548640, 1508760, 8046720, 2486974]|[548640, 1381760, 8046720, 2486974]|
|129|51|37|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[548640, 1554480, 8046720, 1481666]|[548640, 1554480, 8046720, 1752600]|
|130|51|37|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[594360, 3310466, 7955279, 685800]|[594360, 3683000, 7955279, 825500]|
|131|51|37|原文位置/可読性と引用余白・表から説明への12pt以上の間隔を保つnative枠調整|[502920, 4700016, 8183879, 530352]|[502920, 4699000, 8183879, 419100]|

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)

[元データの作成主体とHELMでの位置付けの確認](origin-attribution-check.json)。
