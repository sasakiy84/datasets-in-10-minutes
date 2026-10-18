# ChID 独立レビュー：承認

create_pileが最終58頁とoverviewを個別に拡大確認。修正3件を作者へ返し、最終p40/44/51を再確認した。未解決0。

- p40：步步为营を「慎重に足場を固めながら進む」へ。循序渐进との違いを残す。
- p44：日落西山を「日が西に沈むように、衰えが進む」へ。比喩の意味も保持。
- p51：表セルを「groundTruth：成語の配列」へ短文化し、末尾「列」の1字行を解消。本文引用の少数字行は許容する。

正式ACL一次PDF/HTML、固定公式repo6ファイルとtree、固定HF tree、CLUE ZIP、FewCLUE全15ファイルと固定blob一覧をレビュー専有へ独立取得。原6ファイルの全量は作者専有evidenceを読取のみで全件再走査し、独立GETした固定HF LFS oidへ全SHA/sizeを照合した。原6全量を再GETしたとは記録しない。独立4分割580807文章/728713空欄、Test/Ran/Sim同文・同正解の関係、全行の七候補/空欄/正解を一致確認した。現配布の短い行や同文を、構築方針や分割非重複保証へ読み替えない。

CLUEの群/文章/空欄を四配布で全件再集計し、共有十候補とtrain/devの別JSON正解、両testの正解欠測を確認。devは固定HF competitionのGit blobへ照合した作者保存bytesとも一致。FewCLUE15は独立GET/hash/blob一致、小集合各42・all各202和集合、test_public2002とtest2000/unlabeled7585の欠測を確認。13原例は13異なるcontent、原行SHA/offset/全本文/全候補順/全正解位置・A–Gを一致確認し、各候補と本文の日本語を読んだ。二空欄の例は空欄別の七候補を保ち、原CN全体1頁を優先してJPを別頁にする判断を確認した。

正式論文の構築・1600対5人注釈、空欄単位Accuracy、人間各200文章×3人の平均とモデル全件の範囲を照合。歴史AR/Humanの8図値、モデル表/表現比較9セル、語数と分割数値を確認。原論文の23.0%と40/200、本文14.6と丸め差14.7の不整合を、資料側で独自修正・再転載しない扱いも妥当。CLEVA紙面3候補とFewCLUE七候補、紙面train_2L20とHELM train_3L21、未取得選定版を分離。固定HELMの六設定と8526中CLEVA0、Converterと実推論値未取得の範囲を確認した。

全15原例表示頁のnative本文15pt/正解21pt boldえんじ、全本文・候補・訳の保持、11表/1chart/1工程図を確認。実Python p50を原Devで実行してpositions=[1]を確認（p14は説明用日本語手順として区別）。独立native監査444段落135セル0、新XSD0/マスター既存11、URL62 native/PDF文字中心一致、notes0、字形重複/欠落0。全58頁を最終PDFから独立再ラスタ化してPNG全bytes一致。47枠はレビュー側PNG実画素法で上9.33–10pt/下8.67–10.67pt、上下差最大1.34pt。作者のPDF bbox法との小差を明示した。

最終PPTX `b95550702ff9c8721e69e5062769eb049e56addb7eef1cd2dafae8d99e115d17`

最終PDF `b32450b22db0fdd54442884088bd937fd3b74014ace61da1f49528e3d90d0249`

詳細はreview.json / data-verification.json / native-verification.json / png-pdf-sync.json。
