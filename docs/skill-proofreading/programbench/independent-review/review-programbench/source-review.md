# ProgramBench independent source review

Reviewer: /root/review_programbench. Date: 2026-10-21. Status: source research and all42 native/content reviews completed; final rendering/frame adjustments ongoing.

Read repository AGENTS.md, three local skills, user-instructions.md, managed environment runtime/network references and network policy. Did not inspect secrets, call model APIs, run original programs, execute generated tests, or perform Git operations. Inherited proxy/CA maintained. Remote downloads used explicitly enabled exec networking.

Independently retrieved arXiv 2605.03546 HTML, official Git README/usage/head metadata, HF dataset card/metadata, and all 13 selected test archives plus each ATTRIBUTION/LICENSE. Raw materials stay under raw/. The 39 original license/attribution/archive files exactly match creator materials (independent-source-comparison.json). Creator's replacement jq archive 53795949a2d6 additionally retrieved.

## Findings

- Primary task: reconstruct a complete codebase and build script from executable/documentation; original source and evaluation tests unavailable to worker. Worker may probe executable, choose language/architecture, cannot use network/decompilation. Original executable execute-only.
- Test generation agent has source, native tests and docs, unlike evaluated worker. Construction uses mini-SWE-agent with Sonnet 4.5. Determinism/gold failures, dummy implementations and weak assertion linting inform test filtering.
- Current paper: 200 tasks; 248,853 test functions, median 770. Six source languages per official HF card: Rust107 Go46 C33 C++12 Haskell1 Java1. Source-code line median8635/min212/max2701283.
- Current paper evaluates nine models, all with 0% fully resolved; best Opus4.7 almost-resolved (>=95% tests) 3.0%. 1000 steps/6h,20CPUs60GB RAM. Almost-resolved and tests-pass rate differ from fully-resolved rate.
- Fable card 8.11.1/8.13.1: 34 reference pass<0.9 tasks removed, leaves166 golden; only tests passed by reference are scored. mini-swe-agent, six-hour limit removed. Fable5.1 87.6%, Opus5 85.4%, Fable5 86.3% are hidden-test pass rates under those conditions. Do not compare directly as 200-task complete resolution rates.
- SDK MIT does not replace task-specific original-license obligations. All13 ATTRIBUTION/LICENSE verified; FFmpeg LGPL2.1 contains derivative-portions statement, SQLite public-domain, jq MIT, ripgrep/xsv Unlicense, sd/DuckDB/gron MIT, zstd/PHP BSD3, yj/fd/hexyl Apache2.
- Original selected jq test_pipe_operator came from an ignored gold_fail module. Sent creator actionable finding; creator replaced with nonignored 53795949a2d6::test_arg_sets_named_variable_and_consumes_two_params. Other12 selected modules not ignored in creator's tests.json.

## Content and visual review completed

Read all41 initial native slides and all42 revised native slides. SQLite array length wording corrected,95%-pass task-fraction denominator clarified, a missing card-backed claim removed, gron golden output added as a second page, reference introduction prose revised, formal system-card title restored, stale zero-resolved conclusion contextualized with independently checked current leaderboard results. Removed repetitive warning and internal next-page reference. All13 independent programs represented with3 main and10 additional examples.

Actual-viewed individual pages1–30 of v1, saved10-page checkpoints. Re-viewed revised8,9,13,14,16,17,18,19,21,29 on42-page candidate; re-viewed1,26 after frame edits. P9 source overlap and p29 answer/explanation overlap fixed. Numeric count column right-aligned. MuPDF continuous render band/number artifacts cross-checked with single-page Poppler of identical PDF; final changed views use Poppler.

Final all42 package/PDF/table checks performed:57 schema parts,no unexpected schema errors, valid bounded buSzPct lexical exceptions121; no broken refs,duplicate IDs,notes,nonURL linked runs; author sasakiy84;6 native tables69cells with expected borders and PDF cell text; PDF native paragraph/cell omission0,outside-page0,36 links with2 harmless root-URL trailing slash normalizations. Glyph outline/frame inspection identified bibliography URL overflow (fixed) and remaining small head frame overhangs awaiting creator edits. Tail31–42 reviewed separately by /root/visual_programbench_tail; their final approval and canonical coverage aggregation remain outstanding.

## Final approval

Final pair independently hash-verified: PPTX b2194ee668571bf92bfe46fef2a8040ba258ffbe6d32695388f22245f17d3e67; PDF6c8f1a558f8a473ef41bd9e59848ce18c6971dfc79b0fe8a89cc1d859eba2aff. All42 native/content and package technical checks approved. Own actual visual scope1–30; independently approved tail31–42 is inherited from visual-programbench-tail/review.json on the same final pair. Canonical per-page assignments and inspection/bridge provenance are in review.json and visual-coverage.json. Remaining: none.
