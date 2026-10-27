# 出典と確認範囲

作成者：create_nrct。取得日：2026-10-28。Gemini・外部生成API・モデル評価は未使用。日本語校正はローカルの日本語校正スキルで実施し、実際に保存した初稿と最終版の文言対を [proofreading.json](skill-proofreading/nrct/proofreading.json) に記録した。

公式公開データ [CSV](https://geoshape.ex.nii.ac.jp/nrct/dataset/nrct-20250719.csv)（2025年7月19日版）を自分でも取得した。10,723,294 bytes、SHA256 f70a6c3fc7ae9a74e01efa85d7fa8eabe215869fb3c2f62061f6047618652e7c。親が先行取得した同版とは別のHTTP取得で一致した。

取得したこと、全件を機械的に検査したこと、選択した項目や本文を人が読んだことを区別する。詳細は [data-audit.json](data-audits/nrct.json)、[data-manifest.json](skill-proofreading/nrct/data-manifest.json)、[source-read-scope.json](skill-proofreading/nrct/source-read-scope.json)。原CSV・全生タイル・レンダ・スクリプトはprivate作業ディレクトリに置き、公開記録には要点とSHAだけを残す。

1. [CODH公式サイト](https://geoshape.ex.nii.ac.jp/nrct/)：公開範囲、方法、更新履歴、CC BY 4.0と指定クレジットを本文全読。
2. [地域一覧](https://geoshape.ex.nii.ac.jp/nrct/resource/)：47都道府県＋京都市の48区分を全読。JIS都道府県コードとは扱わない。
3. [NII公開発表](https://www.nii.ac.jp/news/release/2023/1018.html)：本文全読。2023年初公開と辞典の成立。記事中の初期件数と2025配布件数を混同しない。
4. [GeoNLP配布](https://geonlp.ex.nii.ac.jp/dictionary/geoshape-nrct/)：本文とメタデータ読解。別形式の入口を紹介。GeoNLP未実行。メタデータの80503をNRCTCSVの件数に転用しない。
5. [ジャパンナレッジの辞典紹介](https://japanknowledge.com/contents/rekishi/)：本文全読。全辞典15万超と公開行政項目約8万の違い。
6. [地理院タイル一覧](https://maps.gsi.go.jp/development/ichiran.html#pale)：淡色地図のズームとVMAP0帰属部分を読解。実際のxyzタイルを取得して描画。全タイル種の全文読解とは主張しない。
7. [GSI利用規約](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)：本文全読。PDL1.0・第三者帰属・加工表示を確認。PDL本文は既存マップ作業で取得された公式本文を引き継ぎ、自分でも全読。自分の新規HTTP取得とは記録しない。
8. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)：公式サーバは403。SPDX公式ミラー https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt の本文を取得し全読。CODH一次ページの適用宣言と併用。
9. DOI https://doi.org/10.20676/00000448 ：公式トップ指定値を使用。リダイレクト先の内部item_id478をDOIに転用しない。

描画と帰属は [map-draw-verification.json](skill-proofreading/nrct/map-draw-verification.json)、[map-manifest.json](skill-proofreading/nrct/map-manifest.json)、[ATTRIBUTION-NRCT.md](licenses/nrct/ATTRIBUTION-NRCT.md)。CSVの測地系は一次topに明記を確認できていないため、説明図の重ね合わせとして度の緯度経度をWGS84相当で扱った。データセットがEPSG4326と明示しているとは説明しない。表示座標はWeb Mercator（EPSG3857）。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-nrct.pptx)・[PDF](../slides/datasets-in-10-minutes-nrct.pdf)。本編27頁、総38頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/nrct.json)・[校正の修正対](skill-proofreading/nrct.md)・[全ページ文言](skill-proofreading/nrct/pages.jsonl)・[最終検証票](skill-proofreading/nrct/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[ATTRIBUTION-NRCT.md](licenses/nrct/ATTRIBUTION-NRCT.md)、[LICENSE-CC-BY-4.0.txt](licenses/nrct/LICENSE-CC-BY-4.0.txt)、[LICENSE-PDL-1.0.txt](licenses/nrct/LICENSE-PDL-1.0.txt)、[LICENSE-GSI-CONTENTS.txt](licenses/nrct/LICENSE-GSI-CONTENTS.txt)。
