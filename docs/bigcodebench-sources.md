# BigCodeBench: sources and editorial decisions

Collected 2026-10-22 from public primary sources; no model evaluation was run.

- Zhuo et al., **BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions**, ICLR 2025, arXiv v4 (2025-04-01): https://arxiv.org/abs/2406.15877 . Used for purpose, construction, Complete/Instruct, Full, task domains, test coverage and initial raw zero-shot/greedy Pass@1 comparisons.
- Official fixed dataset: https://huggingface.co/datasets/bigcode/bigcodebench/tree/b74c0d0bf70d2c0bc459be537895cca163007f1a . The v0.1.4 parquet has1,140 distinct tasks, 2,362,110 bytes. English originals/codeprefixes, canonical implementations and public tests for selected13 are in examples.json and raw/dataset.json. Main IDs25/140/32; Appendix19/52/56/60/110/145/148/408/536/26. No invented task/output used.
- Official repository: https://github.com/bigcode-project/bigcodebench . Used for evaluation environment and Apache2.0 code license. Actual upstream LICENSE retained; HF card also specifies Apache2.0. Attribution file explains reproduction and Japanese additions.
- Official project/leaderboard: https://bigcode-bench.github.io/ . Real styled screenshot captured after choosing Full; screenshot introduces site, not a separately claimed2026 performance table.
- Official Full results pin08ceb6b15ecd9c0f7c82932e4e248208ffeeb9b4: https://huggingface.co/datasets/bigcode/bigcodebench-results . Hard pin522a45334d838a87b421ac96db27b2ef7fc165bb: https://huggingface.co/datasets/bigcode/bigcodebench-hard-results .202rows each, latest model.date2025-04-14. The12 displayed values come from these fixed HF parquets; the websiteJSON differs and is not silently mixed. Prefill false/false/true is displayed for GPT4.1Mini/DeepSeekV3/Qwen2.5Coder32B. Prefill and calibrated setup repair are distinct.
- Zhuo (2024), **Introducing BigCodeBench-Hard**: https://huggingface.co/blog/terryyz/bigcodebench-hard . Used for Hard148 selection and cheaper difficult subset. Disputed fine thresholds/reference-length units omitted.
- Lee, Chen and Korbak (2026), **Training Agents to Self-Report Misbehavior**: https://arxiv.org/abs/2602.22303 ; OpenAI Alignment article2026-03-21 https://alignment.openai.com/self-incrimination/ ; public implementation https://github.com/brucewlee/self-incrimination . Documents continuing use of Full1140 Complete among seven general capability checks after training. GPT4.1/GPT4.1mini/Gemini2.0Flash; no invented Astra/Fable adoption or new score.

## Example and translation scope

Every original Instruct natural-language word and codeprefix is retained on one originalpage; Markdown fence delimiterlines are represented by native monospaced codeformatting. JP translates every natural-language instruction; codeprefix stays in English on the originalpage. Expected behavior is a static interpretation of the actual supplied tests, not an evaluated output. IDs25/26 distinguish base64 encoding from encryption;26 has random ciphertext so no fixed goldstring.145 explicitly labels mocked2addresses.148 English Encrypt is translated as integerencoding to reflect LabelEncoder/reference/test behavior.536 shows Instruct's absolute path rather than Complete's inconsistent relativeexample.

A bilingual layout was actually rendered and accepted for536:17.5pt original plus17.5pt JP, followed by expectedbehavior/testdetail page. Original25/32/60 need roughly197–217pt at18.5pt before JP; combining fullJP and21pt expectedbehavior would crowd source/footer. Original-first separate pages preserve readable question and meaningful expectedbehavior. One original was never split just to add JP.

The website/cardless publication year is recorded n.d. with actual accessdate; paper and datedblog use their verified years. SHA/repro details remain in records, not teaching slides.

## Quality evidence

Creator and independent reviewer scope are separate. Creator actually viewed candidate1 pages1–59 individually at1600px and recorded batch issues. Final modifiedpages are reopened; unchangedpages are checked by a rawpixel bridge against that own actuallyviewed baseline. Structural/schema/native/render/table/ink/link audits bind exact artifacts; supported schema divergence is recorded as known valid-range buSzPct integer lexical parsing by the installed OOXML schema, not claimed clean vanilla XSD.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-bigcodebench.pptx)・[PDF](../slides/datasets-in-10-minutes-bigcodebench.pdf)。本編31頁、総59頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/bigcodebench.json)・[校正の修正対](skill-proofreading/bigcodebench.md)・[全ページ文言](skill-proofreading/bigcodebench/pages.jsonl)・[最終検証票](skill-proofreading/bigcodebench/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-BigCodeBench-Apache-2.0.txt](licenses/bigcodebench/LICENSE-BigCodeBench-Apache-2.0.txt)、[ATTRIBUTION-BigCodeBench.txt](licenses/bigcodebench/ATTRIBUTION-BigCodeBench.txt)。
