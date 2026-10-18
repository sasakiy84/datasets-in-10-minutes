# CCPM — 一次調査・版・例・検査の記録

対象はCCPM (Chinese Classical Poetry Matching Dataset)。54頁、本編29頁、sasakiy84、所属なし、2026-10-18 JST。約10分の黙読・流し読みを想定、実際の読了時間は未計測。3skillsを適用し、外部生成API/Geminiは使用しない。

## 成立・書誌と一次資料

Wenhao Li, Fanchao Qi, Maosong Sun, Xiaoyuan Yi, Jiarui Zhang (2021), **CCPM: A Chinese Classical Poetry Matching Dataset**, arXiv:2106.01979v1, 2021-06-03。https://arxiv.org/abs/2106.01979 。公式arXiv HTMLのcitation_date、v1履歴、PDFヘッダーを照合。公式READMEもtechnical report/arXivとして引用し、CLEVA正式論文の参考文献もCoRR, abs/2106.01979とする。確認資料に査読付き会議・雑誌の別掲載先はなく、未確認の会議名を付けない。paper.pdf/txtは全文を読んだ。公式repoのCCPM_report.pdfも別取得・保存（arXiv PDFとはbytesが異なる）。

公式配布 https://github.com/THUNLP-AIPoet/CCPM 。default branchはmaster、READMEの正しい名前は**Readme.md**。main/README.md等の404履歴は削除せずfetch-log.jsonに残す。固定commit **e7db1a0dc1ac1ffdd0ec91f74793c29ae9c8efa5**（2021-08-21）。GitHub API repo/tree/latest commitと、全5ファイル（Readme.md/train.jsonl/valid.jsonl/test_public.jsonl/CCPM_report.pdf）を照合し、Git blob SHA-1をローカルbytesから再計算して全一致。詳細official-files-audit.json。train/testは別担当が同日に取得した原配布キャッシュをコピーし、独立に公式treeのblobで検証した。valid/Readme/reportは固定commit URLへ新規GET。元の共有調査フォルダは変更しない。

後利用一次文献：Yanyang Li et al. (2023), **CLEVA: Chinese Language Models EVAluation Platform**, Proceedings of EMNLP 2023: System Demonstrations, pp186–217, December6–10. https://aclanthology.org/2023.emnlp-demo.17/ 。evidence/cleva-paper.pdf/txtの古典中国語理解の説明、掲載CN例、参考文献を直接確認。未取得CLEVA原評価集合をCCPMの配布全件で代替したとは言わない。

検索モデル一次資料：Guo, Hu & Sun (2020), **BERT-CCPoem**, https://github.com/THUNLP-AIPoet/BERT-CCPoem 。取得READMEはCCPC-Full v1.0の926,024詩/8,933,162文と、モデル・詩句類似検索の構成を確認。CCPM本文では[CLS]表現を用いると記載される一方、BERT-CCPoem READMEのサンプルは平均表現である。CCPMの負例生成説明にはCCPMの[CLS]を採用し、READMEのサンプル処理へ置き換えていない。モデルのダウンロード/再学習/全コーパスの再検索は未実行。

BERTの正式書誌・題名はDevlin et al. (2019), **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**, NAACL-HLT、https://aclanthology.org/N19-1423/ の一次メタデータで確認。CCPMの二方式の条件はCCPM本文を根拠とする。

## 構築方法と元論文の報告

Web上の古典文と現代中国語訳の約6K段落から、句読点/Web行境界で分割。原資料はIntroductionに31K対と述べ、最終形式フィルタ後は27,218対。五言/七言の一行を選び、分けきれない二行の連続した意味の例も残す。作業者人数、個別Webページ、作者名/詩題の対応はこの配布にはないので逆算・推測しない。

負例：BERT-CCPoemの[CLS]ベクトル間コサイン類似度とLSHを使って検索し、0.4 LCS + 0.6 EMBで再順位付け。LCSは最長共通部分列（論文の英語はLongest Common Sequence）、EMBはベクトルのコサイン類似度。LCS値の正規化の細部は本文で明示されないので独自補完しない。最上位1件、2–5位から無作為1件、6–10位から無作為1件の三負例を正解とshuffleする。ネガティブ候補がすべて人手で誤り確認済みという主張はしない。

全27,218=学習21,778/検証2,720/テスト2,720。形式別（構築時Table1）：五言1行12,706、七言1行11,738、五言2行1,281、七言2行1,493。内訳もnative表で保持。配布のUnicode文字種から機械的に再分類した値とは区別する。

構築時評価Table2：BERT-Cls84.96%、BERT-Match82.60%、テスト。両者bert-base-chinese、Adam、初期lr2e-5線形減衰、4epochs。Clsは説明と候補を連結し[CLS]から一致二値分類、Matchは別々にBERT符号化してcosine最大候補を選択。検索用BERT-CCPoemとは別のモデル用途。公開テストの正解/保存予測がないため基準値を再採点・再学習していない。報告百分率から正解件数や試行数を逆算しない。

## 全配布の独立集計

`audit_data.py`/data-audit.json。全JSONLは候補数4。train/validのanswerは全件0–3。**test_publicの2720件は全件answer欠欄**。READMEの評価説明はaccuracy_score(trues,preds)だが、現在のtreeにeval.py/test_privateファイルはない。未配布の正解を原句の記憶等で推定して採点しない。

原文字列の完全一致（正規化なし）：
- train21,778問題一意/説明21,483種類、valid2,720/説明2,710、test_public2,720/説明2,716。
- 分割間の説明種類の積集合：train–valid65、train–test82、valid–test11。
- 説明＋四候補の積集合：0/1/0。共通1問はtrain14,734行とtest_public1,020行。これは元配布の一致であり、未取得CLEVA評価集合の混入率を表す値ではない。
- 各行に同じ候補の重複は0。
- 説明長（元文字列のPython len、句読点等を含む）：train min1/mean15.9409/max116、valid1/16.0544/87、test0/15.96875/80。
- test_public2,026行は説明空文字。回答を補っていない。
- train6,518行の正解「公曰：勿杀」は基本漢字4字で、五言/七言の形式に合わない少数例。train9,443行には拡張漢字㧐、train14,632/valid2,493行には文字コードのようなliteral表記がある。漢字基本ブロックだけを数えた集計を論文の形式数と同一視しない。元bytesを保持する。

正解位置の全件数：train0=5324/1=5455/2=5452/3=5547、valid0=709/1=677/2=661/3=673。stats.jsonは原論文の規模・baselineと、実測監査への参照を分離。

## 13実例の同定と翻訳

examples.jsonは全原JSONL行（終端改行込み）、行SHA-256、全ファイルSHA-256、byte offset、分割名/1始まり行、元record、全説明/四候補/answer、日本語の説明と四候補を保持。元recordにはIDがないため`train.jsonl:L14`等は**位置参照**であり元IDではない。original_id=null。13問は説明＋四候補で相異なる。

本編：train14（HELM docstring、answer0=A）、train18,823（CLEVA論文中国語例、answer3=D）、train14,876（CCPM README/図1、answer1=B）。追加10問：valid1/5/14/24/25/35/47/52/60/65。灯・泉・風・雨・修道/恋愛・領土・白髪・雲中の人・蝉・飛鳥を選び、五言/七言、一行/二行の幅を含めた。

**train18,823と21,287は現代語説明が同じで、四候補と正解位置が異なる。** CLEVA掲載例は前者と全候補一致。後者へ照合をすり替えない。後者は比較用補足表にのみ出し、13例に追加して数えない。

全13頁で原中国語説明＋四候補＋正解を一頁に保持。原文3.8inch/日本語4.8inch、双方15ptの不均等二列を実描画し、同居可能と確認した。原文を分割して訳のスペースを作っていない。正解21pt/bold/#B13731、候補順0–3→A–Dを維持。本文ラベルや改行は表示用に整形し、元bytesはJSONに別保存する。

日本語はこの資料の新規訳で、既存の訓読/日本語訳を引用しない。現代中国語の説明の訳と、古典候補の意味を別々に訳した。古典句にない主体や時制を説明に合わせて補わない。似た候補の意味が日本語で近くなる場合も、元ラベルを変えない。作者/詩題/全文出所は元レコード欠欄、全例poet_attribution/poem_title=null。短い句から帰属を推測して埋めない。

## CLEVA/HELMの範囲と取得制約

HELM v0.4.0 cleva_scenario.py / run_specs.py / run_specs_cleva_v1.confを取得。ClassicalChineseUnderstanding docstringはtrain14と説明・四候補・正解Aが一致。Converterはテンプレートでinput/choicesを作り、labelの位置が一致する候補へcorrect tagを付ける。0–5のprompt IDを設定。IDがあることと全テンプレート実本文の取得を混同しない。

HELM Classic v0.4.0固定公開run_specs全8,526中、CLEVAは0。helm-audit.jsonに元一覧SHAとfilter範囲を記録。コード既定joint max_train_instances5/max_tokens1/temperature0等は設定ファイルで上書きされ得るため、保存runで検証した実条件とは表現しない。この資料にHELM得点はない。

外部CCPM採用CLEVA ZIP `http://39.108.215.175/data/v1/classical_chinese_understanding.zip` はHTTPSへ移り、IPに対する証明書名不一致で取得できなかった（further-fetch.json）。通常のTLS検証を維持。CCPM原配布27,218をCLEVA全評価集合の復元だとは主張しない。CLEVA論文掲載例、HELM docstring、元配布との一致のみ確認。

## 権利と公開範囲

CCPM公式repoのlicenseメタデータはnull、treeにLICENSEなし。READMEはデータ利用時にCCPM技術報告の引用を求める。古典詩句自体、Webの現代語訳、収集データ、論文は権利の単位が異なり、全体に独自のCC/MIT等を付けない。作者/全文出所の未確認分を推定で帰属させない。公開用は出所付き13短問と新規日本語訳、集計、native図表。全JSONL/論文PDF/取得HTMLはローカル照合証跡であり、統合repoへ一括公開しない。

## 制作・校正・検証

master-guided-slides / dataset-introduction-slides / japanese-proofreading、method/review_mode=skill_based_codex、gemini_used=false。実際の変更前後をproofreading-changes.jsonに記録。原文/訳/正解、主述・助詞・修飾・並列、数値の単位/対象、否定、正式書誌を頁ごとに校正する。

PPTXからPDFへ変換し、全頁PNGとoverviewを生成。nativeテキスト・表・図、原文/訳全文、answer21pt色、引用/コード枠上下余白、脚注の非接触、URLのみリンク、XSD既存11/新規0を検査。実際の個別目視範囲と最終hashはpage-review.json/visual-review.json/handoff.jsonへ記録する。独立レビューはcreate_pile（review-ccpm）。未実施の確認を検査済みとはしない。

自己検査完了：全54頁を個別view、overview確認。変更p11/14/17/20/22/25/28/43/48/49は最終描画を再確認した。全13原問/JP15pt同居、正解21pt、全29引用/コード枠は実暗画素の上下余白を確認。最終実測はvisual-review.json。canonical handoffは独立レビュー待ち、成果物hashを固定。

独立レビュー2指摘を反映：p46比較単位を「全行の説明文と四候補」と明記、p53BERT文献紹介の孤立末尾を短文化。2頁を最終再view、全監査再合格。校正実修正対は計12対。承認待ち。

メインspot確認：p6Cの現JP「故郷は次第に遠くなるはずだ。」は原CN故乡应渐遥と正しく対応し、変更不要と確認。p7Dを「山の雨に、ようやく晴れる兆しが見え始めた。」へ自然化し、同頁のJP引用枠高さを実字形で調整、p6/7再view・全監査再合格。校正実修正対は13対。

メイン最終組版指示でp7C/Dを意味境界の明示改行へ変更し、末尾「た。」だけの孤立行を解消した。原文・日本語の意味・15pt・正解は維持。実変更対は文言修正13対＋改行のみ2対の計15対。最終p7再view・全監査再合格。

独立レビュー最終承認：create_pileが全54頁個別view、最終p7/46/53再view、13原例/JP/labels/全集計/正式一次資料/全文/29枠/54PDF描画同期/構造/URLと最終hashを独立確認しapproved=true、残件0。記録 `/workspace/artifacts/helm-parallel/review-ccpm/review.json` /review.md /handoff.json。最終PPTXca01549557ec94ad39e004c6ad341d2ec342bc135cbfadab3ff47ccbec12e582、PDF82e8bec9ff4bfc64eecc17f269b4a9df9292418c0a11afd7901ddaaeba7a9ef5。承認後成果物変更なし。

最終組版方針の訂正：メインが本文の少数字折返しを許容するskillを再確認し、p7 C/Dの一時的な明示改行を撤回。本文は自動折返しへ戻し、D自然化・全原CN・意味・15ptは保持した。校正最終差分は文言修正13対、一時改行2試験はtemporary-linebreak-trial-history.jsonへ分離し最終修正対に数えない。p7再目視、全技術監査・原票照合を再合格。最新hash {'pptx_sha256': '3561737576aa59007fa4ee5da80d247a7b126ddb5e19949abf6be9c96976df5b', 'pdf_sha256': '04eb2155ef634aec560ae7c2f1d0f14961b90c5199655ba3eb2a015a11bd5323'}

Pileは通常自動折返しへ戻した最終p7を再承認。最終35617375…/04eb2155…で独立承認・未解決0、canonical passed同期済み。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/ccpm.json)、[実際の校正対](skill-proofreading/ccpm.md)、[全ページ文言](skill-proofreading/ccpm/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/ccpm/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/ccpm/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
