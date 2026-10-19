# WikiFact 出典・制作記録

WikiFactはHELMで新規構築した事実補完データ。WikiData/Wikipediaと同名の独立百科事典や、文の真偽を判定する別データセットとは区別する。表紙のWikiFactに公式の展開形は確認できないため、架空の長い名称は作らない。論文初公開は2022年、掲載はTMLR 2023年。本編28頁、全52頁、黙読・流し読みの予定600秒（未実測）。著者sasakiy84、所属なし、制作日JST。

技能はmaster-guided-slides、dataset-introduction-slides、japanese-proofreadingを使用。全頁校正はskill_based_codex、Gemini・外部生成APIは不使用。校正前後の実際の修正対はproofreading-changes.json、頁ごとの最終テキストとチェックはpage-review.json。

## 一次資料

1. Percy Liang et al. (2023), Holistic Evaluation of Language Models. Transactions on Machine Learning Research. https://arxiv.org/abs/2211.09110
   - §5.2とAppendix E.2.1で、2022年1月のWikidata dump、12分野・86関係、主語または目的語にWikipediaページのない三つ組の除外、関係ごと1000問、100 train / 50 dev / 850 testの設計を記載。
   - Table 10とTable 11は同じ86関係の表。重複を二度数えない。各関係の手製テンプレートを確認。Art 6、Law 7、Philosophy 2、Politics 8、Geography 6、Economics 5、Math 2、Computer Science 4、Physics 2、Chemistry 5、Biomedicine 5、Other general 34を行から集計した。本文には各分野2–7関係という記述もあるが、表のPolitics 8・Other general 34とは一致しないため、資料では表の86行の集計を使った。
   - 許容対象が複数である場合と、同一対象に複数の別名がある場合の両方を参照に含めると説明。
   - 貢献記録ではHongyu Renの設計・実装、Lucia Zhengの注釈・前処理、Michihiro Yasunagaの知識チーム統括、Neel Guhaらの貢献、Percy Liangの全体統括を確認。
2. Fabio Petroni et al. (2019), Language Models as Knowledge Bases? EMNLP-IJCNLP, 2463–2473. https://aclanthology.org/D19-1250/
   - WikiFactの先行するLAMAの一次資料として取得。文の穴埋めから言語モデルの知識を調べる手法を説明する。
3. 公式HELM WikiFact結果 https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/wikifact
   - ブラウザにCSS・フォント・JSを読み込んだ画面を取得して実際にview_imageした。ページは「Leaderboard: WikiFact」を表示。公式スクリーンショットとasset logを保存。
   - latest/config.jsも取得し、Classic latestがv0.4.0（2023-11-17）であることを確認。元run suiteはv0.3.0。
4. 公式scenario https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/wikifact_scenario.py
   - PID辞書をASTで読み、86関係を確認。subject引数は関係名であり主語エンティティではない。
   - JSONLのpropertyで選別し、templateを入力、result_namesをflattenして前後空白を除いた各文字列を正解参照にする。
   - CodaLab bundleのtrain/dev/testを2026-10-18に取得試行したが全て503。失敗ログを保持し、元JSONLを取得したとは記載しない。
5. 公式採点 https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/metrics/evaluate_reference_metrics.py
   - completionを総logprobの降順に並べ、最高候補と正解群の最大値をscore、全候補と正解群の最大値をscore@Kとする。
   - quasi_exact_matchは小文字化、ASCII句読点、冠詞a/an/the、余分な空白を正規化した一致。USLなどの略語の展開や意味判定はしない。

## 公開版と件数

v0.4.0のrun_specsには、WikiFactの実行がある関係は10種類。対応実装の86関係と同一の範囲ではない。

|関係|test|dev|
|---|---:|---:|
|author|850|50|
|currency|850|50|
|discoverer_or_inventor|850|50|
|instance_of|850|50|
|medical_condition_treated|850|50|
|part_of|850|50|
|place_of_birth|850|50|
|plaintiff|96|15|
|position_held|850|50|
|symptoms_and_signs|566|50|

testの重複なしinstance IDは合計7462件（関係ごとのIDを試行間でまとめた件数）。入力文字列の一意数は7456件で、authorは850 ID／849文、currencyは850 ID／845文。各3試行の元requestは別に数える。全体成績は10関係の正答率の単純平均であり、問題数による重み付き平均ではない。画面の#eval 746.2は関係別件数の平均であり、1問の小数件数ではない。

## 実行条件と独立再計算

モデルはOPT-175B（2022）、text-davinci-003（2022）、Llama 2 70B（2023）。各10関係30条件のstats、全scenario_stateを取得した。固定URL・byte・SHAはfetch-log.json、llama-records-audit.json、opt-records-audit.json、file-manifest.json。正確なname/adapter/指標はstats.jsonとevidence/selected-run_specs.json。

全条件でmax_train_instances=5、temperature=1、max_tokens=8、stop_sequences=[改行]。公開statsのnum_train_instancesは5、prompt_truncatedは0。OPT/davinciは3試行、Llama 2は1試行。

重要な差：num_outputs=5という設定でも、Llama 2の全10関係・全7462 testレコードのresult.completionsは1件。原因を推測していない。OPT/davinciでは全3試行testレコードで5件を確認。したがってLlamaの@1=@5を「5候補でも改善しなかった」と解釈しない。

recompute.pyで各モデル・関係・試行の候補をlogprob順へ並べ、各参照と正規化比較し、試行平均を再計算した。30条件すべてで公開quasi_exact_matchとquasi_exact_match@5に1e-10未満で一致（metrics-recomputed.json）。既存表示値をコピーしただけで再計算とは記載していない。

|モデル|Accuracy@1（%）|Accuracy@5（%）|実候補数|試行|
|---|---:|---:|---:|---:|
|OPT-175B|22.03257061364004|32.28388328829765|5|3|
|text-davinci-003|37.33717002702141|44.03034105868496|5|3|
|Llama 2 70B|44.92147682394512|44.92147682394512|1|1|

2023年のClassic固定版の結果であり、2026年の最新モデル順位や最新Wikidataの事実ではない。

## 実例・訳・公開範囲

全13実例は、公開text-davinci-003のtest・第1試行から10関係を意図的に選んだ。本編3＋追加10、独立ID13件。入力全文と全参照を原順・重複込みで1頁に保持し、訳を同居させた。単一対象の複数別名は訳でまとめる場合があるため、訳は「答えの意味」と表示し、英語参照の完全一覧と混同させない。日本語訳が英語採点の追加参照であるとは記載しない。

examples.jsonには関係内ID、source file、request_states内のtest/trial0に絞ったindex、入力SHA、原request/response、全候補logprob、固定run URLを保存。HELM IDはWikiData QIDではない。元JSONL未取得のためQIDを推測して足していない。

実例3のモデル出力はUSL、Unisys Corporation、Unisys Corporation、Unix System Laboratories.、The United States of America（logprob順）。正解参照はUnix System Laboratoriesのみで、正規化一致は[0,0,0,1,0]、@1=0、@5=1。原出力の複製や句点も保持した。

原文の不自然なテンプレート（例Apgar score was discovered by）は修正しない。訳では対象の意図に合わせて「考案した」とした。未確認の人名の日本語定訳を作らず、Thomas N. ScortiaとFrank M. Robinsonは原綴りを用いた。参照の同じ名前の重複を消して別のデータにしない。

## 権利と取得制約

HELMコードのLICENSEを取得しApache License 2.0を確認。コードのライセンスを元知識基盤や加工済みデータ全体へ自動適用しない。WikiFact配布物の専用ライセンス表示は今回取得した論文・scenarioでは確認できなかった。Wikidata:Licensing、Wikidata:Database_download、Wikidata Main Page、Wikimedia Foundation Terms of Useへの取得は403だった。これを「ライセンスがない」と断定せず、未確認として残す。引用元はHELM公開入力へ帰属し、原文・訳の区別を維持する。

全86関係の元JSONLと2022年1月のWikidata dumpは未取得。全体総件数、元のQID、全関係の分布や元dumpのbyte/hashは実測したとは書かない。

## 描画と品質検査

共通SlideMaster由来の編集可能なnative PPTX。本文・引用・回答・11表はnative text/table、公式画面1件だけが画像。発表者ノートなし。最終PPTXから独自LibreOffice profileでPDF化。

全52頁をoverviewと各頁pngで実際にview_imageし、日本語を1頁ずつ確認。PDF字形から26引用枠の上下余白を調整し、変更した13実例頁を再確認。p38で長い参照と自明な注記の接触があったため、その注記を表示から削除（原記録では保持）。p15の表見出しと各表注の距離も調整した。

package-audit.json：新規XSDエラー0、master既存11件と整数buSzPct差を分離、ZIP・内部参照・図形ID合格。layout-audit.json：セル・引用・source gapの実字形検査。overlap-audit.json：異なるnative text shapeの字形交差を検査し0。同じ段落内の通常行送りによるフォントbboxの重なりは、このshape間検査の対象としない。links-audit.json：44 URL runとPDFリンク矩形が完全一致。text-audit.json：native本文とPDF文字の照合。独立レビュー待ち。

## 独立レビュー完了
review-wikifactで全52頁、30条件の@1/@5、13実例を独立検査し合格。p17・本記録のID件数と文字列一意数の区別を修正し、最終版を再確認。未解決のレビュー指摘なし。元配布503・ライセンス文書403という取得範囲の制約は上記のとおり。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/wikifact.json)、[実際の校正対](skill-proofreading/wikifact.md)、[全ページ文言](skill-proofreading/wikifact/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/wikifact/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/wikifact/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
