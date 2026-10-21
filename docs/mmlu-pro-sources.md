# Primary sources and acquisition

All own new downloads use inherited proxy/systemCA, no login/APIkey/modelAPI/modelrun. Deck date2026-10-22JST.

- Wang et al.2024. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark. NeurIPS2024 Datasets and Benchmarks. https://arxiv.org/abs/2406.01574 — own full24pagePDF and relevant text read. 5shotCoT exceptGemini1.5models0shot; GPT4o72.6,Claude3Opus68.5,Gemini1.5Pro69.0,Llama370BInstruct56.2. Initial constructreview/24promptconditions retained.
- Official https://github.com/TIGER-AI-Lab/MMLU-Pro — own repoAPI/README/LICENSE. Code LICENSE is Apache2.0. No standalone official project is linked in README/paper; reasonable project URL https://tiger-ai-lab.github.io/MMLU-Pro/ independently404.
- Official dataset https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro — own API/card/tree and full test+validation Parquet, fixedb189ec765aa7ed75c8acfea42df31fdae71f97be. Dataset MIT declaration in card; codeApache2not inherited for data. Actualtest12032/validation70; all questions/options/answers public. 2026Janoptionleadingwhitespacefix,2025Apr15medicalgoldfix.
- Official leaderboard https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro and firstparty app https://tiger-lab-mmlu-pro.hf.space/ — ownHTML/config and successful directapp CSS screenshot. Creator individually viewed PNG and final slide; HFparent had rendered CSS with blank embedded app, so successful official directapp is used.
- Current Mercor firstparty benchmark https://www.mercor.com/apex/oss-benchmarks/oss-mmlu-pro-leaderboard/ — own directGET403. Root acquired official webpage via webtool and saved W/mercor-mmlu-pro-web.json; inherited acquisition, independently read content. Publictasks12032/Pass@1/Opus5.5Max93.4/Fable5.1Max93.0/GPT6AstraMax91.5/Gemini3.1ProHigh91.3. Same page also repeats originalMMLU57subjects; not used for MMLU-Pro14subjects definition. Fewshot/promptdetails not disclosed in exact retrievedpage; do not invent them.
- Anthropic2026 Claude Fable5.1 and Mythos5.1 SystemCard — inherited localPDFandtext identified during scout. CoTcontrollability is distinct from ordinaryaccuracy; not used in the deck because Mercor provides current firstparty ordinaryaccuracy.

## Examples and licenses

13 independentquestions,13categories(other omitted), main3+extra10. Sourcefield retains originalMMLU vsSTEM etc. Exact originals/choices/answer/index in examples.json; Japanese translations and explanatorynotes added. MIT datasetcard retained as ownlicensefile; sourcecodeApache2license retained separately. No modelreasoning traces generated; suppliedcot_content retained in raw data but not used as verifiedsolvedproof. Reviewer independently calculated numerical examples and read all13originals.

Own paper §6.3 confirms 24prompt score range, not standard deviation. Paper §4 states random-choice fallback after failed regex extraction. Both are reflected in the final correction batch.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-mmlu-pro.pptx)・[PDF](../slides/datasets-in-10-minutes-mmlu-pro.pdf)。本編27頁、総52頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/mmlu-pro.json)・[校正の修正対](skill-proofreading/mmlu-pro.md)・[全ページ文言](skill-proofreading/mmlu-pro/pages.jsonl)・[最終検証票](skill-proofreading/mmlu-pro/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[CODE-APACHE-2.0.txt](licenses/mmlu-pro/CODE-APACHE-2.0.txt)、[DATASET-CARD-MIT.md](licenses/mmlu-pro/DATASET-CARD-MIT.md)。
