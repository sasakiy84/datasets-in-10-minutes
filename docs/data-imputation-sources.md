# Data imputation — Buy / Restaurant 制作・出典記録

日本語54頁（本編29頁）、sasakiy84、所属なし。作成日2026-10-18 JST。共通SlideMasterからnative PPTXを制作し、その最終PPTXを専用LibreOffice profileでPDFへ変換した。スライド本文・引用・12表は編集可能なnative要素。ブラウザ画像は公式IPM GitHubの画面のみ。ノートなし、外部生成API不使用。

## 範囲と一次資料

HELM Classicの表示名はData imputation、シナリオ名はentity_data_imputation。リリースv0.4.0（2023-11-17）から抽出した134 run_specsはBuy/Restaurant各67モデルで、引数のdatasetはこの2種類だけ。元suiteは選定6条件ともv0.3.0。性能比較は全モデル一覧ではなくOPT-175B、text-davinci-003、Llama 2 70Bの3モデルを選んだ。

固定コード：https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/entity_data_imputation_scenario.py
現在コード：https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/entity_data_imputation_scenario.py
提示条件：https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py
採点：https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py
公開記録：https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/entity_data_imputation

取得した固定シナリオのread_tables/get_splits/serialize_rowをASTから直接実行し、全1,515行の分割・入力全文・正解を再現した（verify_data.py / input-and-score-audit.json）。独自の再記述だけに頼らない。mainの同3メソッドはAST一致で、現在のダウンロード先はHELMミラーへ変更されている。元配布と現在ミラーの2アーカイブはそれぞれバイト一致した。各ファイルのbytes/SHA-256はevidence/file-manifest.json、取得URLはfetch-log/run-fetch-log/additional-fetch-log/source-indexに記録。

## 二つの表と前処理

Buy：元Abt-Buy.zipにはAbt.csv（1,081行）、Buy.csv（1,092行）、正対応表（1,097組）。HELMで読むのはBuy.csvだけで、照合対応表やAbt側の行は使わない。元配布 https://dbs.uni-leipzig.de/file/Abt-Buy.zip （リダイレクト先は取得log）。配布説明 https://dbs.uni-leipzig.de/research/projects/benchmark-datasets-for-entity-resolution 。

固定実装はidを除き、description欠損441行だけを除外する。残り651行にはprice欠損269行が残り、文字列nanとなって入力される。manufacturerの欠損は元6行、処理後0行。隠す属性はmanufacturer、残す列はname/description/price。seed=1234のpandas.sampleによりtrain469/valid117/test65。testのprice欠損は33行。全表のmanufacturer正解文字列は62種類、test30種類（表記を統合しない）。

Restaurant：https://www.cs.utexas.edu/users/ml/riddle/data/restaurant.tar.gz 。HELMはfz.arffの864行を読み、電話番号を含まないfz-nophone.arffは使わない。class列を除外し、他の列から二重引用符と前後空白を除きdropna。今回のファイルは除外0行。隠す列city、入力はname/addr/phone/type。train622/valid156/test86。city正解文字列は全表49種類、test14種類。

Restaurantは照合用のため同じ店を示すclassを共有する行を含む。元classは752種類。分割単位は行で、test86行中17行はtrainにも同classの別行がある。この17は学習表への重複であり、プロンプトに提示した5例への混入率ではない。classは入力へ含まない。元のFodor’s/Zagat’s記録とREADMEも同じアーカイブに含まれる。READMEはSheila Tejada→Nick Kushmerickという受領経緯、電話番号を含む照合は容易すぎるという説明を記す。HELMの課題はその照合とは別のcity補完である。

入力は属性名+「: 」+元値を「. 」で連結し、最後に「. manufacturer?」または「. city?」。docstringにある縦棒区切りやtitle名の例と実際のname列・ピリオド区切りを混同しなかった。元セルが唯一の参照正解で、自然欠損に新しい人手注釈を付けたものではない。

## 公開実行と再採点

3モデル×2表の全2,968 request（重複試行を含むvalid/test）を元表と全件照合した。Buyは各モデル182個、Restaurantは各モデル242個の異なるvalid/test行。入力・参照正解・HELMのID・分割が全件一致する。testは計1,057出力（151行×OPT3/davinci3/Llama1試行）を再採点した。

主指標quasi_exact_match：Buy OPT85.1282051%、davinci85.6410256%、Llama86.1538462%。Restaurant OPT59.3023256%、davinci82.1705426%、Llama81.3953488%。各モデル/表のexact/quasi/prefix/quasi-prefixの4指標が公開statsと一致した。独自実装の照合に加え、取得したBasicMetricの公式関数をASTから実行して再検算した。

normalize_textは小文字化→ASCII句読記号除去→a/an/the除去→空白整理。同義語辞書・地理的包含関係・商標名統合はない。LACIE/LaCieはquasi一致、Canon Camcorders/CanonとLG Electronics/LGとla/los angelesとnew york city/new yorkは不一致。prefixはpred.startswith(gold)で、OPTのtest id778第1試行は正解new york・出力new york cityなのでexact/quasi0、prefix/quasi-prefix1（metric-demonstration.json）。逆向きの包含を同じ採点としない。

全モデル実送信はmax_tokens5、num_completions1、温度0、stop newline、5学習例、prompt_truncated0。OPT/davinci3試行、Llama1試行。設定と実送信の差は今回なかった。候補一覧なしのgenerationで“What is the missing value?”→正解付き5例→対象行→Answer:、自由生成した文字列を採点する。出力表は前後空白を除いた表示で、raw出力は保持。

## 研究と版の違い

Mei, Song, Fang, Yang, Fang, Long (2021), **Capturing Semantics for Imputation with Pre-trained Language Models**, IEEE ICDE, 61–72, DOI10.1109/ICDE51399.2021.00013。

作者公式IPM：https://github.com/EliasMei/IPM 、固定commit583826e41205c04a48548673945213181085536c。READMEのmain取得と固定commit版はバイト一致。IPM-Multiは値を多クラス分類、IPM-Binaryは候補ごとの適否を2値分類し、事前学習モデルを追加学習する。READMEとsrcの実装を照合した。公式READMEが補完属性を挙げる8データはwalmart/amazon/restaurant/buy/housing/phone/zomato/flipkart。HELMの対象はこのうち2表。READMEの10%欠損の5サンプルとHELMの3試行の少数例提示を同一視しない。

**取得上の限界**：Mei論文のIEEE landingは202/0bytes、stampPDFとCrossrefのPDF先は418で本文取得に失敗。著者サイトの候補URLも404。OpenAlex/Semantic ScholarではOA本文URLがなく、arXiv題名検索でも該当なし。本文を読んだと記録せず、作者公式README/実装を直接確認して手法と対象属性を説明し、未読本文の表・性能値を採用していない。書誌はCrossrefの正しいDOI、作者README、出版社へのリンクで照合。crossref-guess.jsonは調査初期の別論文への誤った候補であり、採用出典ではない。検索HTMLも根拠へ使っていない。

HELMの一次論文 **Holistic Evaluation of Language Models** (Liang et al., TMLR2023)、E.3.12を実際に確認。本文のBuy470/118/66・Restaurants623/157/87は今回の元配布/固定コード/公開実行と各1件ずつ異なる。本文には2表を列挙しながらthree datasetsとする箇所、city補完と一般化する記述もある。実装と公開記録に即してBuy manufacturer、Restaurant cityの2表として説明し、件数差をp46に具体的に示した。差の来歴は断定しない。原研究IPMの結果とHELMの少数例生成の結果を同じ条件で順位付けしていない。

Buy元データの帰属：Köpcke, Thor, Rahm (2010), **Evaluation of entity resolution approaches on real-world match problems**, Proceedings of the VLDB Endowment3(1)。Leipzigの公式公開ページで著者・年・掲載先・題名・概要を照合し、配布ページの帰属依頼に応じp54で紹介した。

## 実例・翻訳・公開範囲

examples.jsonは本編3/Appendix10の独立13行（Buy6/Restaurant7）。全てtestから選定し、説明用の選定であって平均的な難易度の標本としない。各例に元の1-based物理行番号、0-based表row_index、rawレコード、元ファイルSHA、元行UTF-8の完全バイト（元のCRLF/LFを含む）とSHA、日本語訳、正解、HELM ID、原scenario_stateのSHAとselector、raw出力を保存した。Buy.csvにはCRLFがあるため、raw行hashはread_textによる改行正規化を避けて元バイトから計算した。全13原行を再照合済み。

原文はHELMに実際に渡した属性列の全文。各例の原文を1頁の左、対応する訳を右に保ち、翻訳のために原文を分割・省略しなかった。元セルの正解は書換えず、独立表示21pt bold #B13731。日本語の属性名、機器仕様・数値・金額・nan、住所・電話番号・否定を確認。Sony/Speckの対応機器とメーカーを混同しない。52' / 13'は該当するテレビ/ノートPCのインチ表記として訳し、原入力のアポストロフィはそのまま保持。住所と固有名の綴りを保持した。

Buy配布ページはCC BY4.0へのリンクを明記する。リンク先ライセンス本文の取得は403だったため、本文を今回取得したとは記録しない。配布ページの表示と参照先を示した。RestaurantのREADMEに独立した再配布ライセンス表示は見当たらず、public accessを自由な再配布許可と同一視しない。IPM repoにもLICENSEファイルは一覧になく、勝手にコード/元表のライセンスを付与しない。

資料・可搬examplesは解説用に選んだ行と出力を引用する。全アーカイブ、展開全表、全processed-rows、全scenario_state、学習5例を含む完全promptはローカル照合用で、可搬資料へ一括再配布しない。examplesのrecordではrequest.promptを明示して除き、対象行からAnswer:までの連続末尾prompt_tailを保持。元の完全記録はevidence/selected-records-full.jsonおよび各scenario_stateに保持する。p23のprefix実出力は追加の採点説明としてmetric-demonstration.jsonへ別保存。

## 日本語・描画・監査

master-guided-slides / dataset-introduction-slides / japanese-proofreadingを使用。method/review_mode=skill_based_codex、gemini_used=false。実際の日本語修正対はproofreading-changes.jsonに4件、最終全頁文言と校正項目はpage-review.json。組版の実修正はlayout-changes.json。訳や数量を変えない文を架空に修正したとは記録しない。

初稿53頁の全頁を個別view_imageで確認し、最終変更12頁（6/13/14/16/23/46/47/50/51/52/53/54）を再度個別確認。その時点の残る42頁は、実際に見た版とPNGのSHAが一致した。独立レビュー後には引用枠17箇所を持つ14頁をさらに再描画・個別確認した。最終overviewも確認した。visual-view-log.json/visual-review.jsonに実施範囲と画像hashを記録。表/引用/参考文献/公式画面を全頁拡大した。初回はPDFの字形bboxを使い、27引用枠を上inset5pt・下余白8ptへ調整した。独立レビューで実画素のinkを測定すると17枠の下余白が4.1〜4.9pt長かったため、該当枠だけ高さを縮めて上下をそろえた。native引用13組、答え/出典の距離、タイトル・表セルの単独1〜2字折返し、字形・重なりを確認した。

最終監査：layout333段落/122セル問題0、native table12、notes0、text54頁欠落0、URL-only56箇所（PDF文字中心/ネイティブrunともURLのみ）、XSD新規0（マスター既存11を区別）、図形ID/内部参照/ZIP整合合格、cross-shape字形重複0。PDFリンクの字形bboxによる隣接行の拾い込み6件は、文字中心とnative runでURLのみであることを独立に検証し、links-auditに詳細を保持した。

PPTX/PDFの最終hashとレビュー引継ぎ状態はhandoff.json。独立レビューは引継ぎ時点で未実施。

## 独立レビュー対応（進行中）

p50の参考文献説明から制作過程の文「手法説明は作者公開実装とも照合した。」を削除。本文未取得という調査範囲は本記録に保持する。yearは初稿でIPM研究年2021を入れていたが、資料主題のHELMシナリオの初出年2022へ修正する。一次根拠はHolistic Evaluation of Language Models, arXiv:2211.09110v1, 16 Nov2022, E.3.12 Data Imputation（evidence/helm-paper-v1.txt）で、既にBuy/Restaurantsを記載する。Abt-Buy元表2010・IPM研究2021・HELM課題化2022を区別する。Restaurant元表の初公開年は今回の一次資料では未確定。PPTX内のMei2021表記は研究年として正しいため保持する。

独立レビューの第3対応：review-data-imputation/panel-ink-checks.jsonの全27枠を形状ID/先頭文と結び、上下差>2ptの17枠だけをtop-bottom分縮小。変更はp7/8/9/20/32〜41の14頁で、全頁を再度個別view。残り10枠、原文/訳/字体/位置/答え/出典は保持。panel-ink-corrections.jsonにbefore/after高さと測定値を保存。

## 独立レビュー最終承認

create_pileによる独立レビュー合格、未解決0。全54頁の個別view、1515行/2968request/1057test出力の4公式指標、13全文対訳・原行/hashを独立照合。修正14頁を再viewし27枠の実画素上下差は最大0.674pt。54PNGを最終PDFから独立再描画しバイト一致。承認記録はreview-data-imputation/review.jsonおよびreview.md。最終PPTX194521baaa9cfe9c7797d52eaccb449f814d838c1f2520bab28d08b80a8702be、PDF12d38c09ae4b9aea047d5e60980777872fbc74af5782cc3c992ce6823e0d1cad。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/data-imputation.json)、[実際の校正対](skill-proofreading/data-imputation.md)、[全ページ文言](skill-proofreading/data-imputation/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/data-imputation/review.json)。
