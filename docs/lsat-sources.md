# LSAT / AR-LSAT 制作記録

## 範囲と一次資料

HELM Classicのlsat_qa:task=allを1資料に統合する。対象はLSAT全体ではなく分析的推論のAR-LSAT。表紙にLaw School Admission Testを併記。2021年はAR-LSAT公開年で、試験制度の開始年ではない。主著はZhong et al., *AR-LSAT: Investigating Analytical Reasoning of Text*, arXiv:2104.06598v2（2021-04-15）。§3.2は1991–2016年の約90試験から5選択肢の分析的推論問題を収集したと記す。論文PDF、abstract、README、LICENSE、3分割JSON、HELM v0.3.0コードをevidenceに保存した。

公式配布は https://github.com/zhongwanjun/AR-LSAT 。取得時mainのcommitは41f78ca7be3e24602b694b9d6b78105fc0c8bfc6（2023-01-20）。official-repo-revision.jsonに記録。公式画面は通常のTLS検証を通したHTTP応答をChromiumで実描画。CSS/文字/画像の読込を目視し、official-site.pngとして掲載。GitHubのREADMEに2022年の別研究とcomplete_lsat_dataも載るが、HELMが使うdata/AR_*Data.jsonと混同しない。

## 論文と配布版の違い

論文Table 1・§5は計2046問、train1585/dev231/test230。今回取得した公式dataはtrain1630/280passages、dev231/40、test230/40、計2091問。差45問の増減経緯は確認できない。現在の本文・設問・全5選択肢・正解が、公開HELMのdev231/test230全461件と全件一致することを、ID以外の内容で照合した。質問文だけでは同一テキストが複数あるため、split・全選択肢も含めて照合した。

現在のtags[2]はtrain273/dev184/test182が空欄。テストでは1件に質問型の文字列を入れており、ゲーム型の辞書にない。公式v0.3.0 LSATScenario.get_question_typesをAST抽出して実行すると、train397/dev191/test183件がassertに失敗する。classification-replay.jsonに記録。過去の成功runが現在のtagsからそのまま作れるとは記さない。公開runの内容と一致する事実、現在の分類パーサとの不整合を区別する。

論文Table 1のordering42.5/grouping38.75/assignment18.75%は原研究の手分析として引用。現在の欠損tagsを使って割合を作り直していない。Table 2の設問型は一部のみ掲載し、全てを尽くす分布とは書かない。正解ラベルA–Eと、ARMの参加者・位置・論理関数抽出の人手評価注釈を区別した。

## HELM版・条件・独立再計算

掲載サイトはClassic v0.4.0（2023-11-17）、run suiteはv0.3.0。release run_specsから標準lsat_qaグループのmultiple_choice_jointを選び、ablation_multiple_choiceのseparate方式と混ぜていない。

- OPT-175B：test230×3試行、各19.1304348/22.6086957/24.3478261%、平均22.0289855%。
- text-davinci-003：test230×3、22.6086957/23.4782609/23.9130435%、平均23.3333333%。
- Llama 2 70B：test230×1、23.4782609%。

全1610test出力を読む。completionをlogprob降順で選び、stripした選択文字をoutput_mappingへ対応付け、正解選択肢と照合。全出力がA–Eの1文字であり、ラベル比較による再計算と公開quasi_exact_matchが3モデルで一致した。設定上max_train_instances5、実際も全testで5、prompt_truncated0。OPT/davinciのadapterはmax_tokens5・num_outputs1、Llama2はmax_tokens1・num_outputs5。3モデルの実requestはmax_tokens1・num_completions1で、各出力も1件。stopは設定上改行、実requestでは空配列。温度0。設定値と実リクエストを別記した。公開statsのtrial平均のcount3をtest件数と混同しない。raw request/resultと固定run URL・SHAはrun-fetch-log.json、stats.json、examples.jsonに保存。

原研究Table 5：BERT21.4/RoBERTa23.1/ARM30.9%。学習や探索を含む方式であり、HELMの5例提示と同条件ではない。人間59.7%は約100問をLSAT専門訓練のない大学生10人（文学・商学・法学）に解かせた平均。HELM230test全件の人間値や上限としては扱わない。

## 13実例と日本語

本編3・追加10の相異なるテスト設問を、短めで条件が完全な13passagesから選定した。統計的な無作為標本ではない。公式原文の全条件・設問・5選択肢・正解を1頁へ収め、その直後に日本語訳。訳のために原文を分割せず、原文の語句を削除しない。選択肢の横並び区切りと表示上の改行だけを加える。人名・記号は原綴りのまま保持。only if、否定、条件追加、人数上下限、排他的orを反転しない。日本語訳は採点参照ではない。

examples.jsonに公式元ID、HELM ID、原passage/question/options/answer、raw質問・passage、trial0実出力と元request全体、出所ファイルSHA、訳を保存。13例の全選択肢と正解を公式原JSON・公開run双方へ再照合。正解はモデルが出す出力形式と同じA–Eを21pt太字えんじで表示。原文の選択肢本文も全て掲載する。

実例1の解説配置は別途全720順列を列挙。10配置が条件を満たし、Yoshidaの位置は4/6。選択肢にあるのは4（B）だけ。evidence/chorus-solver.json。実例2はYoder不選択→Wong不選択、Myers選択→Ortega/Paine/Schmidt不選択で最大3人となり4人以上条件に反する。これらの説明は解説用の導出であり、元データの論理式注釈ではない。

## 公開範囲と権利

リポジトリにMIT License（Copyright 2022 Wanjun Zhong）がある。ただし文言はSoftwareおよび関連文書を対象とし、元LSAT試験問題の権利を明示的に譲渡する資料は確認していない。LSAC公式サイトにはCopyright表記がある。コードのライセンスだけから元試験問題の全体的な自由利用権を断定せず、資料では出典を示す解説用引用とした。現行LSAC Types of LSAT Questionsを取得し、LR/RCが現行案内に載ることを確認。2024変更告知の試行URLは403/404だったため、変更月・変更経緯の主張には使わない。

## 制作・検査

指定SlideMaster由来のnative PPTX、表9個。本文は日本語校正スキルをCodexで適用、Gemini未使用。62頁を個別表示し、全26引用頁・9表・3参考文献頁・公式画面を拡大確認。引用枠は一度PDF化し実字形bboxから上下余白を修正し、そのPPTXを再PDF化して検査した。各ページ文言、実校正対、原文照合、XSD差分/内部参照/shape ID、PDF字形、URL-only範囲、最終hashを同梱する。独立レビュー待ち。

再生成：prepare.py → build.py → convert.py lsat → fit-panels.py → convert.py lsat → render.py lsat → 各監査 → records.py。各スクリプトは本フォルダだけへ書き込む。

独立レビューで、学習1630レコードのうち本文・設問・全選択肢の一意な組は1609、21組が2重であることを確認。正解は同じでtagsに差がある（例200706_1-G_1_1とindia1_1-G_1_1）。開発・テストは各231/230組が一意。これは論文との45問差の経緯を解明したものではない。

独立レビューで、現学習1630レコードは5択1585問・4択45問と確認。開発231/テスト230は全て5択。本文の5択はHELMの評価および実例を指し、現在配布全体を一律5択とは説明しない。4択45問と論文学習件数との差45は数として一致するが、版の来歴とは断定しない。

## 独立レビュー完了
review-lsatで全62頁、全1610出力の写像後採点、3モデル各461原文、13問全5選択肢の独立総当たりを検証。設定差・4択45問・学習重複21組を反映した最終版が合格、未解決事項なし。最終hashはhandoff/review-lsatで一致。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/lsat.json)、[実際の校正対](skill-proofreading/lsat.md)、[全ページ文言](skill-proofreading/lsat/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/lsat/review.json)。
