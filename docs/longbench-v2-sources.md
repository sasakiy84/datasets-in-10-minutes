# LongBench v2 — source and editorial record

- [Bai et al., LongBench v2 (2024)](https://arxiv.org/abs/2412.15204): construction, six domains,20 tasks,503 English fourchoice problems, reported8k–2M words; initial model comparison and15minute human condition.
- [Official site](https://longbench2.github.io/): actualCSS screenshot and later2025 board; retrieved2026-10-26.
- [Official repository](https://github.com/THUDM/LongBench): current README, direct/CoT prompts, pred.py and result.py statically inspected.
- [Canonical fixed dataset](https://huggingface.co/datasets/zai-org/LongBench-v2): all503 acquired;13 examples selected from distinct fixed rows. Revisions and exact examples in data-audit.json / examples.json.
- [LongBench v1, ACL2024](https://aclanthology.org/2024.acl-long.172/): earlier Chinese/English21task comparison;2023 dataset vs2024 paper dates kept distinct.
- [Qwen3.5-397B-A17B model card](https://huggingface.co/Qwen/Qwen3.5-397B-A17B): primary2026 adoption evidence, own LongBench v2 score63.2; other systems' columns not merged with official-board conditions.

## Read scope and genuine examples

Acquired and parsed all503 metadata and contexts; no claim of reading465MB end-to-end. Creator read all13 questions/all choices/golds, selected displayed context fragments and necessary surroundings. The13 rows are295,270,435,477,288,196,112,326,487,492,398,478,289. Main3 plusAppendix10 cover all6 domains. Long contexts are represented by sufficient source excerpts to demonstrate the gold, never labelled the full input. Short questions use bilingual same-page when legible. Long original questions are split only for their own length, using complete semantic fields.

Manual arithmetic/source logic is recorded in data-audit.json. Ambiguous or internally inconsistent candidates were excluded rather than altering official gold; actual reasons in excluded-candidates.json. Source-native-audit.json binds original13 questions/choices/gold and every displayed excerpt to fixed raw rows. Japanese questions/options are full translations, while context prose is labelled summary.

## Rights and distribution

Actual Apache2 dataset text, MIT repository text, dataset-card declaration and CC-BY-SA4 website legal text are retained. Underlying original material attribution and limits appear in ATTRIBUTION-LongBench-v2.txt. Only educational short excerpts/translations and derived selected-column tables are distributed; full contexts remain workspace source evidence. No broad thirdparty licensing claim is inferred from the benchmark card.

## Review and timing

The main37 pages have a600second planning allocation; reading duration was not measured. Creator all-page actual review and exact technical reports are separately recorded. Independent reviewer acquired canonical13 rows separately and reports own source/image/technical scope in the sibling review packet; root's main/representative supplemental review is a separate scope, never described as wholedeck independent review. All correction pairs use local Japanese proofreading skill; no Gemini or external generation API, no model/evaluation run.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-longbench-v2.pptx)・[PDF](../slides/datasets-in-10-minutes-longbench-v2.pdf)。本編37頁、総97頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/longbench-v2.json)・[校正の修正対](skill-proofreading/longbench-v2.md)・[全ページ文言](skill-proofreading/longbench-v2/pages.jsonl)・[最終検証票](skill-proofreading/longbench-v2/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-LongBench-Data-Apache-2.0.txt](licenses/longbench-v2/LICENSE-LongBench-Data-Apache-2.0.txt)、[LICENSE-LongBench-Code-MIT.txt](licenses/longbench-v2/LICENSE-LongBench-Code-MIT.txt)、[LICENSE-LongBench-Dataset-Card.md](licenses/longbench-v2/LICENSE-LongBench-Dataset-Card.md)、[LICENSE-LongBench-Site-CC-BY-SA-4.0.txt](licenses/longbench-v2/LICENSE-LongBench-Site-CC-BY-SA-4.0.txt)、[ATTRIBUTION-LongBench-v2.txt](licenses/longbench-v2/ATTRIBUTION-LongBench-v2.txt)。
