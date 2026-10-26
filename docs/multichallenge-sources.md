# MultiChallengeの出典と実例

## 一次資料

- Ved Sirdeshmukh, Kaustubh Deshpande, Johannes Mols, Lifeng Jin, Ed-Yeremai Cardona, Dean Lee, Jeremy Kritz, Willow Primack, Summer Yue, Chen Xing (2025). *MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs*. arXiv:2501.17399, v2 (2025-03-06). https://arxiv.org/abs/2501.17399
  - 四つの評価軸、会話の候補生成と人による改訂、判定質問を用いる採点、人手評価と自動採点の比較を報告する。
  - 70ページを取得し、本文pp.1–9の関連箇所を実読した。全70ページを通読したとは扱わない。初期の成績表と本文の一部に数値の不一致があるため、表の値を採用した。
- Scale AI (2026). *MultiChallenge*. Hugging Face, test. https://huggingface.co/datasets/ScaleAI/MultiChallenge
  - 現行の公式配布。固定したrevisionは670fd81f270314d0f8f82b34fcfe2187fd28f699。266会話の履歴、評価軸、採点質問、合格判定を含む。
  - 全266件を機械取得・集計し、選定13件の全会話・判定質問・合格条件を実読した。266件すべてを人手で精読したとは扱わない。
- Scale AI (n.d.; 2026-10-26参照). *Scale Labs Leaderboard: MultiChallenge*. https://labs.scale.com/leaderboard/multichallenge
  - 現行モデルの成績、95%信頼区間、採点モデルの更新を掲載する。公開ページでは試行回数・温度の詳細を確認できなかったため、公開CLIの既定1回を現行表へ転用していない。
  - scale.comからlabs.scale.comへリダイレクトする。最初の撮影は相対CSSの参照先がずれたため不採用にし、正規のlabs.scale.comでCSS・フォント・ロゴ・表が表示された画面を取得して実見した。
- Scale AI / ekwinox117 (2025). *MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs*. Official repository. https://github.com/ekwinox117/multi-challenge
  - 固定commitは5ccefcca6a39020d66c1383c4e6a809cb07afa33。main.py、src/evaluator.py、src/conversation.py、src/result_parser.pyを静的に読んだ。採点は判定結果とpass_criteriaの一致、総合は四評価軸の正解率の単純平均、複数回指定時は一度でも合格した会話を合格とする。
  - 応答生成や評価ハーネス、外部生成APIは実行していない。公開コードは研究時の実装であり、現在の公式リーダーボードの実行条件をすべて再現するものとは主張していない。

## 選定と表示

現行公式配布から、本編3件、Appendix10件の異なる13会話を選んだ。指示の保持5件、過去の利用者情報の活用4件、会話内の一貫性2件、過去の版を踏まえた改訂2件を含む。最初の候補は短い指示制約に偏っていたため、5件を差し替えて異なる能力が分かる構成にした。

会話履歴の既存アシスタント応答も、最後の利用者発言までの固定入力として保持した。最後の応答は新しく生成していない。唯一の正解文は作らず、公開判定質問に対応する「期待される応答」を示す。target_questionとpass_criteriaは採点用で、回答するモデルへの入力とは分けた。

原文と日本語訳は全文を示す。文量が多い会話は、発言・段落・コードブロックなどの意味のまとまりで分け、コードの導入文とブロックを一緒に保つ。元の空行は読みやすさのため詰めることがあるが、文言・数値・役割・列挙・コードを削除しない。訳を同じページへ入れるために原文を分割していない。短い最終訳と期待挙動・解説をまとめられる場合は同じページに置いた。

原票・日本語訳・採点質問の対応は[実例記録](skill-proofreading/multichallenge/examples.json)、集計・版・採点・確認範囲は[データ監査](skill-proofreading/multichallenge/data-audit.json)、変更対は[校正記録](skill-proofreading/multichallenge.md)に残す。

## 利用条件と帰属

現行の公式データカードはCC BY 4.0を指定する。出典、著者・配布元、ライセンス、訳と解説を追加したことを示し、[ライセンス原文](licenses/multichallenge/LICENSE-MultiChallenge-CC-BY-4.0.txt)と[帰属情報](licenses/multichallenge/ATTRIBUTION-MultiChallenge.md)を保存する。公式サイトの画面は、説明対象を示す引用としてURLを対応させ、データのCC BY 4.0がサイト全体を覆うとは扱わない。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-multichallenge.pptx)・[PDF](../slides/datasets-in-10-minutes-multichallenge.pdf)。本編39頁、総116頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/multichallenge.json)・[校正の修正対](skill-proofreading/multichallenge.md)・[全ページ文言](skill-proofreading/multichallenge/pages.jsonl)・[最終検証票](skill-proofreading/multichallenge/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-MultiChallenge-CC-BY-4.0.txt](licenses/multichallenge/LICENSE-MultiChallenge-CC-BY-4.0.txt)、[ATTRIBUTION-MultiChallenge.md](licenses/multichallenge/ATTRIBUTION-MultiChallenge.md)。
