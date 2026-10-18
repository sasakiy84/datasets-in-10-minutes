# TwitterAAE 制作・出典記録

対象はTwitterAAE（2016）と、同じ資源に由来するHELM ClassicのAA／white二条件。baseは集約グループで、別データの資料として数えない。本編25頁、全49頁。黙読・流し読みの予定600秒、時間は未実測。著者sasakiy84、所属なし。共通SlideMaster由来のnative editable PPTXを作り、その最終PPTXからLibreOfficeでPDF化した。発表者ノートなし。

使用技能はmaster-guided-slides、dataset-introduction-slides、japanese-proofreading。校正方式はskill_based_codex、gemini_used=false。全ページの最終文言と校正チェックはpage-review.json、実際に適用した修正対はproofreading-changes.json。調査・取得ネットワークは通常TLS検証と継承proxy、生成APIは未使用。

## 一次資料と調査結論

- Su Lin Blodgett, Lisa Green, Brendan O’Connor (2016). Demographic Dialectal Variation in Social Media: A Case Study of African-American English. EMNLP, 1119–1130. https://aclanthology.org/D16-1120/
  - 2013年ストリーム160億件、地理対応9000万件、前処理後5920万件・280万ユーザーは§2.1。block groupとAmerican Community Surveyの4共変量も同節。
  - §2.3のユーザー単位AA／white条件：対応成分80%以上、Hispanic+Asian成分5%未満。83万／730万投稿。
  - 構文と比率の表はTable 2。語・表記・習慣be・未来gon・完了doneを言語学的に検証。
  - langid.pyの13.2%／7.6%はTable 3。Twitter-1／2は別分類器ではなく同じ予測の欠損値の扱い。人手1500件は各decile・各識別条件で「非英語」とされた投稿から抽出、13件が明らかな非英語（§4.1）。
- 公式研究ページ：https://slanglab.cs.umass.edu/TwitterAAE/
  - ブラウザでCSS3枚・フォント読み込み後の画面を取得し、実際に目視。asset failureなし。スクリーンショット公式ページ題名はHTML上SLANG Lab at UMass、本文の見出しはTwitterAAE: Research on African-American English on Twitter。
  - full-v1.zipは表示5.5 GB。全体ZIP未取得、公式UD ZIP取得325410 bytes。研究目的のみ・研究利用時の指定論文引用を案内。
- モデル公式リポジトリ：https://github.com/slanglab/twitteraae
  - READMEの出力は「人口統計に関連する言語／方言が文内で占める語の割合」であり著者属性の信頼度ではない。AA／whiteだけを信頼して言語学的検証したと明記。
  - MITはコードのライセンス。これを元投稿本文の包括的再配布許諾へ拡張しない。
  - 取得時commitはevidence/commit.json、README/LICENSEのhashはevidence/file-manifest.json。
- Su Lin Blodgett, Johnny Tian-Zheng Wei, Brendan O’Connor (2018). Twitter Universal Dependency Parsing for African-American and Mainstream American English. ACL, 1415–1425. https://aclanthology.org/P18-1131/
  - 公式研究ページとUD配布に各250投稿との説明。UDは追加資源で、HELM CSVの代替同一集合とは扱わない。

## HELMの固定版と公開実行

latest/config.jsを2026-10-18取得。Classic latestはv0.4.0（2023-11-17）、元run suiteはv0.3.0。2026年の最新モデル順位としては扱わない。

HELM実装：https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/twitter_aae_scenario.py
HELM結果：https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/twitter_aae
指標コード：https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/basic_metrics.py

HELMは投稿単位のAA比率上位83万、white比率上位730万から各5万を標本抽出したとdocstringに記載。2016年のユーザー単位集合と同一視しない。CSV読込では先頭列をinput.text、references=[]、split=testとする。二つのCodaLab CSVを再取得したがどちらも503。取得失敗を「例が公開されていない」とは扱わず、公開scenario_stateを取得して各1000件を確保した。

正確なrun名・suite・adapter_spec・摂動なしtest指標はstats.jsonとevidence/selected-run_specs.json。4runともlanguage_modeling、max_eval_instances=1000、max_train_instances=0、num_train_trials=1、temperature=0、max_tokens=0。prompt_truncated=0。公開input/実際のprompt/トークンのlogprobは原レコードを保存した。

|モデル|AA BPB|white BPB|AA perplexity|white perplexity|
|---|---:|---:|---:|---:|
|together/opt-175b|2.1143207409278326|1.5060743306648166|184.99029608680192|65.76136161424033|
|openai/text-davinci-003|2.5223225031029552|1.8618913711143457|152.5133900232998|77.068421430109|

BPBは−総対数確率/(総byte数×ln2)で、投稿ごとのBPBの算術平均ではない。実例1は原レコードlogprob=-101.668241781、52 bytesからBPB=2.8206974660259387を算出した。公開モデル出力は入力をechoした確率で、生成した正解文は付けていない。

## 実例と帰属

13件はすべて公開v0.3.0のscenario_state内のinput.text全文。AA7件、white6件。本編3件＋Appendix10件、重複なし。原文・日本語訳・条件内ID・request_states配列index・全文SHA・request/resultをexamples.jsonへ保存した。HELM IDはTwitter IDではない。同じ文字列のIDが両条件に出るためaa/id...の複合キーで同定する。

選定は短い自立した自然文と、縮約・語りかけ・反復・日常話題を優先。人名／アカウントや文脈の解釈が必要なもの、長いエスケープ表現は避けた。表現を誤文として修正せず、訳は話者の強調と語りかけを保った。原文にない人種や関係性を訳へ追加していない。OOMF=one of my followersの略語解釈は文脈に基づく。元の筆者やTwitter投稿URLは公開runには含まれず、推測して補わない。投稿本文の著作権・元プラットフォーム条件まで開放されたとは記載しない。

公開ファイルのURL、HTTP結果、bytes、SHAはevidence/fetch-log.json、run-fetch-log.json、file-manifest.json。全体ZIPとCodaLab各5万件未取得のため、元集合全件の分布・重複等は未検証。

## 検査範囲

全49ページのoverviewと各ページpngを実際にview_image。公式画面、全引用、全native表、全参考文献を個別に拡大して確認。初回のp15表見出し末尾折返しとp48参考文献overflowを修正し、変更ページを再PDF化・再描画・再確認。

package-audit.jsonはZIP整合性、内部参照、図形ID、標準XSDを確認。マスター由来の既存11件と整数buSzPctの字句形式差を分離し、新規XSDエラー0。native tables=6、charts=0。layout-audit.jsonはPDF実字形と枠・セル・出典gapを照合。links-audit.jsonはnativeURL runとPDFリンク矩形を照合。text-audit.jsonは全ページのnative文言とPDF抽出を照合。独立レビューはcreate_cnndmが実施し合格。p12段落配置とp34のtiredの訳を修正し、最終版を再確認した。レビューは/workspace/artifacts/helm-parallel/review-twitter-aae/review.json。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/twitter-aae.json)、[実際の校正対](skill-proofreading/twitter-aae.md)、[全ページ文言](skill-proofreading/twitter-aae/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/twitter-aae/review.json)。
