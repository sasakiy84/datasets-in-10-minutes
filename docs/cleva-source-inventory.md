# CLEVA 個別データセット採用元の独立調査

2026-10-18。正式EMNLP2023論文、固定HELM v0.4.0設定・説明例、原配布を照合。新規スライドは制作していない。

台帳37行：confirmed 32、unavailable 5。confirmedは採用元または出典系列の確定であり、CLEVA原評価集合の取得済みを意味しない。candidateは各行内にも明示した。

31課題、65課題/下位課題組、253プロンプトは、論文の84データセットと単位が違う。84件を復元したとは主張しない。22既存中国語データセットも本台帳の系列単位で数え直さない。公開CLEVA runは0、原評価集合は未取得。

## 原配布照合で追加確定した点

FewCLUE BUSTM/EPRSTMT、CLUE AFQMC/TNEWSは原文とラベルを直接照合した。CCPM、C3、CLUEWSC、OCNLI、COLD、Math23K、幽默分類、CrossWOZでも原例または著者配布への対応を確認した。詳細な位置とSHAは各JSONに保持。

WMTの論文1例・HELM2例は公式WMT2020 test archiveのsource/reference両方に一致する。これでWMT2020由来の公開例は確定するが、CLEVA翻訳集合全体が2020のみとは断定できない。既存WMT14資料とは年・言語対が異なる。

CSDSの論文ニュース例、CrossWOZの論文テレビ例は原データ照合未確認。CrossWOZのHELMホテル対話は公式val12121に一致する。論文の採用元説明と説明例の一致状態を分ける。opinion_miningをCOAEとする根拠はない。

## 採用元台帳

|採用元・状態|CLEVA課題/下位課題|公開原例の状態と制約|
|---|---|---|
|CLUECorpus2020 / confirmed|language_modeling / news, wiki|Official source identified; full corpus not downloaded in this investigation。Public paper says samples from corpus; exact crawl/version and CLEVA-selected documents unknown.|
|CLUEWSC / CLUEWSC2020 / confirmed|coreference_resolution / (default)|Official CLUE ZIP downloaded; paper and HELM examples matched。CLUEWSC2020 public train; does not recover full CLEVA selection.|
|CCPM / confirmed|classical_chinese_understanding / (default)|Official train and test_public JSONL downloaded; both paper and HELM examples matched。Paper example train line18823 answer3; same translation line21287 has different options and answer0. HELM line14 answer0.|
|ChID / confirmed|cultural_knowledge / idiom|Official author repository and original/competition distribution links identified; raw data not fetched。Original ChID and later competition release must be distinguished. CLEVA changes candidates/format; exact source release not determined.|
|OCNLI / confirmed|commonsense_reasoning / textual_entailment|Official CLUE ZIP downloaded; paper premise+hypothesis+entailment matched。Paper record dev line1163 id1162; CLUE public distribution does not establish all CLEVA sampling.|
|Math23K / confirmed|mathematical_reasoning / math_word_problem|Follow-up author implementation distribution downloaded; paper example and two HELM docstring examples matched。Source is 2019 follow-up author distribution, not established byte identity to original 2017 release. Paper id19868 ans720; HELM id14819 ans672 and id15691 ans406. Similar duck questions ids3183/6285/17744 are different.|
|COLD / confirmed|toxicity_detection / (default)|Official three CSV splits downloaded; HELM input matched train CSV line242。Label mapping must be retained; public repository LICENSE Apache-2.0 does not imply unrelated CLEVA corpus is all licensed alike.|
|CDial-Bias / confirmed|bias / dialogue_gender_bias, dialogue_occupation_bias, dialogue_race_bias, dialogue_region_bias|Official README identifies public Hugging Face dataset; raw split not fetched。Current README describes 2.0; CLEVA source version unknown. Research-only usage; other uses need further permission. Four demographic categories are subsets, not automatically four independent base datasets.|
|CHEF / confirmed|fact_checking / (default)|Official preprocessed Pipeline claim_gold.json downloaded; HELM Venus claim matched。This preprocessed list combines claim/evidence strings; it does not by itself preserve claim ID or class label. Original train/dev/test linked via Drive/Tsinghua/Baidu but not fetched. Gold-film phrase appearing inside evidence is not a confirmed full paper claim record.|
|C3 / confirmed|reading_comprehension / (default)|Official CLUE ZIP downloaded; paper dialogue and HELM mixed-text question matched。Paper d-train array941 q0 answer双方缺少交流; HELM m-train array3136 q0. Original C3 d/m splits must be retained.|
|NLPCC 2018 Open Domain QA / confirmed|closed_book_question_answering / generative_question_answering|2018年公式Task 7ガイドラインと中国語KBQAの説明例1件を取得。学習・テスト配布リンクを特定したが、原コーパスとCLEVA選定版は未取得。他2課題とNLPCC2016は区別する。[記録](data-audits/nlpcc2018-source-access.json)|
|cMedQA2 / confirmed|closed_book_question_answering / medical_question_answering|作者配布5 ZIPと全5.8百万候補行を取得・独立照合。元の回答選択とHELM公開A/B形式を区別し、自由生成としない。医学的な正しさのラベルではない。原論文本文も取得でき、既存資料の更新中。非商用研究条件・GPLv3は別々に確認。[本文取得記録](data-audits/cmedqa2-paper-access.json)|
|CSDS / confirmed|summarization / dialogue_summarization|Official README has public example image, schema documentation and Drive/Baidu links; raw archive not fetched。Adoption explicit. Paper MoYan IPO/news example is not independently matched to customer-service dialogue source; keep mismatch visible. HELM docstring dialogue plausible but no raw match established.|
|ADGEN / Shao2019 product advertising data / confirmed|data_to_text_generation / (default)|Original paper footnote resolves author repo; README links original Drive archive data/data.jsonl and 119K pairs。Raw archive not fetched. Do not substitute later ChatGLM ADGEN split without showing ancestry/version. Original paper identifies data-to-text source; ADGEN common alias needs original release naming verification.|
|PKU Paraphrase Bank / confirmed|paraphrase_generation / (default)|Official repository exposes paraphrase_unorder.zip 47,367,792 bytes; README 509,832 pairs; archive not fetched。Exact CLEVA sentence pair unverified. Pair order, deduplication and split unspecified; repository license file must be inspected before publication.|
|CrossWOZ / confirmed|dialogue_generation / task_oriented|Official train/val/test ZIPs downloaded; HELM complete hotel conversation matched val dialogue12121。Paper television/Eyas dialogue has no verified CrossWOZ match; official val example establishes docstring lineage only.|
|WMT 2020 newstest2020 English–Chinese / confirmed|translation / en2zh, zh2en|Official 2020 source and reference files downloaded; all three public CLEVA examples exact source+reference pairs。Paper names past WMT competitions without year. Paper House title=enzh global910 docfoxnews.100085 seg1; HELM enzh global1411 docen.ndtv.com.13041 seg8; HELM zhen global18 docchinanews.com.102568 seg3 (0-based globals). WMT2019 checked no matches. Does not prove all CLEVA translations use only2020; newstestB variant also shares sources and exact variant provenance not fixed.|
|BUSTM (FewCLUE) / confirmed|paraphrase_identification / short_utterance|Official raw files downloaded; paper pair and HELM pair exact with labels。Paper same meaning label1; HELM different meaning label0. Multiple FewCLUE fewshot files repeat records; not unique independent examples.|
|AFQMC (CLUE) / confirmed|paraphrase_identification / financial_question|Official CLUE ZIP downloaded; HELM pair and label0 exact。train.json line7; paper explicitly cites CLUE/FewCLUE families, specific AFQMC identity independently established from pair match.|
|EPRSTMT (FewCLUE) / confirmed|sentiment_analysis / (default)|Official raw files downloaded; paper phone review negative and HELM mall review positive exact。Original text and label exact; same record repeated across fewshot sets; full CLEVA selection unknown.|
|TNEWS (CLUE/FewCLUE) / confirmed|text_classification / news|Official CLUE TNEWS ZIP downloaded; paper education108 and HELM automotive107 exact。Paper train line37403; HELM line50683. Chinese label order in CLEVA is its own multiple-choice order. Common TNEWS corpus membership confirmed; FewCLUE-vs-CLUE sampling ancestry cannot be decided by shared text alone.|
|SPR / CCL2020 Humor Computation / confirmed|text_classification / humor|Paper footnote official repo; raw train/dev ZIP and Chinese labeled CSV fetched; HELM example matched。cn_train.csv line12671 ID12669 Dialogue347 Utterance5 Speaker傅明 Label0. CLEVA renders speaker+说：+sentence. Keep paper alias SPR; no unsupported expansion of acronym.|
|HumanEval (Chinese adaptation) / confirmed|code_synthesis / (default)|Original source public; Chinese CLEVA test prompts not downloaded。Adoption translated; existing HumanEval material covers original source, not equal prompt text/score under CLEVA.|
|TruthfulQA (Chinese adaptation) / confirmed|closed_book_question_answering / truthful_question_answering|Original source public; CLEVA translated collection not obtained。Chinese translated prompts and scoring must be distinguished from English benchmark.|
|HELM-style Dyck language synthesis / confirmed|reasoning_primitive / dyck_language|Official generators public; paper/docstring illustration public; CLEVA instance files unavailable。Paper says synthesize similar to HELM, not demonstrated identical seed/sample.|
|HELM-style synthetic reasoning / confirmed|reasoning_primitive / pattern_induction, pattern_matching, variable_sub|Official HELM generator public; CLEVA generated files unavailable。Paper HELM family citation; all subtask implementation parameters not recovered.|
|HELM Copyright code lineage / confirmed|copyright / code|Original HELM code corpus/public runs separately documented; CLEVA converted collection unavailable。Do not transfer HELM public scores to CLEVA. Paper copyright text is Chinese collected content, distinct from popular English books.|
|BIG-bench source family / confirmed|inductive_reasoning / add, sub, mul|Family adoption explicit; exact original task/subtask record mapping not completed。Paper says collected from BIG-bench; addition offset example is a paper explanation, not newly generated data.|
|BIG-bench arithmetic source family / confirmed|mathematical_calculation / add, sub, mul, significant_figures|Family adoption explicit; task file/version mapping not completed。Paper jointly cites BIG-bench and Inverse Scaling; allocation among add/sub/mul/significant_figures not proven by citation alone.|
|Inverse Scaling source family / confirmed|instruction_following / redefine, pattern_matching_suppression|Paper explicit translated origin; exact source files not fetched。Subtasks redefine and pattern_matching_suppression configured; source task/version confirmation still required.|
|Inverse Scaling deductive/commonsense source family / confirmed|deductive_reasoning / modus_tollens|Translated source citation explicit; original Julia/Beatles record not matched。Same paper source also serves commonsense_reasoning/commonsense_question_answering; this is a source-family row, not a claim of one unique dataset.|
|Patel–Pavlick physical-concept synthesis / confirmed|conceptual_generalization / (default)|ICLR2022本文と著者実装を取得。CLEVAの独自生成器・seed・評価集合は未取得で、原論文や実装を使う再現例と混同しない。[記録](data-audits/cleva-family-origins.json)|
|Opinion target extraction: unidentified base / unavailable|opinion_mining / opinion_target_extraction|Public paper movie example and HELM Xiamen example; no confirmed primary raw corpus。Liu2012/COAE references are background, not provenance proof. Later COIG-PC related mirror Reading-Comprehension has exact Xiamen text/target but cannot establish ancestry or original dataset name.|
|CLEVA pinyin data / unavailable|pinyin_transliteration / zh2pinyin, pinyin2zh|Only public explanation examples/metadata; original evaluation records unavailable。No primary source collection name or transformation script/seed identified.|
|CLEVA intent data / unavailable|intent_understanding / (default)|Only public explanation examples/metadata; original evaluation records unavailable。Exam-like Chinese passage does not establish a named exam dataset.|
|CLEVA subject knowledge collection / unavailable|subject_knowledge / biomedicine, philosophy, geography, computer_science, politics, economics, art, law, math, other_general, chemistry, history, literature, physics|Only public explanation examples/metadata; original evaluation records unavailable。14 subject names are not14 identified base datasets; no proof of MMLU/C-Eval/CMMLU identity.|
|CLEVA Chinese copyright text collection / unavailable|copyright / text|Only public explanation examples/metadata; original evaluation records unavailable。Chinese work collection unspecified; do not substitute HELM English BookCorpus/popular_books; no works/permission list recovered.|

## 出典と制作への引継ぎ

各行の一次URL・論文PDF頁・HELM class/行番号・照合JSONはinventory.jsonに記録した。主な原配布のURL/bytes/SHAはfinal-source-fetch-log.json、fewclue-fetch-log.json、crosswoz-extra-fetch.json、wmt-original-matches.jsonを参照。原文の詳細レコードはローカルevidenceおよびmatch JSONに保持し、配布許諾を自動推定しない。

独立資料の候補は原公開データを取得できるCCPM/C3/CLUEWSC/OCNLI/AFQMC/BUSTM/EPRSTMT/TNEWS/Math23K/COLD/CrossWOZ等。各資料ではCLEVA版未取得を分離し、元データとして紹介する。cMedQA2は非商用研究、CDial-Biasは研究目的に限定する明示条件がある。ADGENは原著者repoと原Driveリンクを確認し、後のChatGLM版との同一性は未確認。

HumanEval/TruthfulQA/Dyck/SyntheticReasoning/CopyrightCodeは既存資料へCLEVAの翻訳・設定差の対応注記を加える案で十分。元データと同一評価条件・同一採点結果という扱いにはしない。MedQAとcMedQA2は別データセット。

opinion_mining、固有名未判明の分野知識/意図/ピンイン/中国語著作権文章は原集合取得や同定まで個別データセット資料の確定を保留する。BIG-bench/Inverse Scalingは出典系列を確認できるが、原ファイル・版・変換単位の確定が次の調査。

原評価集合未取得のため、独立レビュー用プラットフォーム資料では「論文の公開説明例」と明記する方針を支持する。

## cMedQA2の形式に関する追加確認

元データは回答選択である。HELM v0.4.0のmedical_question_answering公開説明例は、医師が患者の問いに答えているかをA/Bで判定する二択で、自由生成とはしない。元の候補ラベルは質問と回答の対応関係であり、医学的な正確さの検証結果ではない。生のCLEVA選定・変換後の評価集合は未取得のまま区別する。cMedQA2の作者配布5 ZIPは制作中に取得し、独立レビューはこれから実施する。

## NLPCC2018の公式ガイドラインを追加確認

2018年当時の公式案内の公開アーカイブから、Task 7の公式ガイドラインPDFを取得した。中国語KBQA・KBQGと英語KBQUの3課題を区別し、正解の形式と採点方法を確認できた。中国語KBQAの公開説明例は1件で、原コーパスの全体やCLEVA選定版を取得したことにはならない。公式テストZIPは現サイト503、照会したアーカイブにはスナップショットがなく、訓練データのBaiduリンクはこの環境の接続経路で403となった。[取得先・SHA・公開例・接続結果](data-audits/nlpcc2018-source-access.json)を記録した。

## 概念の一般化：参照論文の本文を取得

Patel–PavlickのICLR2022論文 *Mapping Language Models to Grounded Conceptual Spaces* は、OpenReview現サイトへの接続が403だったが、公式PDF URLの公開アーカイブから本文を取得できた。原論文と著者実装を照合する材料が増えた一方、CLEVA独自の生成器・乱数seed・中国語の評価集合は未取得のままである。[取得先・SHA・ページ数](data-audits/cleva-family-origins.json)を更新した。

## cMedQA2の原論文本文を追加取得

公式IEEE PDF URLの公開アーカイブから、2018年の原論文11ページを取得できた。現サイトの418等は過去の接続記録として残し、現在の本文取得済みの状態と区別する。公開済み56ページ版の未取得説明・構築条件・ACC@1・主要報告値を担当が見直し、独立レビュー後に更新する。CLEVA変換済み集合は引き続き未取得である。
