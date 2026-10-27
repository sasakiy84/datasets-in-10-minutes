# Wikimedia公式データ6資料の制作・校正記録（2026-10-28）

Wikipedia本文、閲覧回数、記事間の遷移、編集等の履歴、変更イベント配信、および別プロジェクトWikidataの構造化知識について、それぞれ独立した紹介資料を制作した。評価課題の定型を当てはめず、実データ、収録範囲、形式、更新・取得方法、利用条件を軸に構成した。

|資料|本編|全頁|配布物|記録|
|---|---:|---:|---|---|
|Wikipedia本文データ（MediaWiki Content File Exports）|28|41|[PDF](../../slides/datasets-in-10-minutes-wikimedia-content-dumps.pdf)・[PPTX](../../slides/datasets-in-10-minutes-wikimedia-content-dumps.pptx)|[出典](../wikimedia-content-dumps-sources.md)・[修正対](wikimedia-content-dumps.md)・[検証票](wikimedia-content-dumps/review.json)|
|Wikimedia Pageviews|31|40|[PDF](../../slides/datasets-in-10-minutes-wikimedia-pageviews.pdf)・[PPTX](../../slides/datasets-in-10-minutes-wikimedia-pageviews.pptx)|[出典](../wikimedia-pageviews-sources.md)・[修正対](wikimedia-pageviews.md)・[検証票](wikimedia-pageviews/review.json)|
|Wikipedia Clickstream|26|39|[PDF](../../slides/datasets-in-10-minutes-wikipedia-clickstream.pdf)・[PPTX](../../slides/datasets-in-10-minutes-wikipedia-clickstream.pptx)|[出典](../wikipedia-clickstream-sources.md)・[修正対](wikipedia-clickstream.md)・[検証票](wikipedia-clickstream/review.json)|
|MediaWiki History|29|39|[PDF](../../slides/datasets-in-10-minutes-mediawiki-history.pdf)・[PPTX](../../slides/datasets-in-10-minutes-mediawiki-history.pptx)|[出典](../mediawiki-history-sources.md)・[修正対](mediawiki-history.md)・[検証票](mediawiki-history/review.json)|
|Wikimedia EventStreams|30|39|[PDF](../../slides/datasets-in-10-minutes-wikimedia-eventstreams.pdf)・[PPTX](../../slides/datasets-in-10-minutes-wikimedia-eventstreams.pptx)|[出典](../wikimedia-eventstreams-sources.md)・[修正対](wikimedia-eventstreams.md)・[検証票](wikimedia-eventstreams/review.json)|
|Wikidata|30|41|[PDF](../../slides/datasets-in-10-minutes-wikidata.pdf)・[PPTX](../../slides/datasets-in-10-minutes-wikidata.pptx)|[出典](../wikidata-sources.md)・[修正対](wikidata.md)・[検証票](wikidata/review.json)|

ローカルの制作・日本語校正スキルを使用し、Geminiおよび外部生成APIは使用していない。公開データの限定取得・解析・可視化と表示コードの確認を実施し、モデルの評価は行っていない。本編の流し読みは各600秒の計画で、閲覧時間は未実測である。

資料ごとに作成担当と独立確認担当を分け、一次資料、実レコード、日本語、すべての実ページ、構造・描画の技術検査を確認した。各担当の実施範囲は個別の記録に示した。変更のないページを以前の実見から引き継ぐ場合は、同じ担当が実際に表示した基準版との全ページRGB比較を記録し、変更ページを再表示した。メイン担当の補助レビューは、本人が読んだ文言・表示したページの範囲に限って記録した。

修正前後の文言は、保存した編集可能な版の同じページ・native要素を照合した実際の対である。書式調整や内容の追加は文言の対と分けた。各最終検証票は配布PDF/PPTXのSHA-256と対応する。全ページのnative段落・表セルをJSONLに残し、画像内の文字についてOCRを実施したとは主張していない。取得したファイル全体と、人が精読した範囲も区別した。原ファイル、制作スクリプト、個別の実見画像などは作業領域に保持し、公開記録は確認結果・代表例・出典・利用条件に絞った。

本文のスナップショットと編集イベントの履歴を区別し、EventStreamsを現実の出来事の整理済みデータとは説明していない。WikidataはWikipediaそのものとは別のWikimediaプロジェクトとして紹介した。第三者が加工したコーパスをWikimedia公式配布として扱っていない。本文、集計統計、イベント、構造化知識では、公開される範囲や利用条件が異なるため、それぞれの公式資料と実配布を確認した。

ギャラリーにはデータの種類「構造化」と用途「本文コーパス」「閲覧統計」「編集履歴」「イベント配信」「知識検索」を追加した。用途や作成・更新日時の条件はクエリパラメーターと対応する。既存130件のカタログ行と260件の配布ファイルを保持し、合計136件とした。今回の依頼は[ユーザー指示履歴](../user-instructions.md)の130に収録した。

最終ローカル検査では、新規6資料のPDF/PPTXとプレビューの一致、全239頁のnative段落・表セルの順序と重複、6件の公開記録peer承認、既存130行・260配布物の保持を確認した。日本語の校正対は合計59件で、内容の変更・差し替えや書式の調整と分けている。ギャラリーでは136件、新しい用途と構造化の絞り込み、作成・更新順、タイトル検索、リセットを検査し、作成担当とは別の担当が2画面と新6サムネイルを個別に表示して確認した。

[ローカル検証票](wikimedia-official-datasets-2026-10-28/local-verification.json)・[全頁文言の照合](wikimedia-official-datasets-2026-10-28/native-page-transcripts.json)・[ギャラリーの機能確認](wikimedia-official-datasets-2026-10-28/gallery-browser-check.json)・[ギャラリーの実見](wikimedia-official-datasets-2026-10-28/gallery-visual-review.json)・[資料別コミット](wikimedia-official-datasets-2026-10-28/dataset-commits.json)。
