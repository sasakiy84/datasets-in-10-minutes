# Global PIQA 制作・出典記録

2026-10-17（Asia/Tokyo）。本編29ページ、全64ページ。日本語の黙読・流し読み約10分を想定、未実測。著者sasakiy84。

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

公式ファイル一覧からnon-parallelの現行TSV136本、parallelの現行TSV131本を確認。全件TSVをダウンロードしたとはしていない。non-parallelの日本語・英語と、今回追加した10言語のTSVを取得。parallelは日本語・英語を取得。全体の件数・割合は2026年原著による。13,600 + (130×103 + 101) = 27,091問。

v1の原著はGPT-5.4、Claude Sonnet 4.6、Gemini 3.1 Proを評価する。掲載した平均値は公式aggregated_by_split.csvの値を100倍、小数第2位に丸めたもの。Geminiはnon-parallel 93.93% / parallel 96.83%、GPT-5.4は91.27% / 91.18%、Claudeは90.17% / 87.66%。Gemini 3 Proの2025年モデルカードのGlobal PIQAの値を、v1の値として流用しない。

生成設定は原著Appendix G：temperature 0.90、上限2048トークン、Gemini/Claudeのthinking 1024、GPT-5.4 medium（一部の上限超過例はlow再実行）。モデル別の言語正答率の平均。並行集合におけるGemini 3.1 Proの英語・ペルーのスペイン語・日本語・エクペイ語の成績を公開CSVで照合した。

## 実例と表示範囲

独立した問題は本編3件＋追加10件の13件。日本語・英語に加え、スペイン語（スペイン）、フランス語（フランス）、ドイツ語、ポルトガル語（ブラジル）、インドネシア語、スワヒリ語、アラビア語、ヒンディー語、韓国語、中国語（簡体字）を扱う。12言語から選んだ問題で、地域の食物・道具・慣習と、農具・水・乳製品などの日常知識を取り上げた。

原文の設問と全選択肢をそのまま掲載し、日本語以外の例は次ページに全文の日本語訳と正解を示す。日本語訳と文化語の補足は本資料で追加したもの。parallelの袋の問題は、日本語・英語で候補の並びが異なり、日本語A・英語Dが対応する。複数ページへ分けた同じ問題を件数に重ねて数えていない。

追加例は同じnon-parallel改訂6777742のTSVから、0始まりでspa_latn_spai[29]、fra_latn_fran[29]、deu_latn[57]、por_latn_braz[47]、ind_latn[14]、swh_latn[11]、arb_arab[34]、hin_deva[22]、kor_hang[21]、cmn_hans[62]を選定。英訳注釈も読み、設問・両候補・ラベルとの対応を確認した。アラビア語は右から左の段落とNoto Sans Arabic、ヒンディー語はNoto Sans Devanagariを明示し、実際のPDFで字形と記号の位置を確認する。

|ページ|内容|言語設定|ID|配布label|
|---:|---|---|---|---:|
|8|実例1：トイレ用スリッパ|`jpn_jpan`|`group0035_ex000062_jpn_jpan_0_v1`|0|
|9|実例2：調味料を分けて出す|`eng_latn`|`group0123_ex000088_eng_latn_0_v1`|1|
|10|実例2：日本語訳と解説|`eng_latn`|`group0123_ex000088_eng_latn_0_v1`|1|
|12|実例3：密封した袋の空気（日本語）|`jpn_jpan`|`parallel_ex000000_jpn_jpan`|0|
|13|同じ袋の問題を、英語で読む|`eng_latn`|`parallel_ex000000_eng_latn`|3|
|14|英語の選択肢を、日本語で確かめる|`eng_latn`|`parallel_ex000000_eng_latn`|3|
|33|追加例1：ネウラスを浸す|`spa_latn_spai`|`group0042_ex000020_spa_latn_spai_0_v1`|0|
|34|追加例1：日本語訳と解説|`spa_latn_spai`|`group0042_ex000020_spa_latn_spai_0_v1`|0|
|35|追加例2：クレープを焼く道具|`fra_latn_fran`|`group0004_ex000001_fra_latn_fran_0_v1`|1|
|36|追加例2：日本語訳と解説|`fra_latn_fran`|`group0004_ex000001_fra_latn_fran_0_v1`|1|
|37|追加例3：Bienenstichの二つの意味|`deu_latn`|`group0121_ex000066_deu_latn_0_v1`|1|
|38|追加例3：日本語訳と解説|`deu_latn`|`group0121_ex000066_deu_latn_0_v1`|1|
|39|追加例4：蚊が繁殖する水|`por_latn_braz`|`group0013_ex000094_por_latn_braz_0_v1`|0|
|40|追加例4：日本語訳と解説|`por_latn_braz`|`group0013_ex000094_por_latn_braz_0_v1`|0|
|41|追加例5：サンバルをすりつぶす|`ind_latn`|`group0010_ex000244_ind_latn_0_v1`|0|
|42|追加例5：日本語訳と解説|`ind_latn`|`group0010_ex000244_ind_latn_0_v1`|0|
|43|追加例6：くわの用途|`swh_latn`|`group0062_ex000182_swh_latn_0_v1`|1|
|44|追加例6：日本語訳と解説|`swh_latn`|`group0062_ex000182_swh_latn_0_v1`|1|
|45|追加例7：ハリッサの材料|`arb_arab`|`group0065_ex000039_arb_arab_0_v1`|0|
|46|追加例7：日本語訳と解説|`arb_arab`|`group0065_ex000039_arb_arab_0_v1`|0|
|47|追加例8：攪拌した乳製品|`hin_deva`|`group0098_ex000091_hin_deva_9_v1`|1|
|48|追加例8：日本語訳と解説|`hin_deva`|`group0098_ex000091_hin_deva_9_v1`|1|
|49|追加例9：餅の種類と食感|`kor_hang`|`group0018_ex000012_kor_hang_0_v1`|1|
|50|追加例9：日本語訳と解説|`kor_hang`|`group0018_ex000012_kor_hang_0_v1`|1|
|51|追加例10：快板での手の位置|`cmn_hans`|`group0048_ex000334_cmn_hans_2_v1`|1|
|52|追加例10：日本語訳と解説|`cmn_hans`|`group0048_ex000334_cmn_hans_2_v1`|1|

Pythonの読み込み例は公式データカードの設定名・分割と照合し、row 0のprompt/labelをTSVから読み込んで確認。制作環境にdatasetsライブラリは未導入であり、load_dataset呼び出し自体の実行済みとはしていない。

## 利用条件・画面・検証

データはCC BY-SA 4.0。転載した設問・選択肢・正解と、加えた日本語訳は同ライセンスで提供する。著者と配布先を実例ごとに表示。[ライセンス本文](licenses/global-piqa-CC-BY-SA-4.0.txt)。https://creativecommons.org/licenses/by-sa/4.0/ 。提供元は別途、AI学習および合成学習データの種としての利用を認めないと明記する。本資料は紹介・評価目的。

冒頭は公式リポジトリのREADMEを実ブラウザで撮影した。Global PIQA v1の説明と世界地図が見える位置で、CSSとフォントの読み込みを確認。https://github.com/mrlbenchmarks/global-piqa#readme

今回の全資料での配置・公式画面の確認結果は[横断レビュー](series-layout-and-sites-review.md)に記録。旧52ページ版のページ番号・ハッシュ・確認件数は、この改訂の値として流用しない。制作・調査・検査用のスクリプトはscratchのみへ置き、コミットしない。
