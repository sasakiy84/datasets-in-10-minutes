# HELM Classic：残りの制作順

2026-10-18にlatest/config.jsを再確認。最新版は引き続きv0.4.0（2023-11-17）。既存資料の体裁修正ではなく、未作成データセットの新規資料を順に制作する。

同じデータの評価条件違いをまとめ、非CLEVAの36シナリオを29資料に整理した。HELM独自の生成課題やコーパスも、対象・作り方・評価方法を明らかにして扱う。CLEVAは最後にプラットフォーム資料を作り、公開事例のある構成データセットを個別に制作する。構成データセット数は実データで確かめる。

|順|対象|HELMシナリオ|状態|
|---|---|---|---|
|1|narrativeqa|narrative_qa|作成済み|
|2|naturalquestions|natural_qa_closedbook, natural_qa_openbook_longans|作成済み|
|3|quac|quac|作成済み|
|4|msmarco|msmarco_regular, msmarco_trec|作成済み|
|5|cnn-dailymail|summarization_cnndm|作成済み|
|6|ice|ice|作成済み|
|7|the-pile|the_pile|作成済み|
|8|twitter-aae|twitter_aae, twitter_aae_aa, twitter_aae_white|作成済み|
|9|wikifact|wikifact|作成済み|
|10|dyck|dyck_language|作成済み|
|11|numeracy|numeracy|作成済み|
|12|synthetic-reasoning|synthetic_reasoning, synthetic_reasoning_natural|作成済み|
|13|math|math_regular, math_chain_of_thought|作成済み|
|14|legalbench|legalbench|作成済み|
|15|legal-support|legal_support|作成済み|
|16|lsat|lsat_qa|作成済み|
|17|medqa|med_qa|作成済み|
|18|lextreme|lextreme|作成済み|
|19|lexglue|lex_glue|作成済み|
|20|billsum|billsum_legal_summarization|作成済み|
|21|multilexsum|multilexsum_legal_summarization|作成済み|
|22|eurlexsum|eurlexsum_legal_summarization|作成済み|
|23|data-imputation|entity_data_imputation|作成済み|
|24|entity-matching|entity_matching|作成済み|
|25|copyright-text|copyright_text|作成済み|
|26|copyright-code|copyright_code|未着手|
|27|disinformation|disinformation_reiteration, disinformation_wedging|未着手|
|28|realtoxicityprompts|real_toxicity_prompts|未着手|
|29|synthetic-efficiency|synthetic_efficiency|未着手|

各資料で一次資料と公開実例を調べ、本編3例と追加10例を目安に選定。日本語校正スキルをページごとに適用し、原文・訳・参照回答・出典、全ページ描画、引用・表・参考文献の個別確認を終えてから、資料ごとにコミットする。Geminiは使わない。

## CLEVA系列

[採用元台帳](cleva-source-inventory.md)で31課題と公開元コーパスの対応を管理する。84データセット全件の復元はできていない。元データの紹介と、未取得のCLEVA選定・翻訳版を区別する。以下は元データの制作対象であり、84件を分解した一覧ではない。公開例が未確認の対象は一次配布の調査から始める。

|順|対象|資料範囲|状態|
|---|---|---|---|
|0|cleva|プラットフォーム|独立レビュー中|
|1|cluecorpus2020|CLUECorpus2020|未着手|
|2|cluewsc2020|CLUEWSC / CLUEWSC2020|未着手|
|3|ccpm|CCPM|制作中|
|4|chid|ChID|未着手|
|5|ocnli|OCNLI|制作中|
|6|math23k|Math23K|未着手|
|7|cold|COLD|調査中|
|8|cdial-bias|CDial-Bias|未着手|
|9|chef|CHEF|未着手|
|10|c3|C3|制作中|
|11|nlpcc2018-qa|NLPCC 2018 Open Domain QA|未着手|
|12|cmedqa2|cMedQA2|未着手|
|13|csds|CSDS|未着手|
|14|adgen|ADGEN / Shao2019 product advertising data|未着手|
|15|pku-paraphrase-bank|PKU Paraphrase Bank|未着手|
|16|crosswoz|CrossWOZ|未着手|
|17|wmt2020-enzh|WMT 2020 newstest2020 English–Chinese|未着手|
|18|bustm|BUSTM (FewCLUE)|未着手|
|19|afqmc|AFQMC (CLUE)|未着手|
|20|eprstmt|EPRSTMT (FewCLUE)|未着手|
|21|tnews|TNEWS (CLUE/FewCLUE)|未着手|
|22|ccl2020-humor|SPR / CCL2020 Humor Computation|未着手|

既存5資料はCLEVAでの翻訳・設定差を追記する。BIG-bench／Inverse Scaling／物理概念の出典系列は元のタスク・生成法を追加確認する。出所不明の5系列は公開説明例と未取得条件を記録し、別のデータセットの例で代用しない。
