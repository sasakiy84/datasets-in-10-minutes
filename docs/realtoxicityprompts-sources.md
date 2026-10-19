# RealToxicityPrompts 調査・制作記録

Gehman, Samuel; Gururangan, Suchin; Sap, Maarten; Choi, Yejin; Smith, Noah A. (2020). **RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models**. Findings of EMNLP 2020, 3356–3369. DOI 10.18653/v1/2020.findings-emnlp.301。ACL論文PDFと、Appendixを含むarXiv PDFを取得した。本文と実験条件は原資料を読み、結果の表をnative表として転記した。

## 配布・版・集計

公式コードは https://github.com/allenai/real-toxicity-prompts 。論文デモサイト https://toxicdegeneration.allenai.org/ は取得時503だったため、冒頭は実ブラウザで公式GitHubを表示した。CSS・フォント・README見出しと論文／デモ／データへのリンクが読み込まれた画面を個別表示した。screenshot-log.jsonにHTTP状態とasset記録を残した。

HF固定改訂は `f21629712ffd6a3d13a54fd2807ccd521c55ef74`。prompts.jsonl 67,690,996 bytes、SHA256 `4b6808878edc985fcc6bcb6a2a7239a0fb05420cb495f1f6ca1450da5e35c163`。HELMの実装が参照する公式S3アーカイブからREADMEとprompts.jsonlだけをストリーム抽出し、HFファイルとバイト単位で同一と確認した。取得アーカイブは3,715,984,281 bytes、SHA256 `97e742e6d6f5bc35ba2f503ebcce4c846651005c97a50021c6b82e618db0be46`。抽出と記録後、大容量tar本体は作業領域から削除した。他のアーカイブ構成物は展開していない。

全99,442行を集計。promptのTOXICITYがあるのは99,016行で、そのうち0.5以上21,744行、0.5未満77,272行。promptのnullは426、continuationのnullは550。前半の非nullの四区間は59,633 / 17,639 / 11,152 / 10,592行。論文の25,000×4は二分前の文を選ぶ条件であり、この前半分布とは異なる。challenging=trueは1,199行で、論文の制御なし全モデルに関する1,225件との違いは原因不明として明示し、新しいモデルすべての失敗ラベルとは扱わない。

HFカードには古いimage-generation / image metadataという記述があるが、現物と論文の課題は英語テキストの生成評価。コードLICENSEとHFカードはApache-2.0を掲示する。引用された元ウェブ文の著者・媒体の帰属とコードのライセンスを同一視せず、原文はOpenWebText由来と記録した。

## 原例と公開生成

本編3＋Appendix10の異なる13原行。元prompt・continuationは両方全文で、全件EN/JP同居。最小の原例本文は16pt、コードを含む全引用本文の下限は15pt。各例のfilename/begin/end、固定行位置、全8属性（null含む）、原レコード、JSON行SHA256（改行LFを除く）、構造化レコードSHA256、訳、表示範囲をexamples.jsonに保持した。説明のため、一般的な語の文脈、報道・引用・否定、閾値近傍、欠測を含めた。極端な転載を増やすことを例の選択基準にはしていない。

実例1/2/3のtext-davinci-003公開生成は、各5候補すべてと日本語訳を示した。原文字列は改行・空白を含めてexamples.jsonとscenario_state.jsonに保存。表示だけ空白を整えたことを各頁で明示し、英語内容を省略・補完しない。日本語の省略記号は原生成の途中終了を表す。原continuationはモデルの唯一の正解ではない。個別候補の毒性スコアは取得stateに付かず、per_instance_statsの5候補最大値等を特定候補へ割り当てていない。新たな生成API・採点APIは呼んでいない。

## 2020年の評価

Table2の5モデルの出現率10値、最大値平均と入力間標準偏差20値、Table3のGPT-2制御なし＋4制御手法の低スコア入力に関する15値を転記した（計45値）。標準偏差は学習の複数試行のばらつきではない。基本比較は25候補・top-p0.9・temperature1・最大20トークン。DAPT、ATCON、Vocabulary Shift、Word Filterの役割を本文で説明する。

PPLMは10,000入力・10候補・GPT-2-medium355M・top-k10・temperature1・最大20トークン。Table3の総括captionには25候補とあるが、本文§5.2とAppendix Table9の明示値10を採用した。他の124M GPT-2・25候補の値と同一条件の順位にしない。PPLMの低スコア入力の最大値平均0.32±0.19、出現率17％も条件付きで補足した。

TOXICITYは0〜1の較正済み分類器スコア。閾値0.5以上という判定、候補の最大値、入力単位の一度以上の出現、候補単位の割合を区別した。検出器の集団言及・言語変種への偏りと、文脈を読む必要性を原論文に即して説明する。論文の人手確認はOWTC文書100件とGPT-2生成100件、最初の3著者によるもの。人手判断とTOXICITY APIスコアの一致88％/80％、Pearson相関0.83/0.65。

## HELM

固定公開版v0.4.0のrun_specs全8,526件から42モデル・42実行を抽出した。選定するtext-davinci-003、OPT-175B、BLOOMの各実記録のsuiteはv0.3.0。3モデル分のstatsと、davinci003の全scenario_state（36,789,185 bytes）・per_instance_stats（7,702,757 bytes）を取得した。run名、URL、bytes、SHA256、adapter_specはdata-fetch-log.json/selected-runs.json/evidenceに保存。

0shot、各1,000入力、1試行、5候補、temperature0.9、最大20トークン、stop指定なし。実davinci003 requestのtop_pは1で、2020年のnucleus top-p0.9とは異なる。入力のseed0並べ替え後のIDで全1,000行を原データへ照合した。同文promptが原データに複数あるため、文字列辞書だけで原行の同一性を決めない。先頭1,000行をそのまま使ったとは説明しない。

davinci003は高223/その他777入力。低側にスコアnullの3入力が含まれる（id91844/id81016/id72808）。5,000候補枠のうち非空4,997。重複候補を含む要求13件、id16221は5候補中3候補が空。ToxicityMetricは空を除き、文字列キーのAPI応答辞書から0.5以上の件数を数えて非空候補数で割るため、同文重複の扱いにも注意を要する。score=0はtruthinessで一覧に入らないが、閾値以上の件数や最大値0の定義に影響する形ではない。実APIの新規応答は取得していない。

保存された摂動なしtest値のみ採用。davinci003の最大値平均・出現率・toxic_fracを高/低それぞれper_instance_statsから再集計し6値すべて一致。全1,000件の入力・ID・参照なし・trial0・提示例0・切詰め0・生成数・request条件を照合した。3モデルの公開statsから表示した12値の丸めを確認する。

## 制作・校正・検査

共通マスター由来の編集可能なnative PPTX、最終PPTXからLibreOfficeでPDFを作った。専用UserInstallationを使用。9 native表、1 native処理図、1 code。引用・コード59枠はPNGの灰色枠端と実glyph端から上下余白を測った。最終の数値はpanel-visible-gaps.json。

日本語スキルで全62頁を校正。実際のbefore/after/reason/pageをproofreading-changes.json、全頁のnative本文とPDF文言をpage-text-and-proofreading.jsonに保存した。特にdidn'tとsaid、引用発言を入力/後半の対応する範囲へ保持し、生成の訳は未完部分を補完しない。method/review_modeはskill_based_codex、gemini_used=false。

全62頁を個別にview_imageし、最終の変更24頁も再表示した。全頁overviewも確認した。最新の監査はlayout440段落/124セル・問題0、XSD新規0（master由来11は別記）、URL-only62件がPDF範囲まで完全一致、ノート0。これらの判定と最終hashはhandoff.json参照。検査範囲を実施以上に広げて記録していない。

本編33頁は、日本語本文・原例・評価表を中心に約10分で流し読む予定配分（595秒）。実測ではない。英文の全候補とAppendixをすべて読み上げる時間の保証ではない。独立レビューはcreate_cnndm担当へ引き継ぐ。


独立レビュー局所修正：p17は評定者相互の一致ではなく人手判断とAPIスコアの一致と明記。p51候補1訳はnot muchの否定を「できることはほとんどない……」で保持。2026-10-18に2頁再PDF・個別view、layout/package/link/実glyph余白を再検査した。

追加p44訳：配布原文don’t likeを「黒人が好きではない」へ忠実化し、著名発言の記憶から補正しない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/realtoxicityprompts.json)、[実際の校正対](skill-proofreading/realtoxicityprompts.md)、[全ページ文言](skill-proofreading/realtoxicityprompts/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/realtoxicityprompts/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/realtoxicityprompts/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
