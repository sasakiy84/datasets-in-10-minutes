# CharXiv 制作・出典記録

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

作成日：2026-10-17（Asia/Tokyo）。本編29ページ、Appendixを含む65ページ。著者sasakiy84。編集可能なPPTXと、その最終版からLibreOfficeで描画したPDF。

## 一次資料と参照範囲

- Wang, Zirui, Mengzhou Xia et al. **CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs**. NeurIPS 2024 Datasets and Benchmarks Track. https://arxiv.org/abs/2406.18521
- 公式コード・JSON：https://github.com/princeton-nlp/CharXiv （取得コミット `7ebe88f78dee387691551f071abcb2b9e1a8025b`）。READMEのv1.0は評価パイプラインのリリースを指す。データの後続バージョンという意味では使っていない。
- 公式配布：https://huggingface.co/datasets/princeton-nlp/CharXiv 。改訂 `f441eb632fc62f6f777830a0f47619e6e86459b0`。`images.zip`と`val.parquet`を取得した。
- Google DeepMind, **Gemini 3 Pro: Model Card**. 2025年11月の比較。https://deepmind.google/models/model-cards/gemini-3-pro/
- Google DeepMind, **Gemini 3 Pro: Evaluation Methodology**. https://deepmind.google/models/evals-methodology/gemini-3-pro/

Gemini 3 Proの公式モデルカードPDFと評価手順書を再取得した。CharXiv Reasoningはvalidationの推論1,000問。81.4 / 69.6 / 68.5 / 69.5%は順にGemini 3 Pro / Gemini 2.5 Pro / Claude Sonnet 4.5 / GPT-5.1。モデルカードの表は画像であるため、描画画像でも確認した。他社分もGoogleが公式APIを使って計算する。2026年10月時点の網羅的な最新順位とはしていない。

## 名称と配布画面

公式名はCharXiv。公式に別の略語展開形は確認できず、論文タイトルを正式名称の展開形として創作していない。表紙はCharXivと日本語の説明を記載。

`https://charxiv.github.io/` は再試行したがプロキシCONNECTが403。代替として公式Hugging FaceのFiles and versions画面を、実ブラウザで取得した。CSS 4枚、Source Sans Pro適用、フォント読み込み完了を確認。データビューアは画像CDN取得に失敗するため、ファイル一覧を使った。アバター等の失敗は撮影記録に残した。

## 件数と実データの照合

- 図：validation 1,000、test 1,323、合計2,323。両分割の全図IDを取得済みZIPの2,323 JPEGと照合。READMEには2,333 imagesという表記もあるが、原著・配布JSON・実ZIPはいずれも2,323。
- 1図に記述4問と推論1問。全体9,292記述問と2,323推論問、計11,615問。testの正解は非公開。
- 8分野の図数：計算機科学292、経済学287、電気・システム科学291、数学286、物理学294、定量生物学293、定量金融289、統計学291。
- サブプロット数：1個896、2〜4個876、5個以上551。複数グラフの図は61.4%。原著の896に添えた割合28.6%は件数と整合しないため、配布メタデータから集計した。
- 推論の回答種別：図中文字1,044、一般文字229、図中数値512、一般数値538。質問の由来：人の新規作成1,378、GPT案を修正497、GPT案を採用448。全2,323件の公式JSONを集計。
- ZIP実取得141,454,217 bytes（134.9 MiB）、JPEG展開後172,827,923 bytes。容量の細かい違いは主題にしない。
- 採点は公式`reasoning_utils.py` / `descriptive_utils.py` / `get_stats.py`を確認。GPT-4oが最終回答を抽出して0/1採点し、問題単位で平均する。記述と推論は別集計。

## 実例：本編3件、追加10件

すべて公開validationの独立した図・推論問題。各件を図と設問の2ページに分けた。設問英語は全文、正解は配布値を掲載し、日本語訳と図を読む説明を付けた。記述4問の表は本編ID 917を再利用して課題の違いを説明するもので、追加件数には数えない。

|配置|図ID|参照正解|図の原著|
|---|---|---|---|
|本編1|917|1 - 2|[An Evaluation of novel method of Ill-Posed Problem for the Black-Scholes  Equation solution](https://arxiv.org/abs/2011.09136)|
|本編2|1209|4|[Report on the ECFA Early-Career Researchers Debate on the 2020 European  Strategy Update for Particle Physics](https://arxiv.org/abs/2002.02837)|
|本編3|1520|Negatively|[ProGen: Language Modeling for Protein Generation](https://arxiv.org/abs/2004.03497)|
|追加1|8|JeVois (408MHz)|[Performance Evaluation of Low-Cost Machine Vision Cameras for  Image-Based Grasp Verification](https://arxiv.org/abs/2003.10167)|
|追加2|321|4|[What can be learned from satisfaction assessments?](https://arxiv.org/abs/2010.13340)|
|追加3|332|3rd|[Towards robust and speculation-reduction real estate pricing models  based on a data-driven strategy](https://arxiv.org/abs/2012.09115)|
|追加4|620|3000 to 4000|[Dynamic Resource Optimization for Decentralized Estimation in Energy  Harvesting IoT Networks](https://arxiv.org/abs/2008.01498)|
|追加5|903|Minimum-Risk (Exact)|[Outcome-Driven Dynamic Refugee Assignment with Allocation Balancing](https://arxiv.org/abs/2007.03069)|
|追加6|1505|G-proteins|[Classification of particle trajectories in living cells: machine  learning versus statistical testing hypothesis for fractional anomalous  diffusion](https://arxiv.org/abs/2005.06239)|
|追加7|1818|Train|[Asset Price Forecasting using Recurrent Neural Networks](https://arxiv.org/abs/2010.06417)|
|追加8|2124|0.5|[Handling missing data in a neural network approach for the  identification of charged particles in a multilayer detector](https://arxiv.org/abs/2004.05374)|
|追加9|2145|kw_avg_avg|[Breiman's "Two Cultures" Revisited and Reconciled](https://arxiv.org/abs/2005.13596)|
|追加10|14|94|[LiveChess2FEN: a Framework for Classifying Chess Pieces based on CNNs](https://arxiv.org/abs/2012.06858)|

13件の英語設問・正解がGitHub JSONとHugging Face Parquetの両方で一致した。両配布の画像は縦横寸法が同一で、JPEG再符号化による小差（選定図すべてで各RGBチャネルの平均絶対差は255段階中1未満）がある。掲載図はZIPのJPEGを変形・切り抜きせず使用した。

読み込みコードの`ds[392]`は図ID 917に対応し、`reasoning_q`と`reasoning_a`を公式Parquetから実読み込みして確認。Hugging Face datasetsライブラリ自体は制作環境に未導入のため、配布コード片のload_dataset呼び出しそのものは実行していない。

候補ID 0は配布正解Joint-CNNと図中の精度低下の大小が整合しないように見えたため採用しなかった。ID 903の説明は、図の目盛り付近に終端があることを述べ、棒の正確な値を画像から断定しない。ID 2145はarXivのcitation_authorメタタグが姓名を分離していたので、画面の著者欄からSubhadeep (DEEP) MukhopadhyayとKaijun Wangを確認して直した。

## ライセンスと出典表示

公式READMEは、独自データ（図を除く）をCC BY-SA 4.0、コードをApache 2.0とし、図の権利は各原著者に帰属すると明記する。掲載した設問・回答と、その日本語訳はCC BY-SA 4.0。日本語訳を加えたことを各設問ページに表示し、同ライセンスで提供する。ライセンス本文は[charxiv-CC-BY-SA-4.0.txt](licenses/charxiv-CC-BY-SA-4.0.txt)。https://creativecommons.org/licenses/by-sa/4.0/

論文の図は原著からの引用として、図表読解の説明に必要な範囲で掲載。各図ページに著者・年・原著タイトル・arXiv URLを記載。図にCC BY-SAが適用されるとは表示していない。評価コードは転載していない。

## 描画と最終確認

全65ページを一覧で確認し、13図・13設問・全10表・全2グラフ・コード・参考文献3ページ・表紙・配布画面を1440×811で個別確認。最後の変更後は該当ページを再描画して確認し、他のページはピクセル一致を照合した。

- 見出しは1行、表セルに文字の欠けや境界はみ出しなし。本文は短い行末を許容。表は上下1.2 pt、見出し境界0.6 pt、縦罫線なし。
- 本文・出典の最小間隔12.97 pt、参考文献の項目間25.91 pt以上。コードの上下余白10.88 / 11.19 pt。URLだけをリンク。
- PPTXの全表示段落をPDFの文字列と照合し欠落なし。ページ外テキストなし。発表者ノートなし。ZIP整合と内部参照を確認。
- PPTX XML 82部品をスキーマ検証。共通マスター由来のbuSzPct表記に既知の120件の字句差があり、値の範囲は妥当。その他のスキーマエラーなし。
- 制作・調査・検査用の一時スクリプトはscratchに置き、リポジトリとSKILLには追加していない。

ギャラリーは20資料としてビルド。全サムネイルの読み込み、CharXiv / charxiv / 全角検索、画像・質問応答・2024年のフィルタ、年順、カードのPDFリンク、PPTX取得、構造化データ20件、390 px幅での横はみ出しなしをブラウザで確認。PPTX・PDFはscratchの確認済みファイル、リポジトリ、公開ビルドの3か所でSHA-256一致。

|成果物|bytes|SHA-256|
|---|---:|---|
|PDF|1,778,330|`445554097fe51819f6a47ae53b2507d797c7b51c706488f030892d4d49f013ac`|
|PPTX|781,821|`00accced61f32e94b7f9f8d448dc8cf418a6e05f38109f71643ae377ef2810ae`|
