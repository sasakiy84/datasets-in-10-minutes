# Changes

New 1.0-focused BenchCAD deck made with the shared master. Includes 13 distinct public code_gen examples (three core, ten appendix), plus genuine public CodeEdit and matched Vision/Code QA records. Sources distinguish 1.0 public data, 2.0 Public and held-out Core, current harness2.1 and published harness2.0 conditions. No2.0 case files or images are redistributed.

Japanese proofreading changed sampler wording, hinge/heat-sink descriptions, union-volume definition, and source-condition attribution. All changes are recorded as concrete before/after pairs in changes.tsv and proofreading.json. Initial fixed-angle GT renders of impeller, heat sink, support plate and cam were re-rendered from the same STEP to expose the relevant features.

No Gemini or external generation API was used. Dataset records were downloaded and inspected; all shape outputs come from executing their reference CadQuery programs and rendering their exported STEP geometry.

Final technical review corrected p31 Gemini non-thinking CodeQA from0.838 to0.836 (Table9), and clarified p41 MIT scope as execution/scoring code. Only these two rendered pages changed; their actual final images were opened and all machine checks were rerun.

V-B-1: reduced only the13 distributed4view input pictures from3.65in to3.525in at the same top position, preserving aspect ratio and original bytes. Each conservative source-font-bbox gap is now at least8pt. All70 native text records and all embedded image bytes are unchanged; only the13 expected page PNGs differ.
