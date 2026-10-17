# 日本語校正スキルによる校正記録

実施者はCodex。収集済みの校正採否から作成した[japanese-slide-proofreading](../../.agents/skills/japanese-slide-proofreading/SKILL.md)を適用し、各資料を1ページずつ確認した。今回の新規Gemini API呼出しは0回。過去のGemini案を候補として参照した場合も、スキルでの再判断と明記する。

資料ごとにPPTX・PDF・変更対・全ページの確認記録を1コミットにまとめる。先にGeminiで完了した12資料は[別の記録](../gemini-proofreading/README.md)に保存している。

| データセット | 記録 | PPTX | PDF |
|---|---|---|---|
| arc-agi-2 | [変更対・採否](arc-agi-2.md) | [PPTX](../../slides/datasets-in-10-minutes-arc-agi-2.pptx) | [PDF](../../slides/datasets-in-10-minutes-arc-agi-2.pdf) |
| coco | [変更対・採否](coco.md) | [PPTX](../../slides/datasets-in-10-minutes-coco.pptx) | [PDF](../../slides/datasets-in-10-minutes-coco.pdf) |
| fineweb | [変更対・採否](fineweb.md) | [PPTX](../../slides/datasets-in-10-minutes-fineweb.pptx) | [PDF](../../slides/datasets-in-10-minutes-fineweb.pdf) |
| gpqa | [変更対・採否](gpqa.md) | [PPTX](../../slides/datasets-in-10-minutes-gpqa.pptx) | [PDF](../../slides/datasets-in-10-minutes-gpqa.pdf) |
| imagenet | [変更対・採否](imagenet.md) | [PPTX](../../slides/datasets-in-10-minutes-imagenet.pptx) | [PDF](../../slides/datasets-in-10-minutes-imagenet.pdf) |
| mcp-atlas | [変更対・採否](mcp-atlas.md) | [PPTX](../../slides/datasets-in-10-minutes-mcp-atlas.pptx) | [PDF](../../slides/datasets-in-10-minutes-mcp-atlas.pdf) |
| omnidocbench | [変更対・採否](omnidocbench.md) | [PPTX](../../slides/datasets-in-10-minutes-omnidocbench.pptx) | [PDF](../../slides/datasets-in-10-minutes-omnidocbench.pdf) |
| osworld-verified | [変更対・採否](osworld-verified.md) | [PPTX](../../slides/datasets-in-10-minutes-osworld-verified.pptx) | [PDF](../../slides/datasets-in-10-minutes-osworld-verified.pdf) |
| snli | [変更対・採否](snli.md) | [PPTX](../../slides/datasets-in-10-minutes-snli.pptx) | [PDF](../../slides/datasets-in-10-minutes-snli.pdf) |
| squad | [変更対・採否](squad.md) | [PPTX](../../slides/datasets-in-10-minutes-squad.pptx) | [PDF](../../slides/datasets-in-10-minutes-squad.pdf) |
| tau2-bench | [変更対・採否](tau2-bench.md) | [PPTX](../../slides/datasets-in-10-minutes-tau2-bench.pptx) | [PDF](../../slides/datasets-in-10-minutes-tau2-bench.pdf) |
| terminal-bench | [変更対・採否](terminal-bench.md) | [PPTX](../../slides/datasets-in-10-minutes-terminal-bench.pptx) | [PDF](../../slides/datasets-in-10-minutes-terminal-bench.pdf) |
| ucf101 | [変更対・採否](ucf101.md) | [PPTX](../../slides/datasets-in-10-minutes-ucf101.pptx) | [PDF](../../slides/datasets-in-10-minutes-ucf101.pdf) |

## 2026-10-17の新規資料

次の3資料は新規に作成し、日本語校正スキルで全ページを確認した。Geminiは利用していない。初稿からの修正対とページごとの最終文言を保存し、出典・実例・集計・表示の検証も記録した。

|資料|修正前後の対|全ページの記録|出典・検証|
|---|---|---|---|
|GSM8K|[changes.tsv](gsm8k/changes.tsv)|[pages.jsonl](gsm8k/pages.jsonl)|[制作記録](../gsm8k-sources.md)・[最終検査](gsm8k/review.json)|
|HumanEval|[changes.tsv](humaneval/changes.tsv)|[pages.jsonl](humaneval/pages.jsonl)|[制作記録](../humaneval-sources.md)・[最終検査](humaneval/review.json)|
|VQA v2|[changes.tsv](vqa-v2/changes.tsv)|[pages.jsonl](vqa-v2/pages.jsonl)|[制作記録](../vqa-v2-sources.md)・[最終検査](vqa-v2/review.json)|

## 原文・訳の併記と説明文の最新改訂

全28資料を確認し、15資料を改訂した。Geminiは使用していない。[変更対・ページ対応・検証記録](../slide-language-review/README.md)に、94件の文言変更、36組の併記、現行成果物のハッシュを保存した。このファイルから辿れる従来の記録は、その時点の版の履歴として保持する。

## HELM Classicから選んだ5資料

全5資料・320ページを、日本語校正スキルで1ページずつ確認した。Geminiは使用していない。各資料に本編3件・追加10件の公開実例を収録し、HELM v0.4.0の実行別結果を照合した。

|資料|修正前後の対|全ページの記録|出典・検証|
|---|---|---|---|
|BoolQ|[変更対](boolq.md)・[TSV](boolq/changes.tsv)|[pages.jsonl](boolq/pages.jsonl)|[制作記録](../boolq-sources.md)・[最終検査](boolq/review.json)|
|HellaSwag|[変更対](hellaswag.md)・[TSV](hellaswag/changes.tsv)|[pages.jsonl](hellaswag/pages.jsonl)|[制作記録](../hellaswag-sources.md)・[最終検査](hellaswag/review.json)|
|TruthfulQA|[変更対](truthfulqa.md)・[TSV](truthfulqa/changes.tsv)|[pages.jsonl](truthfulqa/pages.jsonl)|[制作記録](../truthfulqa-sources.md)・[最終検査](truthfulqa/review.json)|
|IMDb|[変更対](imdb.md)・[TSV](imdb/changes.tsv)|[pages.jsonl](imdb/pages.jsonl)|[制作記録](../imdb-sources.md)・[最終検査](imdb/review.json)|
|XSum|[変更対](xsum.md)・[TSV](xsum/changes.tsv)|[pages.jsonl](xsum/pages.jsonl)|[制作記録](../xsum-sources.md)・[最終検査](xsum/review.json)|
