# データセット紹介47資料の日本語・内容構成の見直し

対象は直近に一括制作した47資料（改訂前2,811ページ）。EPRSTMTで承認された改善案と、その後の「各データセット自体を解説する」という指示に沿って、概要と使い方が伝わる内容へ改める。

一覧は資料を選ぶために使い、採用先の評価基盤を解説の主題にしない。データセットの目的、原文を含む実例、構築、評価、利用と入手を中心に、章と表を組み直す。単に基盤名を別の語へ置き換える修正にはしない。作成主体と採用先は一次資料で照合する。

Geminiは使用せず、リポジトリの日本語校正・データセット紹介・スライド制作の各スキルを用いた。作成担当が各ページを確認し、別担当が独立レビューを行い、メインが最終成果物を確認する。資料ごとにコミットする。

不自然な直訳、主述や助詞の不一致、抽象的で意味を追いにくい表現を修正する。チェックサム、制作時の照合手順、細かな実行設定や重複説明はスライドから外し、検証記録に保存する。実例の原文と正解、意味のある数値、評価条件、利用条件、結果を解釈するうえで必要な制約は保持する。

各資料の変更表には修正前後の文言、削除・統合の理由、改訂前後のページ対応を記録する。独立レビューとメインの記録には、実施した確認と最終成果物のハッシュを残す。

最新方針での反映済み：31 / 47資料。反映済み資料は合計1839ページから1500ページへ整理。

| 資料 | 改訂前 | 改訂後 | 修正内容 |
|---|---:|---:|---|
| eprstmt | 58 | 39 | [修正前後の表](skill-proofreading/eprstmt/editorial-2026-10/changes.md) |
| afqmc | 57 | 39 | [修正前後の表](skill-proofreading/afqmc/editorial-2026-10/changes.md) |
| ocnli | 57 | 48 | [修正前後の表](skill-proofreading/ocnli/editorial-2026-10/changes.md) |
| math23k | 59 | 45 | [修正前後の表](skill-proofreading/math23k/editorial-2026-10/changes.md) |
| narrativeqa | 62 | 54 | [修正前後の表](skill-proofreading/narrativeqa/editorial-2026-10/changes.md) |
| naturalquestions | 67 | 53 | [修正前後の表](skill-proofreading/naturalquestions/editorial-2026-10/changes.md) |
| quac | 66 | — | 最新方針に沿って確認・修正中 |
| cnn-dailymail | 69 | — | 最新方針に沿って確認・修正中 |
| cmedqa2 | 56 | 43 | [修正前後の表](skill-proofreading/cmedqa2/editorial-2026-10/changes.md) |
| cold | 60 | 44 | [修正前後の表](skill-proofreading/cold/editorial-2026-10/changes.md) |
| msmarco | 61 | 43 | [修正前後の表](skill-proofreading/msmarco/editorial-2026-10/changes.md) |
| legal-support | 63 | 42 | [修正前後の表](skill-proofreading/legal-support/editorial-2026-10/changes.md) |
| lsat | 62 | — | 最新方針に沿って確認・修正中 |
| medqa | 53 | — | 最新方針に沿って確認・修正中 |
| lexglue | 57 | — | 最新方針に沿って確認・修正中 |
| lextreme | 55 | — | 最新方針に沿って確認・修正中 |
| ccpm | 54 | 45 | [修正前後の表](skill-proofreading/ccpm/editorial-2026-10/changes.md) |
| bustm | 54 | 45 | [修正前後の表](skill-proofreading/bustm/editorial-2026-10/changes.md) |
| chid | 58 | 52 | [修正前後の表](skill-proofreading/chid/editorial-2026-10/changes.md) |
| wmt2020-enzh | 60 | 48 | [修正前後の表](skill-proofreading/wmt2020-enzh/editorial-2026-10/changes.md) |
| twitter-aae | 49 | 36 | [修正前後の表](skill-proofreading/twitter-aae/editorial-2026-10/changes.md) |
| billsum | 79 | 72 | [修正前後の表](skill-proofreading/billsum/editorial-2026-10/changes.md) |
| eurlexsum | 66 | 63 | [修正前後の表](skill-proofreading/eurlexsum/editorial-2026-10/changes.md) |
| multilexsum | 69 | — | 最新方針に沿って確認・修正中 |
| cluewsc2020 | 60 | 49 | [修正前後の表](skill-proofreading/cluewsc2020/editorial-2026-10/changes.md) |
| the-pile | 56 | 51 | [修正前後の表](skill-proofreading/the-pile/editorial-2026-10/changes.md) |
| wikifact | 52 | 39 | [修正前後の表](skill-proofreading/wikifact/editorial-2026-10/changes.md) |
| dyck | 48 | — | 最新方針に沿って確認・修正中 |
| numeracy | 53 | 39 | [修正前後の表](skill-proofreading/numeracy/editorial-2026-10/changes.md) |
| synthetic-reasoning | 55 | — | 最新方針に沿って確認・修正中 |
| math | 55 | — | 最新方針に沿って確認・修正中 |
| legalbench | 84 | — | 最新方針に沿って確認・修正中 |
| crosswoz | 61 | 56 | [修正前後の表](skill-proofreading/crosswoz/editorial-2026-10/changes.md) |
| redefine | 53 | 46 | [修正前後の表](skill-proofreading/redefine/editorial-2026-10/changes.md) |
| pattern-matching-suppression | 54 | 48 | [修正前後の表](skill-proofreading/pattern-matching-suppression/editorial-2026-10/changes.md) |
| ice | 49 | 40 | [修正前後の表](skill-proofreading/ice/editorial-2026-10/changes.md) |
| data-imputation | 54 | 38 | [修正前後の表](skill-proofreading/data-imputation/editorial-2026-10/changes.md) |
| entity-matching | 59 | — | 最新方針に沿って確認・修正中 |
| copyright-code | 57 | — | 最新方針に沿って確認・修正中 |
| copyright-text | 55 | — | 最新方針に沿って確認・修正中 |
| chef | 65 | 58 | [修正前後の表](skill-proofreading/chef/editorial-2026-10/changes.md) |
| cdial-bias | 59 | 51 | [修正前後の表](skill-proofreading/cdial-bias/editorial-2026-10/changes.md) |
| c3 | 65 | 54 | [修正前後の表](skill-proofreading/c3/editorial-2026-10/changes.md) |
| cleva | 62 | 54 | [修正前後の表](skill-proofreading/cleva/editorial-2026-10/changes.md) |
| disinformation | 76 | 66 | [修正前後の表](skill-proofreading/disinformation/editorial-2026-10/changes.md) |
| realtoxicityprompts | 62 | — | 最新方針に沿って確認・修正中 |
| synthetic-efficiency | 66 | — | 最新方針に沿って確認・修正中 |

EPRSTMTは承認済み44項目の対応表も保持する。各資料の詳細記録は`docs/skill-proofreading/<資料名>/editorial-2026-10/`にある。原制作・初回校正の記録は`previous/`、その後の再構成前の記録は`earlier-editorial-pass/`に保存する。
