# BenchCAD — sources and production scope

Created with the repository's master-guided-slides, dataset-introduction-slides, and japanese-slide-proofreading skills, using local Codex. No Gemini or other generation API was used. Existing HTTPS proxy and CA trust were preserved. Environment policy was unrestricted/enforced, vpn_configured=false.

- Zhang, Haozhe; Liu, Kaichen; Chen, Miaomiao; Li, Lei; Yang, Shaojie; Peng, Cheng; Chen, Hanjie (2026). *BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD*. arXiv:2605.10865, v1, 2026-05-11. https://arxiv.org/abs/2605.10865
  - Saved HTML and readable extraction under raw/paper.*. §§3–5, Appendix E/F/G/I/J/N provide construction, counts, QA, evaluation and initial results.
  - Initial Vision2Code Table 10 reports IoU and execution separately; this deck retains those two columns, not a computed new ranking.
  - Historical QA results use the paper's stated ±5% ratio tolerance / exact integer protocol. Current source code has since changed to symmetric-ratio continuous scores for dimensions/ratios; the two protocols are stated separately.
- BenchCAD/BenchCAD-main README, LEADERBOARD, and benchcad_core/scoring/views.py. https://github.com/BenchCAD/BenchCAD-main
  - 17,900 programs, 106 families, 47 standards; code MIT. Vision2Code canonical runner uses 4 diagonal 256px views, one 524px composite. Distributed preview fields are not this evaluation image.
- BenchCAD/BenchCAD, Hugging Face data card and all 18 code_gen Parquet shards. https://huggingface.co/datasets/BenchCAD/BenchCAD
  - Data CC-BY-4.0. Whole-set metadata and local aggregate in evidence/full-statistics.json and metadata.jsonl. Actual distributed view images measured 134x134px. Counts: easy6086, medium6078, hard5736. All 13 selected examples are distinct medium-tier families in shard1; reference code and four views are byte-exact extracts. Selected IDs and full source code are in evidence/selected.json and per-ID directories.
- BenchCAD News. https://benchcad.com/news.html
  - 2026-09-03 Astra launch: 0.959 with Python tool on 1000 Vision2Code cases, lab-reported. Fable's old 0.843 used 128px images. 2026-09-22 re-evaluation at256px: Fable tools0.926/no-tools0.606, previously0.843/0.437. Anthropic system cards supplied those values. Different lab implementations are not treated as a single controlled ranking.
- OpenAI (2026). *GPT-6 Astra: A new generation of intelligence*. https://openai.com/index/gpt-6-astra/
  - Model adoption; Python tool score0.959. Official comparison notes modified Claude evaluation settings. Main agent independently saved official evidence.
- BenchCAD Team (2026-10-12). *Introducing BenchCAD 2.0*. https://benchcad.com/blog/benchcad-2.html
  - Six tasks, held-out100 Core. Published reference experiment uses harness2.0, max30 rounds. Astra max0.59, Opus5.5max0.57, Sonnet5.5max0.41, Fable5.1max0.30. Mean across100 cases, zero for no submission; parts0.8IoU+0.2topology, assembly placement and board connectivity.
- BenchCAD-org/benchcad-2-main. https://github.com/BenchCAD-org/benchcad-2-main
  - Retrieved current README distinguishes harness2.1 (2026-10-18, 60rounds/500k output tokens/reasoning carried) from published2.0 reference (30rounds/no reasoning carry; v2.0-core1). Public100 no Core overlap. Nine development examples in code repository. No private case is reconstructed or shown.
- BenchCAD2.0 Public data card. https://huggingface.co/datasets/BenchCAD/benchcad-2.0-public
  - Evaluation only, not CC-BY; no redistribution of cases, drawings, renders, references; no training/fine-tuning/distillation/RL/search corpora. Deck examples use only1.0CCBY. Public set task counts21/14/23/27/6/9, aggregate100; not reportable, separate Core100.

# Image provenance

The deck's 13 inputs are unaltered distributed4view composites. Reference outputs are rendered by executing each matching source program, with only show_object stubbed for headless execution; no model response or invented geometry is used. Full code, STEP, numeric bounding boxes/volumes, and source image bytes are retained per ID. Output framing is chosen for visibility; evaluation rendering and scores are not run.

Official benchcad.com requests returned HTTP403 via the inherited proxy. The website text was independently fetched with the web connector and stored in raw/web-source.txt. A live CSS-complete official GitHub repository screenshot is used as a disclosed fallback, with its own repository URL. Browser resources are loaded using ordinary hostname- and CA-verified urllib requests, with no TLS verification disabling.


# License copies

raw/LICENSE-code-MIT.txt is the original repository license, including its explicit dataset CC-BY4.0 carve-out. raw/hf-card.txt is the dataset license declaration. raw/LICENSE-data-CC-BY-4.0.txt is the unmodified legal text from the SPDX license-list-data repository: https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt (Creative Commons legalcode domain returned403). The1.0 dataset, including reference CadQuery source, is CC-BY4.0; repository harness/scoring/tooling is MIT.

# Additional task examples

CodeEdit uses the genuine public repository test record battery_holder_box_y_f130 (Y dimension30.0 to39.0), with both exact codes and executed reference shapes. Matched Vision/CodeQA uses tee_nut_000282_s4420, asking barrel outside diameter / thread diameter, reference1.5; reformatted code is AST-equivalent to the original source. The QA images are generated with the official evaluation renderer from this actual source. These two examples are additional to the13 distinct code_gen examples.

Final score correction: historical CodeQA Table9 non-thinking Gemini3.1Pro is0.836;0.838 belongs to thinking. p31 is now0.836. The MIT row on p41 explicitly describes1.0 execution/scoring code; reference CadQuery remains covered by dataset CC-BY4.0.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-benchcad.pptx)・[PDF](../slides/datasets-in-10-minutes-benchcad.pdf)。本編42頁、総70頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/benchcad.json)・[校正の修正対](skill-proofreading/benchcad.md)・[全ページ文言](skill-proofreading/benchcad/pages.jsonl)・[最終検証票](skill-proofreading/benchcad/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-code-MIT.txt](licenses/benchcad/LICENSE-code-MIT.txt)、[LICENSE-data-CC-BY-4.0.txt](licenses/benchcad/LICENSE-data-CC-BY-4.0.txt)、[hf-card.txt](licenses/benchcad/hf-card.txt)。
