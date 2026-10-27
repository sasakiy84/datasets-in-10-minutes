# Wikipedia本文データ：資料と確認範囲

紹介対象は公式のMediaWiki Content File Exportsです。Wikipedia全体の開始年ではなく、この配布方式の開始年は2026年です。

- [本文の公式配布仕様](https://wikitech.wikimedia.org/wiki/MediaWiki_Content_File_Exports)：現行仕様・二つのデータセット・月初の基準時点を確認。
- [旧出力の移行案内](https://wikitech.wikimedia.org/wiki/Legacy_content_dumps_sunset)：六つの旧XML出力だけが対象。pages-articlesやSQL/JSON/RDF全体の廃止ではありません。
- [取得したビスラマ語版](https://dumps.wikimedia.org/other/mediawiki_content_current/biwiki/)：2026-10-01、全1ファイルを取得。3,485ページを構造として全件解析。全ページの文章を通読したという意味ではありません。
- [XML出力形式](https://www.mediawiki.org/wiki/Help:Export)：サイト・ページ・版の構造と逐次処理を確認。現在のスキーマ0.11は取得ファイルを根拠としています。
- [HTML配布のアーカイブ](https://dumps.wikimedia.org/other/enterprise_html/)：同サイトへのEnterprise複製は2025-03-24終了。
- [現行Enterprise API](https://enterprise.wikimedia.com/api/)：HTML/wikitext、無料アカウントの月次Snapshot。登録や認証APIの実行は行っていません。
- [Wikimedia利用規約 §7](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use)：本文・媒体・著者表示・変更表示の条件を確認。

本文抜粋と日本語訳の扱いは[著者表示](licenses/wikimedia-content-dumps/ATTRIBUTION-WIKIPEDIA.md)に記録しています。詳しい確認範囲は[確認記録](data-audits/wikimedia-content-dumps.json)、実例は[実例記録](skill-proofreading/wikimedia-content-dumps/examples.json)、校正の実際の対は[校正記録](skill-proofreading/wikimedia-content-dumps/proofreading.json)にあります。コードは取得済みの圧縮XMLに対して実行し、3,485件のタイトルを照合しました。

主編28ページは600秒の黙読想定配分です。実測した所要時間ではありません。Geminiや外部生成APIは使用していません。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-wikimedia-content-dumps.pptx)・[PDF](../slides/datasets-in-10-minutes-wikimedia-content-dumps.pdf)。本編28頁、総41頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/wikimedia-content-dumps.json)・[校正の修正対](skill-proofreading/wikimedia-content-dumps.md)・[全ページ文言](skill-proofreading/wikimedia-content-dumps/pages.jsonl)・[最終検証票](skill-proofreading/wikimedia-content-dumps/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[ATTRIBUTION-WIKIPEDIA.md](licenses/wikimedia-content-dumps/ATTRIBUTION-WIKIPEDIA.md)。
