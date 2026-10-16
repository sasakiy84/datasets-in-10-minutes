# Global PIQA 制作・出典記録

2026-10-17（Asia/Tokyo）。本編27ページ、全52ページ。日本語の黙読・流し読み約10分を想定、未実測。著者sasakiy84。

## 一次資料

- Chang, Tyler A., Catherine Arnett et al. **Global PIQA: Evaluating Commonsense Reasoning Across 100+ Languages and Cultures**. 2026-05-29のarXiv v2。https://arxiv.org/abs/2510.24081v2
- 初稿は **Global PIQA: Evaluating Physical Commonsense Reasoning Across 100+ Languages and Cultures**, 2025-10-28、データバージョンv0.1。https://arxiv.org/abs/2510.24081v1
- 公式リポジトリ https://github.com/mrlbenchmarks/global-piqa 、取得コミット `bc0400b`（2026-05-29）。READMEはGlobal PIQA v1を明記する。
- non-parallel配布 https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel 、改訂 `6777742fa3634c0583cda3b7f8a482ea7b1b0937`。
- parallel配布 https://huggingface.co/datasets/mrlbenchmarks/global-piqa-parallel 、改訂 `b0b18516a8bc2cb1106bce3dd4db32848ca715ea`。
- モデル別・言語別の結果 https://github.com/mrlbenchmarks/global-piqa/tree/main/eval_results 。両CSVを実読み込みして数値を照合した。
- 評価実装 https://github.com/mrlbenchmarks/lm-eval-global-piqa 。公開READMEの取得成功を確認。
- 先行PIQA：Bisk et al., AAAI 2020. https://arxiv.org/abs/1911.11641 。PIQAの正式名Physical Interaction: Question Answeringを、Global PIQAに含まれる略語の説明として表紙へ記載。Globalの推測した展開形は作っていない。

## バージョン・規模・評価

v0.1は116種類の言語で、二択の独自問題を収録。v1は136種類のnon-parallel（二択、各100問）と131種類のparallel（四択、通常103問、エクペイ語101問）を持ち、和集合141種類。言語・文字・地域を含めた種類の数とISO 639-3の言語の数を混同しない。原著ではnon-parallelは113個のISO言語コード、124個の言語・文字の組み合わせ。

公式ファイル一覧からnon-parallelの現行TSV136本、parallelの現行TSV131本を確認。全件TSVをダウンロードしたとはしていない。日本語・英語・スペイン語non-parallelと日本語・英語parallelを取得。全体の件数・割合は2026年原著による。13,600 + (130×103 + 101) = 27,091問。

v1の原著はGPT-5.4、Claude Sonnet 4.6、Gemini 3.1 Proを評価する。掲載した平均値は公式aggregated_by_split.csvの値を100倍、小数第2位に丸めたもの。Geminiはnon-parallel 93.93% / parallel 96.83%、GPT-5.4は91.27% / 91.18%、Claudeは90.17% / 87.66%。Gemini 3 Proの2025年モデルカードのGlobal PIQAの値を、v1の値として流用しない。

生成設定は原著Appendix G：temperature 0.90、上限2048トークン、Gemini/Claudeのthinking 1024、GPT-5.4 medium（一部の上限超過例はlow再実行）。モデル別の言語正答率の平均。並行集合におけるGemini 3.1 Proの英語・ペルーのスペイン語・日本語・エクペイ語の成績を公開CSVで照合した。

## 実例と表示範囲

独立した問題は本編3件＋追加10件の13件。同じ袋の問題を日本語・英語の2ページに示したが、1件として数える。全設問と選択肢を掲載、配布label 0〜3をA〜Dへ対応させた。同じparallel問題でも候補の並びと正解記号が言語間で変わり、日本語A・英語Dを照合した。

|掲載ページ|集合|ID|配布label|
|---:|---|---|---:|
|8|non-parallel|`group0035_ex000062_jpn_jpan_0_v1`|0|
|9|non-parallel|`group0123_ex000088_eng_latn_0_v1`|1|
|11|parallel|`parallel_ex000000_jpn_jpan`|0|
|31|non-parallel|`group0035_ex000003_jpn_jpan_0_v1`|1|
|32|non-parallel|`group0035_ex000079_jpn_jpan_0_v1`|0|
|33|non-parallel|`group0035_ex000014_jpn_jpan_0_v1`|0|
|34|non-parallel|`group0035_ex000012_jpn_jpan_0_v1`|0|
|35|non-parallel|`group0035_ex000036_jpn_jpan_0_v1`|0|
|36|non-parallel|`group0035_ex000013_jpn_jpan_0_v1`|1|
|37|non-parallel|`group0035_ex000007_jpn_jpan_0_v1`|0|
|38|non-parallel|`group0035_ex000053_jpn_jpan_0_v1`|1|
|39|non-parallel|`group0123_ex000012_eng_latn_0_v1`|0|
|40|non-parallel|`group0123_ex000075_eng_latn_0_v1`|1|

掲載した日本語non-parallel例はllm_used=1であり、Appendixでその属性を説明した。母語話者による検証と、全体4.1%というLLM補助率を両立させて記載する。明らかに正解との整合が取りにくい候補（例：古いテレビがいつも歌舞伎を映すとする問題）は選定していない。

Pythonの読み込み例は公式データカードの設定名・分割と照合し、row 0のprompt/labelをTSVから読み込んで確認。制作環境にdatasetsライブラリは未導入であり、load_dataset呼び出し自体の実行済みとはしていない。

## 利用条件・画面・検証

データはCC BY-SA 4.0。転載した設問・選択肢・正解と、加えた日本語訳は同ライセンスで提供する。著者と配布先を実例ごとに表示。[ライセンス本文](licenses/global-piqa-CC-BY-SA-4.0.txt)。https://creativecommons.org/licenses/by-sa/4.0/ 。提供元は別途、AI学習および合成学習データの種としての利用を認めないと明記する。本資料は紹介・評価目的。

公式配布のFiles and versionsを実ブラウザで撮影し、CSS4枚とSource Sans Pro適用、フォント準備完了を確認。画像は実物を目視した。アバター等の補助リソースの接続失敗は取得記録に残す。

全52ページを一覧で確認し、14実例ページ（同一問題の英語版を含む）、全10表、コード、参考文献3ページ、表紙を1440×811で個別確認した。本文・出典の最小間隔12.24 pt、参考文献の項目間25.91 pt以上、コード上下余白10.88 / 11.19 pt。最終修正はp.46で、他51ページは確認済み版とピクセル一致。

PPTX全表示段落とPDFの文字を照合し、文字欠落・ページ外文字・通常タイトルの折り返しなし。全表のセル内収容と表注間隔を確認。booktabsの上下1.2 pt、見出し境界0.6 pt、縦罫線なし。PPTX ZIP、内部参照、ノートなしを確認。XML67部品を検証し、共通マスターのbuSzPctに既知の字句差124件がある以外、予期しないスキーマエラーなし。

制作スクリプト・調査コード・検査コードはscratchに置き、リポジトリやスキルに追加しない。

|成果物|bytes|SHA-256|
|---|---:|---|
|PDF|1,037,588|`72f439f6b470c6d694d37e01cd951087510d96ee6121c1f436381d0b57d92ed5`|
|PPTX|258,026|`ad7098cfff0863c08e90987f5aa548c9e8109dd9bdce85464f3f446e0ae76874`|

21件のギャラリーをビルドし、全サムネイル読み込み、タイトルの大小・全角検索、言語・質問応答・2025年フィルタ、年順、カードのPDFリンク、PPTX取得、390 px表示の横はみ出しなしを実ブラウザで確認。PPTX・PDFは確認済みscratch・リポジトリ・公開ビルドの3か所でSHA-256一致。
