# IFEvalの一次資料と掲載範囲

- Zhou et al. (2023), **Instruction-Following Evaluation for Large Language Models**. https://arxiv.org/abs/2311.07911 — main sections1–4の定義・作成・採点・初期成績、25種類の指示を確認した。全Appendixの541依頼文を一件ずつ読んだとは主張しない。
- Google Research, **IFEval: Instruction Following Eval**. https://github.com/google-research/google-research/tree/master/instruction_following_eval — README、公開データ、選定13例の判定器、集計コードを確認した。最終パス更新commitはdata-audit.jsonに保存した。
- Google Research, **input_data.jsonl**. https://github.com/google-research/google-research/blob/master/instruction_following_eval/data/input_data.jsonl — 全541レコードを機械集計し、834判定条件・25種類を確認した。選定13件の依頼全文と条件を実読・翻訳した。取得した全件を実読したとは扱わない。
- Pyatkin et al. (2025), **Generalizing Verifiable Instruction Following**, NeurIPS38. https://arxiv.org/abs/2507.02833 — IFEvalからIFBenchへの拡張、2025年モデル比較、設問単位・緩和判定、生成温度を確認した。主要該当節と図・生成設定のみを読了範囲とする。
- Ai2, **Generalizing Verifiable Instruction Following** (current README). https://github.com/allenai/IFBench — IFEval25判定器の継続同梱、58新条件との関係を確認した。IFBenchデータの再配布は行わない。

## 13例と権利

公式データの実例13件（本編3、追加10）を異なるkeyで選んだ。完全な依頼文、公式instruction_id_listとkwargs、追加した日本語訳・要求する形式・解説は[事例票](skill-proofreading/ifeval/examples.json)へ記録した。唯一の正解文はなく、架空の参照回答は作成していない。判定器の静的読解だけを行い、モデル生成・評価ハーネス・外部生成APIは実行していない。

データとコードのApache License2.0および帰属は[ライセンス](licenses/ifeval/LICENSE-IFEval-Apache-2.0.txt)と[帰属情報](licenses/ifeval/ATTRIBUTION-IFEval.md)に保持する。引用した判定コードをスライドに再配布するのではなく、公開された条件の意味を説明した。公式GitHub README画面は2026-10-26に取得し、実描画を確認した。独立した製品サイトを推測で作らず、論文の公式配布先を入口とした。

件数・採点・成績の根拠と、本人が読んだ範囲は[監査票](data-audits/ifeval.json)、取得結果は[source-acquisition.json](skill-proofreading/ifeval/source-acquisition.json)に残した。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-ifeval.pptx)・[PDF](../slides/datasets-in-10-minutes-ifeval.pdf)。本編25頁、総45頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/ifeval.json)・[校正の修正対](skill-proofreading/ifeval.md)・[全ページ文言](skill-proofreading/ifeval/pages.jsonl)・[最終検証票](skill-proofreading/ifeval/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-IFEval-Apache-2.0.txt](licenses/ifeval/LICENSE-IFEval-Apache-2.0.txt)、[ATTRIBUTION-IFEval.md](licenses/ifeval/ATTRIBUTION-IFEval.md)。
