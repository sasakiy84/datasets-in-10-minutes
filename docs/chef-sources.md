# CHEF — 出典・調査範囲

2026-10-18取得。原配布とCLEVA採用版を分けて記録する。

- Hu, Xuming; Guo, Zhijiang; Wu, Guanyu; Liu, Aiwei; Wen, Lijie; Yu, Philip S. **CHEF: A Pilot Chinese Dataset for Evidence-Based Fact-Checking**. NAACL-HLT 2022, pp.3362–3376. Hu/Guo同等貢献。正式PDF/HTMLをevidence/paper.*へ取得。https://aclanthology.org/2022.naacl-main.246/
- 公式THU-BPM/CHEF、commit `8909b3035c14437b55154a341060b6a1866c9ba1`。READMEのDriveリンクから原CHEF.tar.gzを取得。https://github.com/THU-BPM/CHEF
- 原アーカイブ38,326,111 bytes、SHA256 `398329d698aed5ce185751ac6b42f5e6567bb621cbe7af993f583fa0387b2487`。https://drive.google.com/file/d/1QKe9i-yXDKh87p4ukRFSnzE03-hAzMto/view
- Li, Yanyang et al. **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations 2023, pp.186–217. 正式PDF/text取得。https://aclanthology.org/2023.emnlp-demo.17/
- HELM v0.4.0 CLEVA scenarioのdocstringに金星主張と3選択肢・Target Aを確認。https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py

## 原データと全件集計

原train/dev/testを実取得・JSON読込した。Pipeline claim_gold.json合成入力は原配布の代用品として使用していない。train8002/dev999/test999、全10000。原ラベル0/1/2は支持/反証/情報不足。全体3543/5015/1442。train2877/4349/776、dev/testは各333ずつ。stats.json、nonempty-audit.jsonに全件集計。

論文Table4のtrain反証4399と原配布4349は50件差。論文のtrain各ラベル和8052は記載合計8002と異なる。Table3のJiaozhen157/Cnews2689に対し原配布56/2789。Piyao3741に加え原表記違い1件、領域は論文5領域に対し原配布に生活7件がある。原因は確定しない。公式issue4は利用者の指摘であり作者回答は取得したcommentsでは空。版変更・転記誤りと断定しない。

gold欄は全行にあるが非空の根拠文0件の行が2158件。支持394/反証897/情報不足867。根拠文非空19885、検索文書欄50000slotのうち非空43072。この欠測と、論文が初期収集段階で除いた5.6%の候補を混同しない。claimId文字列の重複超過851、claim文字列重複超過369。

## 13例と表示範囲

examples-source.json/examples.jsonに原レコード・原ファイルSHA・レコードSHA・split/0始まりrow/claimId・原labelを保持。主張と全非空gold evidenceを全文表示し、日本語訳を自作。検索文書の全文は表示範囲に含めず、raw recordとして保持する。重複したgold文も消さない。labelは原配布の注釈であり本資料で新規モデルを実行した正解率ではない。

本編3例はtrain128金星/train3728成都/test701白いコウモリ。金星claimId977は元train128に一致。前調査のPipeline配列番号1127と原row128は別の索引。両者0始まり。13例は原文の誤字・古い数値・根拠中の記述を補正せず保持し、現時点の事実断定と区別する。

15pt・中国語4.0in/日本語4.6inの不均等2列で13件を実描画した。初回13頁は全て個別view。空段落除去後に再測定し、最終実例全頁も個別view。実例1/3/5/7/9/10/13は同居、2/4/6/8/11/12は原文1頁＋訳1頁。原文と根拠を切り詰めず、最小15ptを保持する。試行はevidence/coexist-probe-initial とcoexist-probe、決定はlayout-decisions.json。最終29枠の実glyph上下余白はpanel-visible-gaps.json参照。

## 評価条件とCLEVAの限界

元論文Table5は各モデル5独立実行の平均±標準偏差。結果は発表値で、新規再学習はしていない。Micro F1とMacro F1を区別、単一3分類のMicro F1は正解率に一致。Goldを使う条件は自動検索の条件と分ける。70組の数値を一次PDFから抽出してresults.py・6native表と照合し、5点のnative棒グラフも確認。

CLEVA v1 fact_checking.zipは通常TLSの取得を試みたがIP/証明書ホスト名不一致で取得できず、CLEVA翻訳集合・全件・入力選択・採用版は未確認。設定の6prompt_idと実際の全採用入力を同一視しない。公開コードの金星例は主張と選択肢だけで、元CHEFの根拠付き検証と区別する。HELM Classic固定v0.4.0公開run一覧で該当0件を確認したが、CLEVA研究全体の試行数0を意味しない。

## 権利・再現・品質

公式repo直下のデータ全体LICENSEは確認できず、repo API licenseはnull。Joint/LICENSEのMITはJ. Bastings名義の取り込みコードで、全データへの許諾と断定しない。元記事の著作権は各提供元に帰属する。研究紹介に必要な13主張・注釈根拠を出典とともに引用し、自作訳を添える。記事全体をスライドへ転載しない。

Native PPTXの13表・1chart・図・コード・引用は編集可能。マスターの既存XSD11件と新規エラー0を分離。全65頁を個別viewし、全本文を日本語校正。14局所修正後の10頁を再view。参考文献は各頁2件、20本の配布ラベル/公開例答えは21pt bold #B13731。本文/表の全文・原例・日本語訳・notes0・URL61件・最終PPTX→PDF同期を検査。実修正前後はproofreading-changes.json、検査はcontent-audit/layout-audit/package-audit/links-audit。

再生成順：choose_examples.py → prepare.py → build.py → convert.py → render.py → ink_panels.py → convert.py → render.py → audit_content.py/audit_layout.py/audit_package.py/check_links.py → records.py。描画と校正の実目視は自動化記録で代用しない。途中修正パッチapply_proofreading.py/final_local_fixes.pyは現ソースへ反映済みで再実行不要。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/chef.json)、[実際の校正対](skill-proofreading/chef.md)、[全ページ文言](skill-proofreading/chef/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/chef/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/chef/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
