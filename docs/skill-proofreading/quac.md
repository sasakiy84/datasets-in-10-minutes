# QuAC：スキルによる日本語校正

Geminiは使用していない。Codexが日本語校正スキルをページごとに適用した。作成者とは別のサブエージェントもレビューした。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|47|訳（本文抜粋）：William Shockley ／ Shockley Semiconductor|訳（本文抜粋）：William Shockley ／ 質問のsemiconductorは会社を指すと解釈|質問の曖昧なsemiconductorを会社として解釈したことを明示する。|
|21|orig_answerがCANNOTANSWERの質問を集計。論文の学習20.2%とは差がある。|教師の回答から集計。学習の論文値20.2%とは差がある。|注記の対象を平易な日本語で表し、文を短くする。|
|25|主F1・HEQは人同士のF1が40未満の質問を除外。F1 Allも別に報告される。|主F1・HEQは人同士のF1が40未満の質問を除外。除外前のF1 Allも報告。|F1 Allの意味を明示し、注記の折り返しを減らす。|
|32|同じQuACの公式評価。人のHEQ-Dは比較基準として100。HELM得点とは比較しない。|QuACの公式評価。人のHEQ-Dは定義上100。HELMとは採点条件が異なる。|基準値の意味を精確にし、説明の重複を減らす。|

[全ページ文言](quac/pages.jsonl)・[自己検査・独立レビュー](quac/review.json)


## 読者向けの説明・日本語の改訂（2026年10月）

Geminiは使用せず、Codexがスキルで校正し、別担当が独立レビューした。削除・統合を含む[問題点と変更対](quac/editorial-2026-10/changes.md)、[旧ページとの対応](quac/editorial-2026-10/page-map.json)、[独立レビュー](quac/editorial-2026-10/independent-review/handoff.json)、[最終ページの全文](quac/pages.jsonl)。旧版の校正・検証記録は保持している。
