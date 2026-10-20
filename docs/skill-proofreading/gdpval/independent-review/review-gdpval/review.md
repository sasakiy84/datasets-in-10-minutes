# GDPval 独立監査（進行中）

担当: /root/review_gdpval。作者 /root/create_gdpval と独立。Codexによる内容・技能監査であり、Gemini等の外部生成APIは使用していない。

制作ディレクトリ・repo・Gitは変更せず、監査ファイルは本ディレクトリだけに保存。

## 2026-10-20 初期調査

AGENTS.md、および master-guided-slides / dataset-introduction-slides / japanese-slide-proofreading のSKILL.mdを全文読了。既存ユーザー指示履歴末尾も読了。Cloud runtime skill/networking参照を読了。実環境のHTTP policy unrestricted/enforced、observations_current true、VPN configured falseを確認。継承proxy/CAを利用し、TLS検証を保持。機密値は取得・表示していない。

独立再集計（作者保存の公式raw JSONをread-only利用）:
- 220 task、44 occupation、9 sector。全occupation 5 task。
- 8 sector各25 task、Retail Tradeのみ20 task。
- reference_filesなし95 task、deliverable_filesなし35 task、全220 taskにrubric_prettyあり。
- metadataに301 reference_files、248 deliverable_files。公開参照成果物は実在する。
- データカードREADME/metadataに個別licenseは未記載。CC等の許諾を推定しない。

作者への助言:
- 公開職業人参照成果物を実物で示し、唯一正解と呼ばない。
- 全課題に添付があるとは書かない。
- 元GDPval（人間とのblind win/tie比較）とGDPval-AA v2/v2.1（LLM間pairwise Elo）を分ける。
- AA現methodology主節はCrowd-BT、DeepSeek V4.1 Flash(max)=1600アンカー。後段には旧Bradley-Terryの説明が残る。版と主節で説明し、資料間不一致は監査記録へ。
- row0監査課題はprompt指定列H/I→J/Kとrubric G/H→Iに不一致があるため、原文を変更せず実XLSXと合わせて確認する。

閲覧画像: 現在0頁。自身の画像確認は代表30頁以内に制限し、全新頁の独立visual確認はメインによる担当分割票で担保する。全頁を自身でviewしたとは記録しない。

最終承認: 未実施。PPTX/PDF制作・最終hash待ち。

独立取得: OpenAI記事、公式HF API、AA leaderboard、AA methodology、Anthropic Fable記事の5先を自担当からHTTP再取得し200。保存hashはfetch.json。公式論文PDFも自担当取得（11,826,479 bytes、SHA256 37c7604bc9da68cd8d9345ad16938164fe985182ad723fcb09e9415f84dc25d4）。HF現snapshot SHAは作者保存値11e7900cdcac61bc4daf59e65feb238acda98fbfと一致。

論文内不一致も確認して作者へ共有: p19のTable5はgold見出しだがreference最大38/deliverable最大36、本文gold reference最大17・full最大38と相違。参照添付有67.7%も現raw125/220=56.8%と不一致。時間は本文平均7h、Table3 gold平均9.49h/中央値5h、Table4 full平均8.63h/中央値4h。スライド採用値は対象を明示して表または公開snapshotに統一し、内部差を読者向け警告ページにしない。

原型評価は220 gold×各model3 samples×各sample別3 grader=task/model当たり9比較（p6脚注2）。Opus4.1の47.6%はwins+ties。原型評価のUI/APIツール条件も同脚注で確認。

Anthropic記事v2の表は列順Fable5.1/Fable5/Opus5/GPT5.6Sol＝1853/1723/1824/1711。AA現v2.1ではFable5.1 Max1754、GPT6Astra Max1573（出典現ページ、各fallback等条件保持が必要）。版の異なる値を同列順位表にはしない。

原資料の実物確認（デッキではなく公開素材）: official-site.pngをview_imageで独立表示。CSS・書体・ヒーロー内容が反映された公式記事トップであることを確認。取得ログURL一致。

選択機械工学タスクの参照成果物を独立読解（実行なし）すると大きい条件相違を確認。promptはk5/rho2200/cp800/外700°C h1200/内h15、参照PDFはk20〜30（採用20）/rho1800/cp1000/外≈557°C h50/内h5、参照.pyはTi350/hi100/ho5/k0.85で時間も1/5/10/50/100h。PDFの144°C/余裕6°Cをpromptの正答と主張するのは不可。作者とメインに形式紹介としての明示または課題差替えを提案。公開参照成果物は検証済みの唯一正解ではない。

看護師の参照PDFもテキスト読解し、3診断（急性疼痛、身体可動性障害、感染リスク）と各outcome/assessment/intervention構造がpromptと対応することを確認。医療判断の妥当性を別途検証したとの主張はしていない。

差替候補監査（作者依頼）: row112/113のraw prompt・rubricを読解し、2候補の全6入出力ファイルを公式HFの同一SHAへpinして自担当取得。PDF全文を独立読解。row112 X-wing CFDを推薦。mesh77×32×228、inlet292m/s、force X113.797/Y368.146/Z0.004N、Mach max1.19等は入力報告と参照reportで一致。ただしreportのall convergence criteria metは入力Progress72%/14%と整合しないため、紹介では入力数値→表の対応へ絞る。row113参照memoは直接微細組織証拠なしのpromptに対して観察済の微細組織を主張しており、推薦しなかった。

日本語・内容の草稿通読を実施し、作者へ表の『値1/値2/値3』を実四半期列へ、variance訳『分散』を変化率へ、『過速』を支出が速すぎる等へ、hospital encounterを入院期間に狭めないこと、9産業の一覧構成、比較表の出典不足等を提案。最終反映は制作後に再確認する。

126頁候補のネイティブ本文・全表・文献を通読（原文全文はraw別照合用スクリプトを準備）。p88の重複した係り受け、p5の『専門家が作った現実の知識労働』、現raw統計と論文統計の出典不足、比較方法表のOpenAI出典不足を作者へ指摘。メインからの『職業の依頼』『完成物まで進める』の不自然さも最終候補で確認する。

実XLSX 10件をopenpyxlで独立再読しworkbook-raw.jsonに保存。表示する販売入力・ブランド出力、監査入力・変化率、助成金入力/抽出出力、不動産入力、楽団報酬条件の値と見出しを照合。ブランドST%は依頼式と参照成果物値に相違し、スライドの具体的な不一致説明は裏付けられる。楽団Summaryの当年/翌年/翌々年、基本週給2395/2514.75/2640.4875、割増率0.2/0.1、Media fee週30は一致。

126頁候補パッケージSHA39fe6dbc47cd0e309d2b24b70f4c97b8220524cd235d8ae48bdd5cb710caff31で142 XMLパーツschema確認、unexpected0。ZIP、内部rels、図形ID、notes0、URL-only native hyperlink、authorが通過。既知buSzPct整数lexical差126件、全値域25000–400000適合。これは生成途中の検査で、最終承認には最終hashで再実施する。

## 同期128頁候補の独立検査

PPTX b5b67c546b29c41ce8bb27239adf1c3fbb0f2272a82e033b56ac9cb645a9eafa / PDF 9b6472ca145ac8485effd7ececc18d30040419da7512014b17978a9e843e4571。

- 13例の全依頼をraw JSONとmanifestの分割引用に照合し、全て全文一致。さらに各分割引用はnativeとPDFの両方に全文存在。13職種・9産業、提示順番号を確認（examples-audit.json）。
- ZIP/内部参照/図形ID/author/notes0/URL-only nativeリンクが通過。144パーツXSDにunexpected0（既知buSzPct lexical差126件、値域適合）、19native表/1native chart。
- 全128頁のnative/PDF文字を機械照合し、p112コード右端欠落を検出。p112 URL折返しによるリンク注釈の分断2箇所も検出。他の不一致候補p22/82は箇条書き記号・不可視文字の差を確認中。
- 自担当の代表26頁をview_imageで個別画像表示: 1,3,7,8,10,11,12,13,14,17,20,22,26,29,33,36,38,42,51,67,91,97,112,125,127,128。10頁ごとvisual-progress.jsonへ保存。全128頁を自分で画像表示したとは主張しない。公式素材3画像を合わせ、自担当の新規画像確認は29頁に留める。
- 目次p3の重なりを一度疑ったが、同hashを単独再view・文字座標で正常と確認し、その指摘は撤回した。
- 確認された修正依頼: p12画像cropが617住民の行途中、p22看護参照の段落/箇条書き構造が空白連結、p42説明と出典のbbox重なり（370.77 vs367.04pt）、p91表注と出典のbbox重なり（371.12 vs367.04pt）、p67変化率数値列左揃え、p112長行コードの右欠落とURL分断。参考文献p125/126を2件1頁へまとめる検討も依頼。

最終承認は、修正後hashでの必要再検査と、メインから渡されるfresh独立visual全頁票のcoverage確認が済むまで保留。

128頁候補native表追加検査: 全19表335セルにつき、PDF文字中心がnativeセル領域に入る文字列とnativeセル文字列を照合し、全セル一致（tables-audit.json）。横罫線は全表でtop/bottom1.2pt、header midrule0.6pt適合。文字中心方式は実字形ピクセルの完全境界検査とは区別し、独立visual票で実際の描画の余白を確認する。

native/PDF差分候補のp22/82は、本文の実語句欠落ではなく●/○の抽出順序とゼロ幅文字が原因と確認。比較正規化にCfと箇条書き記号の抽出差を明記し除外し、構造の見やすさ自体は画像上で別に確認する。p112の欠落はコードの実文字が無いため真の不具合。

選択13課題の参照入力/参照成果物ファイル35件の存在と保存SHAを作者fetchログへ独立再計算照合し、全件一致（source-files-audit.json）。これは保存物と記録の照合であり、全35ファイルを自担当から再ダウンロードしたとは主張しない。差替候補6件は上記の通り自担当で直接pin取得した。

## 引継ぎ（メイン依頼による中断）

2026-10-20、元作者のstream切断に伴いメインが /root/finish_gdpval へ制作を引継ぐ。自担当はスロットを空け、最終承認を行わず終了する。上の128頁候補の実施済検査・代表26頁viewは保持する。最終修正版はfresh技術/visual担当が別途確認する。

未完:
- 作者修正後のPPTX/PDF同期・hash再検査。
- p11住民返信の項目ごとの改行（短文入力を1段落へ空白連結しない）。
- p12画像cropの文字途中切断と5人目の検査日表示。
- p22看護参照の目標/観察/介入の構造保持。
- p42説明/出典の間隔。
- p67変化率列右揃え。
- p91表注/出典の間隔。
- p112コード長行の右端欠落・URL折返し分断。
- p125/126を2文献1頁へ統合可能か最終検討。
- fresh独立visual全新頁の両hash一致・coverage確認。

handoff.jsonはapproved:falseのまま。final_hashesとは記載しておらず、candidate_hashesのみ保存。承認済み・全頁画像view済みとは扱わない。
