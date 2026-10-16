# SWE-bench Verified：出典と確認範囲

2026-10-16作成。日本語「datasets in 10 minutes」。本編34枚＋Appendix28枚、計62枚。作成者sasakiy84、所属欄なし。GitHubの実Issueに対するコード修正を、テストの実行で評価するVerifiedを紹介する。本編は導入30秒、実例180秒、採点・モデル評価150秒、作成・構成150秒、系列・利用90秒の計600秒を想定する。閲覧時間は未実測。

## 選定と現行モデルでの利用

[Google DeepMind, Gemini 3.1 Pro](https://deepmind.google/models/gemini/pro/)の公式Performance表を今回ライブ取得した。SWE-Bench Verified / Single attemptの欄はGemini 3.1 Pro High 80.6%、Claude Opus 4.6 Max 80.8%、GPT-5.2 xhigh 80.0%。モデルの推論設定と、1回の試行であることを対応させた。独自にモデルAPIを呼び出した評価は実施していない。

## 一次資料と取得した版

- Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* ICLR 2024。共同第一著者はJimenezとYang。参照PDFは[arXiv:2310.06770v3](https://arxiv.org/abs/2310.06770v3)、2024-11-11。今回取得し、収集、属性・実行フィルタ、課題の形式を確認した。元のSWE-benchは2023年初公開。
- [公式評価コード](https://github.com/SWE-bench/SWE-bench)：固定コミット`02e7a74ffd0b707aab73d203fe87bdc7c76afc8e`。README、CHANGELOG、公式CLI文書、`swebench/harness/grading.py`を参照した。5.0.0は評価実装の版で、2026-08-17にtask repo形式を導入。CLIの例は固定コミットのREADMEに対応する。
- [公式タスク配布](https://github.com/SWE-bench/swe-bench-tasks)：固定コミット`3d07b464b7b311a0cbfb5ed5b2d8a3b96f84a33d`。各`task.yaml`の`datasets`に`SWE-bench/SWE-bench_Verified`を含むtest課題を選ぶと500件。問題文・参照パッチ・テスト変更・テスト一覧・メタデータを全件取得した。
- [公式サイトの公開ソース](https://github.com/SWE-bench/swe-bench.github.io)：固定コミット`193160a463a435d05cf44a1fa9dc5eac832113c3`。`templates/pages/verified.html`で人が問題文の明確さ、テストの正しさ、解決可能性を確認したこととBash Onlyの設定を確認。`lite.html`でtest 300課題、元の集合2,294課題を確認。`multilingual.html`と`multimodal.html`で系列の説明と後続版を確認した。
- [公式Hugging Face配布ページ](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified)：データカードを今回取得。APIで確認した改訂は`c104f840cc67f8b6eec6f759ebc8b2693d585d4a`、test 500件。2024-08-13公開。Parquet本体の取得は環境の接続制限により失敗したため、実例・全件集計は取得できた公式task repoを用いた。
- Xiang Deng, Jeff Da et al. *SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?* [arXiv:2509.16941v2](https://arxiv.org/abs/2509.16941v2)、2025-11-14。全1,865課題・41リポジトリ、Public 731課題・11リポジトリ、非公開集合との構成を確認した。Verifiedの単なる版番号として扱っていない。

OpenAIのVerified公開記事と公式サイト本体は、この環境で403／トンネル接続エラーとなった。人による検証の説明は公式サイトの取得済みソースを根拠とし、確認できていない人数や検証回数を追加していない。公式ドキュメントの概説表にあるLite 534件という値より、Lite専用ページが明示するtest 300件を採用した。

冒頭は公式Hugging Face配布ページの実スクリーンショット。CSS 3件とSource Sans Proの適用、500行のデータビュー、見出し・表の描画をブラウザで確認した。一部アバターと外部補助スクリプトは取得できなかった。スライド上の見出しも「公式配布ページ」に対応する。

## 掲載した13課題

本編7ページで、公開Verified 500課題から13課題を選んだことを説明した。13件はすべて異なり、12リポジトリを含む。架空のIssueや修正パッチは作成していない。各コードの行・式は公式`gold.patch`内に存在することを照合した。Issue原文では余分な空行を詰め、Requestsでは再現コードだけを抜粋した。日本語の課題内容・修正の説明は原文とパッチに対応させた。

|掲載ページ|課題ID|紹介する修正|
|---|---|---|
|8–9|`pallets__flask-5014`|空のBlueprint名を拒否する|
|10–11|`psf__requests-1921`|Noneの既定ヘッダーを送らない|
|12–13|`sympy__sympy-16886`|数字1のモールス符号を直す|
|38|`astropy__astropy-7166`|propertyにも文書を継承する|
|39|`django__django-15987`|Path型のfixtureディレクトリも重複検出する|
|40|`django__django-14373`|年を4桁にゼロ埋めする|
|41|`matplotlib__matplotlib-24627`|描画要素の所属参照を解除する|
|42|`mwaskom__seaborn-3187`|凡例のオフセット・科学表記を使わない|
|43|`pydata__xarray-3677`|DataArrayをDatasetへ変換して結合する|
|44|`pylint-dev__pylint-4970`|設定値0で重複コード検査を止める|
|45|`pytest-dev__pytest-7982`|リンク先ディレクトリを探索する|
|46|`scikit-learn__scikit-learn-13779`|Noneの推定器を重み検査から除く|
|47|`sphinx-doc__sphinx-9367`|1要素タプルのカンマを残す|

16ページはFlaskの`test.patch`にある追加テスト。採点対象はFAIL_TO_PASS 1件、PASS_TO_PASS 59件。参照パッチとの完全一致ではなく、テストで解決を判定することを説明した。

## 集計と版の説明

集計対象は固定したtask repo内のVerified全500課題。Django 231、SymPy 75、Sphinx 44、Matplotlib 34、scikit-learn 32、Astropy 22、Xarray 22、Pytest 19、Pylint 10、Requests 8、Seaborn 2、Flask 1。Djangoは46.2%。チャートの「その他」は残り7リポジトリ・84課題。

参照修正の変更ファイル数は`gold.patch`の`diff --git`単位。1ファイル429課題、2ファイル49課題、3以上22課題、最大21ファイル。変更行数は`+`・`-`の行を数え、`+++`・`---`のヘッダーと文脈行を除いた。中央値7、平均14.334、最小1、最大232。1～5行223課題、6～10行107、11～20行79、21～50行65、51行以上26。

Issue本文は前後の空白を除き、改行・コードを含むUnicode文字数を数えた。中央値1,176.5、平均1,672.2、母標準偏差2,015.2206、最小129、最大24,512。`created_at`は収集コードでもPRの作成日時から設定されると確認し、取得した500課題では2013-01-25～2023-08-07。`version`は対象パッケージの版、評価実装5.0.0はハーネスの版として説明した。

Multilingualは9言語・42リポジトリ・300課題。Multimodalは画面情報を使う系列で、公式の2026-09-01のv2公開説明では、不安定・採点不能なテストを除いた480課題をローカル評価できる。スライドでは2024年の初公開と2026年のv2を対応させた。Proは2025年にScale AIが公開した長時間の修正課題の評価として紹介し、問題数をVerifiedへ持ち込んでいない。ギャラリーの公開年は今回の対象Verifiedの2024年。

## 採点実装と確認範囲

固定コミットの`get_eval_tests_report`、`compute_fail_to_pass`、`compute_pass_to_pass`、`get_resolution_status`とテスト状態の判定関数を確認した。完全解決は修正・維持の両指標が1。現行コードではPASSED・XFAILが成功、PASS_TO_PASSのSKIPPEDは維持、FAIL_TO_PASSのSKIPPEDは失敗として扱う。

公式関数をASTからそのまま取り出し、Flaskの実際のテスト名を使うメモリ上の状態マップで、成功・未修正・回帰・FAIL_TO_PASSのスキップ・PASS_TO_PASSのスキップの5条件を実行確認した。成功とPASS_TO_PASSのスキップはRESOLVED_FULL、それ以外はRESOLVED_NOとなった。これは採点ロジックの確認であり、各課題のDocker環境の構築・500課題の参照修正の実行・モデル推論は行っていない。

## 権利と表示確認

公式評価コードの[MITライセンス](licenses/swe-bench-MIT.txt)を同梱した。各実例の原文・コードは元プロジェクトの資料として短い箇所を引用し、課題ID・元リポジトリ・固定した配布パッチへのURLを付けた。SWE-benchのMITライセンスを、各元プロジェクトのコードのライセンスへ一律に置き換えていない。データ本体や完全なパッチ群はこのリポジトリへ収録していない。

全62ページを描画して一覧確認し、コード・引用・表・参考文献を含む38ページをそれぞれ1440×810で開いて拡大確認した。長い見出し、引用と日本語説明の間隔を修正後に再描画した。参考文献6件は1ページ2件、3ページにまとめ、文献間は36pt以上。編集可能な表15個・グラフ1個を含む。

表168セルの文字欠落・セル内収まり、全タイトルの1行表示、全ページの文字とページ外へのはみ出し、本文と出典の11pt以上の間隔、コード背景の上下約10～11ptの余白を確認した。URLだけに付いたPDFリンク54件、ノート0件、ZIPと内部参照も確認。78 XMLパーツを検査し、SDK許容範囲内の既知の`buSzPct`整数表現以外にスキーマのエラーはなかった。

最後に表紙の主題と副題を共通の中央位置へ調整し、再描画して確認した。その際、他61ページは改訂前とPPTX内のXML・PDF描画が一致することも確認した。確認した最終PPTXから出力したPDFをそのまま納品する。制作・一時確認用コードは共有SKILLに追加していない。

実例関連15ページ（9～11、13、16、38～47）は、内容量に応じてコードと説明のまとまりを下方へ移し、各ページ内の余白を調整した。変更ページはすべて1枚ずつ拡大して再確認した。文章・書式・寸法・リンクは維持し、他47ページのPDF描画も改訂前と一致することを確認した。
