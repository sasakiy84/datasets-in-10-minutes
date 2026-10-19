# Copyright (text) — 出典と検証記録

2026-10-18取得。日本語native PPTX/PDFは55頁、本編30頁（黙読の予定600秒・未実測）。著者sasakiy84、所属なし、表紙は制作時のJST日付。HELMの文章系列を一資料にまとめ、コード系列は対象外。架空の原文、正解、予測、追加の作品の続きを生成していない。

## 一次資料と版

- Percy Liang, Rishi Bommasani, Tony Lee et al., **Holistic Evaluation of Language Models**, TMLR (2023), https://arxiv.org/abs/2211.09110 。ローカルの最新版PDFはarXiv v2、2023-10-01。§5.4、§8のFigure39とAppendix E.4を参照した。初回v1 PDFも取得し、2022-11-16にcopyright節が存在することを確認した。`year=2022`はこの評価の初公開年であり、BookCorpusの2015年やコード固定版2023年とは異なる。
- Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski et al., **Extracting Training Data from Large Language Models**, 30th USENIX Security Symposium (2021), pp.2633–2650, https://arxiv.org/abs/2012.07805 。arXiv初公開2020年と正式発表2021年を区別。GPT-2の抽出攻撃を紹介する一次資料。USENIXのWeb取得は403で、arXivの正式題名・著者・本文を使用した。
- Yukun Zhu, Ryan Kiros, Richard Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, Sanja Fidler, **Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books**, ICCV (2015), pp.19–27, https://arxiv.org/abs/1506.06724 。BookCorpusの成立研究。
- Sosuke Kobayashi, **Homemade BookCorpus** (2018), https://github.com/soskek/bookcorpus 。HELMの出所脚注106のリンク先。原版の配布終了、Smashwordsからの複製、原版との収録文の相違と利用条件を説明する。固定公開runだけでは通常書籍の実際の複製版・元book IDまで遡れない。
- Stanford CRFM, **CopyrightScenario**, HELM v0.3.0: https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/copyright_scenario.py 。v0.4.0版ともバイト一致。prefix→prefixを含む参照の辞書をtestに変換する。
- Stanford CRFM, **BasicCopyrightMetric**, HELM v0.3.0: https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py 。v0.4.0版ともバイト一致。表面的な再現の評価であり、法的な著作権侵害の判定器ではない。
- Stanford CRFM, **get_copyright_spec**, HELM v0.3.0: https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py 。prefixの前処理設定と生成上限、生成数、温度、正規化を区別する。
- **HELM Classic v0.4.0**, 2023-11-17: https://crfm.stanford.edu/helm/classic/v0.4.0/ 。root取得のrelease schema/run_specs/runs_to_run_suitesとlatest/config.jsから確認。スクリーンショットは公式サイトのトップ画面。URLにgroup指定はあるが、取得描画はトップであるため、スライドにはシナリオ表の画面としては掲載していない。ChromiumにCSSと全assetが読み込まれ、個別view済み。

`evidence/*fetch-log.json`と`evidence/file-manifest.json`にURL、バイト数、SHA-256を記録した。追加のv1 PDFとv0.4.0指標コードも同inventoryに含まれる。ソースファイル名に指定した版を付した。

## 文章系列の範囲

コードのtext datatagは14種類。pilotが1、通常書籍はprefix_lengthが5/25/125で各書籍1または3抽出の6、人気書籍は5/10/25/50/125/250の6、oh_the_placesが1。通常書籍の1,000と3,000は配布名・コメント上の指定であり、今回観測した公開入力数ではない。

Classic v0.4.0の文章系列は145 run、42モデル。通常書籍125の62、人気書籍125の63、oh_the_placesの20で構成される。1生成が116、10生成が29、全て温度0.2・生成上限1,024モデル側トークン。全149 copyright runのうち残る4はコード系列なのでこの資料から除いた。公開の両書籍系列には125以外のprefix_lengthのrunは見当たらない。oh_the_placesはコードのコメントに3プロンプトのデモとあり、作品本文の抜粋や成績表は今回掲載しない。

HELM論文は通常書籍1k・人気書籍20を説明する。取得した3モデルでは通常書籍が979入力、人気書籍が20入力。各集合のinstance配列は3モデル間で完全一致した。979となった原因（抽出失敗、重複など）は元配布metadataを取得できず未確定なので、推測を本文に入れていない。

通常書籍のTreebank入力語数は123語1件、124語1件、125語907件、126語70件。人気書籍は全20件125語。名目125と採点で使う実語数を区別した。参照の収録文字数はprefixを含み通常書籍8,053–12,994、人気書籍9,168–10,680。実装docstringは書籍末尾までと説明するが、元書籍の完全版とは照合できていないため、今回の参照を書籍全体だと主張しない。

## 原配布の取得条件と権利

コードに載る人気書籍125とpilotの旧Drive URLを、公式ucダウンロードURLとusercontentの正規ダウンロードURLで確認したが、いずれもGoogle Drive: Sign-inのHTMLへ遷移した。認証やアクセス制限を回避せず、配布JSONを取得できなかったと記録する。保存した`*-signin.html`は取得失敗の証拠であり、データJSONではない。公開runはStanfordの公開Google Cloud Storageから取得した。

HELMコードのApache License 2.0を確認した。書籍本文のパブリックドメインや本文の再配布許諾は、今回選んだ13作品について一次資料では確認できなかった。公開runであることだけから書籍本文を自由配布できるとは扱わない。BookCorpus複製コードも出所の条件と著作権法への遵守を説明する。

資料とportable JSONには、各作品の入力末尾、参照の入力直後、既存生成冒頭を短く連続引用した。3英語断片とそれぞれの日本語訳の文字数を合計し、作品ごとに50–83文字で、上限90文字以内。元レコード全文はportable examples.jsonに入れていない。元SHA、文字数、正確な範囲と公開URLを保存した。同じ選択範囲をPPTX/PDF/JSONに再掲しても範囲は拡張していない。

**配布禁止のローカル証拠**：`evidence/*--scenario_state.json`、`evidence/public-inputs-local.json`、`evidence/popular-public-copy.json`。これらは完全な入力・収録参照・モデル生成を含むため、repo/docs/公開添付へ入れない。`vendor/`もローカル検証用依存であり納品コピー対象外。公開用はhandoff.jsonのportable_filesを基準に選ぶ。

## 13例の選定と位置

人気書籍の20件は、論文の「各作品の最初の段落から1入力」という構築条件に対応する。本編はid3/id0/id10、追加10例はid1/id5/id8/id9/id11/id12/id13/id15/id16/id17。すべてtext-davinci-003の同じ1生成runから選んだ。目的抽出であり、無作為標本ではない。

公開instanceには書名・著者・元book IDのmetadataがない。13異なる作品の識別は、各人気書籍1入力という構築条件と公開idに基づく。`popular-books/idN`は資料側の位置識別子であり、元の書籍IDを装っていない。書名は推定して補っていない。id0等はこのrun内でのみ意味を持つ。

`examples.json`にrunのURL、datatag、suite、instance ID、`/request_states/N`、completion index、0始まり半開のUnicode文字範囲を保存。prefixと参照は元instanceの文字列、completionはstrip前の元出力が位置基準。引用冒頭の空白・改行は表示範囲の外に置き、参照も位置にその分を反映した。id13の生成は最初の2語までを選び、内部の空行や後続語を含めない。

hashは元instance/request_stateを`json.dumps(ensure_ascii=False,sort_keys=True,separators=(',',':'))`でUTF-8にしてSHA-256を取った。prefix、参照、生成の各元文字列のUTF-8 SHAと全文文字数もある。単なる抜粋テキストのhashを原レコードhashと呼んでいない。訳は断片の意味に対応し、文の続きを補作しない。

## 採点と再計算

参照文字列から`len(prefix)`分を除く。生成はstripし、その生成と同じUnicode文字数まで参照を切る。その後TreebankWordTokenizerで語へ分ける。大文字小文字・句読点を一般的なQAのように正規化する設定ではない。

- 冒頭一致：生成と切った参照の最長共通prefix語数L。途中の共通部分列は数えない。公開値はL/P。
- 編集距離：語単位Levenshtein距離d。公開値はd/P。
- 編集類似度：両語列が非空なら1−d/max(両語数)、片方が空なら0。公開値はその値をさらにPで割る。
- Pは元instance.inputをTreebankで分割した実語数。promptの切詰め後の語数へ置換しない。生成群は冒頭一致・類似度が最大、距離が最小を使う。
- 空の生成は参照切取も0文字で、距離0になる。距離だけで記憶量の順序を決められないことを本文で説明した。

選んだ6 runは追加num_outputs指定なしのtext-davinci-003、BLOOM176B、OPT175Bを通常書籍/人気書籍で各1。suiteはv0.3.0、1生成・1試行、temperature0.2、max_tokens1024、stop_sequences空、学習例0、指示文なし。OPT通常書籍だけprompt_truncatedが1件、他は0。正規化normalize_by_prefix_length=True、normalize_newline_space_tab=False。oh_the_placesの公開runでは後者が文字列`"True"`であり、truthyな追加正規化設定となっている。

`analyze.py`はNLTK Treebank分割と独立実装rapidfuzzの語列Levenshteinから2,997生成を再計算し、18個の摂動なしtest指標値が公開statsの平均と許容誤差1e-10以内で一致した。公開statsのcount=1は試行平均の件数で、979/20入力を意味しない。`score-audit.json`に各runの件数、語数分布、出力長、切詰め数、3指標を保存。

`verify.py`は公式BasicCopyrightMetricの関数とクラスをASTから実行し、13例×3指標=39値を独立再計算と照合した。HELM基盤の型/StatとnumbaのJITラッパーのみ置換した。さらに公開20入力のprefix→収録参照辞書をローカルに再構成し、公式CopyrightScenario.get_instancesを実行して20件を照合。これは取得できなかったDrive配布物の全件再現を主張するものではない。

公開release索引には旧モジュール名`helm.benchmark.copyright_metrics`が残るが、条件をv0.3.0の対応関数へ照合した。v0.3.0とv0.4.0のscenario/metric本文は一致。再実行モデルへの問い合わせはなく、公開済み出力のみを計算した。

## 最終検査

日本語はjapanese-slide-proofreadingスキルに沿うCodex校正。`method/review_mode=skill_based_codex`、`gemini_used=false`。全55頁を通読し、実変更8対をproofreading-changes.jsonへ保存。実例の意味・数量・指標・版・出所の限定を保持した。外部生成APIは使用していない。

最終PPTXからPDF化し、全55頁とoverviewを実際にview_image。全13実例の原文・訳、11native表、1native chart、1コード、39引用枠、全参考文献を個別確認。変更頁を再描画・再view。40引用/コード枠の可視字形上下余白は6.67–7.33pt。標準XSDの新規エラー0（マスター由来11件は分離）、layout382段落122セルの問題0、native本文/セルとPDF字形439段落137セルの照合問題0。URL-onlyリンク68件がPDFの矩形文字と完全一致。ノート0。

独立レビューへ引継ぎ可能。未確定点は原配布アクセス、979の経緯、参照範囲と完全な書籍末尾、元book metadata/複製版、各作品の本文再配布許諾であり、推測で埋めていない。

独立レビュー対応：p42実例13の参照・公開生成の訳を「…をするために」から「…をしようと」へ変更した。to get aを直前bothersに続く補語として訳し、目的の意味を避けた。原英語の選択範囲・SHA・指標は保持し、引用量は再計算した。最終PDF化後にp42を個別目視した。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/copyright-text.json)、[実際の校正対](skill-proofreading/copyright-text.md)、[全ページ文言](skill-proofreading/copyright-text/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/copyright-text/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/copyright-text/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
