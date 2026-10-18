# CLEVAで再利用される、既存資料の採用元

CLEVAの論文とHELM v0.4.0実装は、次の既存資料で紹介したデータセット・生成課題を参照している。各リンクは元データについての独立した資料であり、未取得のCLEVA選定・翻訳版を取得したものではない。プラットフォームの仕様は[CLEVA資料](../slides/datasets-in-10-minutes-cleva.pdf)、採用元と公開例の確認範囲は[採用元台帳](cleva-source-inventory.md)にまとめた。

|既存の独立資料|CLEVAでの対応|元資料との区別|
|---|---|---|
|[HumanEval](../slides/datasets-in-10-minutes-humaneval.pdf)|中国語のコード合成課題の採用元|元HumanEvalの英語プロンプト・テストと、CLEVAで中国語化されたプロンプトは別の版。未取得の翻訳集合の内容・採点結果を推測しない。|
|[TruthfulQA](../slides/datasets-in-10-minutes-truthfulqa.pdf)|閉じた知識に基づく質問応答のうち、真実性を扱う下位課題|CLEVAの公開説明例は中国語訳の多肢選択形式。元の英語質問・参照回答と、公開された中国語の説明例、未取得の評価集合を分ける。|
|[Dyck Language](../slides/datasets-in-10-minutes-dyck.pdf)|基礎的推論の括弧列生成|CLEVAはHELMに似た手順で合成すると説明する。生成規則の対応があっても、乱数・長さ分布・実際の事例が同一とは確定していない。|
|[Synthetic Reasoning](../slides/datasets-in-10-minutes-synthetic-reasoning.pdf)|パターン帰納・パターン照合・変数置換|元のHELM生成課題を独立資料で扱う。CLEVAでの中国語化・合成パラメータ・選択集合は別に確認が必要。|
|[Copyright (code)](../slides/datasets-in-10-minutes-copyright-code.pdf)|著作権関連評価のコード側の出典系列|既存資料のHELM公開実行記録・Linux照合版・権利表示は、その資料に示した対象についてのもの。CLEVAの変換・選定後のコード集合や成績とは同一視しない。中国語文章側は別の集合として制作する。|

これらの元データの成績をCLEVAでの成績として転載しない。翻訳・選択肢・参照回答・生成条件が変われば、同じ課題名でも比較条件が変わる。HELM Classic v0.4.0の公開run_specs 8,526件にCLEVAの実行記録はなく、公式READMEの参照値はプラットフォーム資料で条件とともに紹介している。

## 確認した一次資料

- Li et al. *CLEVA: Chinese Language Models EVAluation Platform*. EMNLP 2023 System Demonstrations, pp.186–217. https://aclanthology.org/2023.emnlp-demo.17/
- Stanford CRFM. HELM v0.4.0 CLEVA scenarios. https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py
- LaVi Lab. CLEVA公式リポジトリ。https://github.com/LaVi-Lab/CLEVA

[採用元台帳の位置・版・取得記録](cleva-source-inventory.json)、[プラットフォームの出典・独立レビュー](cleva-sources.md)も参照。
