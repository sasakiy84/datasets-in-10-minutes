# SWE-bench Multilingual independent source review (draft stage)

Own downloads: officialHFcard/tree/fixed846e647b9f33c0b51b739d005d13d85493c9af09 testParquet, officialharnessREADME. Full300rows/41repos/uniqueIDs/300pass_and_fail counted.13selected records all15published fields matched exactly to ownParquet; no task reused. These are implementation-language variants, issue texts mainlyEnglish. Officialcard9languages distributionRuby44/Rust43/PHP43/Java43/Go42/C30/JS26/TS17/C++12.

Own content review: read all13 originalissue and Japanese explanation/expectedbehavior. Read relevant goldpatch hunks across13examples, including fmt signedabsolute/prefix, jq lexer.l BINDING (generatedlexer/parser files not claimed individually reviewed), Preact callback+types, CarbonClockInterface, envsignalhandling, GsonEND_DOCUMENT/EOF, LombokcopyJavadoc, Caddyquoted/heredocspace, FPMarchitectureall, Gin100–199white, Rubocopcomparisonprecedence, Redisnegativeindexguards, VueinVPre. Expectedbehaviors accurately reflect reference fixes. No benchmark/model/test execution performed.

JP fixes requested: Carbon names contained doubled actualbackslashes, creator confirmed singlebackslash fix; Preact expectedbehavior should explicitly say callback's secondargument rather than imply hook's secondargument. Japanese is labeled explanation, not claimed literal fulltranslation. Longissue12/13 environment/unansweredfields omitted only per rootapproval and explicit range label; originalfullrecords retained.

Adoption acquisition inherited: /tmp/fable-card.txt; ownread§8.1–8.2pp167–168 supports300/ninelanguages/Fable5.1 89.1,Fable5 86.6,Opus5 89.5,average5trials. Adaptive/maxdefaultspec expressly refersFable5.1/Mythos5.1; do not infer everyoldermodelconditions. FoundationSWEpaper explains taskdesign, not Multilingual initialPython scores.

License: officialHFcardMIT; originalrepositorycode licensing remains separate. Creator fetched repository-specific licensefiles, not yet independentlychecked here. Technical/native/allpagevisual pendingPPTX/PDFdraft.


Independent early-evaluation verification: downloaded metadata.yaml and per_instance_details.json directly from official SWE-bench/experiments raw GitHub for 20260213 mini-v2.0.0a0 Claude4.6Opus/GPT5.2high/DeepSeek3.2. Each has 300 cases and attempts1; independently summed resolved216/200/177 giving72.0/66.7/59.0 percent. These are a separate condition from the Fable system-card five-trial averages. Acquisition records and arithmetic are saved in early-evaluation-source-audit.json and early-evaluation-recalculation.json. No model API or submitted agent execution was used.
