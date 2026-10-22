# Finance Agent Benchmark：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルで作成し、作成担当とは別の担当が内容・原票・描画を確認した。以下は実際に行った修正の対である。最終版の確認範囲とファイルの対応は検証票に記録した。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|1,5,6,13,14,15,16,17,19,21,22,27,28,29,59|Finance Agent|Finance Agent<br>Benchmark|表紙に正式名称を含めた。|
|6|最初から決算書全文が質問に添付される課題ではない。エージェントが検索して資料を取得する。|入力は質問文で、エージェントが検索して資料を取得する。|入力と調査の流れを直接説明する。|
|19|どの数値や説明を満たしたかを細かく確認できる。|どの要点を満たし、どこに誤りがあるかを確認できる。|「満たす」の目的語を自然にした。|
|39|この取引先が予期しない事態でも処理の大幅な中断を防げるよう、適切なバックアップや代替措置を備えていると考えている。|この委託先が適切なバックアップと代替措置を備えており、不測の事態でも処理の大幅な中断を避けられると考えている。|会社の見解と委託先の対応を主語の明瞭な文にした。|
|40,41|正社員|フルタイムの従業員|full-time employeesを雇用契約上の正社員と同一視しない。|
|46,52|に終了する年度|に終了した年度|終了済みの会計年度に過去形を用いた。|
|24|採点は重要な基準を必須条件にし、残る基準の達成度を重み付きの部分点にする。|採点は各基準の達成度を重要度に応じて重み付けし、部分点を付ける。|必須基準が加重平均の分母から除かれるとの誤読を避ける。|
|28|公式リポジトリを展開した場所から読む。Rubric列にはJSON形式の採点基準が入る。|リポジトリ内で実行。Rubric列はJSON形式。|相対パスの位置を正確にし、説明と出典の重なりを解消した。|
|30|全問正解か部分点かを確認して結果を読む。|1問ごとの正誤判定か、部分点かを確認して結果を読む。|全問題に正解する意味と区別した。|
|34|中央値|予想の中心値|midpointを統計的なmedianと混同しない。|
|52|各節を一つのKPIとして|各節は一つの主要な業績指標（KPI）を表す|文を自然にし、専門略語を説明した。|
|47|株式報酬費用：19億3,500万米ドル。|株式報酬費用：19億3,500万米ドル<br>（1.935 billion dollars）。|原問のbillions単位を併記し、意味の切れ目で改行した。|
|34|予想予想の中心値|予想の中心値|根拠記録中の語の重複を修正。PPTX/PDF本文は変更しない。|
|全体|CFO example input/JP and reference answer on two pages|p7 one page with full original/JP/labelled answer/explanation|short example fits readably; retain meaningful detail|
|全体|v1.1 update details/results and archived v2 score table in main|Appendix pp55–57; current v2.1 table p26 after version/scoring explanation|prioritize current published results and relevant comparison conditions|
|全体|TJX answer cites only Q3 release|p11 cites Q3 guidance and Q4 actual results|support both sides of comparison|
|全体|AMD range column/header left aligned|p35 numeric range values and header right aligned|numeric column consistency|
|全体|cover/Appendix/long JP/reference URL ink extends native text frames|native frames expanded without truncating text or shrinking ordinary body orphan text|all actual glyphs remain within editable frames|

[全ページ文言](finance-agent/pages.jsonl)・[最終検証票](finance-agent/review.json)・[メインの確認](finance-agent/main-review.json)
