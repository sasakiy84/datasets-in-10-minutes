# LiveCodeBench 一次資料と確認範囲

確認日：2026-10-25。作成者：sasakiy84。

- Jain et al., *LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code*. https://arxiv.org/abs/2403.07974 。取得版v2（2024-06-06）、本文p.1–13とAppendix p.26–27を自読。四課題、構築、初期511問、平均テスト数、採点、権利説明を確認。全46頁を読了したとは記録しない。
- ICLR 2025 proceedings：https://proceedings.iclr.cc/paper_files/paper/2025/hash/94074dd5a072d28ff75a76dabed43767-Abstract-Conference.html 。発表先を確認。異なる版の収録数を混同しない。
- 公式サイト https://livecodebench.github.io/ 。CSS反映・画像読込後の実画面を撮影。スクリーンショットの出典は実際の画面に対応する。
- 公式実装 https://github.com/LiveCodeBench/LiveCodeBench 。README、MIT LICENSE、ERRATAを自読。確認コミット28fef95ea8c9f7a547c8329f2cd3d32b92c1fa24。
- 公式配布 https://huggingface.co/datasets/livecodebench/code_generation_lite 。確認リビジョン0fe84c3912ea0c4d4a78037083943e8f0c4dd505。loader全体、test6.jsonlの175件を列挙し、選定13件の問題文全文・書き出し・全34公開テストを静的に自読。累積release_v6は全増分の1055問であり、test6単体175問とは区別した。
- 公式Leaderboard https://livecodebench.github.io/leaderboard.html と同サイトperformances_generation.json。HTMLの実集計JS（問題ごとのpass@1平均）と初期期間date_marks[15]〜末尾を確認。454問、4モデルの値を一次JSONから再集計。これは公開済み成績の算術確認で、モデル評価の実行ではない。
- Moonshot AI, *Kimi K2.6 Model Card* https://huggingface.co/moonshotai/Kimi-K2.6 。2026年の公式表と脚注を自読。v6の値91.7/89.6/88.8/85.0、Kimi K2.6のThinking・10試行平均、他モデルの公式報告引用を確認。公式Leaderboardの454問と同条件とは扱わない。

13例の正解欄は、各問題の最初の公開入出力例に対する期待出力を示す。正解プログラム全体が配布されているとは述べない。追加テストの符号化内容は復号・実行していない。問題のプログラム、採点器、外部モデルは実行していない。
