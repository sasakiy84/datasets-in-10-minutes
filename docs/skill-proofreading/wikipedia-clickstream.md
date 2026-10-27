# Wikipedia Clickstream：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルを使い、作成担当とは別の担当が内容・原レコード・全ページの描画を確認した。保存した編集可能な版の同じページ・native要素へ照合した修正対を示す。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|15|typeは参照元とリンクの関係を示す|typeは参照元と移動先の関係を示す|参照元と移動先という列間の関係を題名にする。|
|17|Wikimediaのアクセス記録から、ページ閲覧と判定され、人間からのアクセスに分類されたものを集計する。|Wikimediaのアクセス記録から、ページ閲覧と判定されたものを選び、既知のボットなどの自動アクセスを除いて集計する。|アクセス分類を、人間の確定ではなく自動アクセスを除く処理として説明する。|
|21|リンクが存在することと、そのリンクが実際にたどられた回数を対応させられる。|リンクの有無と、参照元の記事から移動先の記事への遷移回数を対応させられる。|HTTP参照元の集計を、個々のクリックの厳密な証明として言い切らない。|
|22|公開されるのは月間の組と回数である。A→BとB→Cの行があっても、同じ読者のA→B→Cという連続した経路は復元できない。|公開されるのは月間の組と回数である。記事AからBへの行と、BからCへの行があっても、それらが同じ読者による一連の移動だったかは分からない。|記号だけの経路を自然な日本語へ置き換え、読者単位の情報がない意味を明確にする。|

書式・改行の調整は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|1|Wikipedia<br>Clickstream → Wikipedia Clickstream|
|38・39|Appendix: 3. 研究と参考文献 → Appendix: 2. 関連データと参考文献|
|24|import csv, gzip<br>path = "clickstream-jawiki-2026-09.tsv.gz"<br>with gzip.open(path, "rt", encoding="utf-8") as f:<br>    rows = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)<br>    for prev, curr, kind, n in rows:<br>        if prev == "富士山" and curr == "富士登山":<br>            print(prev, curr, kind, int(n)) → import csv, gzip<br>path = "clickstream-jawiki-2026-09.tsv.gz"<br>with gzip.open(path, "rt", encoding="utf-8") as f:<br>    rows = csv.reader(<br>        f, delimiter="\t", quoting=csv.QUOTE_NONE)<br>    for prev, curr, kind, n in rows:<br>        if prev == "富士山" and curr == "富士登山":<br>            print(prev, curr, kind, int(n))|
|1|Title centered on one48pt line; native frame enlarged to include descenders.|
|6・8・9・10・30・31・32・33・34|Actual native table extent aligned to sum of column widths; example tables resized19pt and captions placed after table.|
|11|Removed inherited connector shadow, linear count/100pt thickness and larger caption/source gap.|
|24|Wrapped csv.reader call onto two code lines, preserving exact Python semantics.|
|38・39|Reference band aligned with Appendix section2.|

追加した内容は、文言の校正対と分けて記録する。

|ページ・対象|内容|
|---|---|
|38|Wikimedia contributors. Meta-Wiki. → Wikimedia contributors, n.d. Meta-Wiki. 参照2026-10-28.|
|39|Wikimedia Foundation. → Wikimedia Foundation, n.d. 参照2026-10-28.|
|39|Wikimedia Foundation. GitHub. → Wikimedia Foundation, n.d. GitHub. 参照2026-10-28.|

[全ページ文言](wikipedia-clickstream/pages.jsonl)・[最終検証票](wikipedia-clickstream/review.json)・[メインの確認](wikipedia-clickstream/main-review.json)
