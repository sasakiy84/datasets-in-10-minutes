# CNN / DailyMail — 出典と検証範囲

2026-10-18取得。HELM Classic v0.4.0（2023-11-17）に掲載された非匿名版の要約課題を紹介する。最新モデルの順位表ではない。

## 一次資料

- Abigail See, Peter J. Liu, Christopher D. Manning. 2017. **Get To The Point: Summarization with Pointer-Generator Networks.** ACL, pp.1073–1083. https://aclanthology.org/P17-1099/ — §4の分割・平均長、§5の400 token条件、Table 1の非匿名版結果を使用。匿名版の行は同じ比較表へ混ぜていない。
- Ramesh Nallapati, Bowen Zhou, Cicero dos Santos, Çağlar Gülçehre, Bing Xiang. 2016. **Abstractive Text Summarization using Sequence-to-sequence RNNs and Beyond.** CoNLL, pp.280–290. https://aclanthology.org/K16-1028/ — 読解用ニュースから複数文要約課題への展開。
- Mike Lewis et al. 2020. **BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension.** ACL, pp.7871–7880. https://aclanthology.org/2020.acl-main.703/ — CNN/DailyMail testの44.16/21.28/40.90。HELMとの条件差を保持。
- Karl Moritz Hermann et al. 2015. **Teaching Machines to Read and Comprehend.** NeurIPS. https://arxiv.org/abs/1506.03340 — 読解課題の起源。元の配布ページ https://cs.nyu.edu/~kcho/DMQA/ もHTMLを取得した。
- Abigail See. **CNN / Daily Mail non-anonymized dataset.** https://github.com/abisee/cnn-dailymail — 公式前処理コード・URLリスト・MIT License。READMEとLICENSE.mdの実体を保存。冒頭画面には非匿名版の公式リポジトリを使用し、ChromiumでCSS 33個・主要内容を描画、asset failureなしを確認した。独立した非匿名版の専用サイトはREADMEに示されていない。読解用DMQAページと非匿名版リポジトリを区別した。
- Percy Liang et al. 2023. **Holistic Evaluation of Language Models.** TMLR. https://arxiv.org/abs/2211.09110

## 固定した実データ

配布: https://huggingface.co/datasets/abisee/cnn_dailymail 、config **3.0.0**、revision **96df5e686bee6baa90b8bee7c28b81fa3fa6223d**。test Parquetを全件取得した（30,000,471 bytes、11,490件）。取得URLとbytes/SHA-256はfetchログとevidence-inventory.jsonに保存。データカードの平均781/56 tokenは2017年の報告値として扱い、testの空白語数の実測683.51/55.01と混同しない。

本編3例（test rows 9,10,3）と追加10例（8,7,32,46,55,10003,10006,10016,10019,10028）を使用。追加例にはCNN 5記事とDaily Mail 5記事が含まれる。各例は**記事冒頭の連続した1文を抜粋**し、**参照要約は全文**を表示。原文の抜粋を訳のために分割していない。訳が同居できる実例1・6は2列、残る例はEN/JPの別ページ。ハイライトの意味上の文はすべて残し、画面では改行を空白へ整形した。

examples.jsonは各記事の全文、参照要約、抜粋の文字範囲、訳、配布ID、test行位置、元記事URL、SHA-256を含む。IDは公式all_test.txtの取得元URLのSHA-1と一致。example-audit.jsonで13件を固定Parquetへ再照合した。

## HELMの正確な実行条件

固定版のgroup: https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/summarization_cnndm 。公開run suiteはv0.3.0。標準CPU runのOPT-175B、text-davinci-003、anthropic/stanford-online-all-v4-s3を使用。各runは3試行、各試行1,000記事だが、内訳はvalid 534 / test 466。本文ではtest466記事のROUGEを3試行平均で掲載し、validはAppendixで別表にした。全test11,490記事の集計値とHELMの466記事の評価を区別。

scenario: dataset_name=cnn-dm, sampling_min_length=50, sampling_max_length=150, doc_max_length=512。改行除去と空白正規化後、記事の先頭512語を使う。参照要約は切り詰めない。trainの提示候補は記事長50–150語。実提示は3モデルとも5組、prompt_truncated=0。

adapter: max_train_instances=5, max_eval_instances=1000, num_train_trials=3, num_outputs=1, temperature=0.3, max_tokens=128, stop_sequences=["###"]。指示: “Summarize the above article in 3 sentences.”。v0.3.0のscenario/metrics/basic_metricsコードを保存した。rouge_score.RougeScorer(use_stemmer=True)で各記事のF1を求める設定。CPU版はモデルを使うfaithfulness/BERTScoreの計算を行わない。

実際の生成はtext-davinci-003のtest id16576 / trial0。記事114語、HF test row586 / id fd6bc93561e36fea7ca9a4785f2f4fe2b16828abに、記事全体の空白整形後完全一致で対応付けた。記事全文（ENと訳）、参照要約全文、生成全文を保持。入力は記事以外に5提示例と指示を含み、元のrequest全体もhelm-generation.jsonに保存。候補生成数は1。rouge-score 0.1.2とHELMと同じstemmer条件で再計算し、R1=36.62/R2=8.70/RL=28.17（F1×100）。集合平均ではなく1例の値。

## 権利と帰属

Hugging FaceデータカードにはApache 2.0が表示される一方、本文のLicense欄はversion1.0.0に言及する。非匿名版の前処理コードはMIT（Copyright 2018 Abi See）。これらを、ニュース本文や編集者ハイライトの著作権の譲渡と解釈していない。原記事・編集者ハイライトはCNN / Daily Mailと各著者に帰属する。引用箇所にデータ名、出所、IDを表示し、元URLをexamples.jsonへ保存。日本語訳は本資料制作者による。

## 検査と残る事項

最終PPTXから専用LibreOffice profileでPDF化。全ページoverviewと69ページを個別拡大して確認した。引用・コード・表・グラフ・文献・公式画面を含むページは、最終行、上下余白、ラベル、回答とfooterの間隔を確認。実例5でラベルと回答の重なりを検出し、引用枠の調整時に両方を同時移動するよう修正して再確認。69ページの最終文言と日本語のページ別校正記録、実際の修正対を保存（method/review_mode=skill_based_codex、gemini_used=false）。

パッケージは標準XSDを変更せず検証。マスターに既存の11件と、整数buSzPctの字句形式差を分離した新規エラーは0。7 native tables、1 native chart、本文と引用・コードはnative text。notesSlideなし。全内部参照・shape ID一意性・ZIP整合性を検査。PDFの文字境界と全native段落・表セルを照合し、layout問題0。URLのnative runとPDFの実文字範囲を検査。

原典を取得できなかったもの: 最初のmetricsパス（metricsディレクトリ欠落）とLICENSE（拡張子なし）は404となり、正しいmetrics/summarization_metrics.pyとLICENSE.mdから取得し直した。HF API rowsも調査時に取得したが、最終照合は固定Parquetを使用。確認できなかった最新モデル成績や、未公表の作業者人数は補っていない。独立レビューは別担当者へ依頼する。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/cnn-dailymail.json)、[実際の校正対](skill-proofreading/cnn-dailymail.md)、[全ページ文言](skill-proofreading/cnn-dailymail/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/cnn-dailymail/review.json)。
