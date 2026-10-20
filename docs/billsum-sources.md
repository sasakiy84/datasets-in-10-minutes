# BillSum 調査・制作記録

## 現在の実例表示（2026-10-20改訂）

更新タグ：source-coverage-2026-10。原文は本編18pt、補足17pt、訳は17pt。分割頁を通して選定範囲の全文を表示し、参照要約とその訳も全文を保持している。原文の文字・順序は変えず、組版の空白と改行を整えた。

| 実例 | 原文の範囲 | 原文頁 | 訳頁 |
|---|---|---|---|
| 1 | 法案本文の全文（2つの連続部分） | 7,8,9,10 | 11,12 |
| 2 | 第44253.4条(a)導入、(b)(1)、(f)を抜粋。間のサービス詳細・試験等を省略。 | 16,17,18 | 19,20 |
| 3 | 法案本文の全文。定義、免除、濫用防止・義務復活、規則制定を含む。 | 24,25,26,27,28,29,30 | 31,32 |
| 4 | 改正先と第14項向けの保証料免除・例外を抜粋。第16項・第34項にも同じ条件の改正が続く。 | 56,57 | 58 |
| 5 | 小麦への改正全文と、同じ採草・放牧規定を置く飼料穀物の改正先を抜粋。後者の反復条文を省略。 | 61,62,63 | 64 |
| 6 | 略称・地域表現の改正、39保護地の指定冒頭、ナバホ支援を抜粋。地区別の面積一覧と地図閲覧先を省略。 | 67,68,69 | 70,71 |
| 7 | 法案本文の全文。適用乗率・125%の条件・全国比・指数公表・地域定義・移行規定を含む。 | 74,75,76,77,78,79 | 80,81 |
| 8 | 法案本文の全文。定義・基準時点・算式・夏学期・未修了者・継続教育の算入条件を含む。 | 84,85,86,87,88,89 | 90,91 |
| 9 | 登録資格・電子提出・期限、技術的な語句修正を含む(a)(8)、施行条件(e)全文を抜粋。本人確認の詳細やIT手続の特例等を省略。 | 94,95,96 | 97,98 |
| 10 | 緊急保育施設の認可、35平方フィートの基準とオフィス内例外、児童日中保育施設の追加条文を抜粋。その他の運営条件を省略。 | 101,102,103 | 104,105 |
| 11 | 地域の精神保健基金の目的、対象者の定義、郡のサービス提供を抜粋。詳細な資格条件等を省略。 | 108,109 | 110,111 |
| 12 | 施設入所(b)・投薬(c)の条件、(d)(e)の例外と、弁護士を付ける手続(f)(1)を抜粋。宗教に関する代替治療と施設の除外も含め、審理や事後の調査手続等を省略。 | 114,115,116,117,118,119 | 120,121,122 |
| 13 | 方針策定(b)、無断利用禁止(b)(3)、保存期間(b)(5)(A)〜(C)、二種類のデータ定義(c)を抜粋。担当者・分類・保存先などの他規定を省略。 | 125,126,127,128 | 129,130,131 |

〔中略〕は、同じ法案内で引用しない条項が間にあることを表す。改頁だけの場合は原文・訳の続きを示す。

要約が補う背景には、実例1の行政機関名や参照先増額率の詳しい意味、実例4の制度名、実例6の改正前の指定との比較、実例8の補助金制度、実例10の行政機関・既存法、実例11の郡制度の背景、実例13の別条文にある録音禁止と警察官の例外がある。これらを表示した改正本文だけの直接記述と扱わない。

13件の原入力全文・参照全文・配布行と照合用hashはexamples-original.json、原配布Parquetの配布URLとSHA-256はraw-record-checks.json、実際の選定箇所・原文字位置・訳はsource-selections.json、各表示頁との対応はsource-pages.jsonに保存。参照事実の独立確認はskill-proofreading/billsum/source-coverage-2026-10/independent-review/reference-fact-coverage.jsonにある。


[変更前後・原票・検証記録](skill-proofreading/billsum/source-coverage-2026-10/changes.md)。

以下は初回制作・前回改訂時の調査記録であり、当時の抜粋範囲・ページ数の記述は上記の現行改訂で更新している。

日本語、著者sasakiy84、所属なし、2026-10-18 JST。共通マスター由来のnative PPTXと、その最終PPTXから出力したPDF。本編38頁（約10分の黙読・流し読みを予定、未実測）、全84頁。日本語本文・実例訳を中心に読む時間を想定し、対照用の英語引用をすべて逐語で読む時間とは区別する。ノートなし。

## 一次資料と版

- Kornilova, Anastassia and Eidelman, Vladimir (2019), *BillSum: A Corpus for Automatic Summarization of US Legislation*. Proceedings of the 2nd Workshop on New Frontiers in Summarization, pp.48–56, DOI 10.18653/v1/D19-5406。ACL AnthologyのPDFとBibTeXを取得。PDF内のarXiv表示は1910.00523v2、2019-12-04。https://aclanthology.org/D19-5406/ 。著者所属はFiscalNote Research。
- 公式 https://github.com/FiscalNote/BillSum 。取得したtreeのSHA `f1cbe1c9e1a35a2f7ed3ddedafed54abfc3fac8b`。README、BillSum_Data_Documentation.md、clean_text.py、label_sentences.py、post_process.pyを保存。READMEは2019-12-03のデータ更新を告知。独立の公式プロジェクトサイトは案内されず、論文も同リポジトリを入口にする。
- 公式リポジトリ画面はChromiumでCSS/フォントを読み込んで撮影。初回のGitHub上部には動的コミット情報の取得警告と一覧の読み込み表示が残ったため採用せず、同じURL内のREADME冒頭・データの入口・列説明が完全に描画された位置を再撮影。official-site.pngとscreenshot-log.json。データカードやミラー画面ではない。
- 公開配布 FiscalNote/billsum、固定改訂 `3d8510441c06a3d9dfb32eb0d7f80151730bcc4f`。US test 3,269件とca_test 1,237件のParquetを全件取得。原3列はtext、summary、title。train 18,949件はカードのメタデータで確認し、今回train本文は取得していない。https://huggingface.co/datasets/FiscalNote/billsum 。URL・bytes・SHA256はfetch-log.json、more-fetch-log.json、extra-fetch-log.json。
- Lin (2004), *ROUGE: A Package for Automatic Evaluation of Summaries*。原PDFも保存。https://aclanthology.org/W04-1013/ 。

## 原データと例

13例はUS test 7件、California ca_test 6件。本編はUSの教育給付・学生ローンとCaliforniaの教員認可。追加は融資保証料、農業、遺跡、税、先住民学生数、選挙、保育、精神保健、後見、警察記録。読みやすい内容と短めの参照要約を持つ例を選んだもので、無作為標本ではない。

入力本文は長いため、原レコードから意味の通る連続した範囲を抜粋し、その全文語数を各入力頁に表示。原文抜粋は1枚で保持し、訳のために分割していない。文字や表記は変えず、表示では空白のみ正規化。examples.jsonには原text全文、原summary全文、原title、固定ファイルとrow、抜粋の原文文字範囲、両方の日本語訳、原3列のSHA256を保存。HFの3列にはbill_idがないため、rowは固定配布内の位置であり議会の法案番号ではない。

参照要約は常に全文で、入力抜粋だけから作られた文ではない。今回生成した要約でも、HELMの実出力でもない。元の法案の全文に対応する人手要約として掲載した。参照要約は長文なので本文を17〜20pt程度とし、独立した「参照要約」ラベルを21pt太字accent1 #B13731とした。

EN/JP併記を幅・文字サイズを変えて試し、8例は同居。実例1を16.5pt、EN5.2in/JP3.4inで実際にPDF化した併記試作では、双方の末尾がfooterへ達したため棄却。試作のPPTX/PDF/実画像はevidence/layout-probe。採用版は原文の選んだ範囲を1枚、訳を次頁へ置く。同様に長い4例も原文を1枚のまま訳と分けた。layout-trials.jsonは予測と、実際に描画・目視した採用版/試作を区別して記録する。

## 構築・統計・2019年評価

連邦議会第103〜115議会（1993–2018）はGovinfo由来で22,218件、18,949/3,269へ分割。Californiaの2015–2016会期は1,237件、USで学習したモデルを州へ移す評価用。要約はUSがCRS、CAがLegislative Counsel。本文5,000〜20,000文字、要約2,000文字以下を中心に選び、原文・要約の単語頻度ベクトルのコサイン類似度の平均が0.96を超える近重複を除く。同一題名が残る法案はtrainへ配置。

2019年はDOC（位置・TF-IDF等のrandom forest）、SUM（US本文で追加事前学習したBERT-Large Uncasedの文分類）、組合せを評価。各文と参照要約とのROUGE-2 precision > 0.1で二値ラベルを算出し、MMRで最大2,000文字の抽出要約を選ぶ。二値の文ラベルと、配布される人手参照要約を区別した。

公表成績は本文Table2のROUGE F値をそのまま保存し、US/CA各5方法15数値ずつをnative表へ掲載。PyRougeで算出された2019年の評価であり、別実装で再計算した現代モデルの得点ではない。Oracleは参照のROUGE-2 precisionを使う文選択の参考値で、通常の生成予測ではない。Table1の前処理本文の語数と、今回のHF textからの全件実測も分けた。

今回の全件実測はstr.split()。US testの本文平均1283.5910語、参照要約178.8630語。CAは本文1547.0137語、参照要約336.8286語。2,048語超はUS362件、CA268件。Parquet実取得容量は15,797,079 + 6,121,191 = 21,918,270 bytes。カードのtrain規模を、この取得容量へ加えていない。

## HELMの範囲

HELM Classic latestはv0.4.0（2023-11-17）。schemaにbillsum_legal_summarizationグループがあり、v0.4.0にはLegalSummarizationScenarioとget_billsum_legal_summarization_specがある。最初にbillsum_scenario.pyを探したURLは404で、正しいlegal_summarization_scenario.pyを取得した。v0.4.0/mainの両方を保存。

8,526件の固定公開run_specsを、名前だけでなくscenario_spec.args.dataset_name=BillSumおよびlegal_summarization class名でも検索し、BillSumおよび法律要約の公開実行0件を確認。実行の無い設定から、実モデル得点・試行数・実提示例数を捏造しない。

固定コードの対象はtrain/test/validationの写像で、BillSumにはvalidationがないためスキップ。ca_testは対象にない。入力は改行を空白へそろえ、空白区切り先頭2,048語。train提示例候補は200〜800語。adapterの既定値は上限5例、1候補、temperature0.3、最大1,024トークン、停止###、文数指定なし。これらは公開の定義値で、実行の実測値ではない。参照要約は切詰めない。helm-evidence.jsonへ検索数・根拠関数を保存する。

## 権利・帰属

HFカードはCC0-1.0を表示する。原文・要約はUS議会/CRSまたはCalifornia議会/Legislative Counselに由来し、BillSumの編成・研究はKornilova/Eidelman/FiscalNoteに帰属する。元の作成主体と配布カードの表示を保持し、一律に別ライセンスを付け替えない。公式repoのLICENSEパスは404だったため、そのcode全体へMIT等を推測しない。日本語訳は本資料で作成。

## 校正・描画・監査

master-guided-slides、dataset-introduction-slides、japanese-proofreadingスキルを適用。method/review_mode=skill_based_codex、gemini_used=false。Gemini/外部生成APIなし。実際の修正対をproofreading-changes.jsonへ保存。授業料例の参照訳に、原文にない小さい方との比較を足していた点と、増額基準を生活費とした点を修正した。全頁の最終文言・日本語校正を別JSONへ保存。

全84頁を個別view_imageし、overviewも確認。全引用、全6native表、chart1、code1、公式画面、参考文献（各2件）を拡大目視。引用52枠とコード1枠は最終PDFと可視黒画素で8pt上下余白へ調整。最終p68の文言変更で増えた1行を検出し、その枠だけ再調整。p77のURLリンク矩形が隣の出典文字ボックスへ接触した点は段落間隔を広げて解消。変更頁を再描画・再目視する。

標準XSD、新規エラーとマスター既存11件との差、integer buSzPct、内部関係、ZIP、図形ID、native構造、URL-onlyリンク、全491段落/89表セルのPDF字形、ノート0を監査。最終数値・hashはhandoffと監査JSONに記録する。独立レビュー待ち。

最終検査値：84頁、491段落・89表セルの問題0、新規XSD0（マスター既存11を分離）、URL-only77件とPDF77リンクの矩形文字が完全一致。53枠の実画素余白は上7.60〜8.43pt、下7.57〜8.53pt。最終PPTX/PDFのhashとパスはhandoff.json。独立レビューへ引継ぎ可能。


独立レビュー対応：2026-10-18。入力訳見出し5箇所はページ依存を省いた後、実描画の追加同居試行に基づき5例とも15pt・不均等幅で英日同居へ変更した。原文の選択範囲と訳は全て保持。実例6のremoves or reduces the acreageを「保護対象からの除外や面積の縮小」と訳し直し、実例10の題名から「緊急」を削除。最終79頁・本編37頁、変更7頁を個別再目視。旧84頁の全頁検査と校正履歴は原頁番号も保存。最終監査466段落/89セル、layout0、新規XSD0、URL-only72一致。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/billsum.json)、[実際の校正対](skill-proofreading/billsum.md)、[全ページ文言](skill-proofreading/billsum/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/billsum/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/billsum/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
