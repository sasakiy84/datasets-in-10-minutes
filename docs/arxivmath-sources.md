# Primary sources and acquisition

All new requests used inherited proxy and normal system CA verification; no credentials, model APIs, or model runs. Date2026-10-22(JST planned deck date; acquisition system UTC2026-10-21).

- Official MathArena project https://matharena.ai/?comp=arxiv--september — own HTML and lazy competition-table JSON retrieval, own CSS/font-rendered Chromium screenshot and actual image view. Current September2026 release selected; table source https://matharena.ai/competition_tables/arxiv--september . Project headline announced September release on October16,2026. Actual table values and warning metadata retained raw.
- Official dataset https://huggingface.co/datasets/MathArena/arxivmath-0926 — own API/card/tree + full Parquet at fixed revision4c38882866fb19388cbb4a229c160040b191d4fe. 53rows, answer gold public. Card license CC BY-SA4.0; code license does not replace data terms. Source/title/authors fields retained.
- Jasper Dekoninck et al.2026. Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs. https://arxiv.org/abs/2605.00674 — own PDF v2 May15,2026,57pages, text independently read relevant task/extraction/evaluation/results. No-tools original evaluation; monthly abstract-generated candidates and automated+human checks.
- Official code https://github.com/eth-sri/matharena — own API/fulltree/README/current ArXivMath curation README and June/Septemberconfigs, code LICENSE MIT retained raw/LICENSE. Current README is abstract-first/full-TeX-source-verified and differs from Maypaper pipeline; describe as current documented workflow, do not assign its exact version to every old monthly set.
- Anthropic2026. Claude Fable5.1 and Mythos5.1 System Card, §8.10 — inherited local primary PDF `/workspace/artifacts/frontier-benchmarks-2026-10/fable-5-1-system-card.pdf` + extracted `/tmp/fable-card.txt`, relevant content independently read. Card evaluated June2026 49problems,4runs; current Juneconfig48not assumed same snapshot. Mythos91.33/93.88 no/tools, published external GPT5.6Sol86.73/Gemini3.1Pro65.99 no tools. These are June snapshot scores, not currentSeptember53.
- Each selected source paper credited with exact `source`, `title`, `authors` metadata in examples.json and reading entries. Independent reviewer has downloaded original papers; source-backed example46 rejected pending disagreement between releasedgold and source. Replacement undergoing review; no corrected gold invented.

## License / attribution

CC BY-SA4.0 requires attribution, link, indication of changes, and ShareAlike for adaptations. Deck includes original English questions, reformatted native linear mathematical notation, and Japanese translations, source paper metadata attribution, and CC BY-SA4.0 notice for these adapted dataset materials. No goldanswer computation/model execution. Preserve original source metadata. Dataset card source is raw/hf-card.md; code MIT source raw/LICENSE. Full CC legal text is fetched to own licensefiles before release.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-arxivmath.pptx)・[PDF](../slides/datasets-in-10-minutes-arxivmath.pdf)。本編27頁、総60頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/arxivmath.json)・[校正の修正対](skill-proofreading/arxivmath.md)・[全ページ文言](skill-proofreading/arxivmath/pages.jsonl)・[最終検証票](skill-proofreading/arxivmath/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[CODE-MIT.txt](licenses/arxivmath/CODE-MIT.txt)、[DATASET-CARD-CC-BY-SA-4.0.md](licenses/arxivmath/DATASET-CARD-CC-BY-SA-4.0.md)。
