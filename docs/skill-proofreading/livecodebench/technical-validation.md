# 技術検証と生検出の解決

最終artifact SHAはhandoff.jsonとexact-ink-audit.jsonに対応。

- ZIP整合、XML schemaの想定外エラー、壊れた参照、重複shape ID、ノート、URL以外のリンク、bullet百分率の範囲違反：0。マスター由来のbuSzPct整数表記は114件の既知lexical検出として保存し、有効範囲を別確認。82パーツ検証。
- PPTX67スライド／PDF67頁一致。URLリンク63、リンク不一致0、ページ寸法不一致0。5 native tables / 65 cells、三線罫線・native/PDFセル文字対応の違反0。数値列と列見出しは右揃え（バージョンの第1列にも適用）。
- 最終PDFの全native段落の文字を、baselineとx座標で再構成した実glyph列と照合。missing paragraphs0。FontToolsの実アウトラインとPDFの実文字座標を用い、23465glyphを検査。未知glyph0、ページ外0、native frame外0。本文と出典の実ink間隔最小9.268pt、文献同士33.111/26.040/26.012pt。
- 通常のPDF抽出順を使うrender監査は60件の見かけのmissingを保存している。≤などの別フォントspanが後ろに抽出されることと、移動したRangePowerSum native shapeのXML順により、文章の文字順と単純な抽出順が異なる。全段落を実描画位置順で照合したexact監査では欠落0。PDF画像も全頁を作者が読んだ。生レポートを「0」と書き換えない。
- 通常layout監査のp29出典間隔はフォントmetric bboxによる見積りであり、実ink測定10.311ptで8pt以上。p59英文のmissingは≤別span順で、実文字照合は一致する。フォントmetricの枠検出もexactの実アウトライン測定で別検証した。測定方法と生検出は監査JSONに保存。
- 12例は17pt原文全文1頁、長い1例は意味で2頁。最終3文献頁は各2件。native文字・コードの編集可能性、実文字と背景・後続本文の接触がないことを全頁画像で確認。

作者検証で独立レビューを代替しない。公開用の最終承認は別レビュー記録に従う。

最終追加修正：p25出典だけを各文献1行の2行へ変更し、論文URLと公式Leaderboard URLをそれぞれ付けた。p25を1600pxで再実見し、他66頁は旧最終PDFとピクセル同一。source25-visual-bridge.jsonに記録。
