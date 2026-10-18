# CNN / DailyMail 独立レビュー

判定: 修正確認後、承認。

固定Parquetと13の原文・参照要約・表示範囲・ID・URL SHA-1を独立照合。HELM v0.3.0実装の空白区切り512語、提示候補50–150語、5提示例、3試行、1候補、最大128トークンと停止文字列を確認した。3,000件のrequest_statesから各試行valid534/test466を実数で数えた。id16576の114語本文と参照要約をHF test row586に一致させ、単一例のROUGEとtest466記事×3試行を別実装呼び出しで再計算し、公開statsと1e-12以内で一致した。

重要44ページを実際にview_imageで拡大確認した。全13実例のEN/JP、実生成と入力全文、全native表、chart、コード、公式画面、参考文献を含む。残る本文をページ単位で通読した。

指摘CNNDM-01: p59の生成条件に候補数が未記載だったため、num_outputs=1を明記するよう依頼。担当が「1候補 / temperature 0.3 / 最大128トークン」へ修正し、実画像で収まりと内容を確認した。最終handoffのPPTX/PDFハッシュと再監査（layout0、XSD新規0、URL65本完全一致）を確認。未解決の指摘なし。

詳細はreview.json、独立計算はcontent-checks.json、再現コードはcheck.py。
