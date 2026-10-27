# Wikidata の出典と実データ

Wikipediaと関連する別のWikimediaプロジェクトであるWikidataを、項目・文・修飾子・出典・ランク、JSON・RDF・検索と一括配布の形式から紹介する。作成日は2026-10-28（日本時間）。

## 公式資料

- [Wikidata:Introduction](https://www.wikidata.org/wiki/Wikidata:Introduction)：目的、共同編集、多言語、項目とプロパティの構造。
- [Wikidata:Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)：個別取得、検索、API、一括取得とアクセス方針。
- [Wikibase: JSON](https://doc.wikimedia.org/Wikibase/master/php/docs_topics_json.html)：現行のJSON仕様。旧JSON文書は移転案内であり、本文の根拠には使用していない。
- [RDF Dump Format](https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format)：完全な文とtruthy、修飾子・出典の表現。
- [Help:Ranking](https://www.wikidata.org/wiki/Help:Ranking)：normal・preferred・deprecatedの役割。
- [Wikidata:Database download](https://www.wikidata.org/wiki/Wikidata:Database_download)：一つの配列を構成するJSONダンプ、all/truthy RDF、更新。
- [Wikidata:Licensing](https://www.wikidata.org/wiki/Wikidata:Licensing)：構造化データCC0と、他の名前空間の文章・画像の区別。
- [Wikidata:Tenth Birthday](https://www.wikidata.org/wiki/Wikidata:Tenth_Birthday)：2012-10-29の公開日。

公式トップ画面をCSS・フォント読み込み後に撮影し、作成者が実際に表示して確認した。スクリーンショット、構造化データ、説明文は同じ利用条件ではない。[利用条件と帰属](../../licenses/wikidata/ATTRIBUTION-WIKIDATA.md)も参照。

## 表示した実例

個別のSpecial:EntityData JSONと、Q42のRDF（full相当のdump flavor・simple flavor）を使用した。主な項目は[Q42](https://www.wikidata.org/wiki/Special:EntityData/Q42.json)、[Q17](https://www.wikidata.org/wiki/Special:EntityData/Q17.json)、[Q8577](https://www.wikidata.org/wiki/Special:EntityData/Q8577.json)。追加例は[Q146](https://www.wikidata.org/wiki/Special:EntityData/Q146.json)、[Q2](https://www.wikidata.org/wiki/Special:EntityData/Q2.json)、[Q90](https://www.wikidata.org/wiki/Special:EntityData/Q90.json)、[Q64](https://www.wikidata.org/wiki/Special:EntityData/Q64.json)、[Q60](https://www.wikidata.org/wiki/Special:EntityData/Q60.json)。

図表は取得した項目の文を選んだもので、Wikidata全体を網羅的に集計したものではない。人口グラフは日本のP1082から、P459が国勢調査Q39825で、時点が1995・2000・2005・2010・2015・2020年10月1日の6文を選び、百万人へ換算した。元の整数値を保持し、ラベルは小数1桁で表示した。

人口のランクの例は、取得JSONに格納された値・時点・方法を説明するために使う。2024年の方法Q11381946のラベルは「住民基本台帳」であり、推測した「人口推計」には変更していない。Tokyo2020 Q181278の期間・参加数の疑問点を先行調査で見つけたため、主編の大会例にはQ8577を採用した。Q146の学名、Q60のタイムゾーンは取得JSONに該当プロパティがないため例示していない。

掲載したPythonはローカルJSONを読み、SPARQLはQ42に限定した問い合わせを実行した。巨大な一括ダンプの取得、全項目の検査、モデル評価、Gemini・外部生成APIの利用は行っていない。取得、版ID、SHA、表示例との照合、実行・描画の確認範囲は[データ検証票](../../data-audits/wikidata.json)と[データ記録](data-manifest.json)に残す。
