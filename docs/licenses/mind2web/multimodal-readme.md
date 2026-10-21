---
license: openrail
language:
- en
tags:
- web agent
- multimodal
dataset_info:
  features:
  - name: action_uid
    dtype: string
  - name: raw_html
    dtype: string
  - name: cleaned_html
    dtype: string
  - name: operation
    dtype: string
  - name: pos_candidates
    sequence: string
  - name: neg_candidates
    sequence: string
  - name: website
    dtype: string
  - name: domain
    dtype: string
  - name: subdomain
    dtype: string
  - name: annotation_id
    dtype: string
  - name: confirmed_task
    dtype: string
  - name: screenshot
    dtype: image
  - name: action_reprs
    sequence: string
  - name: target_action_index
    dtype: string
  - name: target_action_reprs
    dtype: string
  splits:
  - name: test_website
    num_bytes: 1589513606.713
    num_examples: 1019
  - name: test_task
    num_bytes: 2004628575.972
    num_examples: 1339
  - name: test_domain
    num_bytes: 5128899015.440001
    num_examples: 4060
  - name: train
    num_bytes: 13439470200.25
    num_examples: 7775
  download_size: 4014045168
  dataset_size: 22162511398.375
---

## Dataset Description

- **Homepage:** https://osu-nlp-group.github.io/SeeAct/
- **Repository:** https://github.com/OSU-NLP-Group/SeeAct
- **Paper:** https://arxiv.org/abs/2401.01614
- **Point of Contact:** [Boyuan Zheng](mailto:zheng.2372@osu.edu)

### Dataset Summary

Multimodal-Mind2Web is the multimodal version of [Mind2Web](https://osu-nlp-group.github.io/Mind2Web/), a dataset for developing and evaluating generalist agents 
for the web that can follow language instructions to complete complex tasks on any website. In this dataset, we align each HTML document in the dataset with 
its corresponding webpage screenshot image from the Mind2Web raw dump. This multimodal version addresses the inconvenience of loading images from the ~300GB Mind2Web Raw Dump.

## Dataset Structure

### Data Splits
- train: 7775 actions from 1009 tasks.
- test_task: 1339 actions from 177 tasks. Tasks from the same website are seen during training.
- test_website: 1019 actions from 142 tasks. Websites are not seen during training.
- test_domain: 4060 actions from 694 tasks. Entire domains are not seen during training.

The **_train_** set may include some screenshot images not properly rendered caused by rendering issues during Mind2Web annotation. The three **_test splits (test_task, test_website, test_domain)_** have undergone human verification to confirm element visibility and correct rendering for action prediction.


### Data Fields
Each line in the dataset is an action consisting of screenshot image, HTML text and other fields required for action prediction, for the convenience of inference. 
- "annotation_id" (str): unique id for each task
- "website" (str): website name
- "domain" (str): website domain
- "subdomain" (str): website subdomain
- "confirmed_task" (str): task description
- **"screenshot" (str): path to the webpage screenshot image corresponding to the HTML.**
- "action_uid" (str): unique id for each action (step)
- "raw_html" (str): raw html of the page before the action is performed
- "cleaned_html" (str): cleaned html of the page before the action is performed
- "operation" (dict): operation to perform
  - "op" (str): operation type, one of CLICK, TYPE, SELECT
  - "original_op" (str): original operation type, contain additional HOVER and ENTER that are mapped to CLICK, not used
  - "value" (str): optional value for the operation, e.g., text to type, option to select
- "pos_candidates" (list[dict]): ground truth elements. Here we only include positive elements that exist in "cleaned_html" after our preprocessing, so "pos_candidates" might be empty. The original labeled element can always be found in the "raw_html".
  - "tag" (str): tag of the element
  - "is_original_target" (bool): whether the element is the original target labeled by the annotator
  - "is_top_level_target" (bool): whether the element is a top level target find by our algorithm. please see the paper for more details.
  - "backend_node_id" (str): unique id for the element
  - "attributes" (str): serialized attributes of the element, use `json.loads` to convert back to dict
- "neg_candidates" (list[dict]): other candidate elements in the page after preprocessing, has similar structure as "pos_candidates"
- "action_reprs" (list[str]): human readable string representation of the action sequence
- "target_action_index" (str): the index of the target action in the action sequence
- "target_action_reprs" (str): human readable string representation of the target action



### Disclaimer
This dataset was collected and released solely for research purposes, with the goal of making the web more accessible via language technologies. The authors are strongly against any potential harmful use of the data or technology to any party.

### Citation Information
```
@article{zheng2024seeact,
  title={GPT-4V(ision) is a Generalist Web Agent, if Grounded},
  author={Boyuan Zheng and Boyu Gou and Jihyung Kil and Huan Sun and Yu Su},
  booktitle={Forty-first International Conference on Machine Learning},
  year={2024},
  url={https://openreview.net/forum?id=piecKJ2DlB},
}

@inproceedings{deng2023mindweb,
  title={Mind2Web: Towards a Generalist Agent for the Web},
  author={Xiang Deng and Yu Gu and Boyuan Zheng and Shijie Chen and Samuel Stevens and Boshi Wang and Huan Sun and Yu Su},
  booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
  year={2023},
  url={https://openreview.net/forum?id=kiYqbO3wqw}
}
```