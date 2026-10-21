# HealthBench — sources and scope

Prepared 2026-10-22 Asia/Tokyo by sasakiy84. Japanese B4–M1 introduction, main planned skim 600 seconds, Appendix. Thirteen genuinely distinct base HealthBench conversations; Professional is explained as a separate evaluation collection within this deck and is not counted as another dataset. No Gemini, model/API execution, credentials, login, access-gate bypass, or Git operations.

## Newly acquired primary sources

- OpenAI, **Introducing HealthBench** (2025-05-12), https://openai.com/index/healthbench/ . Fresh curl HTTP 200 to `raw/official-curl.html`; urllib had returned 403. The live official HTML was rendered at its canonical URL with its original CSS/font/image resources; CA verification and proxy retained. Screenshot `official-site.png` shows the header and introduction, clipped above an audio widget. Screenshot procedure/status in `screenshot-log.json`; actual slide screenshot inspected by creator.
- Arora et al., **HealthBench: Evaluating Large Language Models Towards Improved Human Health** (2025), https://arxiv.org/abs/2505.08775 . HTML HTTP 200, `raw/paper.html` and extracted `raw/paper.txt`; primary construction/scoring/results source. Paper states CC BY 4.0.
- OpenAI official data, https://huggingface.co/datasets/openai/healthbench . Public ungated dataset, metadata and tree in `raw/`; revision `40ee1968852fc57f625934251ac22be47077a8fb`. Official file `2025-05-07-06-14-12_oss_eval.jsonl` downloaded HTTP 200 to `raw/base.jsonl` (60,258,154 bytes). This is the official alternate distribution, not a mirror. The Azure URL linked from the official reference code failed proxy CONNECT 403 once; no repeated attempts or bypass. Data examples and all criterion indices/points/tags were read from the HF distribution.
- OpenAI, https://github.com/openai/simple-evals . Official README, root MIT LICENSE, and `healthbench_eval.py` freshly downloaded to `raw/`. The README explicitly identifies HealthBench under MIT and says contributed datasets use MIT. Official HF README likewise declares MIT. Guessed `openai/healthbench` repo returned 404; it was not used.
- Soskin Hicks et al., **HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats** (2026), https://arxiv.org/abs/2604.27470 . Fresh HTML HTTP 200, `raw/professional.html` and `.txt`; paper CC BY 4.0.
- OpenAI official Professional data, https://huggingface.co/datasets/openai/healthbench-professional . Public ungated MIT, official file `healthbench_professional_eval.jsonl` downloaded HTTP 200 to `raw/professional.jsonl` (2,755,136 bytes); source revision recorded as `349962fd46dd02343a0d8a606491baf59154ea1a`. Parsed by physical newline, because a quoted string contains a Unicode line separator. Own count 525, with use cases consult 236/research 147/writing 142.

## Inherited official adoption source, independently read

Anthropic (2026), **Claude Fable 5.1 & Claude Mythos 5.1 System Card**, official landing https://www.anthropic.com/claude-fable-and-mythos-5-1 . Existing public-source PDF inherited from `/workspace/artifacts/frontier-benchmarks-2026-10/fable-5-1-system-card.pdf`; text `/tmp/fable-card.txt`. The relevant pp.198–199 were read independently for HealthBench and Professional. No new access claim is made for the inherited file. Base Fable 5.1 raw 66.7%, length-adjusted 60.0%; Professional raw 74.2%, adjusted 62.1%. Opus 4.8 grader, five trials, adaptive thinking/max effort/no tools. Fable 5.1 safety classifiers active; provider refusals use an Opus 5 fallback. These are different grader conditions from the initial GPT-4.1 evaluation and are separated in the deck. Astra's different Professional figures were not merged.

## Dataset counts, examples, and license

Own complete parse: 5,000 base conversations, 57,237 rubric occurrences, 48,562 distinct criterion strings, 17,575 negative-weight occurrences. Seven theme counts and all thirteen source IDs, original full conversations/full rubrics, selected complete criteria and Japanese translations are in `data-audit.json` and `examples.json`. Native source footers give each conversation UUID on each example page; criterion indices/points are recorded separately. Initial results are rounded whole-percent readings from the primary figure, not exact table estimates.

`LICENSE-HealthBench.txt` preserves the official MIT permission and copyright notice. MIT permission explicitly covers the published dataset. Separately, the official introductory article asks that examples not be revealed online to reduce contamination: “We request that you do not reveal examples from this dataset in plain text or images online…” This is recorded as a publisher request, not misrepresented as a license prohibition. The explicit user request is to publish thirteen genuine examples, and the parent has confirmed proceeding under the dataset's MIT permission while preserving the notice. No access restriction was bypassed.

## Verification scope

Creator checks and independent review are recorded with the exact PPTX/PDF hashes. Native text/PDF extraction, schema/relations/IDs/notes/author, actual glyph frame bounds, URL-only links, editable table alignment and borders are separate from actual image viewing. Planned reading time is 600 seconds; reading time was not experimentally measured. LibreOffice opening/export and python-pptx reopen are tested; no Microsoft PowerPoint interactive-opening claim is made.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-healthbench.pptx)・[PDF](../slides/datasets-in-10-minutes-healthbench.pdf)。本編39頁、総75頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/healthbench.json)・[校正の修正対](skill-proofreading/healthbench.md)・[全ページ文言](skill-proofreading/healthbench/pages.jsonl)・[最終検証票](skill-proofreading/healthbench/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-HealthBench.txt](licenses/healthbench/LICENSE-HealthBench.txt)。
