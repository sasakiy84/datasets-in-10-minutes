# MathVista：出典・実例・確認範囲

図形、グラフ、表、写真などを含む数学問題の評価データを紹介する。MathVistaの公開testminiから、本編3件と追加10件の異なる実例を選んだ。原文の設問・全選択肢・実画像を保持し、日本語訳、正解、説明を加えた。画像や数値から答えを読めることを優先した。

## 主要な一次資料

- Pan Lu et al. (2024), *MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts*, ICLR 2024. https://arxiv.org/abs/2310.02255 。成立の背景、収集と人手確認、分類、分割、初期の評価と誤り分析の根拠。主に導入と本文の構築・評価節、必要な比較表と定性的分析を実読した。116ページすべてや全参考文献の読了は主張していない。
- [公式サイト](https://mathvista.github.io/)と[公式実装](https://github.com/lupantech/MathVista)。データ形式、公開1,000問・正解非公開5,141問、利用条件、採点コード、EvalScopeの現在の掲載を確認した。公式サイトはCSS・フォントを読み込んで撮影し、画面自体を開いて確認した。
- [公式データ配布](https://huggingface.co/datasets/AI4Math/MathVista)。両分割のJSON計6,141行を取得し、課題・言語・問題形式・収集元を機械集計した。全6,141問の本文や全画像を読み終えたという意味ではない。選定13問の原文、画像、選択肢、正解と日本語は実読した。
- [公式の回答抽出](https://github.com/lupantech/MathVista/blob/main/evaluation/extract_answer.py)と[採点](https://github.com/lupantech/MathVista/blob/main/evaluation/calculate_score.py)。生成、短い答えの抽出、形式の正規化、一致判定を静的に確認した。選択肢の近似文字列対応と整数・小数の扱いも確認した。モデルや評価ハーネスは実行していない。
- OpenAI (2025-04-14), [*Introducing GPT-4.1 in the API*](https://openai.com/index/gpt-4-1/)。MathVistaの採用と、視覚評価表の値を直接確認した。2023年の構築時の実験と同じ採点条件とは主張せず、2025年に報告された値として示した。2026年の最新最高値を網羅したという意味ではない。

## 実例の収集元と選定

|例|公開ID|収集元|確認した答えの根拠|
|---:|---:|---|---|
|1|3|GeoQA+|内角の二等分線から145°を計算|
|2|74|ChartQA / Our World in Data|100%と52.4%の差47.6ポイント|
|3|44|TabMWP|2ドル/kgの二種類を合計し18ドル|
|4|7|IconQA|8時15分の時計と英文空欄|
|5|10|IQTest|文字と左右反転による図形の規則、選択肢E|
|6|17|GeoQA+|斜辺の中点と各頂点の等距離から5|
|7|23|FunctionQA|絶対値関数の右側の傾きがともに2|
|8|28|Geometry3K|直角三角形の三辺から半径8.5インチ|
|9|34|FunctionQA|整数位置での左右の極限の違い|
|10|37|FunctionQA|関数値4と、左右から近づく値3の違い|
|11|43|ScienceQA|月別の棒グラフで5月が最大|
|12|56|IconQA|1ヤードと2ヤードの長方形の周長6ヤード|
|13|188|PaperQA / FC-CLIP|A-847の列で20.0を超える三手法|

各画像を実際に開き、原票の問いと正解を照合した。例13の表はQihang Yu et al. (2023), *Convolutions Die Hard: Open-Vocabulary Segmentation with Single Frozen Convolutional CLIP*の[論文](https://arxiv.org/abs/2308.02487)でも該当する表と数値を確認した。IQTestの規則の説明は図からの解釈であり、配布側の解説を回収したものではない。

候補ID20は、棒の値9.29と12.51の和が21.37より大きいのに、配布正解がNoであったため除外した。正解を勝手に書き換えず、根拠を画像で確認できる別の公開問題を採用した。[除外記録](skill-proofreading/mathvista/excluded-candidates.json)と[13問の照合](skill-proofreading/mathvista/source-fact-verification.json)に残した。

## 利用条件

MathVistaの新規貢献はCC BY-SA 4.0だが、元の画像・設問の権利は各作成者にある。公式READMEの試験用途の商用利用・学習用途禁止という記述だけで、全素材を一律に再許諾されたものとして扱わない。IconQA、TabMWP、ScienceQAのREADME本文は、それぞれデータにCC BY-NC-SA 4.0を指定している。コードのMITや、内容が食い違うバッジをデータの条件へ置き換えていない。

ChartQAの選定画像にはOur World in Data・WHO/UNICEF JMPとCC BYの表示があり、それを保持した。GeoQA+の短いREADMEでは独立したデータ用ライセンスを確認できなかった。IQTestやFunctionQAのsource.jsonでは個々の元図のURLまでは特定できないため、全元画像の権利確認を完了したという主張はしていない。教材中の帰属付き実例として掲載し、元資料の権利を保持する。

[帰属と素材ごとの条件](licenses/mathvista/ATTRIBUTION-MathVista.md)、[元READMEの条件の原文](licenses/mathvista/SOURCE-LICENSE-STATEMENTS-MathVista.md)、[MathVistaのCC BY-SA本文](licenses/mathvista/LICENSE-MathVista-CC-BY-SA-4.0.txt)、[非商用の元データのCC BY-NC-SA本文](licenses/mathvista/LICENSE-original-sources-CC-BY-NC-SA-4.0.txt)を保存した。

## 制作・確認

Geminiや他の外部生成APIは使わず、ローカルの制作・日本語校正スキルを用いた。選定13問の画像の実見、計算・意味の確認、原文と日本語の実読、全ページの描画確認を行った。PNGは公式配布のデコード画像をそのまま埋め込み、画像の切り抜きや内容の変更はしていない。例28のTeX数式は意味を変えずネイティブテキストで読みやすく表記した。数値だけの選択肢は、訳でも値が同じため、同じ頁で一度示したものを共有する場合がある。

本編31ページ・全53ページ、各13実例。本編は600秒の流し読みを計画したが、時間は実測していない。[全ページの文言](skill-proofreading/mathvista/pages.jsonl)、[修正前後](skill-proofreading/mathvista/proofreading.json)、[データ・評価・利用の検証](data-audits/mathvista.json)、[作成担当の描画確認](skill-proofreading/mathvista/creator-visual-review.json)を参照。全ページの目視と技術検査を終えた版を固定し、独立担当が別にレビューする。Microsoft PowerPointでの開封確認は行っていない。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-mathvista.pptx)・[PDF](../slides/datasets-in-10-minutes-mathvista.pdf)。本編31頁、総53頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/mathvista.json)・[校正の修正対](skill-proofreading/mathvista.md)・[全ページ文言](skill-proofreading/mathvista/pages.jsonl)・[最終検証票](skill-proofreading/mathvista/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-MathVista-CC-BY-SA-4.0.txt](licenses/mathvista/LICENSE-MathVista-CC-BY-SA-4.0.txt)、[LICENSE-original-sources-CC-BY-NC-SA-4.0.txt](licenses/mathvista/LICENSE-original-sources-CC-BY-NC-SA-4.0.txt)、[ATTRIBUTION-MathVista.md](licenses/mathvista/ATTRIBUTION-MathVista.md)、[SOURCE-LICENSE-STATEMENTS-MathVista.md](licenses/mathvista/SOURCE-LICENSE-STATEMENTS-MathVista.md)。
