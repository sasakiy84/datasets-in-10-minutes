# SWE-bench Multilingual：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルで作成し、作成担当とは別の担当が内容・原票・描画を確認した。以下は実際に行った修正の対である。最終版の確認範囲とファイルの対応は検証票に記録した。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|10|期待動作：第2引数にerrorInfoを渡す|期待動作：コールバックの第2引数にerrorInfoを渡す|useErrorBoundary自体の引数とコールバックの引数を区別する。独立source reviewで指摘。|
|全体|Psr\\Clock\\ClockInterface / Carbon\\FactoryImmutable|Psr\Clock\ClockInterface / Carbon\FactoryImmutable|引用されたコード識別子を元Issueと同じ単一backslashにする。|
|17|実際のIssueと、解決したPull Requestを組にする|Issueと解決したPull Requestを組にする|通常タイトルを1行に収め、不要な修飾を除く。|
|32,33|テンプレートの区切りを読めるようにする|テンプレートの区切りを認識する|原文/日本語ラベル付きでも1行で読めるように短くする。|

[全ページ文言](swe-bench-multilingual/pages.jsonl)・[最終検証票](swe-bench-multilingual/review.json)・[メインの確認](swe-bench-multilingual/main-review.json)
