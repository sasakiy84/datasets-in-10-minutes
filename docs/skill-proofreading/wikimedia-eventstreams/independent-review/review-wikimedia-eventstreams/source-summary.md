# EventStreamsの独立確認

作成者とは別の担当 `/root/wikimedia_coordinator/create_history` が、2026-10-28 JSTに確認した。

- [公式文書](https://wikitech.wikimedia.org/wiki/EventStreams)と[API仕様](https://stream.wikimedia.org/?doc)を確認した。対象はウィキの編集・操作などの変更イベントで、設定された公開ストリームをHTTP/SSEで配信する。再取得できる期間は設定に依存し、公式文書は7〜31日程度としている。
- [recentchangeのスキーマ](https://schema.wikimedia.org/repositories/primary/jsonschema/mediawiki/recentchange/1.0.0)、[RCFeed](https://www.mediawiki.org/wiki/Manual:RCFeed)、[元の記録項目](https://www.mediawiki.org/wiki/Manual:Recentchanges_table)を読み、版ID、サイズの単位、bot印、種類ごとに異なる項目を照合した。サイズは本文のバイト数で、SSEのidは接続の再開位置を表す。
- 独立に有限取得したSSE8件を解析した。公開中のlatestスキーマは1.0.1だが、取得したレコードは1.0.0を指定していた。実SSEのidにはoffsetを含むものもあり、全メッセージがtimestamp形式であるとは断定していない。
- 作成者が保存した30件のSSEを再解析し、JSON記録との一致を確認した。主編4件と追加5件は異なる実イベントであり、採用した項目、51バイトの増加、先頭6件のUTC時刻、種類・ウィキの集計を再計算した。
- [2017年の公開案内](https://diff.wikimedia.org/2017/03/20/eventstreams/)と[2018年の機能追加](https://diff.wikimedia.org/2018/08/08/eventstreams-updates/)を読んだ。公開年は2017年で、再開機能、時刻からの取得、複数ストリームの利用を時点に沿って説明している。
- [利用規約のライセンスと再利用の項目](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use)を確認した。サービス実装のライセンスを、配信される投稿内容すべてのライセンスとして扱っていない。公開する検証記録には、取得した利用者名・IP・編集要約などの全文を含めない。

生の配信内容、個別の取得ログ、全グリフ座標、検証用コードは非公開の作業領域に保持した。Gemini、外部の生成API、モデル評価は使用していない。
