# Sources and acquisition

All dataset sources below were independently fetched for this deck on 2026-10-22 Asia/Tokyo (executor UTC 2026-10-21). No model or benchmark evaluation was run.

1. SWE-bench, **SWE-bench Multilingual**, official dataset card: https://huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual . Own download `raw/scout-3.txt` and full public `raw/data.parquet` (300 rows, 15 fields). Card specifies nine programming languages, 41 repositories, 300 test issue–PR pairs, unit-test evaluation, and MIT metadata. Issues are primarily English; “Multilingual” refers to implementation languages. Gold patch, test patch, environment definition and fail/pass test sets are published. Card has no distinct Multilingual research-paper citation; it cites the foundational paper, whose initial Python results must not be relabeled as Multilingual results.
2. Jimenez et al., **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**, ICLR 2024, https://arxiv.org/abs/2310.06770 . Own PDF `raw/swe-paper.pdf`. Used only for original task design, issue–PR construction and relation to original Python benchmark.
3. SWE-bench official harness, https://github.com/SWE-bench/SWE-bench . Own README `raw/scout-4.txt`, MIT LICENSE `raw/swe-license.txt`. Multilingual harness invocation and Docker environment documentation. License file preserved with attribution; upstream source repositories retain their own copyrights and licenses.
4. Anthropic, **Claude Fable 5.1 & Mythos 5.1 System Card**, 2026, https://www.anthropic.com/claude-fable-and-mythos-5-1 . Acquisition inherited from `/workspace/artifacts/frontier-benchmarks-2026-10/fable-5-1-system-card.pdf` and `/tmp/fable-card.txt`; relevant text independently read (§8.1–8.2, pp167–168). Five trials; Multilingual resolved scores Fable5.1=89.1, Fable5=86.6, Opus5=89.5. This is current adoption evidence, not a source for task construction.

## Official-screen acquisition

Own requests to `https://www.swebench.com/multilingual.html`, `/multilingual`, `/multilingual-leaderboard.html`, root, and no-www alternative returned HTTP403. No TLS/proxy bypass attempted. Official task-specific Hugging Face card was loaded in Chromium with verified system CA, CSS and fonts, then captured as `official-site.png`. This is labeled “公式配布ページ”; it is not described as the project homepage. Actual screenshot independently opened and inspected: styled site, correct dataset title, no cookie panel.

## Example source scope

`examples.json` retains full official problem_statement, patch, test_patch, base_commit and test labels for each of 13 distinct records. Slides retain the issue text; Redis environment-build details and Vue unanswered environment/additional-comment fields alone are omitted, with honest per-slide scope labels. Long originals may span semantic sections. Repository source code is an additional input, so an issue display is never labeled as the entire agent input. Japanese explanations and expected behavior were written by Codex from the actual original issues and reference patches, not by an external model API. These are desired behaviors, not a claim that a single textual patch is the unique answer.

## Licensing

Official card metadata: MIT. Harness license: MIT, saved in `raw/swe-license.txt`. Task examples originate from respective repositories; repository-specific notices will accompany displayed code excerpts as required. No full upstream repository is redistributed in the deck. Dataset and harness attribution remain separate from copyright of the selected original issue/code material.

5. Official early Multilingual evaluation records: https://github.com/SWE-bench/experiments/tree/main/evaluation/multilingual . Own downloads of metadata.yaml and per_instance_details.json for submitted 2026-02-13 mini-SWE-agent2.0.0a0 runs: ClaudeOpus4.6=72.0%, GPT5.2high=66.7%, DeepSeekV3.2=59.0%, attempts1. This separate-condition table precedes Fable five-trial report; values are not a shared ranking.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-swe-bench-multilingual.pptx)・[PDF](../slides/datasets-in-10-minutes-swe-bench-multilingual.pdf)。本編25頁、総50頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/swe-bench-multilingual.json)・[校正の修正対](skill-proofreading/swe-bench-multilingual.md)・[全ページ文言](skill-proofreading/swe-bench-multilingual/pages.jsonl)・[最終検証票](skill-proofreading/swe-bench-multilingual/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[ATTRIBUTION-SWE-bench-Multilingual.md](licenses/swe-bench-multilingual/ATTRIBUTION-SWE-bench-Multilingual.md)、[LICENSE-SWE-bench-harness-MIT.txt](licenses/swe-bench-multilingual/LICENSE-SWE-bench-harness-MIT.txt)、[LICENSE-fmtlib__fmt.txt](licenses/swe-bench-multilingual/LICENSE-fmtlib__fmt.txt)、[LICENSE-jqlang__jq.txt](licenses/swe-bench-multilingual/LICENSE-jqlang__jq.txt)、[LICENSE-preactjs__preact.txt](licenses/swe-bench-multilingual/LICENSE-preactjs__preact.txt)、[LICENSE-briannesbitt__carbon.txt](licenses/swe-bench-multilingual/LICENSE-briannesbitt__carbon.txt)、[LICENSE-uutils__coreutils.txt](licenses/swe-bench-multilingual/LICENSE-uutils__coreutils.txt)、[LICENSE-google__gson.txt](licenses/swe-bench-multilingual/LICENSE-google__gson.txt)、[LICENSE-projectlombok__lombok.txt](licenses/swe-bench-multilingual/LICENSE-projectlombok__lombok.txt)、[LICENSE-caddyserver__caddy.txt](licenses/swe-bench-multilingual/LICENSE-caddyserver__caddy.txt)、[LICENSE-jordansissel__fpm.txt](licenses/swe-bench-multilingual/LICENSE-jordansissel__fpm.txt)、[LICENSE-gin-gonic__gin.txt](licenses/swe-bench-multilingual/LICENSE-gin-gonic__gin.txt)、[LICENSE-rubocop__rubocop.txt](licenses/swe-bench-multilingual/LICENSE-rubocop__rubocop.txt)、[LICENSE-redis__redis.txt](licenses/swe-bench-multilingual/LICENSE-redis__redis.txt)、[LICENSE-vuejs__core.txt](licenses/swe-bench-multilingual/LICENSE-vuejs__core.txt)。
