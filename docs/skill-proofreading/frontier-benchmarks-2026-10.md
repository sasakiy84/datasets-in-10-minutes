# 最新モデルの評価で使われる未解説ベンチマーク3件

2026-10-20、既存90資料と公式のモデル評価資料を照合して、ARC-AGI-3、GDPval、BenchCADを選定した。CLEVA系列は今回の制作対象に含めない。モデルAPIやGeminiは使用せず、公開一次資料・配布データ・公式評価実装を調べ、ローカルの制作・日本語校正スキルを適用する。

|対象|解説する課題|採用を確認した公式モデル資料|
|---|---|---|
|ARC-AGI-3|初めて見るゲームを操作し、規則や目標を学びながら解く|[GPT-6 Astra](https://openai.com/index/gpt-6-astra/)|
|GDPval|業務上の指示と添付資料から、文書や表などの成果物を作る|[Claude Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) のGDPval-AA v2|
|BenchCAD|複数方向の画像から、実行できるCADプログラムで立体形状を再構成する|[GPT-6 Astra](https://openai.com/index/gpt-6-astra/)|

各資料の主題はベンチマークの内容・構築・評価・使い方であり、モデルの発表内容の解説ではない。最新モデルの評価資料は、現在の利用を確認する根拠として参照した。制作担当と独立レビュー担当を対象ごとに分け、最終ファイルの確認と統合はメインが行う。

評価条件の確認では、ARC-AGI-3のバージョン・履歴管理・人間の行動数による基準、GDPval本体とGDPval-AAの評価方法・公開参照成果物の対応、BenchCADのバージョン・入力解像度・ツール利用・採点実装の変更を個別に照合する。スライドでは結果の解釈に必要な条件を示し、チェックサムなどの制作記録はスライド外へ残す。

## 制作物と確認範囲

|資料|本編／総ページ|実例|配布物|出典と検証・修正記録|
|---|---:|---|---|---|
|ARC-AGI-3|32／50|13ゲーム。操作列と実画面、成功・失敗を区別|[PDF](../../slides/datasets-in-10-minutes-arc-agi-3.pdf)・[PPTX](../../slides/datasets-in-10-minutes-arc-agi-3.pptx)|[出典](../arc-agi-3-sources.md)・[修正対](arc-agi-3.md)・[最終票](arc-agi-3/review.json)|
|BenchCAD|42／70|13部品に編集・数値QAを加えた15例|[PDF](../../slides/datasets-in-10-minutes-benchcad.pdf)・[PPTX](../../slides/datasets-in-10-minutes-benchcad.pptx)|[出典](../benchcad-sources.md)・[修正対](benchcad.md)・[最終票](benchcad/review.json)|
|GDPval|45／129|13職種・9産業の実務依頼と参照成果物|[PDF](../../slides/datasets-in-10-minutes-gdpval.pdf)・[PPTX](../../slides/datasets-in-10-minutes-gdpval.pptx)|[出典](../gdpval-sources.md)・[修正対](gdpval.md)・[最終票](gdpval/review.json)|

本編の流し読みは各600秒を予定して構成したもので、閲覧時間は実測していない。長い実務の依頼は原文を補足に全文掲載し、日本語の要点と区別した。PDFと編集可能なPPTXを同じ最終版で配布する。

作成者以外の担当が、一次資料、配布原票、評価実装、全ページの日本語・表・コード・出典を確認した。全249ページについて独立担当による実画像の個別確認がある。修正後は変更ページを再表示し、変更のないページは既確認画像との画素一致などを照合した。最終票では、今回自ら確認した範囲と過去の確認を引き継いだ範囲を区別した。メインもARC-AGI-3の15ページ、BenchCADの16ページ、GDPvalの14ページを個別に確認し、最終ファイルとの対応は各メイン確認票に記録した。

誤った数値、評価条件の混同、原文の欠落、長文の不自然なページ分割、画像内の文字切れ、出典との接近などを修正した。校正はローカルの日本語校正スキルによるもので、Geminiや外部モデルAPIによる提案ではない。修正前後の文言と理由、原票との照合、実施した確認の範囲を資料ごとの記録に残した。PowerPoint本体での開封と閲覧時間の実測は未実施。

[選定記録](frontier-benchmarks-2026-10/selection.json)・[メインの初期内容レビュー](frontier-benchmarks-2026-10/main-preliminary-content-review.json)。既存90資料のファイルと既存90行のメタデータを保持し、新規3件だけを追加した。資料ごとにmainへコミットする。
