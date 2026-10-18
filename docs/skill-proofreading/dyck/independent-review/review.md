# Dyck 独立レビュー（最終合格）

対象：/workspace/artifacts/helm-parallel/dyck。元成果物は編集していない。

公式v0.3.0シナリオを別namespaceで実行し503件を再生成。公開500件の入力・全参照と全件一致。独立stackで503正解すべてを検証。13実例の入力・正解・実出力を公開trial 0原記録と照合した。実際の採点経路（logprob降順、prediction.strip後に末尾split）で1500出力を再集計し、各試行の末尾指標73.2/76.0/76.0%、全列40.6/49.2/49.2%が一致した。raw版とstrip版で採点差はなかった。

原研究の本文§5、Table 2を照合。原研究は各位置の次記号集合を予測し、全位置正答で1列成功とする。Dyck-2表のtest平均0/1.39/99.99%と10runs・train5000長さ2–50/test5000長さ52–100が一致。BIG-bench固定taskの1000件・multiple_choice_gradeを確認した。HELMの切出し前長さと実入力長を区別できている。

PPTX/PDFの別shape間字形重複は独立測定で0。native表7・グラフ1を構造確認。重要37頁を個別拡大：1,2,6,7,8,9,10,12,13,14,15,16,17,20,21,22,23,24,27,28,29,30,34–48。引用枠内全入力、回答、予測、正誤、表、チャート、コード、参考文献に欠落・接触は認めない。

修正依頼：p6/27/28の原研究フッターが略記のみ。正式題名 Memory-Augmented Recurrent Neural Networks Can Learn Generalized Dyck Languages を追加すること。修正後の対象3頁を個別再目視し、正式題名追加・本文/他出典との間隔・URLを確認。最終shape重複再測定0。修正を受け入れ、未解決事項なし。最終PPTX/PDFのhashはreview.jsonへ記録。
