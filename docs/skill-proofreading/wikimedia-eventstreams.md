# Wikimedia EventStreams：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルを使い、作成担当とは別の担当が内容・原レコード・全ページの描画を確認した。保存した編集可能な版の同じページ・native要素へ照合した修正対を示す。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|10|30件の短い受信サンプルに含まれた例。Wikipediaの記事本文だけを対象としたサービスではない。|30件の受信サンプルから、異なる4つのWikiを示した。|Remove repetition and keep sample scope|
|16|File:Train mw.jpgの説明ページの例。7,467 − 7,416 = 51 bytes。何が追記されたかを読むには、旧版と新版の内容を別に取得する。|File:Train mw.jpgの説明ページの例。7,467 − 7,416 = 51 bytes。変更内容を読むには、旧版と新版の内容を別に取得する。|Net byte increase does not imply append-only edit|
|25|5件受信するか、5秒経過すると接続を閉じる例。コンソールへWiki名と変更の種類を出す。|5件または5秒で終了し、Wiki名と変更の種類を出す。|Shorten acquisition note without changing limit|

書式・改行の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|1・5・12・22・25・27・29・34|Cover alignment; frame/row heights, table width and source clearances. Code/example/bibliographic content changes are separated above.|

内容・コード・出典の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|1|Same title converted to two truly centered paragraphs|
|5|Separate length.old/new rows; omit bot from this table. Same cells across changed field roles are not paired as Japanese edits.|
|12|Opaque SSE id omitted; data contains only wiki/type, exactly preserved from actual event; caption states omission.|
|14|Add official service source for SSE resume timestamp role|
|15|Add official service source for resume position role|
|28|Remove paragraph describing production choices|
|35|Ignore initial empty NDJSON line and stop after five JSON objects; usage note updated|
|38|Use full formal title read from 2018 Diff heading, rather than shortened home-page anchor|
|34|2026-10-27に取得した先頭6件。複数の配信元や種類を合わせて受信するため、必要な処理では時刻やイベントを識別する値も使う。 → 2026-10-27に取得した先頭6件。時刻は各変更のtimestampから変換した。|

[全ページ文言](wikimedia-eventstreams/pages.jsonl)・[最終検証票](wikimedia-eventstreams/review.json)・[メインの確認](wikimedia-eventstreams/main-review.json)
