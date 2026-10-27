# MediaWiki History：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルを使い、作成担当とは別の担当が内容・原レコード・全ページの描画を確認した。保存した編集可能な版の同じページ・native要素へ照合した修正対を示す。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|13|2026-09版は78列。利用者の変更イベントでは、ページ・版の列は空欄になる。|2026-09版は78列。名前空間は、記事・カテゴリなどのページの用途を表す。利用者イベントでは、ページ・版の列は空欄になる。|名前空間の役割を初出で説明する。|
|16|編集回数の累計や直前の編集からの秒数もあり、編集のたびに増える回数や編集間隔を分析できる。|編集回数の累計や直前の編集からの秒数もあり、編集活動の量や編集間隔を分析できる。|累計回数の説明を自然な文にする。|
|25|本文を集める用途と違い、最初から全言語・全期間を取得する必要はない。対象のウィキと分析期間を決めて始められる。|必要なウィキと分析期間を選んで取得できる。小規模なウィキを選べば、全履歴の読み込みや集計を手元で試しやすい。|本文配布との根拠のない比較を除き、小規模wikiを選ぶ利点を説明する。|
|36|利用者イベントは同じ78列に入るが、ページIDと版IDは空欄になる。ここでは利用者名やIDを表示せず、イベントの構造を示した。|利用者イベントは同じ78列に入るが、ページIDと版IDは空欄になる。変更の対象となった利用者の情報は、user_で始まる列に入る。|制作上の表示判断を、利用者イベントの列の説明に替える。|
|37|差し戻されるまでの時間|差し戻しまでの時間|表セルの末尾1字だけの改行を解消する。|

書式・改行の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|1・30|Native title frames expanded4pt; cover bottom margin4pt retains original visible position; Appendix top−2pt.|
|9|NumericID column and header right-aligned.|
|10・23・24・26|Content/body/code/note font and spacing adjusted for readable source gap.|
|24|Horizontal chart ticks every10000.|

構成・コード・出典の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|6|event_entity / event_type revision / create → event_timestamp          2005-07-11 15:16:49.0|
|6|wiki_db                  nawiki → event_entity / event_type revision / create|
|6|revision_id / parent_id   6835 / 6825 → revision_parent_id       6825|
|6|event_timestamp          2005-07-11 15:16:49.0 → revision_id              6835|
|26|from collections import Counter → path = "2026-09.nawiki.all-time.tsv.bz2"|
|26|with bz2.open(path, "rt", encoding="utf-8") as f: →                       quoting=csv.QUOTE_NONE)|
|26|counts = Counter() →     rows = csv.reader(f, delimiter="\t",|
|26|                          quoting=csv.QUOTE_NONE): → print(n)|
|26|    for row in csv.reader(f, delimiter="\t", →     n = sum(r[2:4] == ["revision", "create"] for r in rows)|
|26|path = "2026-09.nawiki.all-time.tsv.bz2" → with bz2.open(path, "rt", encoding="utf-8") as f:|
|18|[1] Wikimedia Foundation, 2026. MediaWiki History配布ディレクトリ（参照2026-10-28）  https://dumps.wikimedia.org/other/mediawiki_history/ → [1] Wikimedia Foundation, n.d. MediaWiki history dumps（参照2026-10-28）|

追加した内容は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|10|[2] Wikimedia Foundation, n.d. MediaWiki Content File Exports（参照2026-10-28）  https://wikitech.wikimedia.org/wiki/MediaWiki_Content_File_Exports|
|18・28|https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Edits/MediaWiki_history_dumps|
|18|[2] Wikimedia Foundation, 2026. MediaWiki History配布ディレクトリ（参照2026-10-28）  https://dumps.wikimedia.org/other/mediawiki_history/|
|28|[2] Wikimedia Foundation, n.d. MediaWiki history dumps（参照2026-10-28）|

削除した内容は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|26|{"page": 26, "element": ["paragraph", 4, 7], "before": "        counts[(row[2], row[3])] += 1"}|
|26|{"page": 26, "element": ["paragraph", 4, 8], "before": "print(counts[(\"revision\", \"create\")])"}|

[全ページ文言](mediawiki-history/pages.jsonl)・[最終検証票](mediawiki-history/review.json)・[メインの確認](mediawiki-history/main-review.json)
