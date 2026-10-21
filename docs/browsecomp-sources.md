# BrowseComp primary-source research

Creator /root/review_programbench, 2026-10-22 Asia/Tokyo. New primary research; original programs/tests/models and model APIs not executed. Public web downloads use inherited proxy and CA with explicit additional network permission. No credential reads, Git operations, interactive login, access-gate bypass or subagents.

## Independently acquired sources

- Wei et al. (2025), *BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents*. https://arxiv.org/abs/2504.12516 ; HTML v1 saved under raw/paper.html and cleaned text. Original paper title, author list, 1266 questions, human construction, topic distribution, human investigation, semantic grading, original model table and compute scaling read directly. BrowseComp expands to Browsing Competition (paper/article).
- OpenAI (2025-04-10), *BrowseComp: a benchmark for browsing agents*. https://openai.com/index/browsecomp/ . Saved raw/project.html and clean text. Official article screenshot captured live with CSS/fonts/hero loaded, no cookie panel, inspected by creator. screenshot-log.json records runtime response/assets. Asset initialization analytics failures did not affect visible article.
- OpenAI simple-evals official repository. https://github.com/openai/simple-evals . raw/README.md, browsecomp_eval.py, LICENSE, revision.json and repo-tree.json. Code MIT license. Public grader rubric asks whether final extracted answer is semantically equivalent to the reference; numeric tolerance allowed. Current source contains a match.group(0) versus 'yes' return comparison inconsistency; no evaluation was run, and reported scores/scoring interpretation come from paper/official article, not a claim that this checkout reproduces them.
- OpenAI official Hugging Face dataset *BrowseComp Long Context*. https://huggingface.co/datasets/openai/BrowseCompLongContext . Ungated, MIT metadata, README and complete JSONL independently downloaded. Card explicitly states this is a subset of BrowseComp and uses the original questions, adding human-reviewed required URLs and supplementary URLs. File has295 records. Public README's documented SHA256/XOR/base64 decoding procedure reimplemented locally for static reading, with each row's public canary; no API calls or original code execution. Source questions and reference answers are preserved verbatim in examples-source.json/examples.json. Dataset metadata/card and code license are distinct evidence.
- OpenAI (2026), *GPT-6 Astra*. https://openai.com/index/gpt-6-astra/ . Newly acquired raw/astra.html,clean text. Professional table names BrowseComp and gives Astra91.5, GPT5.6Sol90.4, Fable5 87.4, Opus5 90.8. Page also names Mind2Web in a1.9x task-completion-speed comparison; that is reserved for the Mind2Web deck. Scores do not imply same harness as2025 paper; each table has its own source/year/context.

## Example scope and public-use conditions

Exactly13 distinct original questions from the official295-record long-context subset: zero-based source rows2,14,238,194,107,108,267,102,115,80,37,215,254. Main3, Appendix10. The source is explicitly stated before the first example and in every example footer. BrowseComp's population remains1266 questions;295 describes the official derived collection used to obtain examples. We do not describe the original web-search task as a supplied-context task, or compare long-context scores to agentic scores.

The paper/article ask that examples not be republished in plaintext or images online to reduce contamination and answer leakage. This is recorded as an author request, not a license prohibition. Official OpenAI HF dataset card explicitly licenses the question/answer/URL dataset MIT. The user requested source-linked genuine examples;13 are educational excerpts from that official public licensed subset. Preserve MIT notice in raw/LICENSE and official-hf-readme.md. Do not silently assign the nonofficial smolagents mirror's Apache metadata to OpenAI data. Only that mirror's metadata/card was inspected during discovery; example content comes solely from official OpenAI HF.

## Access limitations and provenance

Original official Azure CSV endpoint https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv returned403 (proxy CONNECT tunnel denial), retried without changing proxy/CA. No Azure denial bypass attempted. Official ungated OpenAI HF is a separately published resource, not an access-gate workaround. The full original1266-row CSV was not acquired or statically re-counted;1266 is a paper/official article count. Topic counts similarly come from the paper, whose classification was prompted-ChatGPT post-hoc, not new model execution.

Neither inherited Fable card nor existing deck content was used as dataset evidence. Local slide helper was adapted; old paths/date/text were replaced. Planned600 seconds skim reading is not a measured reading time.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-browsecomp.pptx)・[PDF](../slides/datasets-in-10-minutes-browsecomp.pdf)。本編25頁、総50頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/browsecomp.json)・[校正の修正対](skill-proofreading/browsecomp.md)・[全ページ文言](skill-proofreading/browsecomp/pages.jsonl)・[最終検証票](skill-proofreading/browsecomp/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE](licenses/browsecomp/LICENSE)、[official-hf-readme.md](licenses/browsecomp/official-hf-readme.md)、[official-hf-meta.json](licenses/browsecomp/official-hf-meta.json)。
