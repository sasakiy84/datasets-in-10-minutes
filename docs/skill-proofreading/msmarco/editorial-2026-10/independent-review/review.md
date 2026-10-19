# MS MARCO 読者向け改訂・独立承認

旧61頁と新49頁の全native本文/表/出典、findings/page-mapを通読。新49頁を最終PDFから独立描画し、各頁を個別に拡大確認した。49PNGは作者の最終画像と全bytes一致。残件0で承認。

13実例の完全な英語質問/文章と日本語訳を読み比べ、元JSONのID/原文/参照タグ/元ファイルSHAを独立検証。意味・否定・数値・単位と元ラベルを保持。regularの疎な判定、卸売質問と小売文章のずれ、TREC0–3の意味、2/3正例、候補のqrels和集合と上位30限定を一次実装・正式論文へ照合。学習提示2質問と通常4組は保存adapter_specとsample prompt/get_train_instanceを確認。

6公開statsから12セルを小数第4位へ再算出し3試行を確認。教師あり4値はNogueira等2020本文のMRR@10表を照合。4native表はbaselineと全セル一致。原ranking_metricsのobject_to_score_binary_rankingをAST抽出して実行しYes/No/その他とlogprobの順位を独立確認。原公式READMEの件数/配布・公式非商用研究条件と権利範囲も確認。全884万文章の再取得やモデル再実行はしていない。

独立layout305段落43セル0、全native clip316段落52セル0、新XSD0・50URL文字中心一致、notes0。26引用枠は実PNGの黒字形を別測定し上下差2pt以内。全頁に欠落/重なりなし。普通の本文の短い末尾行は許容。

最終hash：
{
  "pptx": "e3057566624c27ba537f91b7872c10c1fb3c166740e05986121a6115c0d23dbf",
  "pdf": "38e63cf791657c738d7c473baf687afbf026e234c8d8dc904519f3767ff0a827"
}
