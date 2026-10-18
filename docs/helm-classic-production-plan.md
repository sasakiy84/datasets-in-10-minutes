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
|16|lsat|lsat_qa|未着手|
|17|medqa|med_qa|未着手|
|18|lextreme|lextreme|未着手|
|19|lexglue|lex_glue|未着手|
|20|billsum|billsum_legal_summarization|未着手|
|21|multilexsum|multilexsum_legal_summarization|未着手|
|22|eurlexsum|eurlexsum_legal_summarization|未着手|
|23|data-imputation|entity_data_imputation|未着手|
|24|entity-matching|entity_matching|未着手|
|25|copyright-text|copyright_text|未着手|
|26|copyright-code|copyright_code|未着手|
|27|disinformation|disinformation_reiteration, disinformation_wedging|未着手|
|28|realtoxicityprompts|real_toxicity_prompts|未着手|
|29|synthetic-efficiency|synthetic_efficiency|未着手|

各資料で一次資料と公開実例を調べ、本編3例と追加10例を目安に選定。日本語校正スキルをページごとに適用し、原文・訳・参照回答・出典、全ページ描画、引用・表・参考文献の個別確認を終えてから、資料ごとにコミットする。Geminiは使わない。
