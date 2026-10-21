# ProgramBench 調査記録（2026-10-21）

採用可。13独立課題の公式配布テストを確保。公式バイナリ・テスト・脆弱性コードは実行していない。静的にPython/シェル/小さな参照テキストを抽出して読んだ。

## 一次資料

- Yang et al. (2026), ProgramBench: Can Language Models Rebuild Programs From Scratch? https://arxiv.org/abs/2605.03546 。HTML v1 https://arxiv.org/html/2605.03546v1 （本文内日付August 24, 2026）。保存: paper.html/paper.txt。200 tasks、9モデル、全問完全解決0件、Opus 4.7の95%以上通過が3%。
- 公式GitHub https://github.com/facebookresearch/ProgramBench 。README.md/docs-README.md/LICENSE/tree.json/repo-meta.json保存。SDK MIT、task_cleanroom_v6が推論環境、task_v6が評価環境、linux/amd64。
- 公式HF https://huggingface.co/datasets/programbench/ProgramBench-Tests 。hf-readme.md/hf-meta.json保存。200 task、AI生成pytestテストは公開。生成者にはsource/testアクセスがある。task workerにはテストを渡さない。HF全体tag MITだが各taskのATTRIBUTION/LICENSEが元repo由来部分の条件を定める。
- 公式トップ https://programbench.com 。website.html保存。
- 最新採用: /tmp/fable-card.txt の8.11.1/8.13.1。200のうちreference binaryがhidden testsで0.9未満の34を除き166、referenceが通るtestのみ採点、mini-swe-agentで6時間制限なし。Fable 5.1 87.6%、Opus 5 85.4%、Fable 5 86.3%。200課題全体の完全解決率とは別指標。

## 課題と評価

入力はgold executableとその使用文書。提出はsource codeとbuild scriptでcandidate executableを作るcodebase。実装言語・構造は自由。ネット禁止。goldを任意入力で動かしてstdout/stderr/exit code/filesystem effectsを調べられるblack-box accessを与える。decompilation不可、goldを読む/複製する/包むのは不可。

テストはsourceの一致ではなく外部動作を見る。全プログラムを一律byte exactで比較する仕様ではない。配布テストはexact bytes、substring、parsed JSON、ファイル内容、エラー、メディア処理など個別assertで定義される。決定的な観測可能動作を仕様とする設計。採点の完全解決は各課題の全testを通すこと。テストが有限なので全入力での等価性を証明するものではない（この一般論を本文で重ねない）。

構築: compiled-language/open source repo候補→agentでビルド→source/existing tests/docsを参照してcoverage-guided test生成・既存behavioral tests収集→goldで決定的に通るか/弱いassert/空のdummyで通らないか確認→source/tests/build artifacts除去。構築agent Sonnet 4.5 + mini-SWE-agent、Ubuntu22.04。workerにはsourceもtestsも渡さない。

## 実例

selected-examples.jsonに13課題から1個ずつの実テスト関数（ファイル/行/全文）を保存。test-index.jsonには抽出した6082関数のindex。tasks/<task>/{task.yaml,tests.json,<archive>.tar.gz,ATTRIBUTION.md,LICENSE,static-tests/}。

本編候補: jqのJSON filter 5→6、ripgrepのliteral string検索、SQLiteのJSON出力。追加候補: xsv CSV行数、sd空pattern置換、DuckDB csv-mode初期化、zstd roundtrip、FFmpeg stdin、PHP argv、yj YAML→JSON、fd深さ制限、hexyl 16進表示、gron JSON展開。13課題は重複しない。

引用する期待出力はassertの強さを保持する。substringを厳密な全出力として示さない。gronは別添goldenを静的抽出済み。zstd fixtureは Hello, World! を100回反復。課題の解答はtest入力への単発出力ではなく、これらを含む振る舞いを実装するcodebaseだと先に説明する。


## 最終追記

2026-10-21の公式トップをCSS適用済みの画面として取得。最新の公開表はOpus5 xhigh 4.5/37.0%、MuseSpark1.3max 2.5/25.0%、GPT5.6Solxhigh1.0/15.5%（完全解決率/95%以上通る課題割合）。原著の248,853test functionsを本文に採用。Fable cardはrootが過去に取得済みのPDF `/workspace/artifacts/frontier-benchmarks-2026-10/fable-5-1-system-card.pdf` と /tmp/fable-card.txt を継承。正規landingは https://www.anthropic.com/claude-fable-and-mythos-5-1 。PDF原URLは https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf 。本担当はcard URLを再取得していない。

jq初期選択branchのmoduleがgold_failであるとの独立reviewを受け、追加取得した53795949a2d6 archiveの名前付き変数の実testへ変更。13選択関数は独立reviewerが別途取得しAST一致を確認。FFmpeg test.mp4は静的mvhdヘッダ解析で2秒と確認（ffmpeg-input-audit.json）。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-programbench.pptx)・[PDF](../slides/datasets-in-10-minutes-programbench.pdf)。本編25頁、総42頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/programbench.json)・[校正の修正対](skill-proofreading/programbench.md)・[全ページ文言](skill-proofreading/programbench/pages.jsonl)・[最終検証票](skill-proofreading/programbench/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-burntsushi__ripgrep.txt](licenses/programbench/LICENSE-burntsushi__ripgrep.txt)、[ATTRIBUTION-burntsushi__ripgrep.md](licenses/programbench/ATTRIBUTION-burntsushi__ripgrep.md)、[LICENSE-burntsushi__xsv.txt](licenses/programbench/LICENSE-burntsushi__xsv.txt)、[ATTRIBUTION-burntsushi__xsv.md](licenses/programbench/ATTRIBUTION-burntsushi__xsv.md)、[LICENSE-chmln__sd.txt](licenses/programbench/LICENSE-chmln__sd.txt)、[ATTRIBUTION-chmln__sd.md](licenses/programbench/ATTRIBUTION-chmln__sd.md)、[LICENSE-duckdb__duckdb.txt](licenses/programbench/LICENSE-duckdb__duckdb.txt)、[ATTRIBUTION-duckdb__duckdb.md](licenses/programbench/ATTRIBUTION-duckdb__duckdb.md)、[LICENSE-facebook__zstd.txt](licenses/programbench/LICENSE-facebook__zstd.txt)、[ATTRIBUTION-facebook__zstd.md](licenses/programbench/ATTRIBUTION-facebook__zstd.md)、[LICENSE-ffmpeg__ffmpeg.txt](licenses/programbench/LICENSE-ffmpeg__ffmpeg.txt)、[ATTRIBUTION-ffmpeg__ffmpeg.md](licenses/programbench/ATTRIBUTION-ffmpeg__ffmpeg.md)、[LICENSE-jqlang__jq.txt](licenses/programbench/LICENSE-jqlang__jq.txt)、[ATTRIBUTION-jqlang__jq.md](licenses/programbench/ATTRIBUTION-jqlang__jq.md)、[LICENSE-php__php-src.txt](licenses/programbench/LICENSE-php__php-src.txt)、[ATTRIBUTION-php__php-src.md](licenses/programbench/ATTRIBUTION-php__php-src.md)、[LICENSE-sclevine__yj.txt](licenses/programbench/LICENSE-sclevine__yj.txt)、[ATTRIBUTION-sclevine__yj.md](licenses/programbench/ATTRIBUTION-sclevine__yj.md)、[LICENSE-sharkdp__fd.txt](licenses/programbench/LICENSE-sharkdp__fd.txt)、[ATTRIBUTION-sharkdp__fd.md](licenses/programbench/ATTRIBUTION-sharkdp__fd.md)、[LICENSE-sharkdp__hexyl.txt](licenses/programbench/LICENSE-sharkdp__hexyl.txt)、[ATTRIBUTION-sharkdp__hexyl.md](licenses/programbench/ATTRIBUTION-sharkdp__hexyl.md)、[LICENSE-sqlite__sqlite.txt](licenses/programbench/LICENSE-sqlite__sqlite.txt)、[ATTRIBUTION-sqlite__sqlite.md](licenses/programbench/ATTRIBUTION-sqlite__sqlite.md)、[LICENSE-tomnomnom__gron.txt](licenses/programbench/LICENSE-tomnomnom__gron.txt)、[ATTRIBUTION-tomnomnom__gron.md](licenses/programbench/ATTRIBUTION-tomnomnom__gron.md)、[LICENSE-ProgramBench-MIT.txt](licenses/programbench/LICENSE-ProgramBench-MIT.txt)。
