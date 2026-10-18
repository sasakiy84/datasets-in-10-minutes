# ChID — 調査・根拠・制作範囲

制作 sasakiy84。対象はChID（2019年）の原論文版を中心とした個別資料。ChID-Adapt/CLUEの共有候補版、FewCLUE、CLEVAの採用例を同一の入力形式・評価集合として扱わない。メインrepo/Git・他担当dirは編集していない。

## 正式資料・公開元・固定版

Chujie Zheng, Minlie Huang, Aixin Sun (2019), **ChID: A Large-scale Chinese IDiom Dataset for Cloze Test**, Proceedings of ACL 2019, pp.778–787。公式ACL HTML/PDFを取得、10頁の本文・図・統計・結果・注釈条件を読解。発表年2019は正式刊行に直接根拠がある。原題のIDの大文字を保持。dataset正式展開は公式CLUE配布等のChinese IDiom Dataset for Cloze Testを表紙へ併記。

公式作者repo https://github.com/chujiezheng/ChID-Dataset 、固定commit `0836ebf72cbe7d2da832021b02ff08f627de885d`。README/Competition README/LICENSE/Resource/DataManager/judgeの全6ファイルのGit blobをローカルbytesから再計算し、固定ツリーに一致（source-version-audit.json）。READMEは原論文版とコンテスト版を明確に分け、作者・年・引用・各HuggingFace配布へのリンクを示す。

原論文版の取得元は作者が直接案内する https://huggingface.co/datasets/thu-coai/chid/tree/main/original 。固定HF commit `47ad8022d369233bea2f4a8112268f9a9a039a43`。全6ファイル（Train/Dev/Test/Ran/Sim/Out）を実取得し、fixed HF treeと元treeが完全一致、全6のbytes/LFS SHA256が取得bytesに完全一致。original trainは365,990,297 bytes。fetch-data-log.jsonとstats.jsonに全URL/bytes/SHA、fix_sources.pyに固定版との対応を保存。main URLで取得したものを、固定版のLFS hashへ照合したという方法を保つ。

別に公式CLUE GCS `chid_public.zip` を取得し、全8メンバーを保存ZIPから検算。作者案内HF competitionのdev.txt/dev_answer.csvも取得し、CLUE devのbytesと全正解対応が一致。FewCLUE固定commit `62a02c6f31cf32814cfe522f78ef088228840f8d` のChID全15ファイルを取得し全Gitblob一致（audit_fewclue.py）。すべて通常TLS・継承proxy使用、外部生成/model APIなし。

初期/追加/データ/別版/FewCLUE取得のURL/status/bytes/SHAは専有fetch-*-log.json。公式repoはChromiumでCSS/フォントが反映された画面を実描画・viewしofficial-site.pngへ。親の旧接続結果だけを根拠に代替へ固定せず、今回は作者repoへ直接到達した。

## 原版の課題と構築

一つの文章contentに、一つ以上の`#idiom#`を置く。各空欄に異なる七候補の配列があり、groundTruthの成語文字列を選ぶ。realCountは空欄数、groundTruth/candidates配列は空欄の登場順。問題ID欄は原版にない。後の共有候補版のルールを原版へ適用しない。

辞典23K超の成語から四字を残し、事前学習ベクトルのない語（約40%）を除く。同意味で一字/語順だけが異なる表記は辞典の又作/犹/同/见等を使って正規化。出現20回未満を除き3,848種類。候補の選別は成語ベクトルのコサイン類似度。正解との類似度が0.7より高い語を除き、残りの上位10語から無作為に三語、上位10語以外から三語を選び、正解と合わせて七択とする。目的は同義語を避け、近義語の使い分けを測ること。全候補が意味上絶対に一意だという保証には置換していない。

ニュース素材はTHUCNews、Web上の小説・エッセイも収集。段落単位、引用符内の成語は空欄化しない方針、100文字未満は次段落と結合、600文字超は除く。頻出成語だけを含む一部文章を削減。実配布には非常に短い行も残るため、現全レコードが最低100文字だとは述べない。

候補類似度と意味関係の調査は0.5〜0.9の8区間×各200対=1,600対を5人でSYN/NEAR/OTHERへ分類。別の近義語頻度調査は200成語×20対、4人、Fleiss kappa .479。原論文の後者の表に「4以上」40/200と23.0%の数値不整合があるため、その23%を独自に直して転載せず、本資料は前者の設計調査を説明する。検証なしに全注釈人数を同一工程へ足し合わせない。

## 原版の全件検算

全6配布ファイルをstream解析。原版の独立した分割は次の四つ：

- Train 520,711文章、648,920空欄、正解に3,848成語。
- Dev 20,000文章、24,822空欄、正解に3,458成語。
- Test 20,000文章、24,948空欄、正解に3,502成語。
- Out 20,096文章、30,023空欄、正解に3,626成語。

計580,807文章・728,713空欄、原論文と一致。Ran/SimはTestと同じ順序のcontent/groundTruthに異なる七候補を付けたもので、文章数の水増しに足さない。全行のrealCount/空欄記号数/候補集合数/正解数が一致、全空欄に7個の一意候補、正解文字列が一度だけ含まれる。新しいモデル出力は作っていない。

Trainの異なるcontentは519,218、Dev19,997、Test20,000、Out20,085。表記どおりの共通contentはTrain/Dev106、Train/Test110、Train/Out1,829、Dev/Test1、Dev/Out60、Test/Out85。候補まで同じ質問数とは呼ばない。領域内（ニュース・小説）/領域外（エッセイ）の設計を、全文の完全非重複や未知作品保証とは言い換えない。原版Dev18295行のcontentは`#idiom#`のみで、文字列最短7。全長はUnicode文字数であり、原論文のJieba分かち書きの平均99/127語と直接比較しない。

stats.jsonは全rows/blanks/single/multi/unique content/unique answer/正解位置分布/文字数/bytes/hash。data-audit.jsonは全6 SHA、整合、Test/Ran/Sim同じ順序・正解、全15組のcontent共有を保持。

## 13独立実例・訳・表示

原論文版11問と、後のFewCLUE版2問（CLEVA紙面とHELM docstringに対応）。本編3問＋追加10問、異なるcontent13種類、空欄は計15。二空欄の例10と13は別々の七候補を持つ。一つの問題を言語で分けても独立件数に加えない。

原版：Dev9276/903/1046/3707、Test231/239/249/380、Out4288/3060/1900。FewCLUE：train_2.json20行(id621、all128行)、train_3.json21行(id42、all33行)。原版にはIDなしをnullのまま保存、ファイル/1起算行/SHA/byte offsetで同定。FewCLUEのidは元値を保持し、集合をまたぐグローバルIDとは仮定しない。examples.jsonに原行（改行込み）/全ファイルSHA/原行SHA/正準JSON SHA、固定URL、原票、全候補順、正解文字列・位置・A〜G、日本語全文と各候補の意味を保持。

原版contentの全文を保持し、原文書全体やWeb記事全体とは呼ばない。FewCLUE行の末尾`...`は元配布にある記号で、本資料が訳を入れるために原文を削ったものではない。固有名の元表記、原候補の「监主自盗」等は勝手に標準化せず保持。JPは新しい意味訳で、字面の直訳と成語の比喩を区別し、既存日本語訳を引用しない。作品・著者が元票にない場合は推測しない（会話例のハ/オを既知作品の登場人物へ断定しない）。

初期訳を日本語スキルで実修正：伤病をけが/体調不良の両方に、告慰を単なる報告から慰める意味へ、却の対比、这件事を職業上の仕事に限定しない等。draft-proofreading-changes.jsonに実際の8対、最終頁へ対応させる。

レイアウト：15ptで13問×3組の不均等2列を39頁実PDF化しcoexist-*へ保存。長い問題と二空欄は回答/出典領域を超えた。代表的な6頁を個別viewした（全39頁を見たとは記録しない）。次に質問CN/JPを上下にし、候補CN/JPを二列で対照する13頁を実描画・全13頁view。例7は3候補/4候補へ列の切り分けを変え、修正後も実view。この形で11問が同居できる（stacked-results.json）。二空欄×七候補の例10/13は同居不可のため、原文全体を一枚にまとめ、訳を別頁にした。訳のために原文を分割していない。正解は21pt bold #B13731。

## 2019年の評価条件と値

指標は空欄単位のAccuracy。文章全空欄をすべて正しく選ぶ割合とは異なる。七候補の一様無作為選択の期待値1/7=14.2857%は理論値で、実行したモデルの得点ではない。

原論文のLM/AR/SAR報告値（Dev/Test/Ran/Sim/Out）を引用：
LM71.8/71.5/80.7/65.6/61.5、AR72.7/72.4/82.0/66.2/62.9、SAR71.7/71.5/80.0/64.9/61.7。ARで成語全体72.4、文字平均63.8、文字合成MLP66.5（Test）。グラフはARとHumanのTest/Ran/Sim/Outをnativeで表示する。

人間はTest/Ran/Sim/Outの各200文章、計800文章を、大学1/2年の3人が解く。報告は各人正解率の平均で、OCNLI等の多数決へ読み替えない。Human87.1/97.6/82.2/86.2、kappa .794/.953/.791/.769。モデルは各集合全空欄、人間は抽出文章という範囲を保つ。原論文の14.6ポイントという本文の差は丸め値87.1−72.4=14.7とずれるため、本資料は独自の差の数値を付加しない。

モデル設定：Jieba、100K単語語彙、200次元事前学習ベクトル、未知ベクトルuniform(-.1,.1)、単語dropout .5、RNN隠れ100、Adam学習率.001、勾配clip5、batch32、Devで1epoch改善なしに停止。試行数や標準偏差が確認できない値を、3回平均や単一seed等と断定しない。2019年の評価であり2026年の最新性能表ではない。モデル再実行なし。

## 共有候補のChID-Adapt / CLUE

コンテストREADMEの原版との差は、複数文章が十候補を共有し、文章間の意味比較や消去を利用できる形式。元の各空欄に別々の七候補という形式とは異なる。未確認の「同じ候補の再利用禁止」や全群での一対一割当を、単に十候補であることから推測しない。

公式CLUE ZIP検算：Train84,709群/461,242文章/577,157空欄、Dev3,218群/18,644文章/23,011空欄、旧Test1.0 3,231群/18,725文章/23,209空欄、新Test1.1 3,447群/34,470文章/34,470空欄。全群十候補、空欄ID一意。train_answer.json577157/dev_answer.json23011の全ID・0〜9候補範囲を照合。両testに正解は同ZIPにない。READMEは1.1新test追加、train/dev不変を説明する。日時が記載されないREADMEへ独自の更新日を付けない。

CLUE devの入力は作者案内HF competition/dev.txtとbytes完全一致。dev_answer.jsonと作者案内CSVの全ID/正解値も一致。作者judge.pyは空欄IDごとの正解率で、予測辞書に答えを集める。CLUE群数の3,218を「空欄3,218問」と呼ばない。全CLUE原レコード/予測を公開用にコピーする意図はない。

## FewCLUE / CLEVA / HELM

FewCLUE全15ファイルは各train/dev小集合42問（7正解位置×6）、五組の質問集合の和は各202種類でall202と一致。小集合の行を重複込みで連結した210ではない。test_public2002=各位置286、test2000/unlabeled7585はanswerなし。全問一空欄・一意7候補、正解整数0〜6（範囲/型一致）、非欠損ラベル競合0。ファイル全件とGitblobが一致。

CLEVA正式2023論文 **CLEVA: Chinese Language Models EVAluation Platform** は文化知識にChIDを採用しAccuracyで評価。紙面の「不过，要想变得…」例はFewCLUE train_2L20/allL128と文字内容が対応（全角/半角句読点と空欄表記の変換あり）。紙面A足智多谋/B语无伦次/C绣花枕头は配布の0/4/5番で、三候補の掲載。配布七候補を紙面三候補と同一にしない。

HELM v040 CLEVACulturalKnowledgeScenarioの映画『宋家王朝』例はFewCLUE train_3L21/allL33と本文/七候補/Target Dが一致。取得原論文版全6とCLUE ZIP全4本文を特徴語で検索したが、この二つのFewCLUE例への同一行対応は確認できていない。別の「宋家王朝」言及行（原train49539/CLUE train19002）は内容も正解も別で、文中の作品名だけで同一例としない。

HELM cultural_knowledge/idiom/v1設定はprompt_id0〜5。public Classic v040全8526 run_specsにCLEVA0。six設定は元コーパス六種類や実行六件ではない。Converterのchoices列挙とlabel index→correct tag、外部templates/infer_params読込を照合。全採用集合/全テンプレート/実推論値は未取得で、得点・max_tokens/提示例数を補完していない。v040コード/設定、CLEVA/FewCLUE/CLUE論文は自分の先行BUSTM/独立CLUEWSC調査の一次取得bytesを専有へコピー（再GETと偽らない）。IPの公式ZIP取得制約は先行で正常TLSの証明書名不一致を確認、今回の課題用URLについても確認ログを残す。

## 権利・公開範囲

固定作者repoにはApache License2.0がありGitHub表示も一致する。READMEはChID論文の引用を求める。コードのライセンスが元のニュース/小説/エッセイの個別作品の権利を一律に置き換えるとは述べない。各原票に作品名・作者のメタデータ欄はなく、文中の人物名から著者・作品を推測しない。13短い提供例へ出典と新規意味訳を添える。全original txt/CLUE ZIP/FewCLUE全json/PDF/HTML/試験作業物はローカル調査証跡で、公開ギャラリー向けのデータ全量再配布にはしない。

## 制作・校正・最終検査

3skills継続、method/review_mode=skill_based_codex、gemini_used=false。全58頁（本編30頁）を1頁ずつ実際に拡大viewし、overviewも確認した。最終変更の実例15頁・工程図p11・コードp50は再view。全頁最終文言と日本語校正をpage-review.json、実際の16修正対をproofreading-changes.json、原行・正解・意味訳をexamples.jsonへ記録。作業中の短い本文折返しだけを理由とする短縮や強制改行は行わない。最終hashはhandoff.json/visual-review.jsonに記録する。

原CN全文・全候補・正解は各問題1頁を維持した。15pt不均等2列を39頁実描画・文字境界測定し、うち6頁を個別view（全39頁を目視したとはしない）。次に全文幅のCN/JPと二列候補へ組み直した13頁を全個別viewし、単一空欄11問は15pt同居が成立した。複数空欄2問だけは全原CN1頁と全JP1頁へ分けた。stacked-results.json/stacked-pages、coexist-results.json/probe-pagesとvisual-review.jsonへ試験範囲を保存。

最終native11表・1グラフ・1工程図、正解15頁を21pt bold #B13731。字形境界と実画素による47枠の上下余白を調整し、最終行と下枠、正解と出典の間隔を確認した。446段落から工程図ラベル整理後444段落・135セルのlayout監査0、標準XSDの新規エラー0（マスター既存11件を分離）、notes0、native本文/セル全文のPDF保持、13原行の全ファイルSHA/行SHA/offset/候補順/ラベル一致。p50のnativeコードを原Devファイルで実行しpositions=[1]。p14は説明用日本語手順で実行コードとは扱わない。

URL62件はnativeのURL-only runとPDF矩形の文字中心が完全一致。4矩形の全字形bbox抽出は隣接行の字形境界にも接触するため、リンク中心で判定したことをlinks-audit.jsonへ明示。原グラフ8値、各種配布全件統計、正式論文の条件と結果は一次資料と照合し、モデル再実行はしていない。

HELM cultural_knowledge.zipのHTTP/HTTPSを通常TLSで再取得試行したが、IPと証明書の不一致で未取得。helm-audit.jsonへ実エラーを保持し、推論パラメータ・全原評価集合・実スコアを補完しない。FewCLUEのallは五つの小集合の質問和集合と一致し、各202種類であることもfewclue-audit.jsonへ記録。

nativeマスターPPTXから最終PDF。再現はbuild.py→convert.py chid→render.py chid→balance-ink.py→再convert/render→監査/records.py。共通engine/repo/Gitは変更せず専有コピーのみ。独立レビューはcreate_pileへ依頼する。

独立レビュー先行指摘によりp40 步步为营を「慎重に足場を固めながら進む」、p44 日落西山を「日が西に沈むように、衰えが進む」へ修正。原CN/候補順/原ラベルは保持。

p51の正解形式セルも「groundTruth：成語の配列」へ短文化し、表セルの末尾1字改行を解消。原データの文字列配列は変更しない。

独立レビューcreate_pile承認、未解決0。review-chid/review.json、全58頁と最終p40/44/51再確認、原6全件/CLUE/Few15/13例/版/数値/native/最終hashを独立照合。承認対象はPPTX b95550702ff9c8721e69e5062769eb049e56addb7eef1cd2dafae8d99e115d17、PDF b32450b22db0fdd54442884088bd937fd3b74014ace61da1f49528e3d90d0249。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/chid.json)、[実際の校正対](skill-proofreading/chid.md)、[全ページ文言](skill-proofreading/chid/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/chid/review.json)。
