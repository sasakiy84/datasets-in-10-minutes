# BillSum 調査・制作記録

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
