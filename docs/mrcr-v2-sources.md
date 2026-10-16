# MRCR v2 制作・出典記録

2026-10-17（Asia/Tokyo）。本編27ページ、全51ページ。日本語の黙読・流し読み約10分を想定、未実測。著者sasakiy84。

## 一次資料と対象

- Google DeepMind, **MRCR v2**, eval_hub（取得コミット `d5637d5`）。https://github.com/google-deepmind/eval_hub/tree/master/eval_hub/mrcr_v2
- Vodrahalli, Kiran et al., **Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries**, 2024, arXiv v2。第一著者Kiran Vodrahalli、最終著者Kate Olszewska。https://arxiv.org/abs/2409.12640v2 。この論文はMRCRを説明・評価するが、課題の初出と断定していない。
- Google DeepMind, **Gemini 3.1 Pro: Model Card**, 2026年2月。https://deepmind.google/models/model-cards/gemini-3-1-pro/
- Google DeepMind, **Gemini 3.1 Pro: Evaluation Methodology**。8-needleの128Kまでの累積評価と1Mの点評価、再現先を明記。https://deepmind.google/models/evals-methodology/gemini-3-1-pro/
- 別配布のOpenAI MRCR。https://huggingface.co/datasets/openai/mrcr 。Googleの手順書が指定するv2とは混同せず、実例には使っていない。

表紙の正式名は公式READMEのMulti-round Coreference Resolution。公開モジュールv2、CSVファイル名v2p1を区別し、公開されていないp1変更点を推測していない。ギャラリーの2026年はv2公開モジュールの年で、先行課題の2024年とは分ける。

## データ・実例・採点

公式download.shが指定するGoogle Cloud Storageから、2・4・8-needleの `mrcr_v2p1_{n}needle_in_(4096,8192)_dynamic_fewshot_text_style_fast.csv` を取得。https://storage.googleapis.com/mrcr_v2/ 。掲載した各例の出典に、URLとCSVの0始まりの行番号を付した。

取得範囲は246問（82・84・80行）。最終指示を除く会話を重複排除すると、各6・8・6会話。context_lenの平均は6,357.61・6,488.00・6,643.30トークン。最短・最長はそれぞれ4,511–8,175、4,823–8,146、4,986–7,995。全ベンチマークの件数とはしていない。

本編3問、追加10問の計13問。最終指示は配布原文の全文（User/Assistantの境界記号を除く）、日本語は指定条件の要約、参照応答は冒頭の連続抜粋。同じ会話から異なる問いを作れるため、13会話とは数えない。条件に一致する依頼を全て抽出し、needle数・指定順・参照応答全文が会話中の対象と一致することを全13問で確認。選択した形式・題材・文体の組は重複しない。

|ページ|needle数|CSV行（0始まり）|指定順|
|---:|---:|---:|---:|
|9|2|0|2|
|11|4|0|1|
|14|8|0|4|
|31|2|2|2|
|32|2|4|1|
|33|2|6|1|
|34|4|4|2|
|35|4|8|2|
|36|4|12|1|
|37|8|8|5|
|38|8|16|4|
|39|8|24|2|
|40|8|32|1|

採点コードrun_evaluation.pyのmrcr_v2_metricをASTから取り出して実行し、完全一致1、指定文字列なし0、cat/cut=2/3を確認した。公開実装は指定文字列の最後の出現をrfindで探す。文字列が応答冒頭にあることを強制する実装とは説明していない。モデルAPIは呼び出していない。

モデル比較は公式モデルカードの8-needle、128Kまでの平均類似度。Gemini 3.1 Pro High 84.9%、Claude Sonnet 4.6 Max 84.9%、Claude Opus 4.6 Max 84.0%、GPT-5.2 High 83.8%、Gemini 3 Pro High 77.0%。1Mの点評価ではGemini 3.1 ProとGemini 3 Proはいずれも26.3%。画像化されたカードの表を目視して照合。

現在の生成コードの形式・題材・文体の設定を説明するが、現行コードに指定されたモデルが配布CSVの実際の生成モデルだったとは断定していない。

## 利用条件・画面・検証

公開モジュールの実装はApache 2.0。[本文](licenses/mrcr-v2-Apache-2.0.txt)。外部ストレージのCSVに別個の明示ライセンスは確認できていないため、CSV全体がApache 2.0とは扱わない。設問と応答は、出典を示した解説目的の短い引用として掲載。

GitHub画面はCSSリソースの取得が失敗したため採用せず、原著のarXiv公開ページを実ブラウザで撮影。適用CSS7枚・Lucida Grandeを確認し、実画面を目視した。補助的な数式・引用機能の取得失敗は画面本文に影響しないことを確認。

全51ページの一覧、13引用、全12表、コード、参考文献2ページ、表紙・導入画面を拡大して確認。PPTX段落とPDFの全文照合、ページ外文字・タイトル折り返し、セル内収容、本文と出典・表注・参考文献の間隔を確認した。引用背景はPDF上の文字の上下に各8ptを確保。booktabsの上下1.2pt・見出し境界0.6pt、縦罫線なし。ZIP・内部参照・ノートなし・XMLスキーマを確認。共通マスターのbuSzPctの既知の字句差以外に予期しないエラーなし。

制作・調査・検査のスクリプトはscratchのみ。

|成果物|bytes|SHA-256|
|---|---:|---|
|PDF|997,453|`2e1436bdab2230ac81ca570dd549e9505d56d28de1396e9c116a8e7bacd8bb6c`|
|PPTX|304,194|`5fe10d72b607364eabaf7e960aaa85da897ca29a761e3d7ca65f69f5e6731448`|

最終チェック：本文と出典の最小間隔12.95pt、文献項目間25.91pt以上、コード上下10.88/11.19pt、XML66部品、既知のbuSzPct字句差121件以外のエラー0。22件のギャラリーで全表紙、大小・全角のタイトル検索、言語・質問応答・2026年の併用、年順、カードPDFリンク、PPTX取得、390pxの横はみ出しなしを確認。確認済みscratch・リポジトリ・公開ビルドの各ファイルはSHA-256一致。
