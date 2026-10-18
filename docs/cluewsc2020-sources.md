# CLUEWSC2020 — primary sources and limits

制作: sasakiy84。対象はCLUEWSC2020の元公開データ。CLEVAプラットフォームやCLEVA選定集合全体とは別資料。メインrepo/Gitは変更していない。

## 初公開・正式論文

- CLUE公式READMEの固定commit `9e61ddd3659ddb57ed82b4d0ba0a8613dfb55a2e` は、2020年3月25日に従来のCLUE WSCとは異なる新CLUEWSC2020を公開したと記す。公開年は2020。
- Liang Xu, Hai Hu, Xuanwei Zhangら32名、**CLUE: A Chinese Language Understanding Evaluation Benchmark**, COLING 2020, pp.4762–4772, https://aclanthology.org/2020.coling-main.419/ 。正式PDFの§4.1、Table1–3、§6を使用。arXiv:2004.05986初回2020-04-13は正式刊行より前。現行モデルの順位を示す資料ではない。
- Hector J. Levesque, Ernest Davis, Leora Morgenstern (2012), **The Winograd Schema Challenge**, KR 2012。https://cdn.aaai.org/ocs/4492/4492-21843-1-PB.pdf 。語を少し変えて指示対象が変わる文対の構想と、自然な中国語文学作品からの対象組二値分類を区別。
- 課題公式repo https://github.com/CLUEbenchmark/CLUEWSC2020 、固定 `446646278671444c79a67e7434b3a1d1d1cbbe88` (2020-05-24)。固定READMEとtreeを独立取得。treeはREADME.md一つで、dataやLICENSEファイルを置かず公式GCS配布をリンクする。

## 配布と件数

https://storage.googleapis.com/cluebenchmark/tasks/cluewsc2020_public.zip 。取得済みの親インベントリから同一バイトを専有evidenceへコピー。ZIP SHA256 `ebe5f357b19392d601be401b2fd4246983f534809a078eab7bda1de418fb3ffe`。原取得ログは親cleva-inventory/fetch-clue-log.json、専有側にもコピーして保存。

2020年の正式構成はtrain1244/dev304/test290、合計1838問。現ZIPのREADME2021-08-29は、旧testをtest1.0.jsonとして保存し、新test.json（v1.1）へ切替えたと明記。現行train1244/dev304/test2574は計4122行。新旧テストを両方含むZIPの四ファイル総計4412行を、単一版の件数とは扱わない。test/test1.0のラベルは全欠落。train/devの件数は歴史構成と一致するが、2020年の固定配布を別途取得してのバイト同一性までは確認していない。

stats.json/data-audit.json/all-records.jsonは配布4ファイルを全行再計算。異なるtextはtrain387/dev104/newtest1424/oldtest88。学習idxは347種類で一意ではない。text+targetの異なる入力はtrain1239/newtest2568。学習の同一入力重複にラベル矛盾なし。全8824spanを文字位置でsliceして一致、新testには候補が代名詞より後にある行464件。完全同一textのファイル間共有は0。これは作品・著者・類似文による漏洩まで否定するものではない。

## 13公開例

本編3、追加10。すべて正解公開のtrain/devから取り、全13例のtextは独立。例1=train681（HELM説明例と同一対象組）、例2=train346（CLEVA紙面の「同行→他、否」と同一対象組）、例3=train4（公式READMEの床→它false）。残10例はdev3/14/16、train37、dev37/40/44/61/81、train698。

examples.jsonに原レコード、生行（改行込み）、file/line1起算/idx/byteoffset/行SHA/fileSHA/zipSHA、全提供文、指定spanの0起算文字位置、正解、全文JP新訳を保存。文学作品全文ではなく配布text全文を表示する。元の作品名/著者欄は存在せず、人物名から推測して補わない。色は指定位置のspanだけに付け、同じ語の他出現を一括強調しない。例2と同じ文章のtrain345/347、例1と同文のtrain682を独立例数へ増算しない。

原textは削除/要約せず1頁。15ptで3幅組（3.8/4.8、4.3/4.3、4.6/4.0in）、39頁を実PDF化してglyph底を測定。全組で収まり、原文全文を保って13例すべて訳と同居。例2は4.3/4.3、他は3.8/4.8を採用。coexist-results/manifest/probePDFに条件を保存。正解は独立21.5pt/bold/accent1。元データには四択質問欄がなく、元text/targetを本資料の見出しで表示する。

## 評価

正式CLUE Table2のWSC列9値を保持（63.45/62.41/63.38/61.54/63.44/61.04/62.44/72.07/81.38）。各モデル3回微調整し、開発成績最良のモデルでtestを報告。early stoppingでcheckpoint選択、ハイパーパラメータはdev調整。3回平均や3生成候補とは記さない。

人手は無作為test100件を3人が解き、94/97/95、平均95.3、多数決98。30–50件のdev演習と議論後の値。モデルの旧test290と評価母集団が異なる。課題repoREADMEのdev77.63/85.53や、CLUE現在READMEの旧WSC表を正式Table2へ混ぜない。現テストは正解欠落のため再採点値はない。

## CLEVA / HELM

Li et al. (2023), **CLEVA: Chinese Language Models EVAluation Platform**, EMNLP System Demonstrations, https://aclanthology.org/2023.emnlp-demo.17/ 。付録B.1.1でCLUEWSC採用、二値共参照判定、accuracyと例を確認。紙面引用年Xu2021は後続利用の参照であり、CLUEWSC2020初公開年を2021へ置換しない。

固定HELM v0.4.0 cleva_scenario.pyのCLEVACoreferenceResolutionScenario、Converter、提示方式分岐、infer_params読取を確認。run_specs_cleva_v1.confはcoreference_resolution prompt_id0–5。6IDをモデル数や試行数とみなさない。

Classic v0.4.0公開索引8526specとruns_to_run_suites名キーを実際に照合しCLEVA名0件。helm-index-check.jsonに原ファイルSHAと検索範囲を保存。英語WSCなど他のHELM課題の公開runが0だという主張ではない。

実装の配布URL http://39.108.215.175/data/v1/coreference_resolution.zip とhttps版を通常TLSで再試行したがIPと証明書名の不一致で取得不可。専有fetch-cleva-coreference-log.jsonに失敗を保持。継承proxy/TLS検証を維持し、無効化しない。したがってCLEVA選定版の全成員・件数、変換済みprompt、infer_params、具体的提示例数/温度/出力候補数は未取得・未確定。元CLUEの分割をCLEVAの実行条件へ補わない。新規モデル出力は生成していない。

## 権利・引用帰属

原文・データの出所はCLUEチームの公式GCS配布。課題固定repoはREADME一つで、データ専用LICENSEなし、GitHubAPIのlicenseもnull。CLUE本体のroot LICENSEも404。ベースラインコード個別のライセンスを文学作品テキストの権利へ拡張しない。13件の短い提供文を識別可能な原位置とともに引用し、新しい日本語意味訳を添えた。既刊の日本語訳を利用していない。元集合のデータライセンス、元作品の著者・作品・許諾範囲は未確定。原文学作品がpublic domainだとは主張しない。調査evidenceは原取得/検算記録であり、ギャラリー用データ全量再配布物を追加作成していない。

## 校正・実描画・技術検査

3skillsを継続適用、skill_based_codex、gemini_used=false。page-proofreading.jsonへ全頁の最終本文と校正項目、proofreading-changes.jsonへ実際のbefore/after/理由/頁を保存。コードは表示されたnative文字列を実行し元train681と一致。PPTXを固有LOプロフィールでPDFへ変換し全60頁とoverviewを作成。全60頁を個別目視し、最終変更頁も再目視。27引用/コード枠の実画素余白を測り、上下差を確認。native11表/1chart/1図、notes0。標準XSDは変更せず、新規問題と既存master由来11件を区別。URLはnative/PDF双方でURL文字だけ。各最終結果とhashはhandoffと監査JSONを参照。

## 独立レビュー完了

create_twitterが全60頁、原4412行/8824span、13原例とJP、9モデル値と7chart値、nativeコード、全技術とhashを独立照合して承認。p22の未取得提示例数を前提としない表現、p34不约而同の無打合せ含意を反映し、両頁再view・残58PNG不変を確認した。最終PPTX6e02728a65ba272589c588a8d2734b188526c1b68b0e249db1da87f72941d33e、PDF98617d59298f1d62661af36399233f4c04a8732c70f797d339b6a08be26aacc7。記録はreview-cluewsc2020/review.json、未解決0。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/cluewsc2020.json)、[実際の校正対](skill-proofreading/cluewsc2020.md)、[全ページ文言](skill-proofreading/cluewsc2020/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/cluewsc2020/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/cluewsc2020/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
