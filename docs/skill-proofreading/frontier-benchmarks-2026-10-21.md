# 最新モデルの評価で使われる未解説ベンチマーク3件（第2回）

2026-10-21、既存93資料との重複を確認し、AutomationBench、Toolathlon-Verified、FrontierMathを選定した。CLEVA系列は制作対象に含めていない。モデルAPIやGeminiは使用せず、ローカルのスライド制作・日本語校正スキルを適用した。

|対象|解説する課題|採用を確認した一次資料|
|---|---|---|
|AutomationBench|模擬業務アプリをまたいで依頼を実行し、最終状態を正しく更新する|[GPT-6 Astra](https://openai.com/index/gpt-6-astra/)とClaude Fable 5.1のシステムカード|
|Toolathlon-Verified|複数のアプリとツールを使い、成果物やアプリの変更を実行ベースの検査で評価する|Claude Fable 5.1のシステムカード、ツール利用評価節|
|FrontierMath|数学者が作成した難問を、検証可能な答えで評価する|[GPT-6 Astra](https://openai.com/index/gpt-6-astra/)とEpoch AIの公式モデル評価|

モデル発表資料は採用の根拠として参照し、解説の中心は各ベンチマークの課題、実例、構築、評価、利用と入手方法に置いた。

課題データを読めるだけで正しいと見なさず、依頼・規則・初期状態・答え・採点条件を照合した。FrontierMathは公開12問のうち、設問に不整合や誤記のある3問を除いた9問を掲載対象とした。除外理由と確認した原文はスライド外のデータ監査記録に残す。Toolathlon-Verifiedは公開Gitの課題・初期データ・期待成果物・検査コードを使い、取得していないモデル実行履歴を実測例として示さない。

## 制作と確認の記録

|資料|本編／総ページ|公開実例|ファイルと記録|
|---|---:|---:|---|
|AutomationBench|41／85|12|[PDF](../../slides/datasets-in-10-minutes-automationbench.pdf)・[PPTX](../../slides/datasets-in-10-minutes-automationbench.pptx)・[修正対](automationbench.md)|
|Toolathlon-Verified|35／80|13|[PDF](../../slides/datasets-in-10-minutes-toolathlon-verified.pdf)・[PPTX](../../slides/datasets-in-10-minutes-toolathlon-verified.pptx)・[修正対](toolathlon-verified.md)|
|FrontierMath|32／61|9|[PDF](../../slides/datasets-in-10-minutes-frontiermath.pdf)・[PPTX](../../slides/datasets-in-10-minutes-frontiermath.pptx)・[修正対](frontiermath.md)|

各資料の本編は600秒で流し読みする予定として設計した。閲覧時間は実測していない。PPTXは編集可能な本文・表・コードを使用し、複雑な数式の一部は原文と照合した再組版画像として収録した。

作成担当と独立レビュー担当の確認範囲は、資料ごとの最終検証票に分けて記録する。メインは原稿の主要箇所、原文、最終表示の抜粋と修正への対応を確認した。独立担当の全ページ確認をメイン自身の実施としては扱わない。Microsoft PowerPointでの実開封、ライブの業務アプリ操作、公開されていないデータの確認は行っていない。

AutomationBenchの本編3例は公開模擬環境で参照操作を再現して採点条件の通過を確認した。モデルの成績を実測したものではない。Toolathlon-Verifiedは公開の初期データ・参照成果物・検査コードを照合し、外部アプリへの操作は行っていない。FrontierMathは掲載9例の原文と答案を照合し、7例の数値計算の整合性を独立に確認したが、すべての証明を再証明したわけではない。

[選定記録](frontier-benchmarks-2026-10-21/selection.json)・[メインの原稿確認範囲](frontier-benchmarks-2026-10-21/main-review-progress.json)・[ローカル検証](frontier-benchmarks-2026-10-21/verification-local.json)。

公開確認は最終配布物の固定後に追記する。
