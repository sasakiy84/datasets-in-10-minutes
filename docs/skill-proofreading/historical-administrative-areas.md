# 歴史的行政区域データセットβ版：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルで作成し、作成担当とは別の担当が内容・原票・描画を確認した。以下は実際に行った修正の対である。最終版の確認範囲とファイルの対応は検証票に記録した。

保存した初稿と最終版の文言を、同じページのnative要素と照合した。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|14|1923年の座標列の冒頭。...は本資料で省略した部分。|1923年の座標列の冒頭。経緯度は度単位。...は省略した部分。|座標の単位を明記する。|
|20|1889〜1919年の収録は一部の都道府県。1920年以降は両資料の統合が進められている。|1889〜1919年の収録は一部の都道府県。1920年以降は、二つの資料を統合している。|公式の統合済み範囲へ説明を合わせる。正式名を意味のまとまりで改行する。|
|21|元の境界データをGeoJSON・TopoJSONへ変換し、名称、標準地域コード、廃置分合の情報などから市区町村IDを付ける。|元の境界データをGeoJSON・TopoJSONへ変換し、名称、標準地域コード、合併などの履歴から市区町村IDを付ける。|初出の廃置分合を、合併などの履歴と言い換える。|
|24|公開後も、年代と内容が追加・修正された|公開後も、境界データが追加された|ファイル名の細かな修正履歴を外し、境界データ追加の歩みを示す。更新年月は一次資料へ照合して訂正。|
|24|2023-07-05|2019-07|ファイル名の細かな修正履歴を外し、境界データ追加の歩みを示す。更新年月は一次資料へ照合して訂正。|
|24|一部のファイル名の月日を0000から1231へ修正|2019年の境界データを追加|ファイル名の細かな修正履歴を外し、境界データ追加の歩みを示す。更新年月は一次資料へ照合して訂正。|
|24|2023-10|2023-07|ファイル名の細かな修正履歴を外し、境界データ追加の歩みを示す。更新年月は一次資料へ照合して訂正。|
|25|境界の差を、そのまま自治体の変更と読まない|境界線の差には、元資料の違いも表れる|読み手が得られる知見を示す自然な見出しにする。|
|30|GeoJSONは形状と属性を、TopoJSONは共有する境界線を表す。代表点とID一覧のCSVも、用途に応じて組み合わせられる。|GeoJSONは形状と属性を持ち、TopoJSONは境界線を共有できる。代表点とID一覧のCSVも、用途に応じて組み合わせられる。|形式と属性の関係を自然な文に整える。|


書式の調整は文言の修正と分けて記録する。

|ページ・対象|書式の変更|理由|
|---|---|---|
|20|Source tablecell split at semantic boundary after筑波大学; same text preserved.||
|1|Cover title native frame and vertical anchor adjusted so beta descender is inside frame.||
|23|Three-row numeric table compacted to6.6in and centered; valuefont/RIGHT preserved.||
|31|Appendix title frame expanded4pt for Latin descenders.||
|6・7・8・33・34・35・36・37|Map credits reflect precise actual source; Sakyo x-ticks separated, Miyake scale bar moved clear of minor island.||

[全ページ文言](historical-administrative-areas/pages.jsonl)・[最終検証票](historical-administrative-areas/review.json)・[メインの確認](historical-administrative-areas/main-review.json)
