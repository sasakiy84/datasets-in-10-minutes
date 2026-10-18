# MedQA 独立レビュー：合格

未解決事項なし。作者フォルダを変更せず、公式原配布・論文・HELMコード・原記録と最終PPTX/PDFを独立確認した。修正依頼はない。

- 公式ZIPのSHAを再計算し、13例をZIP内JSONLの該当原行へ直接照合。3地域9splitの計61,097問、US/Mainland通常5択と4択の全46,974対応、質問・正解・候補の部分集合が一致。
- 公式HELM v0.3.0メソッドを別namespaceで全12,723問実行。各4候補と正解タグ、末尾整形647件が一致。未分割US_qbank14,369問を最終12,723問と混同しない。
- 公式get_med_qa_spec・joint adapterをcapture実行。最大提示5、max_tokens1、num_outputs5がtop_k_per_tokenへ渡り、num_completions1となる。文字A–Dを本文へ写す処理を確認。原関数による制御入力D/空白D/d/D./100%の結果は資料と一致。
- 公開runとsuite索引を独自抽出し0件。原論文の36.7/70.1/42.0%は検索+読解の2020基準値で、HELM成績とは区別されている。3言語が同じ問題の翻訳集合ではないこと、台湾の実験時英訳、英18/中33教科書、dev100問の型2=98%を原論文に照合。
- 13問の医学訳で、年齢・性別・薬剤・閾値・否定・候補・正解を確認。β2 antagonistとmuscarinic antagonist、QT短縮、14mmの記述、甲状腺/副甲状腺既往、蛋白尿と複屈折の区別を保持。原英語の誤記と元正解はそのまま。test[945]のgreen arrow言及と画像fieldなしを確認し、画像問題全除外と断言していない。
- 全53頁とoverviewを実際に個別表示。13例の原文と訳は全文同頁で保持、独立回答22ptえんじ、全8native表・1chart・コード・3参考文献頁に欠落/接触なし。独立したshape間字形測定も重複0。ノートなし。
- ソフトウェアMITと試験問題/教科書の第三者権利を区別し、フルZIP・全質問・教科書を納品しない範囲を明記。可搬13例は出所と原行・hash付き。

独立検証のコードと数値はcheck.py/check_spec.py、independent-data-check.json/independent-spec-check.json/independent-artifact-check.json、shape_gaps.py/independent-shape-overlap.json。最終PPTX/PDFのSHAはreview.jsonへ保存し、作者handoffと一致した。
