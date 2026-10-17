# 日本語校正スキルによる校正記録

実施者はCodex。収集済みの校正採否から作成した[japanese-slide-proofreading](../../.agents/skills/japanese-slide-proofreading/SKILL.md)を適用し、各資料を1ページずつ確認した。今回の新規Gemini API呼出しは0回。過去のGemini案を候補として参照した場合も、スキルでの再判断と明記する。

資料ごとにPPTX・PDF・変更対・全ページの確認記録を1コミットにまとめる。先にGeminiで完了した12資料は[別の記録](../gemini-proofreading/README.md)に保存している。

| データセット | 記録 | PPTX | PDF |
|---|---|---|---|
| arc-agi-2 | [変更対・採否](arc-agi-2.md) | [PPTX](../../slides/datasets-in-10-minutes-arc-agi-2.pptx) | [PDF](../../slides/datasets-in-10-minutes-arc-agi-2.pdf) |
| coco | [変更対・採否](coco.md) | [PPTX](../../slides/datasets-in-10-minutes-coco.pptx) | [PDF](../../slides/datasets-in-10-minutes-coco.pdf) |
| fineweb | [変更対・採否](fineweb.md) | [PPTX](../../slides/datasets-in-10-minutes-fineweb.pptx) | [PDF](../../slides/datasets-in-10-minutes-fineweb.pdf) |
