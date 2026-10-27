# 地図データ3資料の制作・校正記録（2026-10-28）

OpenStreetMap、Overture Maps、国土地理院DEMを紹介する資料を作成した。今回は評価用ベンチマークの定型を当てはめず、実データの地物・形状・属性・標高値と、形式・座標・更新・利用条件を中心に構成した。共通地域の京都に加え、DEMでは富士山を扱った。

|資料|本編|全頁|配布物|記録|
|---|---:|---:|---|---|
|OpenStreetMap|28|40|[PDF](../../slides/datasets-in-10-minutes-openstreetmap.pdf)・[PPTX](../../slides/datasets-in-10-minutes-openstreetmap.pptx)|[出典](../openstreetmap-sources.md)・[修正対](openstreetmap.md)・[検証票](openstreetmap/review.json)・[地図記録](openstreetmap/map-manifest.json)|
|Overture Maps|31|41|[PDF](../../slides/datasets-in-10-minutes-overture-maps.pdf)・[PPTX](../../slides/datasets-in-10-minutes-overture-maps.pptx)|[出典](../overture-maps-sources.md)・[修正対](overture-maps.md)・[検証票](overture-maps/review.json)・[地図記録](overture-maps/map-manifest.json)|
|国土地理院DEM|28|41|[PDF](../../slides/datasets-in-10-minutes-gsi-dem.pdf)・[PPTX](../../slides/datasets-in-10-minutes-gsi-dem.pptx)|[出典](../gsi-dem-sources.md)・[修正対](gsi-dem.md)・[検証票](gsi-dem/review.json)・[地図記録](gsi-dem/map-manifest.json)|

ローカルの制作・日本語校正スキルを使用した。Geminiおよび外部生成APIは使用していない。データの取得、解析、実地図の描画は実施したが、モデル評価は行っていない。本編の流し読みは各600秒の計画で、閲覧時間は未実測である。

資料ごとに作成担当を分け、別の担当が一次資料と実データを確認し、すべてのページの描画と文言をレビューした。メイン担当による補助レビューは、本人が実際に確認した範囲を明記し、独立担当による全ページ確認とは区別した。各検証票は最終PDF/PPTXのSHA-256と対応する。変更の前後対は各資料の修正対に記録した。途中段階の修正を含む場合は編集経過として明示する。

実地図の入力・取得日・範囲・投影・描画方法・原データとの照合・帰属は各地図記録に残した。取得したファイル全体をすべて精読したとは扱わず、閲覧・解析した範囲を担当者別に記録した。原データ、作図コード、実見用のページ画像は作業領域に保持し、公開記録には確認結果と必要な利用条件を収録した。地物IDの全列や歴史的な監査の全字形一覧は、件数・代表例・元記録のダイジェストへ要約した。最終配布物と承認票は変更していない。要約範囲は[記録の整理](maps-datasets-2026-10-28-records-compaction.json)に示す。

ギャラリーには「地理空間」「地図作成」「地形解析」を追加し、用途のフィルターにもクエリパラメーターが対応する。既存121件のカタログ行と242件の配布ファイルは保持した。今回の品質に関する指示は[ユーザー指示履歴](../user-instructions.md)の128に収録した。
