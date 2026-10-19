MedQA 調査・出典・検査記録

対象はJinらのMedQAと、HELM v0.3.0のMedQAScenario。ギャラリー年は初回arXiv公開の2020年とする。2023年はHELM固定コード版の年であり、データセットの初公開年と区別する。資料は53頁、本編32頁、公式米国版testの本編3問＋付録10問。13問はいずれも質問・全4候補・注釈正解を省略せず、同じ頁に全文の日本語訳を置く。短く全問表示でき、遺伝・薬理・機序・診断・検査などの違いが分かるよう目的抽出しており、代表的な無作為標本ではない。

主な一次資料

- Di Jin, Eileen Pan, Nassim Oufattole, Wei-Hung Weng, Hanyi Fang, Peter Szolovits (2020). *What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams*. arXiv:2009.13081v1. https://arxiv.org/abs/2009.13081v1
  公式HTML v1は取得時の無版指定HTMLとbyte単位で同一。evidence/paper-v1.html のSHA-256は a9c034b24f07cd9cc7f5aa3b41868150f60b550c0df1677fa9df7fa0d197d42d。§3.2とTable 3（3言語とsplit）、§3.3/Table 6（dev100問の2型分類）、§4.1（台湾版の英訳）、Table 7/8（検索＋読解baseline）を照合。論文の表はevidence/primary-tables.jsonにも抽出。
- 著者の公式リポジトリ MedQA。https://github.com/jind11/MedQA
  固定commit 27b02f66aac217933c9648a06f82e9f720377925。READMEとLICENSEをcommit URLでも再取得し、現在の取得bytesと一致。evidence/pinned-sources.jsonにURL・bytes・SHAを記録。READMEはUS/Mainland/Taiwan、US/Mainlandの4_options版、質問と教科書の公式配布先を説明する。
- 公式READMEとHELM双方が指すdata_clean.zip。https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view
  通常の公開ダウンロード確認フォームを経て取得。131,741,885 bytes、SHA-256 1c2ca8130b3d86d9a99a432ab9bef14f3bb9807bef20facd9ac86ba36960f629。evidence/archive-retrieval.jsonとarchive-members.jsonに経路・全ZIPメンバーを記録。教科書は抽出せず、質問のみローカルevidenceへ抽出した。Macの._ファイルはJSONL集計から除外。
- Stanford CRFM (2023). MedQAScenario, HELM v0.3.0. https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/med_qa_scenario.py
  evidence/scenario-v030.py、SHA-256 474883333bb75344e76043a2ca39e53961c617086f389055c09e7e1e8b3678ff。docstringには5択の説明例があるが、実装はUS/4_options/phrases_no_exclude_{train,dev,test}.jsonlを読み、4択をassertする。devをvalidへ変換する。
- Stanford CRFM (2023). get_med_qa_spec / MultipleChoiceJointAdapter / BasicMetric, HELM v0.3.0。URLはbuild-info.jsonとスライドのfooterに記録。
  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/run_specs.py
  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/adaptation/adapters/multiple_choice_joint_adapter.py
  https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/basic_metrics.py
- HELM Classic latest設定とv0.4.0配布JSON。https://crfm.stanford.edu/helm/classic/v0.4.0/
  2026-10-18に取得済みの共有release schema / run_specs / runs_to_run_suitesを読み、med_qa、MedQA、class名等を大文字小文字を区別せず検索。該当公開runは0件。schemaは主指標quasi_exact_match、testを定義する。モデルの得点はないので作成していない。stats.jsonの36.7/70.1/42.0%は2020年の構築時baselineで、HELMの成績ではない。

言語・選択肢・規模の照合

英語USMLE12,723問、簡体字中国語MCMLE34,251問、繁体字中国語TWMLE14,123問、合計61,097問。別地域の問題を収集したもので、同じ問題の3言語翻訳集合ではない。通常splitはUS/Mainlandが5択、Taiwanが4択。US/Mainlandの4_optionsは全件4択。全6組の5択/4択splitで、同順序の問題文、正解本文、候補の部分集合関係を照合し、全46,974問が一致した。論文は誤答1件の削除と選択肢順の並べ替えを説明する。

split実測はUS10,178/1,272/1,273、Mainland27,400/3,425/3,426、Taiwan11,298/1,412/1,413。全9値がTable 3と一致。USの未分割US_qbankは14,369行で4〜13択、Mainlandの未分割qbankは34,253行。分割済み最終集合と同じ件数として扱わない。data-summary.jsonに全18ファイル群の集計を記録。US4択のmeta_infoはtrain step1=5,629 / step2&3=4,549、dev701/571、test679/594。

HELM変換・採点

verify.pyは公式シナリオのASTからインフラimportだけをローカルのInput/Output/Reference/Instance型とダウンロード済み質問パスへ置換し、選択ロジックは変更せず全12,723件を実行した。全件で質問、候補順、各1件のcorrectタグ、answer_idxと正解本文の対応が一致。入力questionの完全一致によるsplit交差は0。全50,892候補のうち647件は末尾の引用符と空白が整形された。scenario-audit.jsonに前後の実例と検証結果を記録。13例の原レコード、JSONLの1始まり行番号と0始まり位置、SHAをexamples.jsonに保持する。識別子US/4_options/test/267等はこの資料で作った位置識別子。

joint adapterはA〜Dの文字を生成させ、output_mappingによって候補本文へ写してからBasicMetricで比較する。予測の前後空白はstripするが、小文字d、D.、本文100%を直接出しても文字キーDには一致しない。data-audit.jsonのmetric_input_testsは原関数を用いた制御入力の試験であり、公開モデルの出力を装ったものではない。num_outputs=5は要求のtop_k_per_tokenへ渡し、num_completionsは1。max_train_instances=5、max_tokens=1、temperature=0はコード既定値で、存在しない公開runの実測条件ではない。

医学・翻訳・入力範囲

原文の選択肢、誤記（adherance、sacroplasmic、Labetolol等）、正解文字と本文は改変していない。日本語は標準的な医学用語で全文を訳し、病態、薬剤、年齢、数値、否定、時制、候補の対応を各問照合した。原文にない測定方向「直径」を補った訳を除き、14 mmという記述のみ保持する修正を行った。全13問の訳と原文はexamples.jsonとスライドで一致する。

test[945]はgreen arrowを参照するが、JSONLレコードに画像フィールドはない。この観察をp31に示し、構築時に画像問題をすべて除外したという未確認の説明は採用しなかった。13表示例には画像を必要とする問題を選んでいない。論文で米国版の症例型98%という値は、devから無作為に選んだ100問の注釈結果であり、全件注釈として扱わない。

権利と可搬な配布範囲

公式リポジトリのLICENSEはMIT License、copyright (c) 2022 Di Jin。これはSoftwareと関連文書についての文面で、収集した試験問題や教科書の第三者の権利まで一律に解消するものと解釈しない。論文はfair useを理由とする選択肢加工を説明するが、データ全体をCC BYと宣言してはいない。調査中に見た第三者HF mirrorのCC BYラベルは公式条件として採用していない。

PPTX/PDFとexamples.jsonは、出典を付した選択13問の引用と日本語訳を含む。フルZIP、質問全件、全HELM変換結果、教科書をrepoや配布フォルダへコピーしない。handoff.jsonのdo_not_publishに明記した。これらのローカルevidenceは再検証用である。元の配布元へのリンク・各レコードの識別情報・hashを残す。

制作・校正・目視検査

共通SlideMaster由来のnative PPTX。著者sasakiy84、所属なし、JST日付、ノートなし。編集可能な8表・1グラフ、引用/コードはnative text、回答は22pt/bold/accent1 B13731。日本語校正はskill_based_codex、gemini_used=false。架空の修正対を作らず、実際に変更したp24/p41のbefore/afterと理由をproofreading-changes.jsonに記録。全頁の最終文言と校正結果はpage-proofreading.json。

最終PPTXからPDFを再変換し、全53頁を個別view_imageで閲覧した。公式画面はChromiumでCSSロードされた実画面を確認。全13例の質問・全候補・訳を1枚ずつ検査し、全8表、nativeグラフ、コード、2文献/頁の参考文献も拡大して確認。修正したp24/41、余白を調整したp45と本編例p7/9/11、native文献枠を実字形の範囲へ拡張したp51/52/53は最終版で再目視。visual-review.jsonに実際の閲覧頁を記録。

26引用枠と1コード枠のPNG可視文字を測定し、上下余白は6.67〜7.33pt。layout/text/link/package監査は最終版で問題0。URL-onlyのnative runとPDFリンク56件の文字範囲が一致。標準XSDはマスター由来既存11件と新規0件を分けて記録。各検査JSONとhandoffの最終hashを参照。独立レビューは2026-10-18にcreate_twitterが合格と判定。全53頁、公式原行13例、全46,974版間対応、HELM読込/採点/要求と医学訳を独立確認し、修正依頼・未解決なし。記録は /workspace/artifacts/helm-parallel/review-medqa/review.json と review.md。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/medqa.json)、[実際の校正対](skill-proofreading/medqa.md)、[全ページ文言](skill-proofreading/medqa/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/medqa/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/medqa/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
