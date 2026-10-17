# SimpleQA Verified：出典と制作記録

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

2026-10-17制作。日本語の本編30枚、Appendix23枚、全53枚。シリーズの約10分の黙読・流し読みを想定。編集可能なPPTXと、同じ最終PPTXから出力したPDFを収録する。閲覧時間は未実測。

## 一次資料と採用バージョン

|資料|確認内容|
|---|---|
|[SimpleQA Verified: A Reliable Factuality Benchmark to Measure Parametric Knowledge](https://arxiv.org/abs/2509.07968v2)|Lukas Haas, Gal Yona, Giovanni D’Antonio, Sasha Goldshtein, Dipanjan Das。Google DeepMind / Google Research。初回2025-09-09、論文v2は2026-03-10。作成・検証・採点・2025年のモデル評価。|
|[SimpleQA Verified / Hugging Face](https://huggingface.co/datasets/google/simpleqa-verified)|改訂 `0dc97e0d28d8233463e005cdc4475cc2a13ba2dc`。公式CSV、README、ライセンス、公開履歴。設定simpleqa_verified、分割eval、1,000問。|
|[Measuring Short-Form Factuality in Large Language Models](https://arxiv.org/abs/2411.04368)|Jason Wei, Nguyen Karina et al., OpenAI, 2024。元のSimpleQAの作成・正答／誤答／未回答とF1。|
|[SimpleQA reference implementation](https://github.com/openai/simple-evals/blob/652c89d/simpleqa_eval.py)|改訂 `652c89d0ca9df547706735883097e9537d40dc47`。論文が引き継いだ指標の計算を確認。Verifiedの改訂された採点プロンプトはVerified論文付録を使う。|
|[Gemini 3 Pro: Model Card](https://deepmind.google/models/model-cards/gemini-3-pro/)|2025年11月公開・2026年5月更新。2026-10-17に公式PDFを取得し、画像として埋め込まれた評価表も描画して確認した。|
|[Gemini 3 Pro: Evaluation Methodology](https://deepmind.google/models/evals-methodology/gemini-3-pro/)|2025年11月の公式比較。SimpleQA Verifiedの掲載値は公式Kaggleリーダーボードから採用したと記載。実際の取得物は3ページのPDF。|

## 内容・指標・モデル結果

検索や外部資料を使わず、モデル内部の知識で短い事実質問へ答える評価として説明。入力は質問文、出力は回答。参照正解とURLは採点・検証用。正答／誤答／未回答を判定し、全問での正答率と、正答＋誤答の中での正答率を求め、調和平均をF1とする。

説明用100問を正答40・誤答10・未回答50とし、全問正答率40%、回答した中での正答率80%、F1約53.3と示した。元の公式SimpleQA実装の集計ASTをそのまま実行し、この値、全件未回答のF1=0、全件正答のF1=1を確認した。モデルを呼び出した実測値として掲載していない。

Verified論文の1,000問・ツールなし・標準API条件の結果は、Gemini 2.5 Pro（正答率55.3%、回答内55.9%、F1 55.6）、GPT-5（50.9、53.8、52.3）、o3（51.6、52.0、51.9）、Claude Opus 4（19.2、54.1、28.3）。判定器gpt-4.1-2025-04-14を明示した。回答率の比較はOpus 4の35.5%とGemini 2.5 Proの98.9%。

Googleの公式モデルカードのSimpleQA Verified行は、Gemini 3 Pro 72.1%、Gemini 2.5 Pro 54.5%、Claude Sonnet 4.5 29.3%、GPT-5.1 34.9%。論文の結果とはページと出典を分け、「掲載スコア」として転記した。Googleの評価手順書はKaggleを引用しているが、Kaggle自体は接続制限で再取得できず、追加の実行設定や指標名を推測していない。公式表にない2026年後半のモデル成績を作っていない。

## 作成方法と全体像

元の4,326問から、出典URL重複の整理で3,095、意味の重複で2,871、TF-IDFと人手確認で2,664、出典サイトの利用制御に関する選択で1,855、答えの種類と話題の調整で1,218、非数値の出典照合で1,117、数値の照合で1,073、最後の難度調整で1,000問という工程を論文で確認。意味の類似の閾値0.77、単語の類似0.4超の人手確認も照合した。

数値の許容範囲は問題別の参照正解に従う。小さい個数などの正確な一致、中程度の数量の約±1%、大きな集計値の約±5%という論文の分類を説明。150枚の版画に148〜152枚という許容範囲が付いた実例を掲載した。

現行CSV全1,000問を集計し、topicの10分類とanswer_typeの5分類を掲載。話題は政治176、科学・技術160、芸術145、スポーツ117、地理111、音楽102、その他102、歴史52、テレビ番組20、ゲーム15。答えの種類はOther 249、Date 222、Person 198、Number 185、Place 146。分類は配布ラベルを用い、独自分類へ置き換えていない。

## データ修正と13実例

現行CSVは349,184 bytes、SHA-256 `b5db21155444763543fe31b67e7cf28ce2bb225742a5b889421c5f182e2f92f5`。直前の2025年改訂 `ed392714d14fa5225b07c2b456453983bc75f690` と全レコード・全列を比較した。変化はoriginal_index=55のproblemのみで、latitudeからlongitudeへ修正。正解33.7738、許容範囲33.7586〜33.8022、その他の999問は変わっていない。論文v1・v2の対応する例も描画・テキストで照合した。

原文は全13件とも全文を再掲。日本語は翻訳、回答欄は配布正解の日本語化・表記整理。各ページのoriginal_indexと公式viewerの行番号を元CSVへ照合した。10話題すべてから例を選び、本編3件、追加10件にした。

|ページ|original_index|公式データの行|内容|
|---|---|---|---|
|8|43|[13](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=13)|芸術家の生年月日|
|9|337|[82](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=82)|ドラマーとレストラン|
|10|55|[15](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=15)|Lilongweの経度|
|34|8|[1](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=1)|アイスランド元首相|
|35|254|[59](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=59)|バスケットボール出場数|
|36|31|[8](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=8)|版画の枚数と許容範囲|
|37|4114|[946](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=946)|Quit Indiaのスローガン|
|38|552|[129](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=129)|数学賞|
|39|3306|[764](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=764)|きのこ帝国のEP|
|40|1842|[418](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=418)|ゲームのコンテスト|
|41|596|[136](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=136)|派生テレビシリーズ|
|42|1111|[253](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=253)|Hall Medal|
|43|342|[83](https://huggingface.co/datasets/google/simpleqa-verified/viewer/simpleqa_verified/eval?row=83)|画家と妻の年齢差|

元の問題番号を保持しており、表示順の行番号と混同しない。質問・正解の事実性を新たな独立調査で全件再検証したとはしていない。数値に許容範囲がある場合はそれも回答へ示した。

## 表示・構造・利用条件

共通マスター、Noto Sans / Noto Sans CJK JP、コードはLiberation Monoを使用。表紙52pt太字、左上帯14pt太字。10個の編集可能な表、2個の編集可能なグラフ。表の上下1.2pt、見出し境界0.6pt、縦罫なし。ノートなし。参考文献は2件ずつ3ページへまとめた。

全53枚を一覧で確認し、引用13枚・表10枚・コード1枚・参考文献3枚を1枚ずつ1440×810で拡大確認した。グラフ、表紙、変更ページも確認。タイトルと表セルの短い折り返し、表の行高、本文と出典の間隔、長いURLの折り返しを修正し、同じ形式のページも再検査した。本文の短い最終行は許容する方針を適用した。

全段落のPPTX・PDF照合で文字欠落・ページ外文字・通常タイトルの想定外の折り返しなし。全116セルの文字とセル内の実描画位置を照合し、表注との間隔も確認。本文・表注と出典の最小間隔は約9.1pt、コード背景の上下余白は約11pt、参考文献間の最小間隔は約36.7pt。URLのみの45リンクを確認した。PPTXのZIP・内部参照・70 XMLパーツを検査し、既知の箇条書きパーセント表記以外のスキーマエラーなし。検査済みのPPTX・PDFをそのまま納品先へコピーした。

Googleの公式データカードはMITを指定している。元のSimpleQA評価コードのMIT LICENSEは [licenses/simple-evals-MIT.txt](licenses/simple-evals-MIT.txt) に保存した。データの公開元とコードの権利表記を同一視していない。各引用にデータ名・番号・URL・翻訳の旨を示した。

## 接続・画面・ギャラリー

公式Hugging Face配布ページはCSS3件・Source Sans Proの適用を確認して撮影。SimpleQA Verifiedのページ名と1,000問の表示を目視した。

当初はBrowseCompも調査したが、論文が問題・正解のオンライン再掲載を控えるよう求めているため、公開ギャラリー用の今回の対象から外した。接続設定の変更後、取得できなかった資料を再試行し、Gemini 3 Pro・3.1 ProのモデルカードPDFとGemini 3 Proの評価手順PDFを取得できた。Kaggle、Googleブログ、BrowseCompのAzure Blob配布先は依然としてプロキシの403、OpenAIの紹介ページも403だった。取得済みの公式資料で制作を完了した。追加した接続設定案はstorage.googleapis.comのみで、既存の許可先を保持した。設定の保存と実際の疎通は分けて記録している。

ギャラリーへ「言語 / 質問応答 / 2025」で登録し、ラベルは増やしていない。18資料の全表紙・PDFリンク、SimpleQA Verifiedの大小文字・全角検索、複合フィルター、公開年ソート、リセット、JSON-LDをブラウザーで確認。PC1440px・モバイル390pxのスクリーンショットを撮影し、CSS・画像の適用と横はみ出しがないことを確認した。
