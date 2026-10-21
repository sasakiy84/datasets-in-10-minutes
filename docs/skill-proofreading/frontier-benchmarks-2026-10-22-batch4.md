# 新規8件の制作・校正・独立レビュー（2026-10-22）

未解説の8件を追加した。各資料は概要・実例・構築方法・採点・利用方法を説明し、本編の流し読みを600秒として設計した。時間は未実測。主な実例3件とAppendix10件で、計104件の異なる公開実例を扱う。

|資料|本編|総頁|出典・利用条件|修正前後と最終確認|
|---|---:|---:|---|---|
|BrowseComp|25|50|[一次資料](../browsecomp-sources.md)|[修正対](browsecomp.md)・[最終検証票](browsecomp/review.json)|
|ArXivMath|27|60|[一次資料](../arxivmath-sources.md)|[修正対](arxivmath.md)・[最終検証票](arxivmath/review.json)|
|SWE-bench Multilingual|25|50|[一次資料](../swe-bench-multilingual-sources.md)|[修正対](swe-bench-multilingual.md)・[最終検証票](swe-bench-multilingual/review.json)|
|HealthBench|39|75|[一次資料](../healthbench-sources.md)|[修正対](healthbench.md)・[最終検証票](healthbench/review.json)|
|Mind2Web|26|52|[一次資料](../mind2web-sources.md)|[修正対](mind2web.md)・[最終検証票](mind2web/review.json)|
|MMLU-Pro|27|52|[一次資料](../mmlu-pro-sources.md)|[修正対](mmlu-pro.md)・[最終検証票](mmlu-pro/review.json)|
|DeepSWE|38|100|[一次資料](../deepswe-sources.md)|[修正対](deepswe.md)・[最終検証票](deepswe/review.json)|
|Terminal-Bench-Science 0.1|34|83|[一次資料](../terminal-bench-science-sources.md)|[修正対](terminal-bench-science.md)・[最終検証票](terminal-bench-science/review.json)|

## 確認したこと

Geminiや他の外部生成APIは使わず、ローカルのスライド制作・日本語校正・実例設計スキルを使った。作成者と異なる担当が一次資料、実例原票、日本語、翻訳、全ページの描画を確認し、メインが指摘への対応と最終成果物を確認した。担当を分けた場合の自身の確認範囲と他担当から継承した範囲は、各検証票に区別して記録した。変更後は変更頁を開き直し、変更しなかった頁は担当自身の画像ピクセル比較で対応を確認した。

原文は全文を優先し、17–18pt程度で1頁に収まるかを確認した。短い例は日本語と同じ頁に収め、長い例は意味のまとまりで分けた。Terminal-Bench-Scienceの日本語は全文訳ではなく「日本語の要点」と明記した。正解・期待動作はテーマの赤色で大きく表示した。参考文献は原則1頁2件とし、出典名、URL、寄与を記した。

HealthBenchでは得点の分母を、すべての加点基準を満たす場合の点数として明確にした。ArXivMathでは元論文と正解が一致しない候補を除き、別の公開例へ差し替えた。BrowseCompでは条件に曖昧さのある例を差し替え、Mind2Webでは画像・依頼・操作履歴が整合する実例を選び直した。MMLU-Proでは計算例を再計算し、指示文による「変動幅」を標準偏差と混同しないようにした。DeepSWEでは依頼だけでなく配布テストが確かめる動作を読み、Terminal-Bench-Scienceでは実CSVの1,293観測から光度曲線を作図した。

異なるバージョン、評価時期、エージェント、試行数のスコアは条件を区別した。モデルを実行した評価は行っていない。PPTXは編集可能なテキスト・表・コードを使い、PDFはLibreOfficeで変換して実際の描画を確認した。科学図は実データから標準作図ツールで生成した。Microsoft PowerPointでの確認は行っていない。

既存99件のカタログ行とPDF/PPTX198ファイルは、作業開始時の状態と照合して保持した。各データセットを1件ずつコミットし、作成日時・更新日時をGitの履歴から復元してギャラリーへ追加した。

## ローカル検証と公開

Pythonテスト4件とギャラリーのNodeテストが成功した。ギャラリーを構築し、107件の掲載、新規8件のサムネイル、16配布ファイルとカタログの対応を確認した。詳細は[ローカル検証](frontier-benchmarks-2026-10-22-batch4/local-verification.json)に記録する。公開先の確認結果は[公開検証](frontier-benchmarks-2026-10-22-batch4/publication-result.json)に記録する。

資料ごとのコミットは[対応表](frontier-benchmarks-2026-10-22-batch4/dataset-commits.json)に記録した。ブラウザーでは作成日時降順のクエリ、タイトル検索と更新日時降順の組合せ、リセット後107件表示を確認した。新規8件のサムネイルと[作成日時降順の画面](frontier-benchmarks-2026-10-22-batch4/gallery-created-desc.png)・[検索結果](frontier-benchmarks-2026-10-22-batch4/gallery-science-query.png)を実際に開いて確認した。
