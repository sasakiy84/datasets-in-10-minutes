# HELM Classicの制作対象と進捗

対象：[HELM Classic latest](https://crfm.stanford.edu/helm/classic/latest/)。確認時点で指す版は**v0.4.0（2023-11-17）**。公開スキーマの分類・分析軸、具体的なシナリオ、構想上の領域を分け、同じデータセットの評価条件違いを重複した制作件数に数えない。

最初の5資料はBoolQ、HellaSwag、TruthfulQA、IMDb、XSum。いずれも既存28資料にはなく、読解、常識的な文章補完、真実性、感情分類、要約を横断でき、公開実例がある。

CLEVA系列は最後に扱う。CLEVAそのものの仕組みと評価設計を紹介する資料を用意し、個別データセットは事例が公開されていれば、それぞれ独立した資料にする。スキーマの31個のタスク群を、31個のデータセットとして扱わない。

GSM8KとHumanEvalは既存資料で対象データセットを紹介済み。MMLUに関連する既存のMMMLUは多言語版の資料なので、MMLUを作成済みとは扱わない。HELM固有の設定について必要な追補は、その対象を制作・更新する際に照合する。

[機械可読の全項目・実行設定件数・出典ハッシュ](helm-classic-coverage.json)。実行設定件数は公開されたrun_specsのgroupsに、その名前が含まれる件数。0件はシナリオや公開事例が存在しないことを意味しない。

## 個別シナリオ

|シナリオ|表示名|状態|資料|
|---|---|---|---|
|boolq|BoolQ|作成済み|[PPTX](../slides/datasets-in-10-minutes-boolq.pptx) / [PDF](../slides/datasets-in-10-minutes-boolq.pdf)|
|narrative_qa|NarrativeQA|未着手||
|natural_qa_closedbook|NaturalQuestions (closed-book)|未着手||
|natural_qa_openbook_longans|NaturalQuestions (open-book)|未着手||
|quac|QuAC (Question Answering in Context)|未着手||
|hellaswag|HellaSwag|作成済み|[PPTX](../slides/datasets-in-10-minutes-hellaswag.pptx) / [PDF](../slides/datasets-in-10-minutes-hellaswag.pdf)|
|openbookqa|OpenbookQA|未着手||
|truthful_qa|TruthfulQA|作成済み|[PPTX](../slides/datasets-in-10-minutes-truthfulqa.pptx) / [PDF](../slides/datasets-in-10-minutes-truthfulqa.pdf)|
|mmlu|MMLU (Massive Multitask Language Understanding)|未着手||
|msmarco_regular|MS MARCO (regular track)|未着手||
|msmarco_trec|MS MARCO (TREC track)|未着手||
|summarization_cnndm|CNN/DailyMail|未着手||
|summarization_xsum|XSUM|作成済み|[PPTX](../slides/datasets-in-10-minutes-xsum.pptx) / [PDF](../slides/datasets-in-10-minutes-xsum.pdf)|
|imdb|IMDB|作成済み|[PPTX](../slides/datasets-in-10-minutes-imdb.pptx) / [PDF](../slides/datasets-in-10-minutes-imdb.pdf)|
|raft|RAFT (Real-world Annotated Few-Shot)|未着手||
|civil_comments|CivilComments|未着手||
|ice|ICE (International Corpus of English)|未着手||
|the_pile|The Pile|未着手||
|twitter_aae|TwitterAAE|未着手||
|twitter_aae_aa|TwitterAAE (AA)|未着手||
|twitter_aae_white|TwitterAAE (white)|未着手||
|blimp|BLiMP (The Benchmark of Linguistic Minimal Pairs for English)|未着手||
|wikifact|WikiFact|未着手||
|babi_qa|bAbI|未着手||
|dyck_language|Dyck|未着手||
|numeracy|Numerical reasoning|未着手||
|synthetic_reasoning|Synthetic reasoning (abstract symbols)|未着手||
|synthetic_reasoning_natural|Synthetic reasoning (natural language)|未着手||
|gsm|GSM8K (Grade school math word problems)|作成済み|[PPTX](../slides/datasets-in-10-minutes-gsm8k.pptx)|
|math_regular|MATH|未着手||
|math_chain_of_thought|MATH (chain-of-thought)|未着手||
|code_apps|APPS (Code)|未着手||
|code_humaneval|HumanEval (Code)|作成済み|[PPTX](../slides/datasets-in-10-minutes-humaneval.pptx)|
|legalbench|LegalBench|未着手||
|legal_support|LegalSupport|未着手||
|lsat_qa|LSAT|未着手||
|med_qa|MedQA|未着手||
|wmt_14|WMT 2014|未着手||
|lextreme|LEXTREME|未着手||
|lex_glue|LexGLUE|未着手||
|billsum_legal_summarization|BillSum|未着手||
|multilexsum_legal_summarization|MultiLexSum|未着手||
|eurlexsum_legal_summarization|EurLexSum|未着手||
|entity_data_imputation|Data imputation|未着手||
|entity_matching|Entity matching|未着手||
|copyright_text|Copyright (text)|未着手||
|copyright_code|Copyright (code)|未着手||
|disinformation_reiteration|Disinformation (reiteration)|未着手||
|disinformation_wedging|Disinformation (wedging)|未着手||
|bbq|BBQ (Bias Benchmark for Question Answering)|未着手||
|bold|BOLD (Bias in Open-Ended Language Generation Dataset)|未着手||
|real_toxicity_prompts|RealToxicityPrompts|未着手||
|synthetic_efficiency|Synthetic efficiency|未着手||

## CLEVAのタスク群

|シナリオ|表示名|状態|資料|
|---|---|---|---|
|cleva_closed_book_question_answering|CLEVA (Chinese) closed book question answering|CLEVA系列として最後に着手||
|cleva_summarization|CLEVA (Chinese) summarization|CLEVA系列として最後に着手||
|cleva_text_classification|CLEVA (Chinese) text classification|CLEVA系列として最後に着手||
|cleva_translation|CLEVA (Chinese) translation|CLEVA系列として最後に着手||
|cleva_data_to_text_generation|CLEVA (Chinese) data to text generation|CLEVA系列として最後に着手||
|cleva_dialogue_generation|CLEVA (Chinese) dialogue generation|CLEVA系列として最後に着手||
|cleva_opinion_mining|CLEVA (Chinese) opinion mining|CLEVA系列として最後に着手||
|cleva_paraphrase_generation|CLEVA (Chinese) paraphrase generation|CLEVA系列として最後に着手||
|cleva_paraphrase_identification|CLEVA (Chinese) paraphrase identification|CLEVA系列として最後に着手||
|cleva_reading_comprehension|CLEVA (Chinese) reading comprehension|CLEVA系列として最後に着手||
|cleva_sentiment_analysis|CLEVA (Chinese) sentiment analysis|CLEVA系列として最後に着手||
|cleva_language_modeling|CLEVA (Chinese) language modeling|CLEVA系列として最後に着手||
|cleva_pinyin_transliteration|CLEVA (Chinese) pinyin transliteration|CLEVA系列として最後に着手||
|cleva_classical_chinese_understanding|CLEVA (Chinese) classical Chinese understanding|CLEVA系列として最後に着手||
|cleva_coreference_resolution|CLEVA (Chinese) coreference resolution|CLEVA系列として最後に着手||
|cleva_intent_understanding|CLEVA (Chinese) intent understanding|CLEVA系列として最後に着手||
|cleva_subject_knowledge|CLEVA (Chinese) subject knowledge|CLEVA系列として最後に着手||
|cleva_cultural_knowledge|CLEVA (Chinese) cultural knowledge|CLEVA系列として最後に着手||
|cleva_reasoning_primitive|CLEVA (Chinese) reasoning primitive|CLEVA系列として最後に着手||
|cleva_deductive_reasoning|CLEVA (Chinese) deductive reasoning|CLEVA系列として最後に着手||
|cleva_inductive_reasoning|CLEVA (Chinese) inductive reasoning|CLEVA系列として最後に着手||
|cleva_code_synthesis|CLEVA (Chinese) code synthesis|CLEVA系列として最後に着手||
|cleva_commonsense_reasoning|CLEVA (Chinese) commonsense reasoning|CLEVA系列として最後に着手||
|cleva_mathematical_reasoning|CLEVA (Chinese) mathematical reasoning|CLEVA系列として最後に着手||
|cleva_conceptual_generalization|CLEVA (Chinese) conceptual generalization|CLEVA系列として最後に着手||
|cleva_toxicity_detection|CLEVA (Chinese) toxicity detection|CLEVA系列として最後に着手||
|cleva_bias|CLEVA (Chinese) bias|CLEVA系列として最後に着手||
|cleva_copyright|CLEVA (Chinese) copyright|CLEVA系列として最後に着手||
|cleva_fact_checking|CLEVA (Chinese) fact checking|CLEVA系列として最後に着手||
|cleva_instruction_following|CLEVA (Chinese) instruction following|CLEVA系列として最後に着手||
|cleva_mathematical_calculation|CLEVA (Chinese) mathematical calculation|CLEVA系列として最後に着手||

## 構想上の領域

|シナリオ|表示名|状態|資料|
|---|---|---|---|
|data_to_text_generation|Data-to-text generation|対象データセットの具体化が必要||
|fact_verification|Fact verification|対象データセットの具体化が必要||
|copywriting|Copywriting|対象データセットの具体化が必要||
|story_generation|Story generation|対象データセットの具体化が必要||
|biomedical_scenarios|Biomedical scenarios|対象データセットの具体化が必要||
|clinical_scenarios|Clinical scenarios|対象データセットの具体化が必要||
|financial_scenarios|Financial scenarios|対象データセットの具体化が必要||
|customer_service_scenarios|Customer services scenarios|対象データセットの具体化が必要||
|educational_scenarios|Educational scenarios|対象データセットの具体化が必要||
|very_recent_scenarios|Very recent scenarios|対象データセットの具体化が必要||
|historical_scenarios|Scenarios involving historic data|対象データセットの具体化が必要||
|not_native_English_speaker|Scenarios involving non-native speakers|対象データセットの具体化が必要||
|non_US_demographics|Scenarios involving data from marginalized demographics in non-US English-speaking regions|対象データセットの具体化が必要||
|user_facing_tasks_english_dialects|Scenarios with user-facing tasks on English dialects|対象データセットの具体化が必要||

## 分類・分析軸

|シナリオ|表示名|状態|資料|
|---|---|---|---|
|core_scenarios|Core scenarios|進捗集計の対象外||
|targeted_evaluations|Targeted evaluations|進捗集計の対象外||
|question_answering|Question answering|進捗集計の対象外||
|information_retrieval|Information retrieval|進捗集計の対象外||
|summarization|Summarization|進捗集計の対象外||
|sentiment_analysis|Sentiment analysis|進捗集計の対象外||
|toxicity_detection|Toxicity detection|進捗集計の対象外||
|miscellaneous_text_classification|Text classification|進捗集計の対象外||
|aspirational|Aspirational scenarios|進捗集計の対象外||
|language|Language|進捗集計の対象外||
|knowledge|Knowledge|進捗集計の対象外||
|reasoning|Reasoning|進捗集計の対象外||
|harms|Harms|進捗集計の対象外||
|efficiency|Efficiency|進捗集計の対象外||
|calibration|Calibration|進捗集計の対象外||
|ablation_in_context|Vary number of in-context examples|進捗集計の対象外||
|ablation_multiple_choice|Vary multiple-choice strategy|進捗集計の対象外||
|ablation_prompts|Vary prompting|進捗集計の対象外||
|robustness_contrast_sets|Robustness to contrast sets|進捗集計の対象外||
|robustness_individual|Robustness to single types of perturbations|進捗集計の対象外||
|chinese_cleva|CLEVA (Chinese) scenarios|CLEVA系列として最後に着手||
