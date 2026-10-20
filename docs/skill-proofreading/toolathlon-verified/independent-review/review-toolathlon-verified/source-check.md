# Toolathlon-Verified 独立一次資料確認

レビュー担当: review_officeqa2（OfficeQAから対象変更）。資料制作担当とは別に取得・読解した。Gemini・外部モデルAPI・環境変数の鍵・外部アプリへの書き込みは使用していない。

## 確認資料

- Li et al., *The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution*, arXiv:2510.25726v2。2025-10-29初出、2026-02-26改訂、ICLR 2026。本文1–7頁を読解し、32 MCPサーバー604ツール、7ローカルtoolkit16ツール、108課題、作成工程、評価指標、旧版の代表性能を確認した。
- 公式GitHub https://github.com/hkust-nlp/Toolathlon の公開pin `9be8d8fe07a497b18ee61e3f2ae694e9797f39eb`。108課題それぞれのtask.md、task_config.json、evaluation/main.py、計324ファイルを独立取得し、108件全ての存在・JSON形式を確認。原票の全文読解は選択13件の範囲に限定する。
- 公式サイト https://toolathlon.xyz/introduction 、https://toolathlon.xyz/docs/leaderboard 、https://toolathlon.xyz/docs/blog/toolathlon-verified を別途取得・読解。Verifiedは2026-06-30の改訂で108件の同一課題を保ち、83課題のパッケージに修正がある。旧版と現行版は別の公式スコア系列。全体に604ツールがあることと、一つの課題に全604を渡すことは別。各課題では関連MCPサーバーを設定し、各サーバー内のツールを提供する。
- Anthropic *Claude Fable 5.1 & Claude Mythos 5.1 System Card* 194–195頁。Fable 5.1のPass@1 77.8%、Pass@3 81.5%、Pass³ 73.1%、平均23.7turnsを確認。108課題を各3回、324試行のうち11件をfallbackが部分的または全面的に完了し、4件は安全判定で失敗と扱う。抽出・実行環境は独自harnessであり、公式ボードのスコアとは同じランキング表へ混在させない。公式と独自harnessのnull試行の扱いの差も記述がある。


## 対象名と年

今回の資料タイトルは **Toolathlon-Verified**。公式READMEと公式サイトはこの綴りを現在の最終改訂版名として使い、リリース日を **2026-06-30** と明記する。元研究の正式な課題名は **The Tool Decathlon (Toolathlon)**、論文の正式題名は *The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution*。元研究はarXiv初版の **2025-10-29** に公表された（公式サイトの紹介記事一覧は2025-10-28と表示）。元研究2025年と、今回のVerified改訂2026年を区別する。ギャラリーは紹介対象をVerified改訂版として **year=2026** が適切。

## 指標と採点

Pass@1は各1試行の成功率を三試行で平均する。Pass@3は三試行のうち一回以上成功した課題の割合、Pass³は全三試行が成功した課題の割合。単一ツール呼び出しの正確さではなく、課題の最終ファイルやサービス状態を固有のcheckerで判定する。内部に許容誤差・閾値がある課題もあるため、「全ての課題で全ての項目の100%一致のみが成功」は不正確。

## 独立原票の確認

- 本編候補Canvas: 公開emails.jsonlの9件を読み、homework2の7件から最新提出を選ぶ6名の参照点をcheckerへ照合。Timothy RuizとShirley Rodriguezが10点、他4名が0点。homework1を混ぜない。Canvasサービスを起動した検証ではない。
- 本編候補inventory-sync: 6SQLiteを読み取り専用で開き、各17商品のpending在庫を地域・商品ごとに合算。PROD001はEast647、South851、West986。checkerは地域・商品の数量の一致比率90%以上で成功とする。report.yaml検査は現行mainで無効。WooCommerce実行は行っていない。
- 本編候補sales-accounting: 元xlsx121行（見出し込み）と参照xlsx126行を比較。先頭121行の全セルを保持し、2024-01-07〜10の5取引を追加する。1月16日の今週の取引を除く。taskの日付は2024-01-18であり、スライド制作日ではない。
- 補足候補AB: 20分野の生CSVから各分野のクリック→閲覧率と算術平均を再計算。A73.83961917%、B74.12085660%で参照CSVに丸め一致。B勝利時は所定bucket作成・新しいログ追加なし。Cloud APIは実行していない。

各独立取得ファイルのhash・規模、集計方法・実行結果は専用JSONに保存した。ハッシュはスライドへ掲載する情報ではない。

## 公開範囲・利用条件

GitHub rootにLICENSEファイルがなくGitHub APIのlicenseもnullで、READMEに本体のライセンス指定を見いだせなかった。MIT等を推測しない。論文のライセンス、各上流MCP実装、配布課題・ファイルの利用条件を同一視しない。HF Toolathlon-Verified_Trajectoriesは取得時点でアクセス申請が必要で、raw軌跡の再公開をしない方針が掲示されている。こちらは認証・取得・再配布を行わず、公開GitHubの課題・初期ファイル・参照状態を使用する。

## 保留

最終スライドがまだないため、全ページの内容・日本語・翻訳・PPTX構造・描画を検証したとは主張しない。初稿完成後に全native/PDF本文と最終ファイル対応を確認する。個別画像確認はまず30頁までを担当し、それ以外は別の独立visual担当へ分担する。
