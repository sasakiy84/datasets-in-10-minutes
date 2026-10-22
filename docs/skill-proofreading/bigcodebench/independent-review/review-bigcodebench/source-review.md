# BigCodeBench: independent source review

Reviewer: /root/review_bigcodebench. Method: skill_based_codex; Gemini/external generation APIs not used. All checks below are static document/data/code inspection; no model evaluation, benchmark solution execution, or test execution.

## Independently acquired primary sources

- Official repository README and Apache 2.0 LICENSE: bigcode-project/bigcodebench. Pinned implementation tree 09dd993f46c3fbf3a799465bb96d524edcb0b199, including data loader, evaluator, sanitizer and pass@k estimator.
- Official HF dataset bigcode/bigcodebench, revision b74c0d0bf70d2c0bc459be537895cca163007f1a, v0.1.4 parquet. Independently downloaded, 1,140 unique tasks. Declared libraries independently recomputed139; test-function AST count6,434, mean5.64386, parse errors0.
- Official HF Hard, revision298d2cc7b96612e15e47313c3603ee124cee0c1f, v0.1.4 parquet: 148 unique tasks; all IDs/instruct prompts match the Full subset.
- Official paper, ICLR2025 proceedings, 55pages. Main1–10 content, table/metrics, AppendixF Hard construction, execution/prompt section reviewed. Full title confirmed: “BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions”. Dataset first release2024; conference2025.
- Official website and results.json/results-hard.json independently downloaded. 202 entries in each board, model date fields through2025-04-14. These are observed official board contents at review time, not proof of comprehensive latest2026 model results. Individual date fields can be incorrect (GPT-4-0613 field lists2024); model release years require independent identity evidence.
- OpenAI, “Training models to self-report misbehavior”,2026-03-21, alignment.openai.com/self-incrimination/. The primary article explicitly includes BigCodeBench among7 general capability benchmarks for comparing baseline and posttraining changes, with GPT-4.1/GPT-4.1mini/Gemini2.0Flash training. Does not establish Astra/Fable adoption. This is independent acquisition/content verification, source discovery inherited root.

## Meaningful distinctions

Complete/Instruct are two prompt forms for the same tasks; Full/Hard are task collections. Combining the two prompt forms does not create2,280 distinct problems. Models produce code, not a single textual gold string. Public canonical code is one implementation; behavior is evaluated by tests. Calibrated scoring adds setup code/imports and global definitions supplied in code_prompt; it does not repair arbitrary functional errors. Main initial evaluation uses zero-shot greedy pass@1; alternative sampling conditions must remain separate.

Construction: ODEX API-use seeds, GPT-4-assisted generation/refactoring under expert control, 4,718 preliminary samples→1,223 refactored pairs→1,140 curated tasks.20 annotator authors over1year,13 onrefactoring,7 additional cross-checking. Human97% is32/33 tasks by11 annotators, not a measured human population rate or all1,140. The7 library-domain percentages overlap by task and are not a partition summing100%.

Hard selection uses StackOverflow query similarity and then complexity/model-success filters. Paper Figure8 solve-rate>50 vs text<50, and426tokens vs table426characters are internal inconsistencies. Do not fill overview slides with unverified numerical thresholds. The official release/blog and readable purpose of smaller, more user-oriented subset suffice, with details in records.

## Independent genuine example reading

Main IDs25,140,32; Appendix19,52,56,60,110,145,148,408,536,26. All13 full Instruct prompts, canonical implementations, and complete public test classes (72test methods) independently read. Complete25 also fully read for presentation comparison. Structured own fixed records: source-selected13.json and selected-tests-read.json.

-25 JSON→zlib→base64: tests reverse the transformation and compare dictionaries; no requirement that every valid compressed/base64 output byte string be identical.
-140 DataFrame StandardScaler: selected numeric columns, invalid dataframe/cols/nonexistent/empty data raise ValueError. StandardScaler uses population standard deviation; test pandas std tolerance does not imply sample convention as normalization definition.
-32 HTTP response/first tag: literal TestPage/firstparagraph/None cases are checked. Public .string implementation also returnsNone on some nested/malformed/empty tags.
-19 ZIP: only directory-level files, emptyNone, missing directoryFileNotFoundError, preservingfilecontents; six methods.
-52 stopword-filtered lowercased word frequencies, expected dictionary counts not arbitrary Series tie ordering.
-56 pattern lines→DataFrame, scores explicitly converted to integers.
-60 CSVwithoutindex and JSON, None return, integerJSONkeys become strings.
-110 daily turnover Axes, seeded expected10values, title/ylabel/error behavior. Do not claim a single exact graph image is the gold.
-145 IPv4Network iteration: reference for/30 includes network/broadcast (.0–.3), whereas one public test mocks iteration to two addresses and checks two writerow calls. Label demonstrated expected behavior according to actual chosen source.
-148 original saysEncrypt, but LabelEncoder is categorical integer encoding. Code/tests map apple/banana/cherry to0/1/2. Preserve original English, translate intended operation accurately and record reasoning; no cryptographic encryption claim.
-408 SQLite→pandas query output, fixed5names plus100faker rows, SQLfilter/order behavior.
-536 SQLite table→CSV, absolute returned path, file contents/overwrite and errors.
-26 Fernet encryption then outerbase64: stochastic ciphertext, return/exception checks, not a fixedciphertextgold. The example32-character key is public synthetic task data, no credential values inspected.

## Pending

Creator Japanese13 and final native/PDF content, package/schema/render/table/glyph/URL audits, and individual full-page visual review are pending until an immutable candidate pair is provided. This source review is not deck approval.


## Independent candidate-1 and candidate-2 review

Candidate-1: all 59 pages individually actually viewed at 1600 px. All 59 native pages read in the initial draft, then every changed paragraph and table in the immutable candidate reread. Thirteen original Instruct prompts match independently acquired fixed source records exactly after Markdown fences become native code formatting. Found footer collisions (10/12/35), expected-behavior collisions (37/39/47), split table header (24/25), and genuine glyph ink extending beyond native frames. All findings sent as a batch; original questions retained. Candidate-2: own rawpixel bridge finds 47 identical pages, and the 12 changed pages were individually actually viewed again. Semantic changes on 10/12/28/35 reread and source checked. Only the cover lowercase g native-frame issue remained; creator is fixing it in candidate-3. PDF text-metric bboxes continue to overestimate glyph extents; real FontTools outline bounds resolve these metric-only reports. No outside-page glyphs or unknown glyphs. Current public score conditions and Full/Hard versus Complete/Instruct axes are correct. Reference pair conservative metric gaps exceed 32 pt on all three pages. No runtime model/benchmark evaluation or external generation API was used.
