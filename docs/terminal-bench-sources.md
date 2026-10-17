# Terminal-Bench：出典と確認範囲

最新改訂：原文・訳の併記と説明文の見直し。現行71ページ。[変更対・ページ対応・検証記録](slide-language-review/terminal-bench.md)を参照。以下は初回制作時の記録を含む。

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

2026-10-16作成。日本語版「datasets in 10 minutes」。Terminal-Benchの公開版2.0を中心に、端末で行う作業、実例、採点、作成方法、利用の変遷を紹介する。本編41枚＋Appendix30枚、計71枚。作成者はsasakiy84、所属欄なし。本編の黙読・流し読みの配分は、冒頭30秒、実例160秒、採点と成績155秒、作成方法と全体像150秒、利用と実行方法105秒、計600秒を想定する。

## 選定と現在の利用

現行のプロプライエタリモデルによる利用は、次の公式資料で確認した。

- [Harbor公式README](https://github.com/laude-institute/harbor)：2026-10-16取得。`terminal-bench@2.0`を`claude-code`と`anthropic/claude-opus-5-5`で実行する例を掲載する。
- [Google DeepMind, Gemini 3.1 Pro](https://deepmind.google/models/gemini/pro/)：2026-10-16取得。Terminal-Bench 2.0 / Terminus-2 harnessで、Gemini 3.1 Pro High 68.5%、Claude Opus 4.6 Max 65.4%、GPT-5.2 xhigh 54.0%を掲載する。
- [Anthropic, Claude Opus 5.5（2026-09-22）](https://www.anthropic.com/news/claude-opus-5-5)：同日に先行するHLE資料の調査で取得した公式ページを参照。Terminal-Bench 4.0でOpus 5.5 66.4%、GPT-6 Astra 57.9%、GPT-5.6 Sol 37.3%。Opus 5.5はxhigh effort、GPT-6 Astraはhigh effort。同URLの今回の再取得はHTTP 403だった。
- [OpenAI, GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)：同日の先行調査で取得した公式ページでも、Terminal-Bench 4.0の57.9%を確認した。今回の再取得はHTTP 403だった。

スライドは、公開タスクと採点の具体的な説明には2.0を用い、4.0の公表値は版名を付けた別表へ掲載した。成績表の前に、2.0と4.0がデータセットの版であり、Terminus 2がエージェント名であることを説明した。4.0について、OpenAIの説明にあるソフトウェア開発・システム設定・データ分析、Anthropicの説明にある複数手順の実務課題、同社が参照する公開リーダーボードのClaude Code・各課題5試行という条件を対応する出典とともに掲載した。参照できた資料は4.0の課題総数・2.0からの増減や構成変更を示しておらず、今回の89課題の統計は2.0に限定する。初公開年は公式READMEの引用指定に基づく2025年。モデルAPIの有料実行は行っていない。

## 原著・公開タスク・実行基盤

- Mike A. Merrill, Alexander G. Shaw et al. (2026). *Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces*. ICLR 2026。[プレプリント](https://arxiv.org/abs/2601.11868)、arXiv:2601.11868v1、2026-01-17。原著PDFを取得した。
- [Terminal-Bench公式リポジトリ](https://github.com/laude-institute/terminal-bench)：READMEの引用指定で、正式タイトル、著者、ICLR 2026の書誌を照合した。
- [Terminal-Bench 2.0](https://github.com/laude-institute/terminal-bench-2)：公開課題・環境・参照解法・採点テストを取得した。現在のGitHub画面は`harbor-framework/terminal-bench-2`へ転送される。
- [Harborレジストリ](https://github.com/laude-institute/harbor/blob/main/registry.json)：`terminal-bench@2.0`は89課題すべてにGit改訂`69671fbaac6d67a7ef0dfec016cc38a64ef7a77c`を指定している。実例・集計・コード引用にはこの改訂をチェックアウトして使用した。
- 先行研究の[SWE-bench](https://arxiv.org/abs/2310.06770)と[WebArena](https://arxiv.org/abs/2307.13854)は、原著の参考文献と各公式READMEで、対象課題・初公開年・ICLR 2024の書誌を照合した。

公式サイト`www.tbench.ai`とHarbor文書サイトは、環境の接続経路でCONNECT 403となった。冒頭には、取得できた公式GitHubリポジトリの画面をブラウザーで撮影して掲載した。外部CSSの一部を取得できず、ブラウザーの標準書式で表示されている。

## 実例

本編3件とAppendixの追加10件を、固定した公開改訂から選んだ。英語の指示文は抜粋と表示し、表示に不要な空白・改行を整え、日本語の要旨と採点テストの説明を付けた。各ページに課題名と固定改訂のURLを載せた。

|掲載先|タスクID|確認した合格条件|
|---|---|---|
|本編|`cancel-async-tasks`|関数の配置、並行実行、同時実行上限、SIGINT時の後始末|
|本編|`db-wal-recovery`|JSONの構造、id順、全11件、更新値150・250、重複の排除|
|本編|`cobol-modernization`|指定入力列からのACCOUNTS・BOOKS・TRANSACTIONSの内容一致|
|追加1|`query-optimize`|元と同じ列・行・順序、SQLiteの単一クエリ、サイズ条件|
|追加2|`build-cython-ext`|NumPy 2.3.0、Cython拡張3種類、結び目の計算、既存テスト|
|追加3|`configure-git-webserver`|GitへpushしたファイルのHTTP取得|
|追加4|`log-summary-date-ranges`|指定日2025-08-12、5期間×3重要度のCSV全15行|
|追加5|`multi-source-data-merger`|統合値、優先順位、競合レポート|
|追加6|`overfull-hbox`|PDF生成、行はみ出し警告、許可された同義語・編集範囲|
|追加7|`raman-fitting`|G・2Dピークの4パラメータと許容範囲|
|追加8|`reshard-c4-data`|容量・ディレクトリ項目数、復元後のファイル集合・ハッシュ|
|追加9|`prove-plus-comm`|Coqによる証明の完了、コンパイル|
|追加10|`video-processing`|2動画の踏切・着地フレームの許容範囲、使用ライブラリ|

課題の指示・テストを読んで照合し、各タスクのコンテナーや解法スクリプトは実行していない。Dockerイメージは取得していない。動画処理の例は、動画自体の行動認識例としてではなく、指示文とプログラム作成課題として紹介した。

公開リポジトリのライセンスは[Apache License 2.0](https://github.com/laude-institute/terminal-bench-2/blob/69671fbaac6d67a7ef0dfec016cc38a64ef7a77c/LICENSE)。英文・テストコードは同リポジトリからの抜粋で、日本語要旨とレイアウトを追加した。

## 数値と集計

- 原著が報告する投稿は93人・229課題、採用89課題。人手審査は3人、最終課題当たり合計約3時間。
- 分野は`task.toml`の`metadata.category`を全89課題で集計した。ソフトウェア開発26、システム管理9、科学計算8、セキュリティ8、データサイエンス8、デバッグ5、ファイル操作5、モデル学習4、数学4、データ処理4、機械学習3、ゲーム・個人向け支援・最適化・データ照会・動画処理が各1。合計89、原著Fig. 4の16分類とも一致した。
- 難度はeasy 4、medium 55、hard 30。作者のラベルをそのまま集計した。
- 所要時間見積もりは値のある88課題を対象にした。専門家の中央値60分、最小5分、最大2,400分。若手エンジニアは中央値240分、最小10分、最大19,200分。原著Table 1の時間見積もりの表は74課題に対応するため、その表を公開89課題へ外挿せず、固定改訂の記入値を集計した。
- `agent.timeout_sec`は15分以下51、15分超30分以下22、30分超60分以下14、60分超2。最小600秒、最大12,000秒。全89課題を含む。
- 容量は固定Git改訂の管理ファイルのバイト数を合計し、45,894,095 bytes（43.77 MiB、1 MiB=2²⁰ bytes）。Git履歴・実行用イメージの容量は集計対象に含めない。
- 原著Table 2はGPT-5.2＋Codex CLI 62.9%、Opus 4.5＋Terminus 2 57.8%、Gemini 3 Pro＋Terminus 2 56.9%。エージェント比較のGemini 2.5 ProはTerminus 2 32.6%、Mini-SWE-Agent 26.1%、Gemini CLI 19.6%、OpenHands 15.7%。表の値を照合した。
- 3課題で66.7%の表は、見出しで「説明用」と示した採点例。

## 制作・表示確認

共通マスターを継承し、元の例示8枚を除去した。表紙はNoto Sansの52 pt太字、日本語はNoto Sans CJK JP、緑帯は14 pt太字。本文・目次・章扉も既存シリーズと同じ書式を使う。表24個とグラフ1個は編集可能。罫線は上端・下端1.2 pt、見出し下0.6 pt。発表者ノートは含めない。

最終PPTXからPDFを出力し、全71ページを描画して確認した。段落・表セルとPDF抽出文字を照合し、文字欠落・ページ外へのはみ出し・通常タイトルの折り返しがないことを確認した。本文と出典の実描画間隔は8 pt以上。URLだけのリンク範囲、引用の上下余白、参考文献のまとまり、表紙・目次・転換の実文字境界による中央配置も確認した。

ZIP整合性、内部参照、表罫線、ノート不在を確認した。PresentationML・DrawingML・図表の87 XMLパーツを未変更のISO/IEC 29500-4 XSDで照合し、`buSzPct`の整数表記に関する既知の字句差121件、その他のエラー0件だった。全121値は公式Open XML SDKの定義域25000〜400000に入る。PowerPointデスクトップでの手動編集は未確認。

ギャラリーへ初公開年2025・種別「言語」・共通タスク「エージェント操作」で追加した。表紙の書体を理由にサイトビルドを止める自動検査は追加していない。

2026-10-16追記：本文・表注の曖昧な「原著」を著者名・年に改め、表番号だけの注記を削除した。ギャラリーはタイトル14 CSS px・1行の省略表示とし、検索とアクセシブル名には全文を残す。

## 2026-10-16：p.34の表と全表の再検査

p.34の見出しを著者名・年に置き換えた際、見出しが3行へ広がり、後続行と表注が重なっていた。前回の検査はPDF内の文字の存在とページ境界を調べており、この内部の重なりを見逃していた。見出しを「分類」へ戻し、著者名・年は表注と出典で対応させた。

今回はPDFの各セルの実文字境界をPPTXの各行・列の領域と照合し、表本文と表注の実描画間隔も測定した。修正前のコミットのp.34でセルのはみ出しと表注との重なりを検出できることを確認した。この検査で見つかった実例1・投稿時の検査・利用の変遷・ソース容量・ライセンス案内のセルの折り返しも、文言または行高を調整した。最終71ページ・全244セルではセルからのはみ出し0件、表注の間隔12 pt未満0件。文字欠落・通常タイトルの折り返し・ページ外への文字のはみ出しも0件だった。共通SKILLにも、文言の置換後はセルと表注の収まりを再確認する手順を明記した。
