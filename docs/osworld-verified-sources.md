# OSWorld-Verified 制作・出典記録

最新改訂：原文・訳の併記と説明文の見直し。現行65ページ。[変更対・ページ対応・検証記録](slide-language-review/osworld-verified.md)を参照。以下は初回制作時の記録を含む。

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

2026-10-17（Asia/Tokyo）。本編30ページ、全65ページ。日本語の黙読・流し読み約10分を想定、未実測。著者sasakiy84。

## 一次資料と取得改訂

- Tianbao Xie et al., **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**, NeurIPS 2024。第一著者Tianbao Xie、最終著者Tao Yu。https://arxiv.org/abs/2404.07972 。取得PDFはarXiv v2（2024-05-30）。NeurIPS掲載はVerified報告の書誌情報でも確認した。
- Tianbao Xie et al., **Introducing OSWorld-Verified**, XLANG Lab, 2025-07-28。https://xlang.ai/blog/osworld-verified 。直接ページはCONNECT 403。公式サイトの公開ソース https://github.com/xlang-ai/xlang-ai.github.io/blob/main/data/blog_posts/osworld-verified.md を取得して全文を読んだ（コミット `f9a8a96cbed3077f405b944f093cde5fc4acf115`）。
- 公式コード・課題定義 https://github.com/xlang-ai/OSWorld 、コミット `b138d348256078fa634fc3b73567a7337c793e6b`。
- 公式評価表 https://github.com/os-world/os-world.github.io/blob/main/static/data/osworld_verified_results.xlsx 。公式サイトの公開ソースを取得（`62f8466dbe8b4d67c104b5ead3f8271da01aa09d`、2026-08-08）。実際のサイトはCONNECT 403で、XLSXを直接読み、各掲載行と条件・日付を照合。
- 初期ファイル・参照成果物 https://huggingface.co/datasets/xlangai/ubuntu_osworld_file_cache 。本編3課題の入力と参照を取得。
- 公式操作ログ https://huggingface.co/datasets/xlangai/ubuntu_osworld_verified_trajs 。配布READMEとファイル一覧を取得。実例には `results_klick_openapa_full_newkey_bg2.zip` の初期画面・指示を使う。ZIPの配布サイズは3,320,508,169 bytes。Range取得で索引と必要ファイルを読み、全ZIPをダウンロードしたとはしていない。

表紙は正式な対象名OSWorld-Verified。OSWorldをOperating System Worldなどの推測した名前へ展開せず、原著のタイトルも略語の展開形とは扱わない。ギャラリーの2025年はVerified更新の初出。先行OSWorldは2024年。

## 課題作成・構成・採点

初期報告では、学生9人が約3か月・約1,800人時で、利用場面、依頼、初期状態、採点器と確認を制作。2025年の改修は、約10人・約2か月で300件超のフィードバックを検証・修正。主な変更は、指示の範囲・形式の明示、複数の正解の許容、採点の類似度や許容幅、ウェブの変化への対応、フォント・起動・待機の改善、AWS並列評価、資料のHugging Faceへの移行。初期の134評価関数という数を現行の数として流用していない。

取得改訂のtest_all.jsonは369課題、test_nogdrive.jsonは361課題、test_small.jsonは39課題。Google Driveを含む8課題が差分。全体のJSONファイルも369本。361課題版はOffice 117、Daily 78、Professional 49、OS 24、Workflow 93。アプリ単位はCalc 47、Impress 47、Writer 23、Chrome 46、VLC 17、Thunderbird 15、GIMP 26、VS Code 23、OS 24、複数アプリ93（全体版では101）。入力に画面画像を使うためギャラリー種別は画像、タスクはエージェント操作。

採点は最終状態から各関数の0〜1の値を返し、平均を百分率へ直す。共通evaluate実装は、ANDなら0が一つでもあれば0、すべて正なら平均、ORは最大値。実行不能課題はFAILで終了すれば1点。共通run_single_exampleのステップ数はagent.predictを呼ぶ反復を数え、各予測が返した操作列を実行する。ステップを単一のクリック数とは定義していない。

調査では、現行全369定義にevaluator=infeasibleが27件、補助のtest_infeasible.jsonは26件だった。スライドに全実行不能課題数は載せず、実例の課題JSONと実装の判定を説明する。原著の初期30件を現行の数として扱わない。

## モデル評価

全行が最大100ステップ。追加a11yと複数試行はいずれもNo。日付は公式XLSXにあるDateで、Excel日付値を日付へ変換した。

|構成|課題数|得点（%）|Date|追加コード実行|
|---|---:|---:|---|---|
|claude-4-sonnet-20250514|361|41.40|2025-07-28|No|
|claude-sonnet-4-5-20250929|360|62.88|2025-10-31|No|
|claude-sonnet-4-6|356|72.11|2026-03-08|No|
|OpenAPA w/ gemini-3.1-pro|361|78.34|2026-04-17|Yes|
|Pointer Agent w/ Sonnet 4.6|360|81.45|2026-05-21|Yes|

スライドでは、モデルのGUI操作と外部計画・追加コードを組み合わせる構成を別表にした。各提出の課題数・日付を併記。公開表の256.71/356=72.11%を、整数個の完全成功数の割合へ言い換えない。初期2024年の結果と現行Verifiedを同じ条件の順位表へ混ぜていない。

## 実例の対応

本編3件＋追加10件の13独立課題。すべて同じOpenAPA公開ZIPにあり、各 `step_0.png` と `instruction.txt` を取得。指示は取得改訂のタスクJSONと空白正規化後に全13件一致。元PNGをそのままPPTXへ埋め込み、バイト一致を確認した。生成した操作画面や、画面から創作した指示は使っていない。

|画面ページ|指示ページ|アプリ|課題ID|
|---:|---:|---|---|
|8|9|libreoffice_writer|`0b17a146-2934-46c7-8727-73ff6b6483e8`|
|10|11|libreoffice_calc|`1954cced-e748-45c4-9c26-9855b97fbc5e`|
|13|14|multi_apps|`3680a5ee-6870-426a-a997-eba929a0d25c`|
|34|35|chrome|`bb5e4c0d-f964-439c-97b6-bdb9747de3f4`|
|36|37|chrome|`7b6c7e24-c58a-49fc-a5bb-d57b80e5b4c3`|
|38|39|vlc|`8ba5ae7a-5ae5-4eab-9fcc-5dd4fe3abf89`|
|40|41|gimp|`7a4deb26-d57d-4ea9-9a73-630f66a7b568`|
|42|43|gimp|`f4aec372-4fb0-4df5-a52b-79e0e2a5d6ce`|
|44|45|libreoffice_impress|`5d901039-a89c-4bfb-967b-bf66f4df075e`|
|46|47|libreoffice_impress|`550ce7e7-747b-495f-b122-acdc4d0b8e54`|
|48|49|libreoffice_writer|`0810415c-bde4-4443-9047-d5f70165a697`|
|50|51|vs_code|`982d12a5-beab-424f-8d38-d2a48429e511`|
|52|53|os|`c288e301-e626-4b98-a1ab-159dcb162af5`|

長い端末操作の依頼は、原文p.14と日本語訳p.15へ分けた。原文と課題定義の操作条件を保持。文書編集では実際のGold DOCXに「2」の下付き文字があることを確認し、公開関数compare_subscript_containsをASTから取り出して、Gold/Gold=1、初期文書/Gold=0を実行した。

Invoices.xlsxの18データ行を番号別に数え、参照XLSXのSheet2の6件数と一致。結合課題はfile1.xlsx・file2.ods・output_gold2.csvを読み、Dulce+Abril、Mara+Hashimoto、Philip+Gentの実データを照合。CSV参照には別形式の許容ファイルもある。スライドはそのうち一つを示す。課題JSONの読み込みコードも実行した。VMの起動やエージェント評価の実行済みとはしていない。

## 利用条件・画面・最終確認

実装・課題定義のリポジトリはApache 2.0。[ライセンス本文](licenses/osworld-Apache-2.0.txt)。公開軌跡のデータカードはMITを指定。課題の文書やアプリ画面を含む実例は、個別の出典・IDを付けた説明目的の引用として掲載し、各アプリや第三者資料の権利まで一律にApacheと扱わない。

公式トップへは接続できなかったため、公式ログのHugging Face Files and versionsを実ブラウザで撮影。CSS3枚とSource Sans Proの反映を確認し、画像を目視。実際の画面URLをp.2に付した。アバター等の補助リソースの取得失敗は本文に影響しないことを確認。

全65ページを一覧で確認。引用13ページ、全10表、コード、参考文献3ページ、表紙・導入画面を個別に拡大して確認。引用上下各8pt、引用と訳の間12pt以上、本文と出典の最小間隔14.99pt、参考文献の項目間25.91pt以上、コード上下10.66/11.27pt。全PPTX段落とPDFの文字、全セル内収容、booktabs上下1.2pt・見出し下0.6ptを照合。文字欠落・ページ外文字・タイトル折り返しなし。ZIP・内部参照・ノートなし、XML80部品を検証し、共通マスターの既知のbuSzPct字句差127件以外に予期しないエラーなし。

最終修正はp.2の撮影URL。他64ページは確認済み版とピクセル一致。制作・調査・検査のスクリプトはscratchのみ。

|成果物|bytes|SHA-256|
|---|---:|---|
|PDF|3,429,152|`96cc3f366074d45a580a087c449f942c47cbaee93d68907fb39720ed27e20be4`|
|PPTX|6,957,445|`76b09fdf4d661ac3ac4960c1484cbc06a58df42d8e4b03a11b93ee48c30a33c1`|

24件のギャラリーを実ブラウザで確認。全表紙の読み込み、大小・全角のタイトル検索、画像・エージェント操作・2025年の併用、年順、カードのPDFリンク、PPTX取得、390px表示の横はみ出しなし。確認済みscratch・リポジトリ・公開ビルドのPDF・PPTXはSHA-256一致。
