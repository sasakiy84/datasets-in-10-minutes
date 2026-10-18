# Natural Questions：出典と制作記録

2026-10-18作成。本編36ページ、Appendix31ページ、計67ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能なPPTXと最終版から出力したPDF。共通マスターを使用し、発表者ノートなし。

## 一次資料・配布物

|資料|URL|
|---|---|
|Kwiatkowski et al. (2019), Natural Questions: A Benchmark for Question Answering Research. TACL 7:453–466.|https://aclanthology.org/Q19-1026/|
|Google Research, Natural Questions. dev / Hugging Face公開配布。|https://huggingface.co/datasets/google-research-datasets/natural_questions|
|Google Research, Natural Questions. 公式サイト。2026-10-18参照。|https://ai.google.com/research/NaturalQuestions|
|Google Research, Natural Questions. 注釈仕様と評価コード。|https://github.com/google-research-datasets/natural-questions|
|Liang et al. (2023), Holistic Evaluation of Language Models. TMLR.|https://arxiv.org/abs/2211.09110|
|HELM Classic v0.4.0, NaturalQuestions (closed-book). 2023-11-17の固定版。|https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/natural_qa_closedbook|
|HELM Classic v0.4.0, NaturalQuestions (open-book). 2023-11-17の固定版。|https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/natural_qa_openbook_longans|
|Stanford CRFM, HELM NaturalQA scenario. 2026-10-18確認。|https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/natural_qa_scenario.py|

公式リポジトリ改訂 `fb26a3073b1fe636c97302890a27b491d6530130`。公開Hugging Face配布は `e8103d566bef4154c2c12b17c6095ec5275840cc` のdev全7,830例、7ファイル、合計1,337,126,358 bytes（約1.34 GB）を取得。旧GCSの5つのdev URLは匿名アクセスで403だった。公式サイトのトップ部分をブラウザで撮影し、CSS・フォント・画像の読み込みを確認した。

[検証データ](data-audits/naturalquestions.json)には、取得URL・bytes・SHA-256、全件集計、13実例のID・出所Parquetと0始まりの行位置・長い回答のバイト範囲・全5注釈・原文・訳を保存した。各実例の質問・注釈・HTMLハッシュ・選択フィールドのレコードハッシュを、固定配布の元行と再照合した。タグを除き、空白を整形してlong answer全文を表示。NULLの例だけ記事冒頭を抜粋し、記事全文を対象とした5人の注釈であることを説明した。

## 課題・評価・統計

本編3件と追加10件は、異なる13記事。単一スパン、複数スパン、NULL、yes／noを含む。4例では原文と訳を同じページ、他の9例は原文を1枚に保って訳を次ページに置いた。参照回答は21ptのえんじ色。複数スパンは1人の注釈の集合、yes／noは非NULLの最多注釈を示し、その注釈に対応するlong answerを確認した。

2019年のNQは、5注釈中2人以上の非NULL判定と範囲の一致からP/R/F1を算出する。HELMは元のdevのうち、短い回答のスパンが少なくとも1注釈ある4,289例を対象候補にし、ファイル内で交互に提示用・評価用に分け、評価側1,000件を使う。回答なしとyes／no専用フィールドは使わず、複数スパンは別々の参照回答として生成回答を採点する。両者のF1を同じ指標として比較しない。

HELM Classic v0.4.0の質問のみ／正解long answerありの6実行を、v0.3.0スイートのstatsで照合。OPT・text-davinci-003は3試行平均、Llama 2は1試行。最大5例という設定に加え、実提示例数とprompt_truncatedも確認。公開scenario_stateの摂動なし・第1試行の1,000例は、取得devの質問・参照回答と全件一致した。2026-10-18の公開コードでも2条件の実装を確認した。

全7,830例で、長い回答あり4,608件、短い回答あり3,456件（うちyes／no120件）を集計。回答ありは5人中2人以上の非NULLとして数えた。人数別分布とquestion.tokensの長さも全件集計。学習307,373件・テスト7,842件は論文値。READMEの学習307,372件との差は記録し、原因は推測していない。

## 日本語校正と最終検査

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)をページごとに適用。[実際の修正対](skill-proofreading/naturalquestions.md)、[全ページ文言](skill-proofreading/naturalquestions/pages.jsonl)、[検査とレイアウト記録](skill-proofreading/naturalquestions/review.json)を保存。

全67ページを描画して一覧を確認し、引用・訳・表・グラフ・公式画面・参考文献を個別に拡大。引用枠の可視字形をPNG実画素で測定し、上下各6.67〜7.33ptに調整。回答位置も追従させた。最終変更ページは再出力して確認。文字欠落、枠のはみ出し、出典との重なり0件。URLだけのリンク57件、ネイティブ表8件、グラフ1件。標準XSDの新規エラー0件。マスター由来11件と整数buSzPctの字句形式差は分離し、XSDは変更していない。PowerPointの手動開封は未実施、LibreOffice変換と構造検証を行った。

## Wikipediaの帰属と翻訳

公式リポジトリはApache 2.0。取得した13記事のHTML内のライセンス表示も照合した。Wikipedia本文の抜粋と日本語訳には[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)を適用する。元記事の版付きURLは配布メタデータ由来。タグ・空白を整え、日本語訳を加えた。質問と回答範囲はNQの公開注釈から取得した。

- 実例1：Wikipedia contributors, [Current members of the United States Senate](https://en.wikipedia.org//w/index.php?title=Current_members_of_the_United_States_Senate&amp;oldid=822209735)。タグ除去・空白整形・日本語訳。
- 実例2：Wikipedia contributors, [Commonwealth (U.S. state)](https://en.wikipedia.org//w/index.php?title=Commonwealth_(U.S._state)&amp;oldid=819412022)。タグ除去・空白整形・日本語訳。
- 実例3：Wikipedia contributors, [Industrial robot](https://en.wikipedia.org//w/index.php?title=Industrial_robot&amp;oldid=833623628)。タグ除去・空白整形・日本語訳。
- 実例4：Wikipedia contributors, [Deposition (phase transition)](https://en.wikipedia.org//w/index.php?title=Deposition_(phase_transition)&amp;oldid=832599453)。タグ除去・空白整形・日本語訳。
- 実例5：Wikipedia contributors, [That '70s Show](https://en.wikipedia.org//w/index.php?title=That_%2770s_Show&amp;oldid=838069162)。タグ除去・空白整形・日本語訳。
- 実例6：Wikipedia contributors, [Germ theory of disease](https://en.wikipedia.org//w/index.php?title=Germ_theory_of_disease&amp;oldid=838265678)。タグ除去・空白整形・日本語訳。
- 実例7：Wikipedia contributors, [Library Literature and Information Science](https://en.wikipedia.org//w/index.php?title=Library_Literature_and_Information_Science&amp;oldid=815292448)。タグ除去・空白整形・日本語訳。
- 実例8：Wikipedia contributors, [Chyme](https://en.wikipedia.org//w/index.php?title=Chyme&amp;oldid=802488569)。タグ除去・空白整形・日本語訳。
- 実例9：Wikipedia contributors, [Draft Day](https://en.wikipedia.org//w/index.php?title=Draft_Day&amp;oldid=825688984)。タグ除去・空白整形・日本語訳。
- 実例10：Wikipedia contributors, [Tornadoes in the United States](https://en.wikipedia.org//w/index.php?title=Tornadoes_in_the_United_States&amp;oldid=816870602)。タグ除去・空白整形・日本語訳。
- 実例11：Wikipedia contributors, [List of countries with left-hand traffic](https://en.wikipedia.org//w/index.php?title=List_of_countries_with_left-hand_traffic&amp;oldid=835288332)。タグ除去・空白整形・日本語訳。
- 実例12：Wikipedia contributors, [Dust Bowl](https://en.wikipedia.org//w/index.php?title=Dust_Bowl&amp;oldid=801829264)。タグ除去・空白整形・日本語訳。
- 実例13：Wikipedia contributors, [Pericardium](https://en.wikipedia.org//w/index.php?title=Pericardium&amp;oldid=821015178)。タグ除去・空白整形・日本語訳。

## 独立レビュー後の最終版

作成者と別のサブエージェントが元の固定配布レコードと数値条件を独立照合。実例の原文・質問・参照回答を保持しつつ、幅と余白を調整して原文・訳の併記を追加した。全引用枠の可視字形上下余白は各6.67〜7.33pt。現在は本編36、全67ページ。改訂前の校正対・ページ番号は履歴として保存した。[独立レビュー](skill-proofreading/naturalquestions/independent-review/review.json)。

最大出力長の旧記載100トークンは誤りで、全6実行のadapter_spec.max_tokens=300に訂正した。得点は変更していない。
