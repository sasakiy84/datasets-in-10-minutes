# AA-Omniscience：出典・利用条件・確認範囲

AA-OmniscienceはArtificial Analysisによる、内部知識と回答保留を評価するベンチマークである。公式評価の6,000問と、Apache License 2.0で公開された600問を区別した。紹介例は公開版から13問を選んだ。非公開問題の取得・読解や、モデル・採点器の実行は行っていない。

## 主な一次資料

1. Declan Jackson, William Keating, George Cameron, Micah Hill-Smith (2025). **AA-Omniscience: Evaluating Cross-Domain Knowledge Reliability in Large Language Models**. arXiv:2511.13029. https://arxiv.org/abs/2511.13029
   - 問題の構築、6分野・42トピック、6,000問、四つの判定、指数・正解率・幻覚率、公開版の抽出を確認した。読んだ範囲は関連する導入・方法・結果の説明、限界・結論とAppendix A–Bであり、全参考文献や全図中の全モデル数値を読了したという意味ではない。
   - 2025年11月の初期評価は36モデル、最高はClaude 4.1 Opusの指数4.8、正解率36%。全問を1回ずつ評価した。
2. Artificial Analysis Team (2025). **Public Dataset for AA-Omniscience: Evaluating Cross-Domain Knowledge Reliability in Large Language Models**. Hugging Face. https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public
   - 固定リビジョン `e4883edbb9f5ccf2b2a8fdc6fb65e01a58e99849` のCSVを取得した。600行、6領域各100行。全600行は取得・機械集計したが、個別に原文と答えを読んだ確認範囲は選定13問と除外候補である。全600問を人手で検証したとは扱わない。
   - 公開CSVのFinanceラベルと、論文・現行サイトの上位分野Businessの表記を区別した。スライドの6分野一覧は論文の区分に基づく。
   - 公開600問は10%の標本であり、公開時点の総合成績が全体と近くなるよう抽出された。細かな分野別比較では標本数が小さいという制約がある。
3. Artificial Analysis (n.d., 2026-10-25参照). **AA-Omniscience: Knowledge and Hallucination Benchmark**. https://artificialanalysis.ai/evaluations/omniscience
   - CSSとフォントを読み込んだ実画面を取得・実見した。代表値の説明文でOpus 5.5（Max, Default Fallback）46、GPT-6 Astra（High）44、Fable 5.1（Max, Default Fallback）43を確認した。サイトの代表値の転載であり、動的な全582モデルの表を再構成した結果とは主張しない。
4. Artificial Analysis (n.d., 2026-10-25参照). **Artificial Analysis Intelligence Benchmarking Methodology**. https://artificialanalysis.ai/methodology/intelligence-benchmarking
   - 現行のAA-Omniscience節、総合表と変更履歴の関連箇所を読んだ。対象6,000問・1回、現在の採点器GPT-5.6 Luna（medium）を確認。初期のGemini 2.5 Flash Preview、途中のGemini 3 Flash Previewとの変更を記録した。
   - 現在の総合Intelligence IndexではAccuracy 10%、Non-Hallucination 5%に分けて統合する。AA-Omniscience単独の指数をそのまま15%加えると説明していない。

## 採点の定義

正解数c、部分的な回答p、誤答i、回答保留aとすると、指数は `100(c−i)/(c+p+i+a)`。正解率は `c/(c+p+i+a)`、幻覚率は `i/(p+i+a)`。現在の公式ページと2025年の論文の分母は一致する。部分的な回答と保留はいずれも指数への寄与0。採点モデルの呼出しは実行していない。

## 掲載例と根拠の確認

本編はID575（PEP 371）、63（Scholes）、334（Loveless v. Diehl）。追加は580、588、275、272、119、190、401、405、15、364。英語の原問13件は省略せず、各1頁に収録した。11件は訳・正解・解説も同頁、2件は解説を別頁にした。日本語、短い解説と正解の意味を全13件読んだ。出典の取得結果と実読方法を`source-fact-verification.json`に個別記録した。

- PythonのPEP 371、zoneinfo文書、Requests FAQ、国連文書、Natureの書誌・要旨、OpenStaxの根と茎、adidasの2019年連結貸借対照表、Justia掲載の州最高裁判決は取得した該当本文・表・書誌を読んだ。
- AAP公式受賞者一覧は通常のHTTP取得が403だったが、Webツールが返した公式本文のDistinguished Scientist Award欄で2019 Yvonne Kapilaを読んだ。
- ScholesのNobel公式Facts本文とAPIは403。Web検索が返したNobel公式のAssar Lindbeckによる賞の歴史とMerton Factsの関連本文で、1997年のMerton・Scholes受賞とBlack–Scholesへの帰属を確認した。Factsページを直接取得・全文読了したとは記録しない。
- Hoffmann論文の著者・掲載年・題名は出版社が登録したCrossrefメタデータと出版社の検索索引で確認した。出版社の本文が403であり、論文全体の内容を読んだとは主張しない。
- ダイオウイカ論文の年は出版社登録のCrossrefメタデータ、撮影日はPubMed公式索引の図説明で確認した。PMCの認証画面を論文本文の取得と数えていない。
- 除外候補ID178のDomagkの受賞年は配布goldが1938だが、Nobel公式の記載は1939。答えを黙って書き換える代わりに、この候補を選定から外した。全データの誤り率に一般化していない。

## 配布条件と制作

公開データカードはApache License 2.0を指定する。実際のライセンス本文と帰属・変更の説明（`ATTRIBUTION-AA-Omniscience.md`）を保持した。引用した英語の設問と参照回答を保持し、日本語訳、解説とスライドの構成を加えた。

Geminiや他の外部生成APIを使用せず、ローカルのスライド制作・日本語校正スキルを使った。作成担当が初稿全56頁と再構成版全45頁を1600pxの個別画像で実見した。全13例を1頁ずつ確認し、原文の過分割と短い解説だけの改頁を整理した。全頁のnative/PDFテキスト、URLの範囲、構造、表、実字形・枠外を検査する。最終版は独立担当による別の確認を受ける。

本編は600秒の流し読みを予定したが、時間は未実測。発表者ノートなし。PPTXからLibreOfficeでPDFを出力し、Microsoft PowerPointでの確認は行っていない。取得した大きな一次資料・初稿・画像・一時コードは作業ディレクトリに保存し、再配布スライド用の検証記録と区別した。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-aa-omniscience.pptx)・[PDF](../slides/datasets-in-10-minutes-aa-omniscience.pdf)。本編27頁、総45頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/aa-omniscience.json)・[校正の修正対](skill-proofreading/aa-omniscience.md)・[全ページ文言](skill-proofreading/aa-omniscience/pages.jsonl)・[最終検証票](skill-proofreading/aa-omniscience/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-AA-Omniscience-Apache-2.0.txt](licenses/aa-omniscience/LICENSE-AA-Omniscience-Apache-2.0.txt)、[ATTRIBUTION-AA-Omniscience.md](licenses/aa-omniscience/ATTRIBUTION-AA-Omniscience.md)。
