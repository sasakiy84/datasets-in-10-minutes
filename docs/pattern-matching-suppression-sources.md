# Pattern Matching Suppression — 原資料・実データ・検査

著者sasakiy84、2026-10-18制作。本編30頁/全54頁。ギャラリー名Pattern Matching Suppression、構築論文の表記Pattern Match Suppressionを表紙で併記。year2022は公式Second Round Winnersの引用年。使用した固定データは2023年3月公開版。論文TMLR2023と今回のarXiv v2改訂2024を区別する。

## 一次資料と取得

- Tomasz Korbakが課題提出者。公式 **Inverse Scaling Prize: Second Round Winners**, McKenzie et al. (2022). https://irmckenzie.co.uk/round2/ 。原例と提出者・課題趣旨・受賞を説明。evidence/round2.html/txt。年根拠は公式root READMEの受賞発表引用年で、公開ZIPの年を2022へ置き換えたものではない。
- Ian R. McKenzie et al. (2023). **Inverse Scaling: When Bigger Isn’t Better**. Transactions on Machine Learning Research, October 2023. https://arxiv.org/abs/2306.09479 。今回取得はarXiv v2、2024-05-13改訂、表紙にTMLR10/2023。§3.3.1は提出者、原例、unexpectedの曖昧性、規模に対する傾向。§2/§3はclassification評価/人との一致、Table1は1428件/100.0%、§5.2はfew-shot。正式PDFはevidence/paper.pdf、原取得URL/bytes/SHAはfetch-log.json。Redefine制作時の同じ一次取得物を本専用dirへコピーし、バイトを保持。
- 公式 https://github.com/inverse-scaling/prize 、固定commit **920f17de85f2a7f2415b097bc49e6a7fbf17b0b2**。
- データZIP https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip 。2,098,995bytes、SHA256 85240e3fe11822fa3152bdb99e15c5956a8128632ad40fcf94b8e8a0119071b5。Redefine制作時に固定rawのZIP/README2件へ実GETし、先行キャッシュとbyte一致を確認（fixed-download-log.json）。本専用dirではZIP内pattern-matching-suppression_classification.jsonlが原ファイルとbyte一致、archive-check.json。別課題ファイルを代用品にしていない。
- **Data release** https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/README.md 。1課題1JSONL、part/round、候補形式、few-shot作成、CC BY4.0を定義。root READMEは2023-03-01のデータ公開を記載。
- Yanyang Li et al. (2023). **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations pp.186–217. https://aclanthology.org/2023.emnlp-demo.17/ 。指示追従の下位課題へ採用。
- HELM v0.4.0 **CLEVAInstructionFollowingScenario** https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py 。evidence/cleva-scenario-v040.py。固定conf instruction_following/pattern_matching_suppression、prompt_id0/1、version v1はcleva-config-selected.json（先行固定公式conf取得物から抽出）。

## 全件再集計・正解・原版の不整合

prepare.pyは原JSONL全1428件を直接読み、classesをast.literal_evalで解析。全件round2/part1、候補は異なる2文字列、answer_index=1、promptは全一意。train/dev/test指定なし。12記号対それぞれ119件、各記号対に17指示表現×完成長7種類（6/8/10/12/14/16/20）。各完成長204件で、提示長は5/7/9/11/13/15/19。終端表現はunexpectedly420、unpredictably336、violate336、except336。

全1428行で、提示列が二記号の交互列、長さが指定より1少ない、通常の次記号がclasses[0]、直前と同じ記号がclasses[1]/配布正解であると検算。exceptで除く文字列も通常の次記号と一致。all-structural-checks.jsonへ各行の検算結果を保持する。これは配布正解の構造検算であり、曖昧なunexpectedという指示の一意性まで証明した意味ではない。構築論文もunexpectedの意味の特定不足を限界とする。

**直接取得した原配布に表示不整合がある。** 6群（i/ii、one/two、aa/ab、alpha/beta、first/second、left/right）の全119件ずつ、合計714件では、指示中の集合名がそれぞれ `i i` / `one` / `aa `（末尾空白）/ `alp` / `fir` / `lef` になっている。提示列と候補は完全。全行で集合名が完全な記号対文字列の先頭3文字に一致するという観察は確認したが、生成器の実装・原因は未確認。元の指示を勝手に直さず、p18/p48と該当6実例のmetadata/解説へ明示する。p18等の一覧ではaaと短く表示するが、実例/JSONL/native原文は末尾空白も保持。論文のunexpected曖昧性とは別の観察。

候補順にも表現差がある。構築論文のA/B例はclasses=[A,B]で正解A/位置0、公式JSONLの同じ指示はclasses=[B,A]で正解A/位置1。意味は整合する。元の確率評価では候補配列は採点側の情報で、promptに候補位置が見えていると決めつけない。index1だけ選ぶ仕組みの100%をモデルの指示追従成績とはしていない。

## 13例と日本語・CLEVA範囲

本編3原行は1始まり1310/7/29、Appendix10原行は120/239/358/477/596/715/834/953/1072/1191。全12記号対を覆い、A/Bは長さ20と明示的exceptの異なる原行を採用。全13は指示・提示列・二候補の全文で、原文を一頁に保ち日本語と同居。i/ii、one/two、alpha/beta等はこの課題のリテラル記号名なので、訳でも文字列を変更しない（p6で説明）。日本語の指示/解説は本資料で作成。不存在の続きは生成せず、answer_indexが指す原候補を表示する。

examples.jsonにrow0/line1/原record/原prompt・classes_raw/解析後候補/原正解/訳/解説/構造判定/fileSHA/raw_lineSHA/canonical recordSHA/URL/表示範囲。raw_lineSHAは改行なし元行bytes、recordSHAはensure_ascii=False/sort_keys=True/separators=(',',':')のcanonical UTF8。verify.pyは原行/hash、元prompt・候補のnative完全保持、PDF全文/訳/解説と21ptboldえんじの配布答えを照合。p49 native Pythonも実際に実行しoを確認。

HELM公開docstringの中国語o/x例/候補x,o/TargetBは原JSONL1310行（row1309）に一致。p27で説明例全文と訳、実例1で元英語を示す。同じ原例の重複を別の独立レコードとして13件へ足していない。

CLEVAが選定・翻訳・整形した実v1配布集合は未取得。IPアクセスのhttps証明書ホスト名不一致という先行結果を保持し、TLS無効化はしない。元英語1428件をCLEVA評価件数とはしない。Classic固定v0.4.0公開8526runを再走査しcleva/本課題に該当0、evidence/release-scan.json。元InverseScaling研究に試行がなかったという意味ではない。

## 評価と報告の条件

元classificationは、prompt後に候補文字列全体が出る条件付き確率を候補内で正規化。正解の負対数を平均するlossと、最大確率候補のaccuracy。全語彙に対する単純確率や自由生成列全体の完全一致と混同しない。候補先頭空白保持。

人の一致100.0%は無作為に少なくとも50例を人が解いて提出ラベルと比べた報告値。全1428件の再注釈率やモデル値ではない。§3.3.1の規模依存の観察を文章で保持。最小モデルはGPT-3系列を除き非ゼロ、大きい側で非ゼロだったのはGPT-4/GPT-4 RLHF/GPT-3 FeedME、全般に低成績との記述を参照。図の点を読み取って精密な値の新表は作らない。

§5.2は0～最大72-shot/文脈長制限、Anthropic LM/Gopher/Chinchilla。例示で本課題の傾向がU字/通常方向へ改善するという報告。任意の現行モデルへ一般化せず、新規の学習済みモデル推論は行っていない。nativechartは完成長ごとの原データ件数204×7で、モデル成績を装っていない。

## 権利と品質

原データは公開README/公式root LICENSEのCC BY4.0。課題Tomasz Korbak、公開元Inverse Scaling Prize、研究McKenzie et al.へ帰属。https://creativecommons.org/licenses/by/4.0/ を参考文献に明示。変更は本資料の訳/解説・段組・表示上の改行/候補フィールド整理。原英語・原正解・不整合集合名を保持。

公式README画面は同じ公式Prizeリポジトリの実ブラウザ画像をRedefine制作時の通常TLS取得から無改変で再利用（screenshot-log.jsonに明記）、CSS34/assetfail0、1440x640の比率を保持。今回の最終p2も実目視。

13件の英日同頁を実PDF試作。初回は3例の解説が脚注に近く、実際に短文化し、追加空段落を除き引用開始を上げて再試作。原文を削らず全13例成立、initial-layout-* / layout-trial.* / layout-decisions.json。最終引用/コード29枠は可視上下6.67–7.33pt、参照答えは引用下10ptへ統一、14答え21ptbold B13731。native6表1chart1code。uniqueLOprofile /tmp/lo-helm-pattern-matching-suppression。

全54頁を一頁ずつview_imageで読み、overviewを確認。最終14応答頁を個別に確認し、既に閲覧した11応答頁とp53文献説明を再view。実日本語修正対・頁別最終文言はproofreading.json。method/review_mode=skill_based_codex、gemini_used=false。native404段落66セル/重複0、layout394段落61セル問題0、新XSD0（master既存11）、50URL-only一致、notes0、全54PNGは最終PDF再描画の画素と一致。最終hashはhandoff.json。独立レビューを別担当へ依頼。

再生成: prepare.py→build.py→convert/render→fit_native.py→convert/render→ink_panels.py→convert/render→position_responses.py→convert/render→native_final.py/audit_layout.py/audit_package.py/check_links.py/ink_panels.py --check→verify.py/records.py。途中のrefine.pyはソースへ反映済みで再実行不要。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/pattern-matching-suppression.json)、[実際の校正対](skill-proofreading/pattern-matching-suppression.md)、[全ページ文言](skill-proofreading/pattern-matching-suppression/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/pattern-matching-suppression/review.json)。
