# Data Imputation 独立レビュー

合格・未解決指摘0。54頁の全本文と全54頁の実描画を個別確認した。修正17枠が属する14頁を再度実viewし、27枠の実画素余白も再測定した。最終PDFから54PNGを独立再描画し、表示PNGと全バイト一致した。

公式の元2アーカイブ、HELM固定シナリオ、6stats/6scenario_states、固定IPM README/Multi/Binary、公式metricを別途再取得した。作者保存の該当資料と完全一致。公式シナリオASTで1,515行を再現し、全2,968requestの入力/参照/ID/split/提示数/生成条件を照合した。1,057test出力の4指標を独自の式と公式関数で再計算し、24公開平均値と一致した。Restaurant17/86行の学習表へのclass共有と、提示5例との違いも確かめた。

13全原例は元行の改行を含むバイトhash、元表、公開生成へ一致。native全文/訳/正解、単位・価格・機器名・住所・電話番号・nan・都市表記を照合し、意味対応を確認した。HELM本文と固定実装/公開入力の各+1差、Buy269行のprice欠損残存、5提示/5token/1候補/0温度/改行停止、3/3/1試行を保持する。

修正した指摘はp50の制作過程文の除去、HELM課題2022とIPM研究2021の年の区別、引用17枠の上下実画素余白。年の根拠はarXiv2211.09110v1表紙16Nov2022とE3.12で、Restaurant元表の初公開年は推定しない。Mei論文本文の未取得範囲はsourcesに明記され、手法説明は作者固定README/実装に限り、未読本文の数値は使われない。

監査はlayout333段落122セル問題0、native表12、XSD新規0（既存11を分離）、notes0、全56URL-native run/PDF文字中心でURLだけ。PDF bboxだけで隣接字形を拾う6件は独立に区別し、本文・出典の実描画も確認した。

最終SHAはreview.json/handoff.json、一次取得とデータ照合はnetwork-check.json/more-network-check.json/data-checks.json、native/描画/余白検査はnative-checks.json/render-checks.json/panel-ink-checks.jsonに保存した。
