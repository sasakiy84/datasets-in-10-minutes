# IFBench sources and use

- Pyatkin et al., Generalizing Verifiable Instruction Following, NeurIPS2025 Datasets and Benchmarks; arXiv2507.02833v3. https://arxiv.org/abs/2507.02833 . Read all21pages; definitions/construction,58constraints/300prompts, Figure1 singleturn model comparison and Table3 matched training comparison. The abstract contains different training values; slides use Table3 only. Table8 explicitly excludes custom constraints from appended WildChat prompts.
- Ai2 IFBench repository https://github.com/allenai/IFBench fixed1c40f0c10d9b5c5c2f10a175a28007ebb64f7f4d. README, evaluation_lib.py, registry,14 selected checker classes and Apache2.0 license statically read. Loose checks each constraint against transformations independently. Checkers primarily judge form, not factual answers.
- Ai2 IFBench_test https://huggingface.co/datasets/allenai/IFBench_test fixed2e8a48de45ff3bf41242f927254ca81b59ca3ae2. Evaluation300rows under split train. Full selected originals keys280/274/24 main and47/100/64/70/74/83/110/126/241/296 appendix. These are13distinct actual rows, not generated examples. Each original is unchanged in full, Japanese translation in full and expected output conditions on the same page. All selected prompts equal GH fixed data. Whole data differ at13/19 only, not selected.
- Ai2, Why Artificial Analysis uses Ai2’s IFBench instruction-following eval, May11 2026. https://allenai.org/blog/ifbench-artificial-analysis . Official introductory site screenshot with realCSS/fonts and cookie refusal; historical adoption in2025. The article's historical model values are not presented as current scores.
- Artificial Analysis, IFBench Benchmark https://artificialanalysis.ai/evaluations/ifbench and Intelligence Benchmarking Methodology https://artificialanalysis.ai/methodology/intelligence-benchmarking, accessed2026-10-22. Currentv4.3.2 Additional Evaluations standalone, removed fromIndex inv4.1,294questions×5repetitions, singleturn loose prompt-level. Currentfloat fields decoded from publicHTML RSC; selected3series use83.3/82.9/81.4. Do not equate these conditions with paper300-question runs. Why294subset is unspecified.
- Zhou etal., Instruction-Following Evaluation for Large Language Models (2023), https://arxiv.org/abs/2311.07911 ; prior25 verifiable constraints.
- Ai2 Open Instruct https://github.com/allenai/open-instruct ; IF-RLVR implementation reference.

ODC-BY1.0 data and Apache2.0 code licenses are retained as uniquely named root files, with ATTRIBUTION-IFBench.md. The data license does not license all paper/site/third-party output material. This educational Japanese deck displays source attribution. Source originals, fullJapanese, checker interpretation, exact metrics/conditions and file hashes are recorded in examples.json/data-audit.json. No external generation API or model/checker evaluation was run. Japanese revisions are skill_based_codex (not Gemini); actual before/after pairs are in proofreading.json.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-ifbench.pptx)・[PDF](../slides/datasets-in-10-minutes-ifbench.pdf)。本編29頁、総47頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/ifbench.json)・[校正の修正対](skill-proofreading/ifbench.md)・[全ページ文言](skill-proofreading/ifbench/pages.jsonl)・[最終検証票](skill-proofreading/ifbench/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-IFBench-code-Apache-2.0.txt](licenses/ifbench/LICENSE-IFBench-code-Apache-2.0.txt)、[LICENSE-IFBench-data-ODC-BY-1.0.txt](licenses/ifbench/LICENSE-IFBench-data-ODC-BY-1.0.txt)、[ATTRIBUTION-IFBench.md](licenses/ifbench/ATTRIBUTION-IFBench.md)。
