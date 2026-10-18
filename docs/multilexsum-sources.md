# Multi-LexSum 調査・制作記録

2026-10-18 JST、sasakiy84、所属なし。native editable PPTXと、その最終版からのPDF。主題は米国連邦裁判所の民事人権訴訟の多粒度要約。master-guided-slides、dataset-introduction-slides、japanese-proofreadingを適用。生成API/Geminiは使用せず、review_mode/method=skill_based_codex、gemini_used=false。

## 一次資料・版

正式なNeurIPS2022論文とSupplementを公式proceedingsから取得した。arXiv:2206.10883v3も保存したが、公表条件の説明は正式版を優先する。arXiv本文のtest割合30%は、正式版では20%へ訂正されている。正式版のTable2にはLong件数4534と記載される箇所が残る一方、SupplementのTable9は3177/454/908で計4539。実配布の4539と9280要約が一致するため、資料の構成・分割表は固定配布を用いた。

公式HF改訂055f5fa5300a5fdefb5b691c4d6c1e58f485b379のv20220616/train.json・dev.json・test.jsonとloaderを取得。3ファイルの総bytesは22,265,708。HFツリーメタデータのsources.jsonは2,219,115,572 bytesだが、本体は未取得。13実例の実入力Shortと参照Tinyは概要ファイルに全文がある。原文書そのものをモデル入力として表示したとは主張しない。

配布ケース4539、Long4539・Short3138・Tiny1603、計9280。文書ID40119は重複なし。分割ごとの件数はstats.json。内部subset欄は現配布ファイルと多数不一致だが、公式loaderはこの欄を使わずファイルで分割するため、実例のsplitはtest.jsonに対応させた。語数の独自測定は空白split。論文のspaCy計測と単位を混ぜない。

現v1.1/v20230518は事件と原文書のメタデータ追加をloaderとデータカードで照合。現在の本文を全件比較したとは主張しない。公式GitHub改訂caaed77631c7ed1a012fb857b979adf0a60c03ee、公式サイト、HFカードを保存。2026年現在のモデル順位は調査対象でなく、2022年公表の学習済みモデルと公式配布を説明する。

## 実例13件

異なる13事件のS→T課題。本文3＋追加10、いずれも固定v20220616のtestファイルにある非空のShort/Tiny。原入力と参照文は一字も補わず全文保持し、元レコード・配布の行index・ファイル/レコードSHA256もexamples.jsonへ保存。参照は専門家の一つの表現であり唯一解とは呼ばない。

投稿時点や執筆の文脈も含むため、TinyにはShortにない精確な人数や後の処分などがある。例2の1697対just under1700、例6の仮差止め・判事発言、例12のCOVID-19などを、入力から当然復元できる事実として説明しない。例6の参照にあるE.D. Ohioは原文どおり保存。日本語で実在する裁判所の正式名を補わず、E.D. Ohioという表記のまま訳した。

自然な日本語の訳は原文の主張/否定/日付/数値/係属の時点を保持。「Added to Clearinghouse」「Documents now posted」等の投稿表現を事件内容だけへ置き換えない。EN/JP同居は15pt以上・不均等幅を試し、参照21pt太字B13731を優先。coexist-probeには13件の実描画試験を残す。成立例のみ正規版へ採用する。

## HELM・評価

HELM v0.4.0のLegalSummarizationScenarioを取得。docstringのShort→Tiny例に対し、実行コードはsummary/long→summary/short。v20220616を指定しShort空欄を除外、改行・空白整形、任意のdoc_max_lengthは空白区切り語数、trainだけsampling_min/max_lengthを適用する。release run_specs全8526件をscenario_specとnameから確認し、legal_summarization/MultiLexSum該当は0。HELMのモデル値・試行数・実提示数を作っていない。

モデル結果は正式論文の2022年Table3（D→L/S/T）とTable4a（L→S/T、S→T）のROUGE2 F1×100。BART、PEGASUS、LED16384、PRIMERAの対応を保持。6epoch/lr5e-5が本文の基本条件、Supplementでは長文モデルの設定差あり。入力上限1024/4096/16384はモデルtoken、データの語数と別。beam5、4gram以上反復抑制。通常のTable3/4を特定の試行数平均と断定する記載はないため、3試行平均などを補わない。Supplementの別split安定性実験・5foldも主結果とは混ぜない。

人手評価は新規40事件、D→Long、2人、180時間。実際には関連スニペットを人が選びBARTで段落を生成する支援システム。0〜3尺度で平均0.43、編集87token/段落=76%、生成→編集後のROUGE2=30.0。一般の全モデル評価や単純な完全自動生成のスコアへ拡大しない。

## 権利・公式画面

公式説明をそのまま区別：データベースODC-By、要約/メタデータCC BY-NC4.0、原文書public domain、ローダーApache2.0。商用向け別ライセンスの連絡方式もカードにある。13引用の著者帰属はページfooter、版とケースIDを添える。

トップ全体をブラウザで取得すると埋込み外部動画が読み込めず大きな灰色枠となった。DOMを変更せず、公式トップのタイトル・正式題名・NeurIPS掲載・ナビが読める1440×250 viewportで再取得し、CSS/フォント/アイコンを実viewで確認。画像は公式トップの見えている領域で、動画を偽の代替に置換していない。screenshot-log.json参照。

## 独立レビュー修正と取得例

create_pileの先行レビューを反映し、例6のformal policing/earliest form inを自然な訳へ、例11の取下げ対象を訴えへ修正。生成制御は4-gram表記にした。Tiny非空でもShortが空のtrain/SD-IL-0001（row897）が1件あるため、S→T利用可能組はtrain1129/dev161/test312と実集計してp57へ追加した。要約組を読むp64のコードは、固定改訂のJSONLを直接取得し、先頭レコードとの完全一致を実行確認（evidence/code-check.json）。

## 検査

全69頁の本文と最終PDFからのoverviewを確認し、各頁を個別にview_imageで実目視。最終局所変更頁も再確認した。416段落・99表セルのlayout問題0、文字欠落0、原13例の全文/参照/hash一致、答え26runは21pt太字B13731、引用26枠の実画素上下6.67〜8pt、表下注記12.52〜12.54pt。native表8、標準XSD新規0（元マスター11との差）、内部参照/shapeID/ZIP、整数bullet145、notes0、nativeURL-only66とPDF66完全一致を確認。独立レビュー待ち。具体的な校正変更・閲覧頁・値は各JSON。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/multilexsum.json)、[実際の校正対](skill-proofreading/multilexsum.md)、[全ページ文言](skill-proofreading/multilexsum/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/multilexsum/review.json)。
