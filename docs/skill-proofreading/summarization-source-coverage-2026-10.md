# 要約資料：入力本文と要約の対応の見直し

2026-10-20。Codexが制作・データセット紹介・日本語校正スキルで見直した。Geminiは使用していない。修正担当と別の担当が、原データ、訳、要約との対応、変更ページの実際の描画を確認した。旧版の記録は保存している。

全90資料のカタログとPPTX本文の検索から、要約専用5資料と、混合課題FACTS Groundingの要約例を点検した。全90資料の全内容を新たに校正したという意味ではない。

|資料|点検結果と対応|ページ数|変更・確認記録|
|---|---|---:|---|
|CNN / DailyMail|13記事すべてを冒頭1文から記事全文へ。原文・全文訳・参照要約を同じ実例の連続したページで示し、情報選択を説明する。|55→150|[変更前後](cnn-dailymail/source-coverage-2026-10/changes.md)|
|BillSum|13例で本文を拡張。算定式、定義、例外、保存期間まで読める条項を選び、短い法案4件は全文を示す。参照要約は全文を保持する。|72→137|[変更前後](billsum/source-coverage-2026-10/changes.md)|
|EUR-Lex-Sum|13例を目的条項だけから複数の意味ある節へ。対象・措置・手続・条件と参照要約を対応させ、人口統計の代表例では参照全文も示す。|63→153|[変更前後](eurlexsum/source-coverage-2026-10/changes.md)|
|XSum|13例すべて配布document・参照要約の全文を掲載済み。今回の表示不足に当たらず、スライドは変更しない。|69のまま|[原票との照合](xsum/source-coverage-2026-10/input-coverage-audit.json)|
|Multi-LexSum|13例すべて公式Short→Tiny課題の入力Short・参照Tiny全文を掲載済み。今回の表示不足に当たらず、スライドは変更しない。|63のまま|[入力と参照の対応](multilexsum/source-coverage-2026-10/reference-fact-coverage.json)|
|FACTS Grounding|混合課題の要約実例p11–12を追加点検。ハッシュの算出・改変検出・nonceの変更の根拠が掲載段落にあり、表示不足に当たらない。|60のまま|[対象と判断](summarization-source-coverage-2026-10/scope-audit.json)|

本文にない背景が参照要約に含まれる例では、参照を黙って書き換えたり、本文で裏付けられると説明したりしない。本文の追加で確かめられる内容と、参照が補う背景や表現差を区別した。長い原文は段落や条項で分け、改頁にかかる省略表示も保持した。

[全90資料からの対象確認](summarization-source-coverage-2026-10/scope-audit.json)・[統合後のファイル／メタデータ確認](summarization-source-coverage-2026-10/integrated-verification.json)。変更したのは上記3資料のPPTX・PDFで、他87資料のファイルとカタログ行は同一である。作成日時も保持した。

- [CNN / DailyMailの独立レビュー](cnn-dailymail/source-coverage-2026-10/independent-review/handoff.json)
- [BillSumの独立レビュー](billsum/source-coverage-2026-10/independent-review/handoff.json)
- [EUR-Lex-Sumの独立レビュー](eurlexsum/source-coverage-2026-10/independent-review/handoff.json)
