# Wikipedia Clickstreamの一次資料

対象はWikimediaが公開する月次Clickstream。2026-10-28JST確認時点の最新掲載月は2026-09。日本語版の単月gzipを全件取得・集計した。他言語のデータ自体は未取得で、40言語という収録範囲は当月の公式ディレクトリから数えた。

- Wikimedia contributors. **Research:Wikipedia clickstream**. Meta-Wiki. https://meta.wikimedia.org/wiki/Research:Wikipedia_clickstream . 完全本文、形式、初期公開履歴、用途を読んだ。2015年のcanonicalcitationと2015年1月の公開により開始年2015を確認。本文の「10以下を除外」は現行実装と実配布の10件行に一致しないため、現行月にはその説明を転用しなかった。
- Ellery Wulczyn and Dario Taraborelli (2015). **Wikipedia Clickstream**. figshare. https://doi.org/10.6084/m9.figshare.1305770 . Canonicalcitationは公式Meta本文で確認。figshare配布版を現在の月次ファイルとみなさず、原データは公式月次配布から取得した。
- Wikimedia. **Analytics Datasets: Clickstream**. https://dumps.wikimedia.org/other/clickstream/readme.html . 短い全文を確認し、Analyticsデータ自体のCC0適用を確認。READMEの5言語は旧説明で、現月の40言語一覧を優先した。
- Wikimedia. **Clickstream September2026**. https://dumps.wikimedia.org/other/clickstream/2026-09/ . 日本語版94,943,464bytesのgzipを取得し、全6,269,506行を最後まで展開・解析した。prev/curr/type/nの4列、最小n=10を確認。個別の閲覧履歴や非公開のアクセス記録にはアクセスしていない。
- Wikimedia. **ClickstreamBuilder.scala**. analytics-refinery-source. https://github.com/wikimedia/analytics-refinery-source/blob/master/refinery-job/src/main/scala/org/wikimedia/analytics/refinery/job/ClickstreamBuilder.scala . prepareClickstreamのWHERE/GROUPBY、ページ・リダイレクト・リンクの結合、type分類、count>=minCount、config既定値10を直接確認。現行masterのソースを文書的根拠として読んだが、当該月に実際にデプロイされたcommitを確定したとは主張しない。コードを配布スライドへ転用せず、読み込み例はPython標準ライブラリで独自に作成・実行した。
- Wikimedia Research. **WikiNav**. https://wikinav.toolforge.org/ . ツールの役割は公式Metaの説明を確認。live app入口のHTTP200は確認したが、live app内のクエリ操作は実行していない。
- Wikimedia. **Analytics/AQS/Pageviews**. https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews . Pageviewsとの関係の補足に使った公式文書。API呼出の実測やPageviews時系列の取得はこの資料ではしていない。
- Creative Commons. **CC0 1.0 Universal**. https://creativecommons.org/publicdomain/zero/1.0/ . 公式のdedication、waiver/fallback/limitationsを確認。Metaの画面は別のCC BY-SA4.0で、取得した画面のfooterリンクを直接確認した。

図は実際に取得した日本語版2026-09の4本の遷移から作った。タイトル・ラベル・値はnativePPTX。公式MetaスクリーンショットはCSS5枚とfont loadedを待って撮影し、作者が実際の画像を開いて確認した。画像内の文字にOCRを実施したとは記録していない。

制作・校正はローカルの日本語校正スキルを適用。Gemini、外部生成API、モデルによる評価は使っていない。
