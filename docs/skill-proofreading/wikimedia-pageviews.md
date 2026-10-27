# Wikimedia Pageviews：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルを使い、作成担当とは別の担当が内容・原レコード・全ページの描画を確認した。保存した編集可能な版の同じページ・native要素へ照合した修正対を示す。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|7|編集操作や、多くの特別ページへの要求は集計から除かれる。|編集操作や、多くの特別ページは除く。検索ページなど一部の特別ページは含む。||
|15|[1] Wikimedia Analytics API. 富士山、2025-09・日次・user。CC0.|[1] Wikimedia Analytics API. 富士山、2025-09・月次・アクセス方法別・user。CC0.||
|20|「富士山」の2025年9月1日分。実際の応答では、日ごとのレコードがitems配列に並ぶ。|「富士山」の1日分。日次レコードはitems配列に並ぶ。||
|26|requestsを導入して実行する。User-Agentの連絡先を自分のものへ変更する。|requestsを導入し、連絡先を自分のものに変更して実行する。||
|34|公式順位|順位||

書式・改行の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|1・4・5・7・8・9・10・11・13・15・16・17・18・19・20・21・22・23・24・25・26・27・29・30・31・32・34・35・36・37・38・39・40|Native frame containment and specified source clearances; title left glyph bearings, code note sizes, and numeric table widths. Text pairs above exclude format-only edits.|

構成・コード・出典の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|23|{"pages": [23], "kind": "page_reconstruction", "reason": "Replace prose-only format explanation and incorrect URL encoding statement with actual hourly dump line, four-column table and UTC end-of-window explanation. Shape identities are not treated as corresponding across this reconstruction.", "before_native": [{"shape_id": 2, "paragraph": 0, "text": "時間別dumpは、1行に1ページの集計を置く"}, {"shape_id": 3, "paragraph": 0, "text": "pageviewsの時間別ファイルは、プロジェクトコード、ページタイトル、閲覧数、第4列の値を空白で区切る。"}, {"shape_id": 3, "paragraph": 1, "text": "ファイル名の日時が、どの1時間を集計したかを表す。ページタイトルはURLエンコードされ、mobileサイトはコードでも分かれる。"}, {"shape_id": 3, "paragraph": 2, "text": "旧形式と互換性を保つ第4列は、現在のpageviewsでは応答容量の測定値として使わない。記事別の回数を読むなら最初の3列が中心になる。"}, {"shape_id": 4, "paragraph": 0, "text": "3. データの作成と配布形式"}, {"shape_id": 5, "paragraph": 0, "text": "[1] Wikimedia Foundation. Data Platform/Data Lake/Traffic/Pageviews."}, {"shape_id": 5, "paragraph": 1, "text": "https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Traffic/Pageviews"}], "after_native": [{"shape_id": 2, "paragraph": 0, "text": "時間別dumpは、1行に1ページの集計を置く"}, {"shape_id": 3, "paragraph": 0, "text": "3. データの作成と配布形式"}, {"shape_id": 4, "paragraph": 0, "text": "af.m Adidas 1 0"}, {"shape_id": 5, "row": 0, "column": 0, "text": "フィールド"}, {"shape_id": 5, "row": 0, "column": 1, "text": "実レコードの意味"}, {"shape_id": 5, "row": 1, "column": 0, "text": "domain_code"}, {"shape_id": 5, "row": 1, "column": 1, "text": "af.m はアフリカーンス語版のmobileサイト"}, {"shape_id": 5, "row": 2, "column": 0, "text": "page_title"}, {"shape_id": 5, "row": 2, "column": 1, "text": "Adidasというページ名。空白は_で表す"}, {"shape_id": 5, "row": 3, "column": 0, "text": "count_views"}, {"shape_id": 5, "row": 3, "column": 1, "text": "その1時間に1回閲覧された"}, {"shape_id": 5, "row": 4, "column": 0, "text": "total_response_size"}, {"shape_id": 5, "row": 4, "column": 1, "text": "0。旧形式に合わせて残る互換列"}, {"shape_id": 6, "paragraph": 0, "text": "20250901-010000のファイルから取得。2025-09-01 01:00 UTCで終わる1時間の集計。"}, {"shape_id": 7, "paragraph": 0, "text": "[1] Wikimedia Foundation. Data Platform/Data Lake/Traffic/Pageviews."}, {"shape_id": 7, "paragraph": 1, "text": "https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Traffic/Pageviews"}]}|
|26|import requests<br>from urllib.parse import quote<br>base = "https://wikimedia.org/api/rest_v1/metrics/pageviews"<br>path = "/per-article/ja.wikipedia/all-access/user/"<br>path += quote("富士山") + "/daily/2025090100/2025093000"<br>headers = {"User-Agent": "my-analysis/1.0 (contact@example.org)"}<br>r = requests.get(base + path, headers=headers, timeout=30)<br>r.raise_for_status()<br>data = r.json()<br>print(data["items"][0]) → import requests; from urllib.parse import quote<br>base = "https://wikimedia.org/api/rest_v1/metrics/pageviews"<br>path = "/per-article/ja.wikipedia/all-access/user/"<br>path += quote("富士山") + "/daily/2025090100/2025093000"<br>headers = {"User-Agent": "my-analysis/1.0 (contact@example.org)"}<br>r = requests.get(base + path, headers=headers, timeout=30)<br>r.raise_for_status()<br>data = r.json()<br>print(data["items"][0])|

[全ページ文言](wikimedia-pageviews/pages.jsonl)・[最終検証票](wikimedia-pageviews/review.json)・[メインの確認](wikimedia-pageviews/main-review.json)
