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

初回制作時の全5資料・320ページを、日本語校正スキルで1ページずつ確認した。Geminiは使用していない。各資料に本編3件・追加10件の公開実例を収録し、HELM v0.4.0の実行別結果を照合した。

|資料|修正前後の対|全ページの記録|出典・検証|
|---|---|---|---|
|BoolQ|[変更対](boolq.md)・[TSV](boolq/changes.tsv)|[pages.jsonl](boolq/pages.jsonl)|[制作記録](../boolq-sources.md)・[最終検査](boolq/review.json)|
|HellaSwag|[変更対](hellaswag.md)・[TSV](hellaswag/changes.tsv)|[pages.jsonl](hellaswag/pages.jsonl)|[制作記録](../hellaswag-sources.md)・[最終検査](hellaswag/review.json)|
|TruthfulQA|[変更対](truthfulqa.md)・[TSV](truthfulqa/changes.tsv)|[pages.jsonl](truthfulqa/pages.jsonl)|[制作記録](../truthfulqa-sources.md)・[最終検査](truthfulqa/review.json)|
|IMDb|[変更対](imdb.md)・[TSV](imdb/changes.tsv)|[pages.jsonl](imdb/pages.jsonl)|[制作記録](../imdb-sources.md)・[最終検査](imdb/review.json)|
|XSum|[変更対](xsum.md)・[TSV](xsum/changes.tsv)|[pages.jsonl](xsum/pages.jsonl)|[制作記録](../xsum-sources.md)・[最終検査](xsum/review.json)|

## HELM Classicから追加した10資料

初回制作時の全10資料・507ページに、日本語校正スキルを1ページずつ適用した。Geminiは使用していない。各資料に本編3件・追加10件の公開実例を収録。WMT14はHELMの公開実行が0件で、得点を掲載していない。

|資料|修正前後の対|全ページの記録|出典・検証|
|---|---|---|---|
|OpenBookQA|[変更対](openbookqa.md)・[TSV](openbookqa/changes.tsv)|[pages.jsonl](openbookqa/pages.jsonl)|[制作記録](../openbookqa-sources.md)・[最終検査](openbookqa/review.json)|
|MMLU|[変更対](mmlu.md)・[TSV](mmlu/changes.tsv)|[pages.jsonl](mmlu/pages.jsonl)|[制作記録](../mmlu-sources.md)・[最終検査](mmlu/review.json)|
|bAbI|[変更対](babi.md)・[TSV](babi/changes.tsv)|[pages.jsonl](babi/pages.jsonl)|[制作記録](../babi-sources.md)・[最終検査](babi/review.json)|
|BLiMP|[変更対](blimp.md)・[TSV](blimp/changes.tsv)|[pages.jsonl](blimp/pages.jsonl)|[制作記録](../blimp-sources.md)・[最終検査](blimp/review.json)|
|APPS|[変更対](apps.md)・[TSV](apps/changes.tsv)|[pages.jsonl](apps/pages.jsonl)|[制作記録](../apps-sources.md)・[最終検査](apps/review.json)|
|BBQ|[変更対](bbq.md)・[TSV](bbq/changes.tsv)|[pages.jsonl](bbq/pages.jsonl)|[制作記録](../bbq-sources.md)・[最終検査](bbq/review.json)|
|BOLD|[変更対](bold.md)・[TSV](bold/changes.tsv)|[pages.jsonl](bold/pages.jsonl)|[制作記録](../bold-sources.md)・[最終検査](bold/review.json)|
|RAFT|[変更対](raft.md)・[TSV](raft/changes.tsv)|[pages.jsonl](raft/pages.jsonl)|[制作記録](../raft-sources.md)・[最終検査](raft/review.json)|
|CivilComments|[変更対](civil-comments.md)・[TSV](civil-comments/changes.tsv)|[pages.jsonl](civil-comments/pages.jsonl)|[制作記録](../civil-comments-sources.md)・[最終検査](civil-comments/review.json)|
|WMT14|[変更対](wmt14.md)・[TSV](wmt14/changes.tsv)|[pages.jsonl](wmt14/pages.jsonl)|[制作記録](../wmt14-sources.md)・[最終検査](wmt14/review.json)|

## 2026-10-18：追加10資料の正解表示と出典表現

全507ページを点検。5資料90ページの独立した正解表示を12.5ptから22ptの太字に拡大し、8資料の図表番号を含む9か所の出典表現を整理した。原文・訳・正解値・評価値・ページ数は保持。BOLDは対象なし。Geminiは使用していない。

|資料|正解表示|出典表現|今回の点検記録|
|---|---:|---:|---|
|OpenBookQA|22|0|[記録](openbookqa/answer-and-citation-review.json)|
|MMLU|13|1|[記録](mmlu/answer-and-citation-review.json)|
|bAbI|16|1|[記録](babi/answer-and-citation-review.json)|
|BLiMP|13|1|[記録](blimp/answer-and-citation-review.json)|
|APPS|0|1|[記録](apps/answer-and-citation-review.json)|
|BBQ|26|1|[記録](bbq/answer-and-citation-review.json)|
|BOLD|0|0|[記録](bold/answer-and-citation-review.json)|
|RAFT|0|1|[記録](raft/answer-and-citation-review.json)|
|CivilComments|0|1|[記録](civil-comments/answer-and-citation-review.json)|
|WMT14|0|2|[記録](wmt14/answer-and-citation-review.json)|

## 2026-10-18：正解色の好み

今回の10件を点検し、独立した正解表示のある5資料90か所をテーマaccent1（#B13731、えんじ系の赤）へ変更した。ユーザー個人の好みとして制作スキルにも記録した。22pt・太字と、文章・値・配置は保持。Geminiは使用していない。

[openbookqa](openbookqa/answer-color-review.json)・[mmlu](mmlu/answer-color-review.json)・[babi](babi/answer-color-review.json)・[blimp](blimp/answer-color-review.json)・[bbq](bbq/answer-color-review.json)

## 2026-10-18：原文を1枚にまとめる優先順位

昨日・今日（JST 10月17〜18日）に作成した29資料を確認し、11資料・72実例を再構成した。68実例は原文を1枚に収め、原文自体が長いAPPSの4実例のみ意味の区切りで分割。訳は併記できる場合のみ同じページに配置し、その他は別ページにした。11資料の合計は642→591ページ。変更した124ページを1枚ずつ描画・目視し、原文・訳の欠落、タイトル、正解枠、出典リンク、PPTXの構造を検査した。Codexによるスキル適用で、Gemini使用なし。[29資料の確認結果と各資料の記録](../original-first-review-2026-10-18.json)。過去の変更表のページ番号は当時の番号として保持し、各資料のoriginal-first-review.jsonに現行との対応を記録した。
