# Independent source review — Global-MMLU

Reviewer: /root/review_global_mmlu. Scope completed so far: independently retrieved paper PDF, official HF API/card, 7 test parquet files and English dev; independently checked HF Git HEAD. Creator files were used only to identify selected examples, then compared against reviewer downloads. No Gemini/API/key reading. Repo/Git files unchanged.

## Primary evidence
- https://arxiv.org/pdf/2412.03304 : downloaded PDF identifies v2, 19 February 2025. Paper §2.1: 200 compensated professional/community annotators; random 50 questions in each of 57 subjects = 2,850 English questions. Cultural/geographic/dialect knowledge annotated; English dialect category is about original English references.
- §3.1–3.2: Google Translate first used for 41 target languages; four paid post-edit languages Arabic/French/Hindi/Spanish, community work in 11 additional languages; OpenAI MMMLU contributes remaining 10 professionally translated languages after overlap. Thus OpenAI MMMLU and Global-MMLU are different datasets with a documented reuse relation.
- §3.2: full 42-language test 589,764 language-specific entries; annotated 2,850 original question identities, CS792, CA2058. Labels extended to corresponding translations. Lite15 languages ×400 samples =6,000.
- https://huggingface.co/datasets/CohereForAI/Global-MMLU : independent card/API download, API and git ls-remote HEAD/main both 0e619dbeb34206cd48705a1a0ea7fb21cae09993. Independent parquet recount in source-audit.json: 7 tests each14,042, English dev285, 57 subjects; labels -=11,192/CA2,058/CS792; 50 annotated questions per subject. Other 35 language counts are card metadata, not independently downloaded.
- Dedicated Cohere /research/global-mmlu and GitHub CohereForAI/Global-MMLU both returned404. HF is official linked distribution; this is not evidence that no other website exists.
- Inherited /tmp/fable-card.txt (not independently downloaded): own reading lines6489–6519 verifies Fable5.1 uses Global MMLU across42 languages and reports94.0, Fable5 93.6, Opus5 92.5, Sonnet5 89.0; all adaptive thinking/max effort, one trial, no tools/custom system prompts. Source acquisition inherited; passage review owned.

## Selected examples
13 distinct sample_id identities, 3 main +10 appendix; 7 languages. Every displayed question, all4options, answer and cultural label compared exactly against reviewer-downloaded fixed-revision original and English-reference records. All13 are annotated; no inferred CS/CA classes. This is not13 translated versions of one identity. Individual matches recorded in source-audit.json.

Japanese independently read against source-language question/choices and English reference; no claim of external native-speaker review. Corrections sent to creator: example6 Spanish B el Ministerio de Defensa = 国防省 (English reference secretary of defense differs); example12 Hindi D की अवहेलना करने = 無視する (English reference override differs). Preserve official source wording, translate displayed language. Other11 translations preserve meaning. Short glosses numen, mashiach/メシア, Guru Hargobind, maxim, Arkansas toothpick provide needed cultural/vocabulary context. Arkansas toothpick answer explicitly marked distribution answer; no assertion that Bowie and Arkansas toothpick are identical in modern knife taxonomy.

## Manuscript independent review (build.py initial source)
All initial build.py prose read. Verified paper initial evaluation 14 models/9 families/5-shot; open option log-probability vs closed generated-letter extraction. Verified group averages CA/CS small51.3/54.8, medium59.1/61.7, large61.6/66.8 against PDF p19. Independently recalculated 6-field CS/CA table from English records: STEM23/927; Humanities442/208; SocialSciences208/392; Medical19/331; Business36/164; Other64/36. Majority threshold is half-or-more, minimum3 annotators. Anatomy unanimity/Moral Scenarios disagreement verified PDF§2.1.
Requested creator remove unverified Global expansion from formal title, remove production statement about seven downloaded languages, and replace appendix example9 generic language/culture warning with specific Inca historical context. Creator confirmed translation fixes and prose changes in progress. Card language-resource classification differs from paper§4.1; no slide uses that unneeded breakdown.

Not yet completed: final manuscript/Japanese/native-structure/render/visual review. No final PPTX/PDF hash yet.


## Final fixed pair review
Final native text bridge confirms no old question/option/translation/answer string removed; only cultural glosses for Guru, Arkansas toothpick and Kant maxim added on38/41/43. These are consistent with the examples. Spanish B 国防省 and Hindi D 無視する corrections verified in final native source. Formal MMLU expansion is identified separately from Global-MMLU. Production details removed from user-facing prose. Summary directly states42languages/14,042questions/2,850cultural labels.3 detached explanation tables removed. Fable sources present on28/30, title/header orphans resolved.

Final head1–30 is pixel-identical to previously directly reviewed f7eb/4169 pair at144dpi, with all30pages compared independently. Intermediate head changed13pages were directly reopened after initial c5c1/5c6a visual1–30. PNG artifacts and all version hashes retained. p11 Latin A/B/C/D PDF glyphs use NotoSans-Regular fallback and actual3x crop visibly includes every prefix. Green-band text on9/11 present in PDF glyphs and actual PNG. Root independently observed an image-display discrepancy; no source-file glyph omission found.


## Official project and Lite3.0 update (new review delta)
Root discovered https://cohere.com/research/globalmmlu (without hyphen), distinct from earlier404 /research/global-mmlu. Reviewer independently downloaded official-project.html, extracted TryGlobalMMLU/ TryGlobalMMLULite links to officialHF CohereLabs datasets. Update p2 to actual official project screenshot. Project prose contains stale/inconsistent6,000count alongside23languages; its conference/date text was not used as evidence.

Independently downloaded Lite card/API and git ls-remote main. All agree36c2fd756f19ccf13a9a96c8e53ccecc02192b8b. Card3.0 May2026; initial1.0 Dec2024=15languages; current3.0=23languages. Card explicitly says paper scores correspond to original15. Independently downloaded all23 currenttestParquets and recounted each400 withCS200/CA200, total9,200. Audit in lite-v3-source-audit.json. FullGlobal-MMLU42language base and thirteenexamples unchanged. Updates are limited to official project screenshot and Litehistory/current counts/source references.
