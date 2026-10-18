# Redefine — 一次資料・原データ・版・検証

著者sasakiy84、制作2026-10-18（表紙JST）。本編29頁/全53頁、3+10の13例。年2022は公式第1回受賞発表でredefine-mathとして公表された年。使用データは2023年3月の公開Round2更新版であり、旧Round1版は含まれない。

## 一次資料と固定版

- Xudong ShenがRedefineを提出。公式 **Inverse Scaling Prize: First Round Winners**（2022） https://irmckenzie.co.uk/round1/ にredefine-mathと提出者・狙いを記載。**Second Round Winners** https://irmckenzie.co.uk/round2/ は前回受賞2課題への更新受理を記載。evidence/round1.html/txt、round2.html/txt。
- Ian R. McKenzie et al. (2023). **Inverse Scaling: When Bigger Isn’t Better**. Transactions on Machine Learning Research, October 2023. https://arxiv.org/abs/2306.09479 。今回の取得PDFはarXiv v2、2024-05-13改訂、表紙はTMLR10/2023。投稿年と改訂年を区別する。§3.1.3はRedefine/提出者/二候補/正解定義/ゼロショットの傾向、Table1は1244件と人の一致100.0、§2と§3は評価/人手確認、§5.2はfew-shot。論文の図から精密な点数を読み取って新しい成績表にしない。
- 公式リポジトリ https://github.com/inverse-scaling/prize 、固定commit **920f17de85f2a7f2415b097bc49e6a7fbf17b0b2**。root README・data-release README・ZIPは固定rawへGETし、先行キャッシュとbyte一致を確認。evidence/fixed-download-log.json。
- 公開ZIP https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip 。2,098,995bytes、SHA256 85240e3fe11822fa3152bdb99e15c5956a8128632ad40fcf94b8e8a0119071b5。ZIP中のredefine_classification.jsonlと取得ファイルのbyte一致をarchive-check.jsonへ記録。生データ・ハッシュはevidenceに保持。
- **Data release** https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/README.md 。redefineはRound2更新版のみ。Round1のredefine-mathを落とし、賞の評価前に重複除去。part/roundの意味、classification形式、few-shot構成方法、CC BY4.0を明記。公式READMEは2023-03-01公開と記載する。
- Yanyang Li et al. (2023). **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations pp.186–217. https://aclanthology.org/2023.emnlp-demo.17/ 。Redefineを指示追従素材として採用する。
- HELM v0.4.0 **CLEVAInstructionFollowingScenario** https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py 。evidence/cleva-scenario-v040.pyに固定コード。evidence/cleva-config-selected.jsonはinstruction_following/redefine、prompt_id0/1、v1。元confはcleva-inventoryの固定一次取得物。公開説明例の中国語「将e视为48+12。问：e的第一位数字是啥？答：」/候補6・2/TargetAは、原英語610行目（0始まり609）に対応する。元英語と日本語訳は実例1、公開中国語説明例と訳はp27。説明例の対応を、CLEVA全採用集合の取得と同一視しない。

## 全件再集計と実例

prepare.pyが原JSONL全1244件を直接JSON読込し、classesをast.literal_evalで解析する。全件2つの異なる候補、answer_index0/1、round=2、prompt一意1244。part1=900/part2=344、answer_index0=572/1=672。part1は0=400/1=500、part2は0/1各172。元ファイルにtrain/dev/test指定なし。

part1は各100件の9連続ブロック（1始まり1–100/101–200/201–300/301–400/401–500/501–600/601–700/701–800/801–900）。文字列の先頭、+や÷の数字としての扱い、π/eの整数・加算式・剰余式という指示に応じ、900件全ての期待数字を別計算して配布正解に一致。文字列として読む指示で無断に加算/除算しない。part2全344件について形式・配布値は検査したが、全件の意味判断を機械的に正しいと証明したとはしない。採用した4件は日本語と意味を個別確認。

13実例の行（1始まり）は610/1/1001（本編）、101/201/301/401/501/701/801/1113/1191/1244（Appendix）。異なる13原行のprompt・二候補を全文、原順・先頭空白を英語側に保持。classes_rawはPython形式の文字列で、解析後の候補配列も別保存。選択肢をpromptのA/Bと偽って混ぜない。A:は元promptの回答位置。日本語側は語を再定義する際に参照対象が変わらないよう、polite/rude等の語を原綴りで保ち、解説で日本語の意味を示す。No/Yes候補は日本語側でいいえ/はい、配布答えにも訳を併記。原文の回答内容を生成し直さず、answer_indexと原候補の文字列を示す。

examples.jsonは原行番号・row0・原レコード・fileSHA・raw_lineSHA・canonical recordSHA・原prompt/classes/正解・訳・説明・範囲。raw_lineSHAは改行を除いた元JSONL行のbytes、recordSHAはUTF8/ensure_ascii=False/sort_keys=True/separators=(',',':')のcanonical JSON。verify.pyは原位置・hashとnative/PDFの全文を再照合する。

## 評価条件と限界

元classificationは、各候補文字列全体の条件付き確率を二候補内で正規化し、正解候補の負対数を平均するlossと、最大確率候補のaccuracyを扱う。全語彙に対する正解の単純確率や、自由生成の完全一致ではない。全公開例の候補文字列先頭空白を保つ。

論文Table1の人の一致100.0%は、各part50例から算出して平均する人手確認方式の報告。1244全件の人手再注釈やモデル点数とはしない。§3.1.3のゼロショット傾向（全系列で最大モデル<最小モデル、最小は全系列ランダム超、最大は半数超の系列がランダム以下）を文章で保持し、図から数値を捏造しない。§5.2のfew-shotは0～最大72例または文脈長の限界、Anthropic LM/Gopher/Chinchilla。GopherのRedefineはinverse/inverted-U傾向が残る。現行モデル全体や任意の規模へ一般化しない。

公式公開READMEのfew-shotは、対象promptを除く全例から重複なし抽出、正解付きpromptを3改行で連結。元英語配布に学習用分割があるという意味ではない。

CLEVAが選定・翻訳・整形した実v1配布集合は未取得。既存調査はIPアクセスのhttp→https転送後に証明書ホスト名不一致を確認し、通常TLSを無効化しない。Classic固定v0.4.0公開8526runを再走査しcleva/redefine該当0、evidence/release-scan.json。この0は元InverseScaling研究のモデル試行がないという意味ではない。本資料でモデルの新規学習・推論を行っていない。

## 権利・表示変更

公式データ公開READMEおよびroot LICENSEはCC BY4.0。帰属は課題提出者Xudong Shen、Inverse Scaling Prize公開版、McKenzie et al.研究に向ける。https://creativecommons.org/licenses/by/4.0/ をPPTX/PDF参考文献へURLとして付記。変更は本資料による日本語訳・解説、改行・段組と候補フィールドの見やすい表示。原英語prompt/候補/配布正解は保持し、CLEVA翻訳集合を再配布したとはしない。

## 品質と再生成

53頁を最終PPTXからPDF、uniqueLOprofile /tmp/lo-helm-redefine。native6表/1chart/1code、29quote/code枠。原文一頁優先の英日2列を全13例で実PDF試作。初回は例11の解説が脚注に近く、実際に短文化して再試作し、全13が成立。initial-layout-*とlayout-trial.* / layout-decisions.json。最終ではNo/Yesの日本語候補も明示。原文は切っていない。

公式画面は通常TLS・CSS34/assetfailure0のブラウザ描画、1440x640を同比率で配置。GitHub READMEのタイトル・課題趣旨・公開履歴が見える位置を採用。試した未採用キャプチャを最終確認と誤記しない。

全最終頁は個別view_imageで日本語・原文・余白・出典を確認し、overviewも確認する。実際の修正対と頁別記録はproofreading.json、method/review_mode=skill_based_codex、gemini_used=false。native字形/編集可能枠・重複・XSD既存11/新規・notes0・50URL-only・PDF/PNG画素同期をnative-final-audit/layout/package/links/panel-ink-auditへ保存。具体的な最終hashと検査数はhandoff.jsonを参照。独立レビューは別担当。

再生成順: prepare.py→build.py→convert.py redefine→render.py redefine→fit_native.py→convert/render→ink_panels.py→convert/render→native_final.py/audit_layout.py/audit_package.py/check_links.py/ink_panels.py --check→verify.py/records.py。日本語修正は最終ソースへ反映済み。途中のapply_proofreading.py/translate_choices.pyは再実行不要。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/redefine.json)、[実際の校正対](skill-proofreading/redefine.md)、[全ページ文言](skill-proofreading/redefine/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/redefine/review.json)。
