# cMedQA2 — sources, scope, and verification

Japanese native PPTX/PDF for datasets in 10 minutes, sasakiy84. This is the original Chinese medical **answer-selection** dataset, distinct from the medical-examination MedQA dataset. It distinguishes original candidate labels, the HELM v0.4.0 public A/B example, and the unacquired converted CLEVA evaluation set.

## Original publication and what was obtained

Sheng Zhang, Xin Zhang, Hui Wang, Lixiang Guo, Shanshan Liu (2018). **Multi-Scale Attentive Interaction Networks for Chinese Medical Question Answer Selection**. IEEE Access 6, 74061–74071. DOI https://doi.org/10.1109/ACCESS.2018.2883637 . The official repository cites this work. Crossref and DOAJ metadata independently establish the formal title, five authors, year, venue, pages, DOI. DOAJ public abstract https://doaj.org/article/653d2813e83142db84670b2bb19a9b00 was read and preserved as evidence/doaj.json.

The abstract describes online medical communities where users ask qualified doctors, Chinese medical question-answer selection, multiscale deep semantic extraction, shortcut connections, and attentive interaction. It says the work updates/expands cMedQA v2.0 and outperforms earlier models, but supplies no score table. **The 2018 full paper was not obtained.** Normal publisher PDF/staging/stamp paths returned HTTP418; the document page returned 200 with zero bytes. Google returned a JavaScript interstitial, DuckDuckGo a human challenge (not solved), Bing returned unrelated dictionary results. All attempted URLs/results are in paper-fetch-log.json, paper-more-fetch-log.json, paper-search2-log.json, search-fetch-log.json, search-more-fetch-log.json. No score, learning rate, seed, trial count, collection site, or annotation method was inferred from an inaccessible full text.

## Fixed original distribution

Author repository https://github.com/zhangsheng93/cMedQA2 fixed commit **85feb9278c3ae552c591205cbf3e828368c91f8f** (2019-01-09). README, LICENSE and five ZIP archives were downloaded with normal TLS/proxy. URL/bytes/SHA-256 logs: fetch-fixed-log.json; expanded file SHA-256 and sizes: stats.json. Actual file names are question.csv, answer.csv, train_candidates.txt, dev_candidates.txt, test_candidates.txt. README refers to plural questions/answers; extracted archive names are preserved rather than renamed.

question.csv: 120,000 unique question IDs. answer.csv: 226,266 unique answer IDs, each with owner question_id and content. All candidate references exist. The candidate-used question IDs are 100,000/4,000/4,000; the unique positive answer IDs are 188,490/7,527/7,552. These sums,108,000 and203,569, match README, but are **not** the raw corpus row counts. Questions outside these three sets:12,000. Answers outside the positive-candidate sets:22,697, including22,404 owned by unused questions and293 owned by train questions but absent as positive candidates. Their generation history is unknown.

train has5,000,000 rows, exactly50 comparison triples per question: question_id,pos_ans_id,neg_ans_id. All positive answers belong to that question and all negative answers to a different question. There are188,783 raw answers owned by train questions, versus188,490 unique train positives. All226,266 answer IDs appear somewhere in the train negative pool. This is a shared candidate-answer pool; it is not described as a label-disjoint answer partition.

dev/test each have400,000 rows, exactly100 candidate rows per question: question_id,ans_id,cnt,label. For all800,000 candidates, label=1 **iff the answer's owner question ID equals the candidate question ID**. This checks recorded answer correspondence, not clinical truth, safety, quality, or an independent medical adjudication. Positives dev7,527/test7,552, negatives392,473/392,448. Positive counts per question:dev1–19, test1–41. Test distribution:1=2,350;2=841;3=404;4+=405. Native chart preserves these four counts. A constant-zero candidate classifier would have test accuracy392448/400000=98.112%; this is an arithmetic illustration, not a model result or a successful answer ranking.

All dev/test cnt values run0–99 in file order. Positives precede negatives for every question. cnt is not a predicted rank or score. Duplicate answer-ID occurrences within questions:dev89/test91. No question IDs overlap across splits; exact question-content string intersections are train–dev35/train–test46/dev–test1. ID partitioning and text uniqueness are different. Causes of duplicates were not assumed.

Mean Python Unicode len(content), using split question IDs and unique positive answer IDs: train47.94238/100.74451695; dev48.45825/100.47694965; test48.80525/99.60010593. README integer entries48/101,49/101,49/100 are shown separately; no cause of the small measurement/rounding differences is asserted.

## Public examples, original scope, and Japanese

examples.json preserves13 distinct question IDs, selected answers, raw question/answer/candidate records, 0-based rows, physical lines, raw/canonical SHA-256, fixed commit, source URL, CN and JP, and original label. There are6 positives and7 negatives. Each displayed original is the **full question plus one selected full candidate answer**, not all100 evaluation candidates or the entire training comparison set. Original answer prose, including questionable or mismatched medical statements and a patient-like text in the answer field, was retained. Translation does not repair or endorse it.

Example1 question24731702 / answer11064 is train comparison row0, and exactly matches the HELM medical docstring's patient/doctor content after whitespace normalization. Example2 test question4002896 / answer148636 is positive. Example3 dev33850817 / answer125372 is negative: the answer owner is36883628, even though both discuss cough. Further examples deliberately include overlapping topics; no label was changed on semantic or medical grounds.

Co-location was actually tested: coexist-probe used15pt CN3.5in/JP5.1in and default line spacing, which overflowed JP; coexist-probe2 used the same font/width with16.2pt line spacing and adjusted heading/footer positions. The latter fit the full pair; its native layout was adopted for example1. All other pairs use16.5pt CN4.1in/JP4.5in. All13 CN/JP pairs fit a single page. Original texts were never split to keep the translation alongside them. Actual glyph measurements set each quote frame to approximately8pt top/bottom;27 panels include26 quoted-language panels and1 native code panel. Labels use21.5pt bold accentB13731. Probe PDFs/PNGs are local layout evidence, not portable deliverables.

## CLEVA / HELM scope

Li et al. (2023). **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations186–217. https://aclanthology.org/2023.emnlp-demo.17/ . The Closed-Book QA section cites Zhang et al.(2018), describes the broader family as answering without extra information, and mentions exact match. This generic description does not establish the medical subtask's complete prompt/output form.

Fixed HELM v0.4.0 CLEVAClosedBookQuestionAnsweringScenario docstring instead shows the medical public example as patient+doctor text and **A.否 / B.是, Target B**. That A/B wording is retained as public-implementation evidence and is not a clinical-validation claim. Source: https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py . The Converter retains choices as references and marks the selected label with CORRECT; original numeric candidate labels and A/B labels are different representations, and all prompt candidate orders were not inferred.

Fixed run_specs_cleva_v1.conf has closed_book_question_answering / medical_question_answering prompt_id0–5. The public Classic v0.4.0 run index, release2023-11-17, has8,526 runs and0CLEVA/cMedQA2 matching runs. helm-index-check.json records input-release hashes and the exact search. Configuration count6 is not a count of completed runs. There are no acquired public model outputs or metrics to rescore. Actual shots, temperature, output count, truncation, prediction normalization, model scores, and prompt-specific medical scoring are not asserted.

The converted closed_book_question_answering.zip endpoint at39.108.215.175 failed ordinary TLS hostname verification over both advertised HTTP redirect and HTTPS. cleva-endpoint-probes.json preserves the failures. Converted train/test membership, prompts.json and infer_params were not obtained. Raw original108,000 used question IDs are not the CLEVA denominator and were not substituted for the selected evaluation set.

## Rights and portability

README explicitly says **non-commercial research**, v2.0, anonymized/no personal information per the distributor. Repository LICENSE is **GNU GPL v3**. No unsupported assumption that GPL applies only to code, or that the noncommercial condition is nullified, is made. These source statements and their unresolved scope relationship are both retained. Article metadata/abstract licensing is separate from data licensing. Medical raw records are local verification evidence; the portable whitelist contains only the13 sourced example pairs and aggregate/slide artifacts, not whole CSV/ZIP archives. Do not publish evidence/, vendor-like research raw files, or coexist-probe*/.

## Reproduction, actual proofreading and audits

analyze.py streams all5.8million candidate rows, joins original question/answer tables, asserts all ID and owner/label relations and computes stats.json. prepare.py extracts the13 actual records. build.py creates native text,10 native booktabs tables,1 native chart and references2/page from the common master. The adopted workflow additionally applies actual raster ink fitting and native layout fixes. Own LibreOffice profile /tmp/lo-helm-cmedqa2 is used. Shared engine/repository/Git were not modified. No model/generation API was called.

Final sequence: build/convert/render → ink_panels.py → convert/render → final_layout.py → final_native_fixes.py → add_appendix_navigation.py → convert/render → audit_layout/check_text/check_links/audit_package/measure_panels/verify. The latter navigation script is a one-time native insertion; final_native_fixes.py p11 positioning is one-time after the initial build. Do not apply those twice to the same final native file. build.py also carries the new Appendix navigation for future rebuilds; final artifacts and recorded hashes are authoritative.

Every final page is individually viewed and Japanese-proofread using skill_based_codex, no Gemini. Actual before/after changes are in proofreading-changes.json; no unchanged sentence is represented as an edit. All13 sources/content/labels, native tables/chart, native-vs-PDF text, all URL-only hyperlink rectangles, XSD/new package issues, empty notes, raster padding and final hashes are recorded in the audits/handoff. Independent reviewer: create_cnndm.

再構築時の注意：現在のbuild.pyはAppendix転換/目次を含む56頁版なので、上記の歴史的な最終同期手順にあるadd_appendix_navigation.pyは再実行しない。native生成→convert/render→ink fitting→再convert/render→final_layout→final_native_fixes→再convert/render→各監査・verifyを適用する。

独立レビュー修正：実例1の日本語を「妊娠2か月のときに1回、5か月のときに1回」とし、原回答の時点を明示。原CN/ラベル/数値は保持。p7を実再view、残55PNG不変、27枠/全監査/13例を再照合。実校正対は6件。最終hashはhandoff。

独立レビュー追加修正：p28は帰属・非商用条件と原文/訳/説明を区別する再利用説明、p29は固定版・hash・ID/候補行による原票参照説明へ。数値/原13例/条件は保持。変更2頁を個別再view、残54PNG不変、全監査0。実校正対10件。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/cmedqa2.json)、[実際の校正対](skill-proofreading/cmedqa2.md)、[全ページ文言](skill-proofreading/cmedqa2/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/cmedqa2/review.json)。
