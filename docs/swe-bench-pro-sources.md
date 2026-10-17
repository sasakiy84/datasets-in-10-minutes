# SWE-bench Pro：出典と制作記録

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

2026-10-17制作。日本語の本編33枚、Appendix33枚、全66枚。シリーズの約10分の黙読・流し読みを想定した構成。編集可能なPPTXと、同じ最終PPTXから出力したPDFを収録する。

## 一次資料とバージョン

|資料|確認したバージョン・用途|
|---|---|
|[SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/abs/2509.16941v2)|Xiang Deng, Jeff Da et al., Scale AI, 論文v2、2025-11-14。初回公開は2025年9月。当初の構成・課題の作成工程・モデル結果。著者名と順序はPDF冒頭を採用し、リポジトリの簡略BibTeXとは混ぜていない。|
|[SWE-bench Pro V2](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f9276/v2)|改訂 `66f92766bba642462d4bbe5479e83f91f9211862`。データのバージョン2、642課題・11リポジトリ、HARD-51、評価手順と従来バージョンからの変更。|
|[Release gate](https://github.com/scaleapi/SWE-bench_Pro-os/blob/66f9276/v2/GATE.md)|2026-09-22、Harbor 0.22 / Modal。参照・空パッチ・公開コンテナの全件確認。|
|[SWE-bench_Pro / Hugging Face](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)|改訂 `2d52cb3df914a3fcf80c7f66738b3a88ae37fc50`。default = V2（642）、hard = HARD-51（51）、v1 = 従来731課題。|
|[Gemini 3.1 Pro / Performance](https://deepmind.google/models/gemini/pro/)|2026-10-17取得。現行のプロプライエタリモデルがSWE-Bench Pro (Public)を公式比較に使うこと、モデル名・推論設定・1回試行を確認。|

論文のバージョン2（2025年）とデータのバージョン2（2026年）は別の更新として説明する。当初は公開731・商用276・留保858の計1,865課題、リポジトリ数は11・18・12。データV2は公開側を731から642へ変更したもので、全体を642へ置き換えたという説明にしない。公開年は初回公開の2025をギャラリーに登録した。

## モデル評価と実行条件

論文v2の公開731課題、SWE-agent、最大50ターン、問題文・要件・インターフェースを与える条件の1回試行を掲載。Claude Sonnet 4.5 = 43.6%、Sonnet 4 = 42.7%、GPT-5/high = 41.8%、Haiku 4.5 = 39.5%。論文中の別予算・別集合の表と混ぜていない。

Googleの公式比較はGemini 3.1 Pro/high = 54.2%、Gemini 3 Pro/high = 43.3%、GPT-5.2/xhigh = 55.6%、GPT-5.3-Codex/xhigh = 56.8%。対象はPublic、1回試行だが、表にデータのバージョン指定がないため、その条件を資料内にも明記し、V2成績とはしていない。

V2の固定手順はエージェントの作業時間50分、作業中はモデルAPI以外の通信を禁止し、Web検索・取得も無効。提出したgit diffを新しい環境へ適用して採点し、元の環境の得点と再採点の両方を報告する。正式な値は再採点。準備・採点段階は通常のネットワーク接続を維持する。

公開元のRelease gateでは参照パッチ642/642合格、空パッチ642/642不合格、642個の公開manifestを確認した。基盤の一時エラーは再試行済み。HARD-51は5系列中2系列以上が失敗した課題を基に、後で曖昧さが見つかった3課題を除いた51課題。選定に使った5系列はV2 READMEに記された名前を採用し、非掲載のモデル得点を作っていない。

## 掲載した13実例

全例を取得したV2の `instruction.md`、`solution/gold_patch.diff`、`tests/config.json`、`tests/test_patch.patch` へ照合した。英語は課題文の実際の抜粋、日本語は要約・説明。各実例の2枚目は、配布された参照修正と採点テストを日本語で解説する。表示したURLは短くまとめ、リンク先は各課題の固定改訂ディレクトリへ直接対応する。

|掲載ページ|リポジトリ・課題ディレクトリ|内容|
|---|---|---|
|9–10|[NodeBB/NodeBB / `instance_NodeBB__NodeBB-f9ce92df988db7c1ae55d9ef96d247d27478bc70-vf2cf3cbd463b7ad942381f1c6d077626485a1e9e`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_NodeBB__NodeBB-f9ce92df988db7c1ae55d9ef96d247d27478bc70-vf2cf3cbd463b7ad942381f1c6d077626485a1e9e)|アップロード先の存在確認|
|11–12|[navidrome/navidrome / `instance_navidrome__navidrome-c90468b895f6171e33e937ff20dc915c995274f0`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_navidrome__navidrome-c90468b895f6171e33e937ff20dc915c995274f0)|アルバムの保存場所集約|
|13–14|[qutebrowser/qutebrowser / `instance_qutebrowser__qutebrowser-0833b5f6f140d04200ec91605f88704dd18e2970-v059c6fdc75567943479b23ebca7c07b5e9a7f34c`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_qutebrowser__qutebrowser-0833b5f6f140d04200ec91605f88704dd18e2970-v059c6fdc75567943479b23ebca7c07b5e9a7f34c)|Qtのエラー通知|
|37–38|[ansible/ansible / `instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5)|コレクション名の予約語検証|
|39–40|[internetarchive/openlibrary / `instance_internetarchive__openlibrary-427f1f4eddfc54735ca451779d4f95bf683d1b0e-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_internetarchive__openlibrary-427f1f4eddfc54735ca451779d4f95bf683d1b0e-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4)|検索クエリと版IDの正規化|
|41–42|[flipt-io/flipt / `instance_flipt-io__flipt-abaa5953795afb9c621605bb18cb32ac48b4508c`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_flipt-io__flipt-abaa5953795afb9c621605bb18cb32ac48b4508c)|ストレージの設定|
|43–44|[future-architect/vuls / `instance_future-architect__vuls-8659668177f1feb65963db7a967347a79c5f9c40`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_future-architect__vuls-8659668177f1feb65963db7a967347a79c5f9c40)|除外した脆弱性数|
|45–46|[element-hq/element-web / `instance_element-hq__element-web-7c63d52500e145d6fff6de41dd717f61ab88d02f-vnan`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_element-hq__element-web-7c63d52500e145d6fff6de41dd717f61ab88d02f-vnan)|入力欄の案内表示|
|47–48|[protonmail/webclients / `instance_protonmail__webclients-32ff10999a06455cb2147f6873d627456924ae13`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_protonmail__webclients-32ff10999a06455cb2147f6873d627456924ae13)|連絡先の件数・複数形|
|49–50|[tutao/tutanota / `instance_tutao__tutanota-de49d486feef842101506adf040a0f00ded59519-v10a26bfb45a064b93f4fc044a0254925037b88f1`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_tutao__tutanota-de49d486feef842101506adf040a0f00ded59519-v10a26bfb45a064b93f4fc044a0254925037b88f1)|復号失敗のエラー変換|
|51–52|[gravitational/teleport / `instance_gravitational__teleport-1b08e7d0dbe68fe530a0f08ad408ec198b7c53fc-vee9b09fb20c43af7e520f57e9239bbcf46b7113d`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_gravitational__teleport-1b08e7d0dbe68fe530a0f08ad408ec198b7c53fc-vee9b09fb20c43af7e520f57e9239bbcf46b7113d)|X11ソケット解決|
|53–54|[NodeBB/NodeBB / `instance_NodeBB__NodeBB-82562bec444940608052f3e4149e0c61ec80bf3f-vd59a5728dfc977f44533186ace531248c2917516`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_NodeBB__NodeBB-82562bec444940608052f3e4149e0c61ec80bf3f-vd59a5728dfc977f44533186ace531248c2917516)|投票者一覧の閲覧権限|
|55–56|[ansible/ansible / `instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5`](https://github.com/scaleapi/SWE-bench_Pro-os/tree/66f92766bba642462d4bbe5479e83f91f9211862/v2/tasks/instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5)|複数ポートの規則生成|

NodeBBの採点はFAIL_TO_PASS 1件・PASS_TO_PASS 34件、qutebrowserは1件・9件を配布configから確認。Navidromeの課題文のパス例とEmbedArtPath、参照差分の5ファイルを照合した。Fliptの非DATABASEでreadOnly=falseという条件は、課題文と実際の参照コードの両方にある条件をそのまま掲載した。

## 内容・構造・表示の確認

V2の全6,436ファイルは配布 `SHA256SUMS` に一致。642ディレクトリを従来データの課題IDと照合し、全11リポジトリの課題数を集計した。合計642、HARD-51の51件すべてがV2に含まれること、掲載13課題が互いに異なることを確認した。

公式 `tests/test.sh` の最終採点ブロックをそのまま取り出し、ローカルのテスト結果JSONを渡して実行した。必要な35件すべてがPASSEDなら終了コード0、修正対象1件が欠ける場合と全件欠ける場合は終了コード1となった。モデルAPI、Modalでの全件実行は行っていない。642件の動作保証の数値は公開元の実行記録による。

冒頭は公式Hugging Face配布ページ。ブラウザーでCSS4件・Source Sans Proと642件のdefault表示を確認して撮影した。Scaleの研究トップは接続制限で取得できず、取得した配布ページを掲載した。

共通マスター、Noto Sans / Noto Sans CJK JPを使用。表紙52pt太字、左上帯14pt太字。コードはLiberation Mono。11個の編集可能な表、1個の編集可能なグラフを含む。表は上下1.2pt、見出し境界0.6pt、縦罫なし。発表者ノートなし。

全66枚を一覧で確認し、引用13枚・コード1枚・表11枚・参考文献3枚は1440×810で1枚ずつ拡大確認。長いタイトル、コードのページ外へのはみ出し、日付の折り返しによる表の拡大を修正し、同じ形式のページも再確認した。タイトル・表セルの1〜2文字だけの折り返しを調整し、本文などの短い最終行は許容した。参考文献は1ページ2件ずつ、題名・著者情報・説明・URLをまとまりとして配置した。

全段落のPPTX・PDF照合、文字欠落・ページ外文字・タイトルの想定外の折り返しがないことを確認。表114セルは描画後のセルごとの文字と位置を照合。本文と出典の最小間隔は約9.1pt、コード背景の上下余白は各約10.8pt以上、参考文献の最小間隔は約36.7pt。URLのみの58リンクを確認した。

PPTXのZIP、内部参照、82 XMLパーツを検査し、既知の箇条書きパーセント表記以外のスキーマエラーなし。検査したPPTX・PDFを再生成せず納品先へコピーした。制作・確認用スクリプトはスキルとしてコミットしていない。

## 利用条件とギャラリー

取得した公開リポジトリのMIT LICENSEを [licenses/swe-bench-pro-MIT.txt](licenses/swe-bench-pro-MIT.txt) に保存した。各対象ソフトウェアは独自のライセンスを持つ。課題文とコードの短い引用に、元プロジェクト名・課題ID・公開元を添えた。

既存ラベル「言語 / エージェント操作 / 2025」で17件目として登録。全表紙とPDFリンク、SWE-bench Proの大文字・小文字・全角検索、複合フィルター、年ソート、リセット、JSON-LDをブラウザーで確認した。PC1440px・モバイル390pxのスクリーンショットを確認し、CSSとサムネイルの適用・横はみ出しがないことを確認した。


## 実例の配置と参照修正の説明の改訂（2026-10-17）

全13組の実例26ページと、実例の読み方を示す導入1ページを更新した。本編33・全66ページの順序と例の対応は維持。

課題のページは、日本語の説明から入り、その直下に原文ラベルと引用を置く。引用と説明を上下の固定位置へ離して置く方式をやめ、実際に描画した文字の高さからまとまりとして配置した。原文13件は従来の抜粋と同一で、配布instruction.mdと再照合。引用背景の上下余白は各8pt、日本語説明から原文ラベルは14pt、ラベルから背景は12pt。

各実例の2枚目は「実例／追加例N：参照修正の解説」と明記する。公開元が用意した修正例が参照修正であることを導入で説明し、「変更後の動作」「参照修正が行うこと」「テストが確認すること」の3項目で構成した。コード識別子だけの説明を、利用時の具体的な変化から読める文へ書き直した。たとえば、Open Libraryは配布テストのedition_key:OL123Mと+key:"/books/OL123M"、Navidromeは課題文の2ファイルと集約パス、Proton Mailは単数・複数の表示を示す。NodeBBのコード抜粋ページは、保存前の存在確認とエラー応答を説明するページに改めた。

参照修正・テストの説明は13課題のinstruction.md、gold_patch.diff、test_patch.patch、config.jsonへ照合した。テスト数は各設定のFAIL_TO_PASS／PASS_TO_PASSを数えたもの。TestModelなどの集合を、内部の個別テスト数とは言い換えていない。Fliptの「falseかつ非DATABASE」の条件は配布課題文と参照コードの実際の条件を維持した。

最終PDFの全66ページを一覧で確認し、実例26ページ、導入、全表・引用・コード・参考文献、表紙を1440×810で拡大確認した。PPTXの全段落・表セルとPDFの文字が対応し、文字欠落、ページ外文字、タイトルの想定外改行なし。本文と出典の最小間隔は約9.1pt、参考文献の最小間隔は約36.7pt。13引用の上下余白と、13解説の項目順・対応を再確認。修正対象外39ページのスライドXMLは元ファイルと完全一致した。PDFの字形に微差が出た2ページも拡大確認した。

OOXMLの82部品、ZIP・内部参照、11表・1グラフ、ノートなしを検査。最終検査・目視確認後のPPTX・PDFをそのまま公開用へコピーし、ビルド後の配布ファイルともハッシュ一致を確認した。制作・検証スクリプトは一時領域に置き、コミット対象に含めない。
