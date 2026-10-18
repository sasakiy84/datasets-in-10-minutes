# マスターに沿った日英スライド制作

研究発表、成果物紹介、授業などの編集可能なPPTXとPDFを作るためのスキルです。情報設計、一次資料の確認、組版、描画・検証を扱います。

## スキル

|スキル|役割|
|---|---|
|[master-guided-slides](.agents/skills/master-guided-slides/SKILL.md)|汎用の情報設計・表現・組版・検証・納品|
|[dataset-introduction-slides](.agents/skills/dataset-introduction-slides/SKILL.md)|データセットの目的・実例・作成方法・統計・評価・利用の調査と内容設計。汎用スキルと併用|

共通マスターは[SlideMaster.pptx](.agents/skills/master-guided-slides/SlideMaster.pptx)です。

## 使い方

利用先プロジェクトの`.agents/skills/`へ、必要なフォルダを以下の相対位置でコピーします。汎用制作だけなら`master-guided-slides/`、データセット紹介には両方を使います。

```text
.agents/skills/
├── master-guided-slides/
│   ├── SKILL.md
│   └── SlideMaster.pptx
└── dataset-introduction-slides/
    └── SKILL.md
```

材料、目的、聴衆、言語、時間と読み方、作成者・所属を指定してください。

> $master-guided-slides を使い、添付論文を日本語の学会発表スライドにしてください。本編15分の口頭発表。完全版のPPTXとPDFを提示してください。

> $dataset-introduction-slides を使い、指定したデータセットを紹介してください。日本語、本編10分の黙読とAppendix。完全版のPPTXとPDFを提示してください。

## 制作環境

PPTXの編集・描画にはPowerPointやLibreOfficeなどを使います。コードで制作する場合は`python-pptx`や`lxml`、PDF確認にはPyMuPDFなどを利用できます。共有スクリプトや別添設定ファイルは必須ではありません。

フォントは日本語にNoto Sans CJK JP、英数字にNoto Sans、コードにLiberation Monoなどの等幅フォントを使います。フォント本体は同梱していません。

[HELM Classicの対象と制作進捗](docs/helm-classic-coverage.md)を記録しています。CLEVA系列は後回しにし、プラットフォームと公開実例のある個別データセットを分けて制作します。

## Webギャラリー

CSV管理のスライドギャラリーをGitHub Pages向けにビルドできます。

```sh
python -m pip install -r site/requirements.txt
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

資料情報は[site/datasets.csv](site/datasets.csv)、サイト設定は[site/config.json](site/config.json)で管理します。[公開・更新・カスタムドメインの手順](docs/github-pages.md)を参照してください。

## 制作例：datasets in 10 minutes

このシリーズでは、速い読者が本編を約10分で黙読・流し読みする想定です。Appendixは時間に含めず、閲覧時間は未実測です。原稿や口頭の補足がなくても理解できる説明を資料内に置きます。

- 表紙左上：`datasets in 10 minutes (YYYY-MM-DD)`。新作はユーザーのタイムゾーンでの作成日、既存資料の修正は指定された日付を維持。
- 作成者：`sasakiy84`。所属欄なし。
- 成果物：完全版のPPTXと同じ改訂のPDF。発表者ノート・本編だけの版は標準では作成しない。
- 保存先：`slides/datasets-in-10-minutes-${dataset_name}.pptx`と同名の`.pdf`。

|データセット|PPTX|PDF|
|---|---|---|
|ImageNet|[PPTX](slides/datasets-in-10-minutes-imagenet.pptx)|[PDF](slides/datasets-in-10-minutes-imagenet.pdf)|
|SNLI|[PPTX](slides/datasets-in-10-minutes-snli.pptx)|[PDF](slides/datasets-in-10-minutes-snli.pdf)|
|SQuAD|[PPTX](slides/datasets-in-10-minutes-squad.pptx)|[PDF](slides/datasets-in-10-minutes-squad.pdf)|
|UCF101|[PPTX](slides/datasets-in-10-minutes-ucf101.pptx)|[PDF](slides/datasets-in-10-minutes-ucf101.pdf)|
|COCO|[PPTX](slides/datasets-in-10-minutes-coco.pptx)|[PDF](slides/datasets-in-10-minutes-coco.pdf)|
|FineWeb|[PPTX](slides/datasets-in-10-minutes-fineweb.pptx)|[PDF](slides/datasets-in-10-minutes-fineweb.pdf)|
|GPQA|[PPTX](slides/datasets-in-10-minutes-gpqa.pptx)|[PDF](slides/datasets-in-10-minutes-gpqa.pdf)|
|HLE|[PPTX](slides/datasets-in-10-minutes-hle.pptx)|[PDF](slides/datasets-in-10-minutes-hle.pdf)|
|Terminal-Bench|[PPTX](slides/datasets-in-10-minutes-terminal-bench.pptx)|[PDF](slides/datasets-in-10-minutes-terminal-bench.pdf)|
|ScreenSpot-Pro|[PPTX](slides/datasets-in-10-minutes-screenspot-pro.pptx)|[PDF](slides/datasets-in-10-minutes-screenspot-pro.pdf)|
|τ²-bench|[PPTX](slides/datasets-in-10-minutes-tau2-bench.pptx)|[PDF](slides/datasets-in-10-minutes-tau2-bench.pdf)|
|MMMU-Pro|[PPTX](slides/datasets-in-10-minutes-mmmu-pro.pptx)|[PDF](slides/datasets-in-10-minutes-mmmu-pro.pdf)|
|ARC-AGI-2|[PPTX](slides/datasets-in-10-minutes-arc-agi-2.pptx)|[PDF](slides/datasets-in-10-minutes-arc-agi-2.pdf)|
|SWE-bench Verified|[PPTX](slides/datasets-in-10-minutes-swe-bench-verified.pptx)|[PDF](slides/datasets-in-10-minutes-swe-bench-verified.pdf)|
|SciCode|[PPTX](slides/datasets-in-10-minutes-scicode.pptx)|[PDF](slides/datasets-in-10-minutes-scicode.pdf)|
|MCP Atlas|[PPTX](slides/datasets-in-10-minutes-mcp-atlas.pptx)|[PDF](slides/datasets-in-10-minutes-mcp-atlas.pdf)|
|SWE-bench Pro|[PPTX](slides/datasets-in-10-minutes-swe-bench-pro.pptx)|[PDF](slides/datasets-in-10-minutes-swe-bench-pro.pdf)|
|SimpleQA Verified|[PPTX](slides/datasets-in-10-minutes-simpleqa-verified.pptx)|[PDF](slides/datasets-in-10-minutes-simpleqa-verified.pdf)|
|MMMLU|[PPTX](slides/datasets-in-10-minutes-mmmlu.pptx)|[PDF](slides/datasets-in-10-minutes-mmmlu.pdf)|
|CharXiv|[PPTX](slides/datasets-in-10-minutes-charxiv.pptx)|[PDF](slides/datasets-in-10-minutes-charxiv.pdf)|
|Global PIQA|[PPTX](slides/datasets-in-10-minutes-global-piqa.pptx)|[PDF](slides/datasets-in-10-minutes-global-piqa.pdf)|
|MRCR v2|[PPTX](slides/datasets-in-10-minutes-mrcr-v2.pptx)|[PDF](slides/datasets-in-10-minutes-mrcr-v2.pdf)|
|FACTS Grounding|[PPTX](slides/datasets-in-10-minutes-facts-grounding.pptx)|[PDF](slides/datasets-in-10-minutes-facts-grounding.pdf)|
|OSWorld-Verified|[PPTX](slides/datasets-in-10-minutes-osworld-verified.pptx)|[PDF](slides/datasets-in-10-minutes-osworld-verified.pdf)|
|OmniDocBench|[PPTX](slides/datasets-in-10-minutes-omnidocbench.pptx)|[PDF](slides/datasets-in-10-minutes-omnidocbench.pdf)|
|GSM8K|[PPTX](slides/datasets-in-10-minutes-gsm8k.pptx)|[PDF](slides/datasets-in-10-minutes-gsm8k.pdf)|
|HumanEval|[PPTX](slides/datasets-in-10-minutes-humaneval.pptx)|[PDF](slides/datasets-in-10-minutes-humaneval.pdf)|
|VQA v2|[PPTX](slides/datasets-in-10-minutes-vqa-v2.pptx)|[PDF](slides/datasets-in-10-minutes-vqa-v2.pdf)|
|BoolQ|[PPTX](slides/datasets-in-10-minutes-boolq.pptx)|[PDF](slides/datasets-in-10-minutes-boolq.pdf)|
|HellaSwag|[PPTX](slides/datasets-in-10-minutes-hellaswag.pptx)|[PDF](slides/datasets-in-10-minutes-hellaswag.pdf)|
|TruthfulQA|[PPTX](slides/datasets-in-10-minutes-truthfulqa.pptx)|[PDF](slides/datasets-in-10-minutes-truthfulqa.pdf)|
|IMDb|[PPTX](slides/datasets-in-10-minutes-imdb.pptx)|[PDF](slides/datasets-in-10-minutes-imdb.pdf)|
|XSum|[PPTX](slides/datasets-in-10-minutes-xsum.pptx)|[PDF](slides/datasets-in-10-minutes-xsum.pdf)|
|OpenBookQA|[PPTX](slides/datasets-in-10-minutes-openbookqa.pptx)|[PDF](slides/datasets-in-10-minutes-openbookqa.pdf)|
|MMLU|[PPTX](slides/datasets-in-10-minutes-mmlu.pptx)|[PDF](slides/datasets-in-10-minutes-mmlu.pdf)|
|bAbI|[PPTX](slides/datasets-in-10-minutes-babi.pptx)|[PDF](slides/datasets-in-10-minutes-babi.pdf)|
|BLiMP|[PPTX](slides/datasets-in-10-minutes-blimp.pptx)|[PDF](slides/datasets-in-10-minutes-blimp.pdf)|
|APPS|[PPTX](slides/datasets-in-10-minutes-apps.pptx)|[PDF](slides/datasets-in-10-minutes-apps.pdf)|
|BBQ|[PPTX](slides/datasets-in-10-minutes-bbq.pptx)|[PDF](slides/datasets-in-10-minutes-bbq.pdf)|
|BOLD|[PPTX](slides/datasets-in-10-minutes-bold.pptx)|[PDF](slides/datasets-in-10-minutes-bold.pdf)|
|RAFT|[PPTX](slides/datasets-in-10-minutes-raft.pptx)|[PDF](slides/datasets-in-10-minutes-raft.pdf)|

[ユーザー指示の記録](docs/user-instructions.md)
