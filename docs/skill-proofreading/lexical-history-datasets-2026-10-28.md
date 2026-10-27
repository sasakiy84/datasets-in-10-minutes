# 語彙・地名データ6資料の制作・校正記録（2026-10-28）

日本語WordNet、WLSP（分類語彙表）、Sudachiの同義語辞書、UniDic、日本歴史地名大系の地名項目データセット、歴史的行政区域データセットβ版の紹介資料を作成した。評価用ベンチマークの定型ではなく、それぞれの語・意味・解析結果・地名・境界の構造と、形式、収録範囲、取得方法、利用条件を中心に説明した。

|資料|本編|全頁|配布物|記録|
|---|---:|---:|---|---|
|日本語WordNet|29|42|[PDF](../../slides/datasets-in-10-minutes-japanese-wordnet.pdf)・[PPTX](../../slides/datasets-in-10-minutes-japanese-wordnet.pptx)|[出典](../japanese-wordnet-sources.md)・[修正対](japanese-wordnet.md)・[検証票](japanese-wordnet/review.json)・[データ記録](japanese-wordnet/data-manifest.json)|
|WLSP（分類語彙表）|28|39|[PDF](../../slides/datasets-in-10-minutes-wlsp.pdf)・[PPTX](../../slides/datasets-in-10-minutes-wlsp.pptx)|[出典](../wlsp-sources.md)・[修正対](wlsp.md)・[検証票](wlsp/review.json)・[データ記録](wlsp/data-manifest.json)|
|Sudachiの同義語辞書|32|42|[PDF](../../slides/datasets-in-10-minutes-sudachi-synonym.pdf)・[PPTX](../../slides/datasets-in-10-minutes-sudachi-synonym.pptx)|[出典](../sudachi-synonym-sources.md)・[修正対](sudachi-synonym.md)・[検証票](sudachi-synonym/review.json)・[データ記録](sudachi-synonym/data-manifest.json)|
|UniDic 2025.12|28|41|[PDF](../../slides/datasets-in-10-minutes-unidic.pdf)・[PPTX](../../slides/datasets-in-10-minutes-unidic.pptx)|[出典](../unidic-sources.md)・[修正対](unidic.md)・[検証票](unidic/review.json)・[データ記録](unidic/data-manifest.json)|
|日本歴史地名大系 地名項目データセット|27|38|[PDF](../../slides/datasets-in-10-minutes-nrct.pdf)・[PPTX](../../slides/datasets-in-10-minutes-nrct.pptx)|[出典](../nrct-sources.md)・[修正対](nrct.md)・[検証票](nrct/review.json)・[データ記録](nrct/map-manifest.json)|
|歴史的行政区域データセットβ版|30|41|[PDF](../../slides/datasets-in-10-minutes-historical-administrative-areas.pdf)・[PPTX](../../slides/datasets-in-10-minutes-historical-administrative-areas.pptx)|[出典](../historical-administrative-areas-sources.md)・[修正対](historical-administrative-areas.md)・[検証票](historical-administrative-areas/review.json)・[データ記録](historical-administrative-areas/map-manifest.json)|

ローカルの制作・日本語校正スキルを使用した。Geminiおよび外部生成APIは使用していない。実データの取得・解析、辞書による実際の形態素解析、地名・境界の実描画は実施した。モデルのベンチマーク評価は行っていない。本編の流し読みは各600秒の計画で、閲覧時間は未実測である。

資料ごとに作成担当と独立確認担当を分け、一次資料、原レコード、コードや描画との対応を確認した。すべてのページを実際に表示して文言と見た目を確認した。最終版で変更のないページを以前の実見から引き継ぐ場合は、本人が表示した基準版との全ページRGB一致を記録し、変更ページを再表示した。担当の再開以前に別の担当が実施した確認は、その担当の実施として区別した。メイン担当の補助レビューも、本人が実際に読んだ文面・表示したページに範囲を限って記録した。

変更の前後対は、保存した編集可能な初稿等と、そのページのnative要素を照合した実際の文言である。修正段階が異なる場合は個別に記載し、表幅や配置などの書式調整を文言の対と分けた。各最終検証票は配布PDF/PPTXのSHA-256と対応する。原データや辞書全体の取得と、全内容を人が精読したことを区別し、解析・閲覧した範囲を担当者別に示した。原ファイル、作図コード、実見用画像は作業領域に保持し、公開記録には必要な確認結果、代表例、出典、利用条件を収録した。

日本語WordNetは2.1を主対象とし、系列の初公開年と紹介版を区別した。UniDicは現代書き言葉2025.12を紹介版としてカタログにも明記した。地名データの代表点と境界を混同せず、歴史的行政区域では自治体IDの有効期間と境界の基準日を分け、ウェブサイト・ID一覧と取得した境界ファイルの利用条件をそれぞれ説明した。

ギャラリーに用途「語彙検索」「意味分類」「形態素解析」を追加した。用途や作成・更新日時の条件はクエリパラメーターと対応する。既存124件のカタログ行と248件の配布ファイルを保持し、合計130件とした。今回の資料作成に関する指示は[ユーザー指示履歴](../user-instructions.md)の129に収録した。
