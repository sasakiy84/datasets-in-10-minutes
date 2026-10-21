# 最新モデルの評価で使われる未解説ベンチマーク3件（第3回）

2026-10-21、既存96資料との重複を確認し、DRACO、ProgramBench、Global-MMLUの資料を作成した。CLEVA系列は対象に含めていない。Geminiや外部のモデルAPIは使わず、ローカルの制作・日本語校正スキルで作成した。

[Claude Fable 5.1・Mythos 5.1の公式発表](https://www.anthropic.com/claude-fable-and-mythos-5-1)に対応するSystem Cardで、3件の継続採用を確認した。カードのPDFは前回作業で公式CDNから取得したものを継承し、該当節を今回の担当が読み直した。今回の直接HTTP取得は403となったため、取得していない再ダウンロードを実施済みとは記録していない。公式発表のWebインデックスも今回確認した。

モデル発表は採用の根拠として参照し、資料の主題は各データセットの課題、実例、作成、評価、利用と入手方法に置いた。

|資料|扱う課題|本編／総ページ|独立した公開実例|配布物と修正対|
|---|---|---:|---:|---|
|DRACO|出典付きの調査レポートを専門家の基準で評価する|37／91|13|[PDF](../../slides/datasets-in-10-minutes-draco.pdf)・[PPTX](../../slides/datasets-in-10-minutes-draco.pptx)・[修正対](draco.md)|
|ProgramBench|実行ファイルの動作を調べ、同じ動作のコードベースを作る|25／42|13|[PDF](../../slides/datasets-in-10-minutes-programbench.pdf)・[PPTX](../../slides/datasets-in-10-minutes-programbench.pptx)・[修正対](programbench.md)|
|Global-MMLU|42言語の知識問題と文化への依存性を分析する|33／55|13|[PDF](../../slides/datasets-in-10-minutes-global-mmlu.pdf)・[PPTX](../../slides/datasets-in-10-minutes-global-mmlu.pptx)・[修正対](global-mmlu.md)|

本編は資料ごとに600秒で流し読みする予定として設計した。閲覧時間は実測していない。各資料に、本編3例と追加10例を収録した。同じ問題の異言語訳や複数ページへの分割は、別の例として数えていない。Global-MMLUは、既存のOpenAI MMMLUと翻訳工程・対象言語・文化注釈が異なる研究として説明した。小規模な派生版Liteは、初期の15言語から2026年5月のバージョン3.0で23言語へ増えている。現在の配布カードと各言語ファイルを照合し、各400問・総9,200レコードを確認して補足を更新した。42言語の本体と混同しない構成にした。

## 内容と表示の確認

作成担当とは別の担当が、原票・出典・日本語・PPTX構造・PDFを確認した。全188ページを分担して一枚ずつ画像で開き、修正後は変更ページを再確認した。不変ページを継承した場合は、対応する確認済み版と最終版の画素一致を確かめた。担当ごとの実施範囲と継承範囲、最終ファイルの対応を資料別の最終検証票に残した。

DRACOは、13例の原文と日本語訳、掲載した26基準と負の重みの例を配布レコードへ照合した。長い原文は全文を保ち、意味の切れ目で分割した。ProgramBenchは公開テストを静的に読み、入力・期待動作・除外指定と個別ライセンスを照合した。元の実行ファイルやテストは実行していない。Global-MMLUは、13問の原文・全選択肢・正解・文化注釈を固定した配布版へ照合し、必要な文化語の説明を実例のそばに置いた。

全ページの文字・表・リンク、発表者ノートがないこと、著者名、文字枠内とページ内の収まりを確認した。PPTXは編集可能な本文・表・コードを持つ。Microsoft PowerPointでの実開封と、新たなモデル評価は行っていない。

画像表示ツールで一部の章名や文字が欠けたように見える箇所は、PDFの実際の文字・字形座標、PNG画素、拡大画像と突き合わせた。表示側の症状と、実ファイルにある文字欠落を区別して記録した。

[選定記録](frontier-benchmarks-2026-10-21-batch3/selection.json)・[メインの確認範囲](frontier-benchmarks-2026-10-21-batch3/main-review-progress.json)・[ローカル検証](frontier-benchmarks-2026-10-21-batch3/verification-local.json)。各資料の校正表と検証票に、実際の修正前後の文言と理由を残した。

ProgramBenchの元プロジェクトのライセンスは原文を保持した。2ファイルの元からある末尾空白は原文保存を優先し、その他の新規文書はGitの空白検査を通した。

## 公開

ローカルのギャラリービルドは99件で成功した。新規6ファイルが最終検証済み版と一致し、表紙サムネイル3枚も確認した。GitHub Actionsのビルド・テスト・デプロイが成功した。公開先から3件のPDF・PPTXとカタログの計7ファイルを取得し、すべてHTTP 200かつ固定した最終版と一致することを確認した。

[公開確認](frontier-benchmarks-2026-10-21-batch3/publication-result.json)・[配布版の固定](frontier-benchmarks-2026-10-21-batch3/publication-frozen.json)・[デプロイ結果](https://github.com/sasakiy84/datasets-in-10-minutes/actions/runs/39610850949)・[ギャラリー](https://datasets-in-10-minutes.sasakiy84.net/)。
