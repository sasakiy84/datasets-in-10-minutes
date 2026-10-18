# CrossWOZ 出典・再現・入手範囲

制作日2026-10-18、著者sasakiy84。本編34頁、全61頁。2020年はCrossWOZ初公開年（arXiv:2002.11893、TACL正式論文2020）。中国語・タスク指向対話。構築時の北京施設情報であり、現在の施設案内ではない。

## 一次資料

- Qi Zhu, Kaili Huang, Zheng Zhang, Xiaoyan Zhu, Minlie Huang (2020). **CrossWOZ: A Large-Scale Chinese Cross-Domain Task-Oriented Dialogue Dataset**. Transactions of the Association for Computational Linguistics 8:281–295. https://aclanthology.org/2020.tacl-1.19/ 。evidence/paper.pdf・paper.txtに保存。構築、5種類の目標、90人、品質、各部品と対話全体の評価。論文CC BY 4.0。
- 公式thu-coai/CrossWOZ https://github.com/thu-coai/CrossWOZ 。固定commit **df82c9fdff91b9b130f2d6b89110d3870ba6260e**。evidence/commit.json/tree.json、各fetch-logにURL・取得日時・bytes・SHA256。train/val/test ZIPは固定treeのgit blob SHA1にも一致。ZIP内JSON、DB、状態・行為、目標生成器、RuleDST評価器を直接調査。
- 固定データ https://github.com/thu-coai/CrossWOZ/tree/df82c9fdff91b9b130f2d6b89110d3870ba6260e/data/crosswoz 。analyze.py・stats_finalize.pyが3ZIP全件を再集計。6,012対話=5,012/500/500、101,626発話=84,692/8,458/8,476、sys50,813=42,346/4,229/4,238。発話は片側1回。分割は対話単位。
- DB https://github.com/thu-coai/CrossWOZ/tree/df82c9fdff91b9b130f2d6b89110d3870ba6260e/data/crosswoz/database 。観光465/飲食951/ホテル1133、地下鉄2549は駅数でなく3施設種の最寄り情報。タクシーは1テンプレート、#CX/#CPは実車ではない。
- RuleDST公式評価器 https://github.com/thu-coai/CrossWOZ/blob/df82c9fdff91b9b130f2d6b89110d3870ba6260e/convlab2/dst/rule/crosswoz/evaluate.py 。reproduce.pyは固定のRuleDST/Database/default_state/calculateJointState等の元コードを改変せず読み込む（必要依存だけを読み込む空のpackage initializerは別に用意）。公式test_sys_stateと同じ更新ループ。正解ユーザー行為と直前の正解状態を与え、sys_state_initからselectedResultsを除いた全スロットを照合。test4238中3023正解=71.3308%。S101/120、M863/1104、M+T535/653、CM1106/1745、CM+T418/616、紙の丸め6値に一致。履歴文から予測するTRADEと入力条件は異なる。再計算は規則のみ、学習済みモデルの新規実行はしていない。
- Yanyang Li, Jianqiao Zhao et al. (2023). **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations pp.186–217. https://aclanthology.org/2023.emnlp-demo.17/ 。CrossWOZ採用を示す。テレビ対話の原版一致は未確認のため13例には採用しない。
- HELM v0.4.0 CLEVAシナリオ https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py 。固定confはdialogue_generation/task_oriented、prompt_id0–2、version v1。evidence/cleva-scenario-v040.py。verify.pyは実際のprocess_dialogue_instanceをASTで抽出して公式全6012対話へ適用。元messagesをdialogueとして渡す範囲では、全sys数と13選択履歴/参照が一致する。未取得のCLEVAファイルwrapper・選定・テンプレート全体を復元した意味ではない。CLEVAが選定・整形した実v1集合は未取得。Classic v0.4.0公開8526runを走査しcleva/crosswoz該当0（evidence/release-scan.json）。原版50,813応答をCLEVA評価件数としない。

## 13実例の単位と日本語

examples.jsonは異なる13原対話。各unitは既存sys応答1件と、それより前の全messages。原応答全文と前方履歴全文を表示し、応答より後の発話は入力へ含めない。元対話全体/注釈はraw_recordとして保持し、canonical JSONのSHA256、split/ID、0-based配列範囲、固定URLを保存。役割ラベルは「利用者」「システム」として表示。中国語の発話内容は改変しない。日本語は本資料の訳で、施設種別・価格・評価・電話・位置・条件と原応答の内容を保持。新たな続きや回答は生成しない。

本編: test11732 sys1、train7568 sys5、test10113 sys5。
Appendix: test118 sys3、test9693 sys3、test10662 sys3、test10490 sys3、train8781 sys1、train9779 sys1、test10838 sys5、train8711 sys9、train7845 sys9、val12121 sys9。
最後のval12121はHELMホテル説明例の全履歴9発話と応答に対応。全13例をverify.pyで公式ZIPレコード/ハッシュ/全文/インデックスと直接照合済み。data-audit.json参照。

## 数値の意味

p22はモデル成績でなく3専門家が50対話806発話を注釈した品質確認。専門家間F1/状態94.59/93.55%、配布注釈との比較95.36/94.95%。p26のBERTNLU95.53/文脈なし91.85、TRADE36.08、SL policy44.92は原論文のtest報告で新規学習結果ではない。p28のS/CM+Tは各種類1000シミュレーション。DA76.5/15.7、NLTemplate67.4/10.0、NLSCLSTM60.6/9.0%。task finishは目標値が埋まる条件で、情報の正確さを別途保証しない。

## レイアウト・校正・監査

原文選択単位一頁を優先。13例を実際のnative PPTX/PDFへ両言語15.5pt履歴/21pt応答で試作、さらに不均等幅14.5ptを実描画。layout-decisions/unequal-decisions.jsonと試作PDF。長い例は原文/訳を別頁へ。長い各言語履歴は同一頁の左→右の2列で連続表示し、途中の内容は除かない。実例9は不均等幅で同居。最終応答は21pt太字えんじ、11native表・1nativechart・nativecode。39引用/コード枠の可視上下余白6.67–7.33pt。枠の実字形を含む編集可能範囲も監査。

全61頁を個別view_imageで読んで校正、overviewも確認。p2スクリーンショットは公式READMEを通常TLS・CSS込み取得しviewport1440x640の比率で配置。p42は参照訳を価格値を保って短文化し、末尾孤立行を修正・再目視。proofreading.jsonに頁別、proofreading-draft-changes.jsonに実際の修正対。method/review_mode=skill_based_codex、gemini_used=false。独立レビューは別担当に依頼する。

## 利用条件と同梱

公式リポジトリroot LICENSEはApache License 2.0。個別データ専用の別LICENSEや上流NOTICEは確認できなかったため、その範囲を越える独自の許諾は主張しない。READMEは論文引用を求める。本資料は13選択例の表示と日本語訳・役割表示・レイアウト変更を行った。元ライセンス本文、帰属、選択13件の識別/改変説明をcrosswoz-notices.zipへ同梱。NOTICE.txtは本資料作成者の説明で上流NOTICEを装わない。全文コーパスや不要な対話本文はZIPに含めない。

配布先: https://datasets-in-10-minutes.sasakiy84.net/assets/crosswoz-notices.zip （本PPTX/PDFのp33からリンク、統合時同時配布予定。現時点で公開済みとは主張しない）。ZIP内LICENSEは公式元バイトと同一。sidecar-audit.jsonにZIP3項目/bytes/hash/本文なしを記録。元の3全文ZIP/vendor/evidenceは検証用ローカルでありサイト配布対象に指定しない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/crosswoz.json)、[実際の校正対](skill-proofreading/crosswoz.md)、[全ページ文言](skill-proofreading/crosswoz/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/crosswoz/review.json)。
