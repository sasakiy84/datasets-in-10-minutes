# FrontierMath — sources

参照日: 2026-10-21（日本時間）。対象は Tiers 1–4。338問を現在のFrontierMath全プログラムの総数とは扱わない。

- **FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI** — https://arxiv.org/abs/2411.04872
  構築、数学者の査読、著者、2024年当時の評価。取得PDFは改訂版。
- **FrontierMath Tier 4 (v2)** — https://epoch.ai/benchmarks/frontiermath-tier-4-v2
  2026年6月12日の改訂、338問、135修正・12削除、採点環境と公開ログ。
- **Sample Problems** — https://epoch.ai/frontiermath/tiers-1-4/benchmark-problems
  公開12問の原文・解法・最終答案。掲載9問。
- **About FrontierMath** — https://epoch.ai/frontiermath/tiers-1-4/about
  専門家の構築、難度、資金・公開範囲。旧350問の説明は現在件数に使用しない。
- **GPT-6.1 Sol** — https://epoch.ai/models/gpt-6-1-sol
  Epoch AIの現在の比較表。Tier 4 v2の整数丸め表示100/98/95/39。
- **GPT-6 Astra** — https://openai.com/index/gpt-6-astra/
  発表時のTier 4 v2 97.6%。Epoch表の98%とは表示精度が異なる。
- **FrontierMath** — https://epoch.ai/frontiermath
  Tiers 1–4 / Open Problems / Erdősの現在の課題群。
- **Joshua Ducey** — https://www.jmu.edu/mathstat/people/faculty-full-time/ducey-joshua.shtml
  所属と研究分野。
- **FrontierMath Tiers 1–4** — https://epoch.ai/frontiermath/tiers-1-4
  公式サイト実ブラウザ画像。

公開問題は問題文と解法を公式ページから取得し、原文の内容を無言で訂正していない。複雑な数式は公式原文をMathJaxで再組版した画像、短い原文・日本語・表・正解はPowerPointネイティブである。公開例と非公開評価集合は別に扱う。本文の600秒は予定値であり、読み上げや流し読みの実測値ではない。

公式サイトは実ブラウザでCSS・フォントの読み込み後に撮影。cookie表示を閉じ、ヘッダーと説明本文が読めるviewportを使用した。原文画像の改行・分割と数式区切りの正規化は question-parts.json / capture-parts-log.json に記録。非公開問題の取得、モデルAPI、Gemini、キー環境変数の読み取りは行っていない。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-frontiermath.pptx)・[PDF](../slides/datasets-in-10-minutes-frontiermath.pdf)。本編32頁、総61頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/frontiermath.json)・[校正の修正対](skill-proofreading/frontiermath.md)・[全ページ文言](skill-proofreading/frontiermath/pages.jsonl)・[最終検証票](skill-proofreading/frontiermath/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-FrontierMath-public.txt](licenses/frontiermath/LICENSE-FrontierMath-public.txt)。
