# CHEF 独立レビュー：合格

全65頁を一頁ずつview_imageで読み、overviewも確認。13原主張・全非空gold根拠・日本語訳・配布ラベルを直接照合し、未解決・修正依頼なし。原文の誤記/重複、画像を参照する例の表示範囲も保たれている。

公式Drive原archive・正式ACL論文PDF・Joint/LICENSEを通常TLSで独立GETし、作成者の取得hashと一致。archive3JSONを再展開hash照合し、全10000件の分割/ラベル/根拠数/空欄/領域/出典/ID重複を別実装で再集計した。13例の元行/全文/hashが一致。論文と原配布の不一致は正確に明示され、原因を推測で埋めていない。

論文Table5の70平均±SD組を一次PDFテキストから独立抽出、results.pyと一致。6完全表と本編抜粋表、5値nativechartも照合。test999・Micro/Macro F1・5独立試行・gold条件を区別。HELM固定公開run8526を独立再走査しCLEVA/CHEF0。公開docstring金星例の選択肢・Aと原train128/claimId977が一致。実CLEVA v1集合は未取得と明示。

Native451段落245セルが編集可能枠内の最終PDF字形と一致、字形重複0。13表1chart、20答え21pt太字B13731、notes0、61URLはnative/PDFリンク文字中心がURL本文と完全一致。全65PNGは最終PDFから別オブジェクトで再描画した画素と同一。XSDは元master既存11/新規0。最終hashはreview.jsonに固定。

出典・脚注・権利の範囲は適切。Jointの取り込みコードMITを全記事/データの許諾に広げていない。対象dirは変更せず、独立記録だけreview-chefへ作成した。
