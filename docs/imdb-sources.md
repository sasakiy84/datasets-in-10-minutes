# IMDb：出典と制作・校正記録

2026-10-17作成。本編31ページ、Appendix22ページ、合計53ページ。本編約10分の黙読・流し読みを想定し、閲覧時間は未実測。完全版PPTXと、その最終改訂から出力したPDFを保存した。

## 出典と版

|資料|用途|
|---|---|
|[Learning Word Vectors for Sentiment Analysis](https://aclanthology.org/P11-1015/)|Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts / ACL 2011。目的、作成方法、初期評価。|
|[公式公開ページ](https://ai.stanford.edu/~amaas/data/sentiment/)|2026-10-17に取得。CSS・フォントを読み込んだ実画面を冒頭に掲載。|
|[stanfordnlp/imdb](https://huggingface.co/datasets/stanfordnlp/imdb)|改訂 `e6281661ce1c48d982bc483cf8a173c1bbeb5d31`。掲載例の原文、正解、全件集計を照合。|
|[HELM Classic v0.4.0](https://crfm.stanford.edu/helm/classic/v0.4.0/)|指定URLのlatestが指す2023-11-17の評価版。公開スキーマ、run_specs、各実行のstatsを取得。|
|[HELMの2023年コード](https://github.com/stanford-crfm/helm/tree/v0.3.0/src/helm/benchmark)|公開リリースが参照する基礎suite v0.3.0のシナリオとadapterを確認。|

## 内容・実例・評価の照合

ラベルはレビュー全体の評点から決まること、5点・6点の除外、学習とテストの映画の非共有を説明した。「最悪」という語を含む肯定例と、好きな点を挙げる否定例を本編に置いた。HELMのvalidは元のtestだけではなく対照例のある元trainも含む。ミラーのlicenseメタデータはotherで、特定のCCライセンスを推定していない。

本編3件、追加10件の独立した公開実例を掲載した。原文と日本語訳は対応する文・段落を同じページで読める配置にした。複数ページにまたがっても同じ実例は1件と数える。選択の記録、原文、訳、識別子とレコードハッシュは[検証データ](data-audits/imdb.json)に保存する。

HELMの得点は集約表示だけに頼らず、canonical実行の指標、split、モデル、例題数、試行数を実行別statsで照合した。この資料の値は3実行について検査し、丸めた表示値まで一致した。XSumはCPUで指標を計算した実行だけを使い、validとtestを混ぜていない。2023年の固定評価版であり、最新モデル順位の網羅を示していない。

## 全件集計と容量

集計対象は `test` の全25,000件。入力の語数は空白区切りで、平均228.53、中央値172.0、母標準偏差168.88、最小4、最大2278だった。質問と段落、本文と要約などは混ぜていない。文字列のHTMLや表示文も、配布レコードの一部として保持した。

取得したファイルのbytes・SHA-256と、配布ミラーの固定改訂を[検証データ](data-audits/imdb.json)に記録した。取得した分割の容量と、全分割の配布容量を混同せず、未取得の全データを実測済みとはしていない。

## 日本語校正と最終検査

**Geminiは使用していない。** リポジトリの[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)をCodexが適用し、1ページずつ最終文言と意味を確認した。[変更対](skill-proofreading/imdb/changes.tsv)、[全ページの最終文言](skill-proofreading/imdb/pages.jsonl)、[検査・描画確認の記録](skill-proofreading/imdb/review.json)を残す。

全53ページを描画し、一覧で構成を確認した後、引用・コード・表・参考文献を含むページは1ページずつ拡大確認した。文字欠落、引用・表セルのはみ出し、本文と出典の間隔、URLだけのリンク範囲を検査した。修正箇所は再出力して確認し、PPTXとPDFのハッシュを記録した。

OOXML検査はスライドだけでなく、マスター、レイアウト、表、内部参照、図形IDも対象にした。標準XSDで新規の構造エラーは0件。マスター由来の既存11件と、buSzPctの整数表記に関するXSDと実装の差は分離し、整数値25000–400000を別に検査した。[BulletSizePercentageの定義](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.bulletsizepercentage)を参照し、XSD自体は変更していない。PowerPointでの手動開封は実施せず、LibreOfficeによる変換とネイティブの編集構造を検証した。

## 2026-10-18：原文をまとめることを優先

原文の表示範囲を1枚にまとめることを優先し、訳は少し小さい文字や配置の調整で併記できる場合のみ同じページにした。併記できない場合は原文と訳を別ページに分けた。原文自体が長い場合のみ意味の区切りで分割し、見出しと説明、入出力の対を保った。この追補を、それ以前の原文・訳の併記方針より優先する。[旧・現ページの対応と実例ハッシュ・検査記録](skill-proofreading/imdb/original-first-review.json)。Codexによるスキル適用、Gemini使用なし。
