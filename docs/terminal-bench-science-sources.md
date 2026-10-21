# Terminal-Bench-Science 0.1 — sources and acquisition

Access date for newly acquired sources: 2026-10-22 (Asia/Tokyo). Network requests use the inherited proxy and system CA; no gate bypass, login, model API, or model execution was used.

## Primary dataset sources (own acquisition)

- Official release v0.1.0: https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0 . `raw/releases.html`, `raw/v0.1.0-CITATION.cff`. Release date 2026-08-26. This is a software/data release; no separate research paper was located. The software release and official task specifications are the primary sources.
- Archived version record: https://doi.org/10.5281/zenodo.22110254 . `raw/zenodo.html`. Concept DOI 10.5281/zenodo.22110253 resolves to this v0.1.0 version record.
- Fixed-tag README: https://github.com/harbor-framework/terminal-bench-science/blob/v0.1.0/README.md . `raw/v0.1.0-README.md`; 70 tasks. Current main contained 71 during scouting; the deck does not substitute its task count for 0.1.
- Fixed-tag task distribution: `raw/v0.1.0-task-coverage.svg`, own acquisition. Domains 19 life / 17 physical / 8 earth / 17 mathematical / 9 engineering = 70.
- Fixed-tag contribution and reviewing guides: `raw/v0.1.0-CONTRIBUTING.md`, `raw/v0.1.0-REVIEWING.md`. Independently read task construction, human domain/technical review, automated checks, reference solution and verifier, and final approval sections. No validation/evaluation commands were run.
- Official project and live 0.1 table: https://terminal-bench-science.ai/ . Own browser capture routed through normal CA-verified HTTP acquisition; `capture.py`, `official-rendered.html`, `official-rendered.txt`, `official-site.png`, `screenshot-log.json`. Real CSS/fonts loaded; no cookie overlay. Individual screenshot was actually opened. Current public table exposes standard errors but does not expose a common trial count in its visible table; do not infer measurement dates from model release dates.
- Fixed-tag license: https://github.com/harbor-framework/terminal-bench-science/blob/v0.1.0/LICENSE . Original Apache-2.0 text retained unchanged in `LICENSE-Terminal-Bench-Science-v0.1.0-Apache-2.0.txt`. Author/notice mapping in `ATTRIBUTION-Terminal-Bench-Science.md`. External task datasets and software can retain additional terms.

## Genuine task examples (own acquisition/read)

The 13 task IDs and exact original text hashes are in `examples.json` and `data-audit.json`. Every selected `instruction.md` and `task.toml` was acquired from v0.1.0, alongside available public tests and reference solve.sh files; fetch logs are retained under raw. Main archive was used to scout candidate task paths and compact readable examples. The 13 selected main instructions were compared byte-for-byte with the fixed-tag instructions and match. The large archive is working research material only, not a distributable deck artifact.

Original instructions are displayed with Markdown decoration normalized; shared HTML benchmark canary comments and the shared 28,800-second deadline/anti-cheating notice are omitted from slide quotations. This scope is stated on example slides. Full raw instructions, including canary and deadline, remain in examples.json and raw. Paragraphs may continue across semantically related original pages; translation pages explicitly contain Japanese explanations, not a claim of word-for-word translation of every mechanical rule. No scientific result or unique answer was fabricated. Submitted artifact descriptions and expected behavior follow original instructions and public verifier specifications.

`variable-star-vetting/environment/data/target_1.csv` was independently downloaded from v0.1.0 (51,294 bytes, 1,293 rows). The deck's scatter figure is generated with Matplotlib from its time, mag, and band fields (CSV and standalone SVG retained); both g and r bands are preserved. No class label or period was inferred or claimed for this target. Its chart is an actual input illustration.

## Current adoption (inherited acquisition / own reading)

The existing `/workspace/artifacts/frontier-benchmarks-2026-10/fable-5-1-system-card.pdf` and `/tmp/fable-card.txt` were inherited from earlier research. Relevant §8.7 text was independently read. The report uses the same 70 tasks, Claude Code --bare with max effort; Fable 5.1 uses 10 trials per task (700 runs), Opus 5 uses 12 (840), and Fable 5 uses 10 (700). Reported rates 52.6%, 29.0%, and 24.7% are kept in a separate table from current official public rates. The public Fable 5.1 rate is 40.0%; no unsupported causal explanation for the difference is asserted.

Current report landing URL: https://www.anthropic.com/claude-fable-and-mythos-5-1 . System-card acquisition is explicitly inherited, unlike all primary task sources above.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-terminal-bench-science.pptx)・[PDF](../slides/datasets-in-10-minutes-terminal-bench-science.pdf)。本編34頁、総83頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/terminal-bench-science.json)・[校正の修正対](skill-proofreading/terminal-bench-science.md)・[全ページ文言](skill-proofreading/terminal-bench-science/pages.jsonl)・[最終検証票](skill-proofreading/terminal-bench-science/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-Terminal-Bench-Science-v0.1.0-Apache-2.0.txt](licenses/terminal-bench-science/LICENSE-Terminal-Bench-Science-v0.1.0-Apache-2.0.txt)、[ATTRIBUTION-Terminal-Bench-Science.md](licenses/terminal-bench-science/ATTRIBUTION-Terminal-Bench-Science.md)。
