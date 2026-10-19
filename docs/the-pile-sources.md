# The Pile 調査・制作記録

- 制作日: 2026-10-18 JST。日本語、著者sasakiy84、所属なし。
- 構成: 本編25ページ（黙読・流し読み約10分の予定、実測なし）、Appendix31ページ。表17件はいずれもnative editable、実例13件はnative text、ノートなし。

## 一次資料と固定版

1. Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, Shawn Presser, Connor Leahy. *The Pile: An 800GB Dataset of Diverse Text for Language Modeling*. arXiv:2101.00027v1, 2020-12-31. https://arxiv.org/abs/2101.00027
   - paper.pdfはv1。容量・重み・反復数はTable 1、40GB同量比較はTable 3、公開/規約/著者同意はTable 5、本文とAppendix Cの収集方法を照合。
   - 元容量825.18 GiB、反復後1254.20 GiB、平均文書5.91 KiBはいずれも保留集合作成前。書籍などの平均文書長と混合比は別の値。
2. EleutherAI公式再構築リポジトリ。https://github.com/EleutherAI/the-pile
   - READMEの22構成要素とpaperを照合。配布コードのMIT Licenseを本文全体のライセンスとして扱わない。
3. Stella Biderman et al. *Datasheet for the Pile*. arXiv:2201.07311, 2022. https://arxiv.org/abs/2201.07311
4. Percy Liang et al. *Holistic Evaluation of Language Models*. TMLR, 2023. https://arxiv.org/abs/2211.09110
   - HELMコードはv0.4.0タグを取得。ThePileScenarioとlanguage_modeling_adapter、basic_metricsの実装を保存。
5. Stella Biderman et al. *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling*. ICML, 2023. https://arxiv.org/abs/2304.01373
   - 公式リポジトリのREADMEで8サイズ、299,892,736,000トークン、標準/重複除去の学習条件と2025年派生研究の案内を確認。https://github.com/EleutherAI/pythia

## 実例13件

公開ミラーNeelNanda/pile-10kの先頭100行のみ、datasets-serverのrows APIから取得（469,594 bytes）。巨大なPile全量や582MBのparquetは取得していない。ミラー説明は「The first 10K elements of The Pile」。データセットの当時HEADは `127bfedcd5047750df5ccf3a12979a47bfa0bafa`。API応答そのもの、行番号、全文、表示する連続したPython文字位置、原文SHA256と原レコードSHA256を保存。revisionを指定したrows応答ではないため、再現の基準は保存したraw応答とそのSHA256である。

本編row 3 / 11 / 20、追加row 2 / 5 / 10 / 18 / 54 / 55 / 63 / 70 / 74 / 36。合計13の異なる文書、12構成要素。いずれもHELMのテスト入力とは称さず、公開サンプル由来の内容例と明示した。全例は連続抜粋。質問形式の本文にも独立した架空の正解を付けていない。コードのJSON、医学論文の参照記法、原文の綴りを改変せず保持。メールの表示範囲は本文だけで、原記録は完全に保存。

ミラーのカードにはbigscience-bloom-rail-1.0とあるが、上流の22構成要素の権利条件を一律に変更する根拠として使わない。本文の権利は各出所で異なる。資料中の短い引用に出所を対応させ、原文の大量転載を避けた。

## HELMの条件と得点

- Classic latest=v0.4.0（2023-11-17）のrelease JSONを使用。9件の元run suiteは全てv0.3.0。
- コードが受け付ける構成要素は22、公開run_specsでthe_pileに該当するのは6構成要素・168実行。実装の対応数と公開評価数を分離。
- 本文テスト集合を構成要素別に分類。lm_perplexityのgroup0索引を重複除去・昇順で使う。Ubuntu IRC、BookCorpus2、PhilPapersは10分割なし。
- 比較はArXiv/Github/Wikipedia(en)×text-davinci-003/BLOOM/OPT-175Bの9実行。language_modeling、0学習例、1試行、最大1000文書、max_tokens=0。stats.jsonは摂動なし、split=test。ArXiv238文書、他1000文書、prompt_truncated平均は全て0。
- BPBは `-logprob.sum / num_bytes.sum / log(2)`。要求ごとの単純平均とは区別。モデルごとのトークン化、文脈窓と分割を含む実行の値で、文脈長まで統一した比較ではない。
- num_perplexity_tokensのmeanは文書を分割した後の要求単位での平均。文書数と区別してAppendixに掲載。
- 9実行のstatsファイル、URL、取得bytes、SHA256はstats.json/evidenceに保存。2026年の最新モデル順位とは称していない。

## 公式画面と取得上の制約

https://pile.eleuther.ai/ は通常TLS検証と継承プロキシで403になった。公式GitHubへ切り替え、Chromiumで実際のCSSを読み込んだREADME画面を確認。表示に合わせて「公式リポジトリ」と表記。スクリーンショット取得logはscreenshot-log.json。

## 校正・検査

日本語校正スキルを56ページ別に適用。method/review_mode=skill_based_codex、gemini_used=false。実際の変更対はproofreading-changes.json（4件）、全ページの最終文言はpage-proofreading.json/final-text.txt。原文・訳・公開例とHELM入力の区別を照合。

最終PPTXからLibreOffice（専用UserInstallation）でPDFを生成。全56ページを描画。標準XSDを変更せず確認し、マスター由来11件と整数buSzPctの字句形式差を分離。新規schemaエラーなし、参照先・図形ID・ZIP整合・ノートなしを確認。URLはnative runとPDF矩形の双方でURL部分だけに限定。引用の実文字境界で枠余白を調整し、説明を本文の直下へ移動。最終目視記録はvisual-inspection.json。

## 独立レビュー後の修正

p17のLAMBADA正解率の説明を「末尾の単語を当てる正解率」へ修正した。Table 3の注にある「最終トークンだけを評価する」はLAMBADAのperplexityの条件であり、ACCの説明へ移さない。p28/34/35は独立レビューの実画素測定に基づき、引用下余白を4/8/4 pt詰めた。PPTX→PDFを再同期し、監査と4ページの実画像を再確認した。修正対と理由はindependent-review-fixes.json。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/the-pile.json)、[実際の校正対](skill-proofreading/the-pile.md)、[全ページ文言](skill-proofreading/the-pile/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/the-pile/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/the-pile/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
