# GPQA：出典と集計条件

2026-10-17の画面・配置の改訂は[横断レビュー](series-layout-and-sites-review.md)を参照。以下の取得失敗や画面・ハッシュの記載は制作時点の記録で、今回再取得した公式画面を優先する。

2026-10-16作成。日本語版「datasets in 10 minutes」。著者はsasakiy84、所属欄なし。本編38ページとAppendix49ページを、一組の編集可能なPPTXと同版のPDFとして収録した。本編は速い読者の約10分の黙読・流し読みを想定し、Appendixは時間に含めない。

## 題材と確認範囲

GPQAを選んだ理由は、GPT・Claude・Gemini系列の現行モデルを含む科学知識の評価で、Diamond版が引き続き使われているため。2026-10-16の公開集約記録で利用と数値を確認した。「現在の全モデルの最高性能」を網羅した順位表ではない。

原著の書誌情報は著者の公式READMEで確認した。論文PDFとモデル提供元サイトの本文は、この環境の接続先制限により取得できていない。作成方法・集合・実例・検証記録については、著者の公式配布物と分析ノートを一次資料として用いた。

## 一次資料

- David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, Samuel R. Bowman (2024). *GPQA: A Graduate-Level Google-Proof Q&A Benchmark*. First Conference on Language Modeling (COLM). https://arxiv.org/abs/2311.12022
- 公式配布リポジトリ：https://github.com/idavidrein/gpqa
- 公式データ：https://github.com/idavidrein/gpqa/blob/main/dataset.zip
- 公式分析ノート：https://github.com/idavidrein/gpqa/blob/main/GPQA_Analysis.ipynb
- OpenAI (2025). *simple-evals*. https://github.com/openai/simple-evals
- GPQA評価実装：https://github.com/openai/simple-evals/blob/main/gpqa_eval.py

公式リポジトリの表示HEADは `56686c06f5e19865c153de0fdb11be3890014df7`。取得したdataset.zipのSHA-256は `461ae7329f15a3e35f8184d2dac24b990f34fdf12f366ca4062d8e6638cd08dc`。

## 集計と実例

公式アーカイブのExtended 546問、Main 448問、Diamond 198問を読み、Record IDの集合についてDiamond ⊂ Main ⊂ Extendedを確認した。これらは独立した学習・開発・テスト分割ではない。

DiamondのHigh-level domainは化学93、物理86、生物19。Subdomainは13区分。質問長はQuestion列の前後の空白を除いたPython文字数で、内部の改行や数式の表記も数える。選択肢を含めない。中央値379.5、最短80、最長1,642文字。ヒストグラムは200文字幅で全198問を含む。

本編に3件、Appendixに重複しない10件の実データを収録した。質問・四つの候補・配布正解・Record IDを対応させ、表示上の選択肢順だけを固定乱数で変更した。空行と一部の数式表記を整えた。日本語の要旨・解説を英語の原文と区別している。配布正解を独自に変更していない。解説は設問と配布解説に基づく。

データのライセンスはアーカイブ内license.txtのCC BY 4.0。リポジトリルートのMITライセンスと区別した。

## モデルの結果

初期のGPT-4（例示なし・推論を促す指示、Diamond 35.7%）は公式分析ノート、GPT-4oの2024-11-20版46.0%とo3-highの83.4%はOpenAI公式simple-evalsの公開表に基づく。同じ設定で再実行した比較ではない。simple-evalsは2025年7月に新モデル・新結果の更新を停止しており、現行モデルの数値の根拠には用いていない。

現行モデルの3例はRichard Donnellのmodel-watchによる二次集約値。2026-10-16 15:46:33 JST生成の公開スナップショットで、Gemini 4 Argon / high 96.4%、GPT-6 Astra / max 95.8%、Claude Sonnet 5.5 / max 95.6%を確認した。

- 集約値：https://github.com/richardadonnell/model-watch/blob/main/data/suggestions.json
- 取得日時などのメタデータ：https://github.com/richardadonnell/model-watch/blob/main/data/latest.json
- 集約実装：https://github.com/richardadonnell/model-watch/blob/main/modelwatch/fetchers/epoch.py
- 集約元：https://epoch.ai/data/benchmarks.csv

集約実装は、同じモデルの試行別mean_scoreを単純平均し、百分率へ換算する。一次CSVは接続先制限で取得できず、個別の試行条件・回数は照合できていない。スライドでは二次集約値として出典と取得日を記した。提供元の自己報告値や、同一プロンプトによる独自測定とは扱わない。本制作で有料モデルAPIを呼び出して評価することはしていない。

補足で紹介したAdam Allcock (2026), *When the Answer Key Is Wrong: A Calibrated Audit of GPQA, MMLU-Pro, and MMMU-Pro, with Corrected Releases*, Zenodo, DOI: 10.5281/zenodo.21613590は、著者公開READMEとPDFを取得した。モデルによる監査を人間による全件認証と混同せず、修正版を元のDiamond 198問とも区別した。https://github.com/adamallcock/answer-key-audit

## 制作と検証

共通SlideMaster.pptxのテーマ・マスター・レイアウトを継承し、例示8枚を除去した。本文、表、番号付き目次、図のデータを編集可能な構造で保持し、発表者ノートは含めていない。転換ページと章扉は、通常タイトルと同じ書体・太字の指定に揃えた。緑帯の章名は既存シリーズと同じ14 ptの太字に統一し、共通マスターのレイアウト・段落既定・空欄末尾にも書式を明示した。マスターから新規スライドを作り、直接のフォント指定なしで緑帯の14 pt太字と転換タイトルの36 pt太字を継承することを確認した。表紙の主題「GPQA」は既存シリーズと同じNoto Sansの56 pt太字に揃え、生成コードの標準ウェイトによる上書きを修正した。表紙の書体と主題名の太字は共通SKILLに明記し、共有マスターから太字を継承することを確認した。表紙の修正時には、表紙以外の描画と全ページの文字内容の一致を確認した。日本語はNoto Sans CJK JP、英数字はNoto Sans、コードはLiberation Mono。数式記号を含む箇所のLatin書体はDejaVu Sansとし、日本語の指定は維持した。

最終PPTXからLibreOfficeでPDFを出力し、全ページを描画して確認した。通常タイトルの1行表示、中央揃え、表の横罫線と余白、原文・コード枠、出典との間隔、URLだけのリンクを確認した。PPTXの段落・表セルとPDFの抽出文字を照合し、ZIP整合性、内部参照、ノート不在、正解の対応も確認した。CSV読み込みコードは配布データに対して実行した。

PresentationML、DrawingML、図表のパーツを、python-pptxのspecに収録されたISO/IEC 29500-4の未変更XSDで照合した。整数表記のbuSzPctに関する字句形式の差が144件あり、その他の構造エラーは0件。字句差を除外して「完全なXSD適合」とは呼ばない。整数値はMicrosoft公式Open XML SDKのBulletSizePercentage定義（Int32Value、25000〜400000）に全件適合することを別に確認した。

- XSD：https://github.com/scanny/python-pptx/tree/master/spec/ISO-IEC-29500-4/xsd
- SDK定義：https://github.com/dotnet/Open-XML-SDK/blob/main/data/schemas/schemas_openxmlformats_org_drawingml_2006_main.json

PowerPointデスクトップでの開封と手動編集は未確認。

2026-10-16の全資料見直しで、推測できる注意書きや重複した免責文を削除し、4ページを削除した。現在は本編38ページ＋Appendix49ページの計87ページ。詳細は[注意書きの見直し記録](slide-editorial-review.md)にまとめた。
