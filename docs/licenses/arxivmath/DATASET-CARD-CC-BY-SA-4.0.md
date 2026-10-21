---
dataset_info:
  features:
  - name: problem_idx
    dtype: int64
  - name: answer
    dtype: string
  - name: problem
    dtype: string
  - name: source
    dtype: string
  - name: title
    dtype: string
  - name: authors
    dtype: string
  splits:
  - name: train
    num_bytes: 87806
    num_examples: 53
  download_size: 239973
  dataset_size: 87806
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
license: cc-by-sa-4.0
language:
- en
pretty_name: ArXivMath September 2026
size_categories:
- n<1K
task_categories:
- question-answering
tags:
- math
- reasoning
- benchmark
- arxiv
---

# ArXivMath September 2026

## Homepage and repository

- **Homepage:** [MathArena](https://matharena.ai/)
- **Repository:** [MathArena evaluation code](https://github.com/eth-sri/matharena)

## Dataset summary

This dataset contains 53 self-contained research-level mathematics questions derived from arXiv papers submitted in September 2026. It is the September release of ArXivMath, used for the MathArena leaderboard. Each question asks for a final mathematical answer supported by its source paper.

## Data fields

- `problem_idx` (`int64`): Problem index within this benchmark, starting at 1.
- `answer` (`string`): Gold final answer, usually expressed in LaTeX.
- `problem` (`string`): Solver-facing mathematical question, usually stored as LaTeX source.
- `source` (`string`): arXiv identifier of the source paper.
- `title` (`string`): Title of the source arXiv paper.
- `authors` (`string`): Authors of the source arXiv paper.

## Dataset split and loading

The dataset contains a single `train` split with **53 questions**. The split name follows the MathArena distribution convention; these questions are intended for evaluation.

```python
from datasets import load_dataset

dataset = load_dataset("MathArena/arxivmath-0926", split="train")
print(dataset[0]["problem"])
```


## Evaluation

Models receive the problem statement and are asked to produce a final answer. An LLM judge checks mathematical equivalence to the reference answer, rather than requiring identical strings. Scores are binary at the individual-answer level. The September harness evaluation allows coding tools without internet access and uses a 12-hour time limit and a $100 model-cost budget per attempt, with up to five minutes for a final answer after reaching the cost budget, within the original time limit.

For evaluation, supply only the `problem` field and the appropriate solver instructions. Keep reference answers or true statements and source-paper metadata out of the solver prompt.

## Licensing information

This dataset is licensed under [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/), following the other MathArena ArXiv benchmarks. Source papers are credited in the `source`, `title`, and `authors` fields.

## Citation information

```bibtex
@article{dekoninck2026matharena,
      title={Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs},
      author={Jasper Dekoninck and Nikola Jovanović and Tim Gehrunger and Kári Rögnvaldsson and Ivo Petrov and Chenhao Sun and Martin Vechev},
      year={2026},
      eprint={2605.00674},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.00674},
}
```
