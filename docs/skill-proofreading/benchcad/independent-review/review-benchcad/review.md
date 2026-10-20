# BenchCAD independent Codex skill audit

Reviewer: /root/review_benchcad. Author: /root/create_benchcad.
Read AGENTS.md and all three applicable slide skills (master-guided-slides, dataset-introduction-slides, japanese-slide-proofreading). No Gemini or other generation API used. Writes confined to review-benchcad.

## Scope and status
Work in progress. Independent source acquisition and fact review started; no finished slide artefacts supplied yet. No visual slide inspection performed yet. Visual inspection by this reviewer will be limited to at most 30 representative pages. Main assigns the remaining independent visual coverage. Final approval must bind all coverage to the final PPTX and PDF hashes.

## Independently retrieved sources
2026-10-20: GitHub BenchCAD-main README (7029 bytes), LEADERBOARD.md (6723 bytes), HF BenchCAD/BenchCAD README (1797 bytes), arxiv HTML 2605.10865v1 (643558 bytes), and repository tree. Direct benchcad.com/OpenAI HTTP requests returned 403; web connector independently opened https://benchcad.com/news.html , https://benchcad.com/blog/benchcad-2.html and https://openai.com/index/gpt-6-astra/ . BenchCAD_webpage/main/index.html is only a redirect, not current website source. Network policy independently checked unrestricted/enforced, VPN false; inherited proxy and CA retained.

## Early findings sent to author and main
- Official News 2026-09-22 says Fable5.1 re-evaluation uses 256px views (no tools .606 / tools .926); previous 128px results .437/.843. Astra .959 must not be presented as same-condition improvement over .843. Latest Anthropic values may be used with their source and condition. OpenAI Claude comparisons are modified settings per official News; Astra source is OpenAI, Claude values should be Anthropic.
- HF card says 134x134 while runner README describes 128px previews and 524px evaluation mosaic. Actual image bytes will be checked, and preview data cannot be called full canonical evaluation input.
- 2.0 official post (2026-10-12) uses Core100 and 30 rounds; author reports current2.1 60-round/500k harness, requiring separate conditions.

## Not yet performed
Finished PPTX/PDF text, example provenance and all 13 full records, JP/translation, aggregate recomputation, technical package/schema/link/layout audit, representative visual and final independent coverage reconciliation.

## Independent data verification (completed 2026-10-20)
All 18 code_gen parquet shards successfully opened after author completed retries: 17,900 records, 106 families; easy 6,086, medium 6,078, hard 5,736. Every view_0_png image is 134×134 pixels. The distributed images are preview renders, not the current runner's 524×524 canonical input. All 13 selected records are distinct families; their metadata and entire CadQuery source match the original shard records exactly. All four view PNGs, composite PNG and gt.py files are byte-for-byte equivalent to the records. See data-audit-progress.json and selected-byte-audit.json. Only these provenance checks completed; rendered geometry/JP and final slide placement remain pending.

## Metric review
Independently fetched QA/scoring/qa_score.py: continuous dimensions/ratios use sign-checked symmetric min/max ratio, zero only matches zero; integer/count/bool use exact match. This differs from paper §4.3 and LEADERBOARD.md prose about ±5% tolerance. Author informed to state code-grounded current QA scoring or explicitly historic paper conditions. CodeEdit paper formula verified: mean clip((IoU(generated,target)−IoU(original,target))/(1−IoU(original,target)),0,1), all original-target pairs <.99. Vision2Code execution failures count as zero, so success-conditional IoU must not be passed off as all-record mean.

## Frontier adoption and versions
Independently opened OpenAI Astra launch article and BenchCAD News. Astra .959 is provider-reported tool result for Vision2Code; current News reports 1,000-file subset. Claude Fable5.1 card, independently read from main-acquired PDF pp186–188, uses 1,000 random files and five-run mean; accepts raw Shapes, fixes camera prompt and parses the last codefence. First two changes merged upstream. The card's original .437/.843 used earlier views; official 2026-09-22 News reports new 256px-view .606/.926. Different dates, input resolution, tool harness and grading changes prohibit unqualified rankings across these sources.

Independently opened official BenchCAD 2.0 blog (2026-10-12), Core Access and METRICS.md: six tasks; Core100 heldout; Public100 disjoint; Core scored at 30 rounds and average across cases. T1/T3 part score combines .8 overlap and .2 topology; assembly and graph matching change what a score means. No-submit is zero. Data terms require evaluation-only use and restrict case redistribution. No Core/Public2.0 raw files downloaded or embedded by this reviewer. Published 2.0 scores cannot be compared numerically to 1.0 IoU as the same task. Main/author handles whether/how current2.1 settings appear.

## Website capture
Author screenshot-log currently records a fully styled official GitHub repository fallback, with exact URL. Main confirmed official benchcad.com returns403 through correct TLS/proxy, while text web connector works; no fabricated recreation of the official website. Skill allows official-repo fallback after retry, with correct heading and URL. Final actual screenshot and its slide will be viewed when available.

## Pre-layout editorial pass
Read complete build.py draft independently. Requested numbered main section dividers and Appendix bands; sampler translation; official article titles; source/heading aligned with repository screenshot; explicit 2.0 repeat aggregation; provisional2.1 wording; hinge and heat-sink terms. Author reports these implemented, code reread confirms core changes. Initial four Vision2Code values (.1884/.2740/.2790/.7497) independently match paper Table10. All author full-statistics values, entire family-count dictionary, difficulty counts, standard_nonempty9018 and every file byte count/SHA independently match. Total code_gen compressed parquet files:746424278 bytes (18 files). Viewable UI screenshot was actually opened and styled; initial crop hid the dataset name/description, author asked to recapture at README heading.

Raw example visual inspection progress: six completed raw4view/GT pairs opened in a provenance contact sheet (not final slide inspection): twisted_drill, bevel_gear, coil_spring, hinge, t_pipe_fitting, impeller. Source shape correspondence confirmed. Impeller GT camera hides the blades behind the disk; author asked to select opposite camera for this specimen. Independent import of spring STEP confirms valid single solid, volume4341.0080, bounds approximately19.9800×19.9800×71.2000, without re-running a model. No final pages inspected yet.
