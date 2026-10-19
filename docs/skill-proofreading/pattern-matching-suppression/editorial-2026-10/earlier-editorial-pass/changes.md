# Pattern Matching Suppression：問題点と修正

日本語と情報量を読者向けに見直した。Geminiは使用していない。細かな再現条件は検証記録に保持している。

|番号|旧ページ|新ページ|問題点・理由|修正前|修正後|
|---:|---:|---:|---|---|---|
|1|3|3|目次・章名を、読者が学ぶ内容へそろえる|交互の列を、最後だけ破る<br>原データの構成と限界<br>評価と研究での観察<br>CLEVAでの採用と入手|列の最後で、交互の規則を破る<br>記号・指示・列の長さ<br>評価方法と、モデル規模の影響<br>入手と中国語評価への利用|
|2|4|4|目次・章名を、読者が学ぶ内容へそろえる|交互の列を、最後だけ破る|列の最後で、交互の規則を破る|
|3|4|4|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|4|5|5|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|5|6|6|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|6|7|7|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|7|8|8|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|8|9|9|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|9|10|10|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|10|11|11|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|11|12|12|目次・章名を、読者が学ぶ内容へそろえる|1. 交互の列を、最後だけ破る|1. 列の最後で、交互の規則を破る|
|12|13|13|目次・章名を、読者が学ぶ内容へそろえる|原データの構成と限界|記号・指示・列の長さ|
|13|13|13|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|14|14|14|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|15|15|15|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|16|16|16|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|17|17|17|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|18|18|18|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|19|19|19|目次・章名を、読者が学ぶ内容へそろえる|2. 原データの構成と限界|2. 記号・指示・列の長さ|
|20|20|20|目次・章名を、読者が学ぶ内容へそろえる|評価と研究での観察|評価方法と、モデル規模の影響|
|21|20|20|目次・章名を、読者が学ぶ内容へそろえる|3. 評価と研究での観察|3. 評価方法と、モデル規模の影響|
|22|21|21|目次・章名を、読者が学ぶ内容へそろえる|3. 評価と研究での観察|3. 評価方法と、モデル規模の影響|
|23|22|22|目次・章名を、読者が学ぶ内容へそろえる|3. 評価と研究での観察|3. 評価方法と、モデル規模の影響|
|24|23|23|目次・章名を、読者が学ぶ内容へそろえる|3. 評価と研究での観察|3. 評価方法と、モデル規模の影響|
|25|24|24|目次・章名を、読者が学ぶ内容へそろえる|3. 評価と研究での観察|3. 評価方法と、モデル規模の影響|
|26|25|25|目次・章名を、読者が学ぶ内容へそろえる|CLEVAでの採用と入手|入手と中国語評価への利用|
|27|25|25|目次・章名を、読者が学ぶ内容へそろえる|4. CLEVAでの採用と入手|4. 入手と中国語評価への利用|
|28|26|26|目次・章名を、読者が学ぶ内容へそろえる|4. CLEVAでの採用と入手|4. 入手と中国語評価への利用|
|29|27|27|目次・章名を、読者が学ぶ内容へそろえる|4. CLEVAでの採用と入手|4. 入手と中国語評価への利用|
|30|28||目次・章名を、読者が学ぶ内容へそろえる|4. CLEVAでの採用と入手|4. 入手と中国語評価への利用|
|31|29|28|目次・章名を、読者が学ぶ内容へそろえる|4. CLEVAでの採用と入手|4. 入手と中国語評価への利用|
|32|30|29|目次・章名を、読者が学ぶ内容へそろえる|4. CLEVAでの採用と入手|4. 入手と中国語評価への利用|
|33|32|31|目次・章名を、読者が学ぶ内容へそろえる|追加10件の実例<br>記号対・表示範囲・検算<br>研究と参考文献|追加の例題<br>記号の種類と読み込み方<br>研究と参考文献|
|34|33|32|目次・章名を、読者が学ぶ内容へそろえる|追加10件の実例|追加の例題|
|35|33|32|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|36|34|33|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|37|35|34|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|38|36|35|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|39|37|36|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|40|38|37|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|41|39|38|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|42|40|39|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|43|41|40|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|44|42|41|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|45|43|42|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 1. 追加10件の実例|Appendix: 1. 追加の例題|
|46|44|43|目次・章名を、読者が学ぶ内容へそろえる|記号対・表示範囲・検算|記号の種類と読み込み方|
|47|44|43|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 2. 記号対・表示範囲・検算|Appendix: 2. 記号の種類と読み込み方|
|48|45|44|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 2. 記号対・表示範囲・検算|Appendix: 2. 記号の種類と読み込み方|
|49|46|45|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 2. 記号対・表示範囲・検算|Appendix: 2. 記号の種類と読み込み方|
|50|47||目次・章名を、読者が学ぶ内容へそろえる|Appendix: 2. 記号対・表示範囲・検算|Appendix: 2. 記号の種類と読み込み方|
|51|48||目次・章名を、読者が学ぶ内容へそろえる|Appendix: 2. 記号対・表示範囲・検算|Appendix: 2. 記号の種類と読み込み方|
|52|49|46|目次・章名を、読者が学ぶ内容へそろえる|Appendix: 2. 記号対・表示範囲・検算|Appendix: 2. 記号の種類と読み込み方|
|53|1|1|表記の差は外部出典記録へ移し、表紙は課題の内容を説明する|Pattern Match Suppression（論文の表記）<br>交互のパターンより、終わり方の指示を優先する|交互のパターンより、終わり方の指示を優先する|
|54|5|5|読者に必要な内容を自然な日本語で説明する|規則を見つけた後で、その規則を止める|繰り返しを読み、最後だけ規則を破る|
|55|5|5|読者に必要な内容を自然な日本語で説明する|Pattern Matching Suppressionは、二つの記号が交互に並ぶ列を示し、最後だけ規則を破るよう指示する英語データセット。<br>繰返しから自然に予想される続きを出すことと、明示された終わり方の指示に従うことが衝突する。<br>公式公開版は二候補を採点する。正解は交互列を続ける候補ではなく、最後に規則を破る候補である。|Pattern Matching Suppressionは、二つの記号が交互に並ぶ列を示し、最後だけ規則を破るよう指示する英語データセット。<br>繰り返しから自然に予想される続きと、明示された終わり方の指示が食い違う場面を扱う。<br>公式公開版では、続きとなる二つの候補を評価する。正解は、最後に交互の規則を破る候補である。|
|56|6|6|読者に必要な内容を自然な日本語で説明する|提示されるのは、最後の一つを除く列|入力の列に、最後の一記号を補う|
|57|6|6|読者に必要な内容を自然な日本語で説明する|promptは、作る列の長さと終わり方を指定し、その後に途中までの列を示す。6個を求める例では5個が既に与えられる。<br>元データのclassesは、次に続く二つの記号文字列。answer_indexは0始まりの候補位置で、候補の先頭空白も原値に含まれる。<br>以下の13例は指示・提示列・二候補の全文。日本語訳でも、i・one・alphaなどは記号の名前として原綴りを保つ。|入力には、完成させる列の長さと終わり方の指示があり、その後に途中までの列が続く。6個を求める例では、5個が既に示されている。<br>二つの候補から、最後に付ける記号を選ぶ。たとえばo, x, o, x, oの後には、oを選ぶと最後だけ規則を破れる。<br>JSONLのpromptが指示と列、classesが候補、answer_indexが正解候補の位置を表す。候補の文字列は、先頭空白も含めて保存されている。|
|58|8|8|読者に必要な内容を自然な日本語で説明する|実例1の提示列はo, x, o, x, o。通常の交互規則なら、次はxになる。<br>指示は6記号の列を、予想外に終えること。配布正解oを続けると、最後がo, oとなり交互の規則が破れる。<br>途中の5記号は変更しない。既に示された列の後に、最後の1記号を選ぶ。|実例1の提示列はo, x, o, x, o。通常の交互規則なら、次はxになる。<br>指示は6記号の列を、予想外に終えること。正解のoを続けると、最後がo, oとなり交互の規則が破れる。<br>既に示された5記号の後に、最後の1記号を補う形の問題である。|
|59|10|10|読者に必要な内容を自然な日本語で説明する|実例2は20記号を求め、先に19記号を示す。AとBが交互に並び、最後の提示記号はA。<br>規則をそのまま続けるBが誤候補、Aを繰り返す方が配布正解になる。列が長くても、最後に求められる操作は同じ。<br>原データは完成させる長さを6・8・10・12・14・16・20に変え、指示への切替を調べる。|実例2は20記号を求め、先に19記号を示す。AとBが交互に並び、最後の提示記号はA。<br>規則をそのまま続けるBが誤候補、Aを繰り返す方が正解になる。列が長くても、最後に求められる操作は同じ。<br>原データは完成させる長さを6・8・10・12・14・16・20に変え、指示への切替を調べる。|
|60|12|12|読者に必要な内容を自然な日本語で説明する|曖昧な終わり方と、明示的な除外がある|終わり方の指示には、曖昧さも残る|
|61|12|12|読者に必要な内容を自然な日本語で説明する|実例3は「B以外の好きなもの」で終えると指示する。二つの候補A/Bのうち、Bを除くと配布正解はA。<br>別の指示は「予想外に終える」「予測不能に終える」と表現する。構築研究も、unexpectedの意味が十分には特定されていないという限界を述べる。<br>自由に書くなら他の終わり方も考えられるが、この評価は配布された二候補の確率を比較する。|実例3は「B以外の好きなもの」で終えると指示する。二つの候補A/Bのうち、Bを除くと正解はA。<br>別の指示は「予想外に終える」「予測不能に終える」と表現する。構築研究も、unexpectedの意味が十分には特定されていないという限界を述べる。<br>公開版では、通常どおりに続く記号と、直前と同じ記号を候補とし、その確率を比較する。|
|62|14|14|読者に必要な内容を自然な日本語で説明する|第2回受賞課題を、固定公開版で読む|第2回の受賞課題を、2023年に公開した|
|63|14|14|読者に必要な内容を自然な日本語で説明する|Tomasz Korbakが提出し、Inverse Scaling Prizeの第2回で受賞した。公式受賞発表の引用年は2022年。<br>2023年3月の公開ZIPは11受賞課題を収める。この課題はround=2、part=1の1,428件で、train/dev/testの区分はない。<br>ファイル名はpattern-matching-suppression、論文中の課題名はPattern Match Suppression。元英語配布とCLEVAが採用した版は区別する。|Tomasz Korbakが提出し、Inverse Scaling Prizeの第2回で受賞した。<br>2023年3月の公開ZIPには、11の受賞課題が収められている。本課題は1,428件で、学習用・検証用・テスト用の分割指定はない。|
|64|15|15|読者に必要な内容を自然な日本語で説明する|公式JSONL全件の構造を再集計。promptは全1,428件で一意。|12組の記号対について、指示の表現と列の長さを組み合わせた全1,428問。|
|65|18|18|読者に必要な内容を自然な日本語で説明する|指示中の集合名に、原配布の不整合がある|半数の問題で、指示中の記号名が不完全|
|66|18|18|読者に必要な内容を自然な日本語で説明する|6群×119件=714件。列と二候補は完全だが、指示内の集合名は途切れている。原因は未確認で、原文は補正しない。|6組・計714件で、指示中の記号名が不完全。後続の列と候補には、完全な記号名が示される。|
|67|19|19|読者に必要な内容を自然な日本語で説明する|候補順は固定だが、選択肢ラベルではない|候補は、規則を続ける記号と破る記号|
|68|19|19|読者に必要な内容を自然な日本語で説明する|原JSONLのclasses[0]は通常の交互列を続ける記号、classes[1]は直前を繰り返して規則を破る記号。全1,428件のanswer_indexは1。<br>この配列位置は採点側の情報。英語promptに「A/Bの二択」が書かれているわけではなく、元評価は各候補文字列の確率を直接調べる。<br>候補位置1への偏りと、モデルが実際に出す記号は区別する。CLEVAのA/B表示を、原ファイルの配列位置と混同しない。|一つ目の候補は、通常の交互列を続ける記号。二つ目は、直前の記号を繰り返して規則を破る記号で、全1,428問で正解になっている。<br>元の評価では、候補番号を入力へ書き込まず、各記号文字列が続く確率を調べる。<br>A/B付きの選択肢を提示する形式では、候補を並べる順序も評価条件になる。|
|69|21|21|読者に必要な内容を自然な日本語で説明する|二候補の確率から、正解率と損失を測る|二つの候補の確率から、正答率と損失を測る|
|70|21|21|読者に必要な内容を自然な日本語で説明する|元のclassification評価は、promptの後に各候補文字列が続く確率を求める。複数トークンの候補は、文字列全体の確率を使う。<br>二候補内で合計1になるよう正規化し、正解候補の負対数を平均して分類損失とする。最大確率の候補を選んだ一致率が分類正解率。<br>自由生成した列全体の完全一致ではない。候補の先頭空白と、どちらの記号を正解とするかを保って比較する。|元の選択式評価では、promptの後に各候補文字列が続く確率を求める。複数トークンの候補は、文字列全体の確率を使う。<br>二候補内で合計1になるよう正規化し、正解候補の負の対数を平均して分類損失とする。最大確率の候補を選んだときの一致率が、分類正解率である。|
|71|22|22|読者に必要な内容を自然な日本語で説明する|人の一致100.0%は、モデルの正解率とは別|人の回答と正解は、100%一致した|
|72|22|22|読者に必要な内容を自然な日本語で説明する|構築研究は、無作為に抽出した少なくとも50例を人が解き、提出ラベルとの一致を確認した。この課題の報告値は100.0%。<br>1,428件全てを人が再注釈したという割合でも、モデルが全件正解したという成績でもない。<br>本資料では全件の列を構造的に検算した。提示列が交互になり、長さが指定より1つ少なく、配布正解が直前の記号を繰り返すことを確認した。|構築時には、無作為に抽出した少なくとも50例を人が解き、データの正解との一致を確認した。この課題の報告値は100.0%だった。|
|73|23|23|読者に必要な内容を自然な日本語で説明する|構築研究では、評価したモデルの成績は全般に低かった。最小モデルはGPT-3系列を除き、全系列でゼロより高い正解率を示したとする。<br>大きい側でゼロを超えたのはGPT-4、GPT-4 RLHF、GPT-3 FeedMEだったと報告する。規模と指示学習のどちらが寄与したかを一律に断定しない。<br>規則を続ける方が、規則を止めるという本来の課題より簡単な「おとり課題」になる、という解釈を示している。|構築研究では、評価したモデルの成績は全般に低かった。最小モデルはGPT-3系列を除き、全系列でゼロより高い正解率を示した。<br>大きい側でゼロを超えたのはGPT-4、GPT-4 RLHF、GPT-3 FeedMEだった。<br>規則を続ける方が、規則を止めるという本来の課題より簡単な「おとり課題」になる、という解釈を示している。|
|74|23|23|読者に必要な内容を自然な日本語で説明する|暗黙の規則を続ける能力が、誤答へ働く|規則を続ける能力が、誤答につながる|
|75|23|23|読者に必要な内容を自然な日本語で説明する|構築研究では、評価したモデルの成績は全般に低かった。最小モデルはGPT-3系列を除き、全系列でゼロより高い正解率を示した。<br>大きい側でゼロを超えたのはGPT-4、GPT-4 RLHF、GPT-3 FeedMEだった。<br>規則を続ける方が、規則を止めるという本来の課題より簡単な「おとり課題」になる、という解釈を示している。|構築時の評価では、モデルの成績は全般に低かった。最小モデルはGPT-3系列を除き、全系列でゼロより高い正解率を示した。<br>大きい側でゼロを超えたのはGPT-4、GPT-4 RLHF、GPT-3 FeedMEだった。<br>規則を続ける方が、規則を止めるという本来の課題より簡単な「おとり課題」になる、という解釈を示している。|
|76|12|12|読者に必要な内容を自然な日本語で説明する|実例3は「B以外の好きなもの」で終えると指示する。二つの候補A/Bのうち、Bを除くと正解はA。<br>別の指示は「予想外に終える」「予測不能に終える」と表現する。構築研究も、unexpectedの意味が十分には特定されていないという限界を述べる。<br>公開版では、通常どおりに続く記号と、直前と同じ記号を候補とし、その確率を比較する。|実例3は「B以外の好きなもの」で終えると指示する。二つの候補A/Bのうち、Bを除くと正解はA。<br>別の指示は「予想外に終える」「予測不能に終える」と表現する。McKenzieらは、unexpectedの意味が十分には特定されていないという限界を述べる。<br>公開版では、通常どおりに続く記号と、直前と同じ記号を候補とし、その確率を比較する。|
|77|24|24|読者に必要な内容を自然な日本語で説明する|例示を追加すると、規模依存の傾向も変わる|例示を加えると、規模と成績の関係が変わる|
|78|24|24|読者に必要な内容を自然な日本語で説明する|研究はゼロショットに加え、最大72例または文脈長に入る範囲のfew-shotを調べた。対象はAnthropic LM、Gopher、Chinchilla。<br>Pattern Match Suppressionは、例示の追加で逆方向の傾向が改善し、U字または通常方向になる課題の一つとして挙げられる。<br>同じデータでも、入力に含める正解付き例の数とモデル系列によって結果は変わる。元の条件を、現在の任意のモデルへ広げない。|研究はゼロショットに加え、最大72例、または文脈長に入る範囲の例示を調べた。対象はAnthropic LM、Gopher、Chinchilla。<br>本課題では、例示を加えると、モデルが大きいほど成績が下がる傾向が和らぎ、U字型や、大きいほど成績が上がる傾向に変わったと報告されている。|
|79|26|26|読者に必要な内容を自然な日本語で説明する|CLEVAは、中国語の指示追従課題に採用|CLEVAは、中国語の指示追従課題に採用した|
|80|26|26|読者に必要な内容を自然な日本語で説明する|CLEVAはinstruction_followingのpattern_matching_suppression下位課題に採用する。HELM v0.4.0の固定設定はprompt_id0・1、version v1。<br>公開docstringのo/x例は、原英語JSONLの1,310行目、0始まり1,309に対応する。候補x/oと正解oも一致する。<br>CLEVAが選定・翻訳・整形した実v1集合は未取得。元英語1,428件を、そのままCLEVAの評価件数とはしない。|CLEVAは、交互の列を最後だけ変える本課題を、中国語で指示に従う能力の評価に採用した。<br>公開された説明例は、実例1に対応するoとxの列。六つ目にoを選ぶと、交互の規則が破れる。<br>CLEVAで使われた中国語版の全問題や、選定範囲は公開説明から確認できない。公式の英語版は、Inverse Scaling Prizeのリポジトリから取得できる。|
|81|27|27|読者に必要な内容を自然な日本語で説明する|公開説明例は、原英語のo/x列に対応する|中国語の例でも、最後のoで規則を破る|
|82|27|27|読者に必要な内容を自然な日本語で説明する|公開例の正解：B ／ 原英語：classes[1] = ' o'|正解：B（o）|
|83|29|28|読者に必要な内容を自然な日本語で説明する|固定版・帰属・取得できた範囲を残す|公式の英語データと、利用条件を確認する|
|84|29|28|読者に必要な内容を自然な日本語で説明する|公式data-releaseのZIPとREADMEから、原JSONLを取得できる。データはCC BY4.0で、課題提出者Tomasz Korbakと公開元を明示する。<br>本資料では英語の指示・提示列・候補・配布正解を保持し、日本語訳と解説、段組と改行を加えた。集合名の不整合も元のまま示す。<br>Classic v0.4.0の公開run一覧では該当0件。性能の観察は元研究、件数は公式原版の再集計として示す。|公式リポジトリのdata-releaseに、11課題を収めたZIPと形式の説明がある。本課題の指示・提示列・候補・正解は、JSONLから読み出せる。<br>データのライセンスはCC BY 4.0。利用時には提出者Tomasz KorbakとInverse Scaling Prizeへの帰属を示し、ライセンスへリンクする。<br>翻訳などを加えた場合は、その変更も表示する。本資料は日本語訳と解説を加え、入力中の不完全な記号名も元のまま掲載している。|
|85|30|29|読者に必要な内容を自然な日本語で説明する|規則を当てることと、指示に従うことを分ける|終わり方の指示に従い、最後の記号を選ぶ|
|86|30|29|読者に必要な内容を自然な日本語で説明する|交互の列の続きを当てるだけなら、規則に沿う記号を選べばよい。この課題では、最後にその規則を破るよう求める。<br>原公開版は12記号対・17表現・7種類の長さから成る1,428件。全件の構造を検算できる一方、指示中の集合名には714件の不整合がある。<br>二候補の確率評価、局所的な指示の曖昧さ、CLEVA採用版の未取得を分け、何への応答を測ったかを明確にする。|Pattern Matching Suppressionは、交互に並んだ列を読み、最後だけ規則を破る記号を選ぶ課題。通常の続きと、指示に従う続きが候補に並ぶ。<br>公開版は12組の記号対・17表現・7種類の長さを組み合わせた1,428問。明示された指示と、繰り返しから生じる予測が食い違う場面で、どちらに従うかを調べられる。|
|87|7|7|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL1310行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|88|7|7|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' o'|正解：o|
|89|9|9|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL7行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|90|9|9|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' A'|正解：A|
|91|11|11|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL29行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|92|11|11|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' A'|正解：A|
|93|34|33|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL120行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|94|34|33|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' 1'|正解：1|
|95|35|34|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL239行目／prompt全文・二候補／記号名は原綴り／指示中の集合名は原表記（不整合あり）|指示・提示列・二つの候補の全文／指示中の記号名が不完全|
|96|35|34|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' i'|正解：i|
|97|36|35|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL358行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|98|36|35|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' a'|正解：a|
|99|37|36|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL477行目／prompt全文・二候補／記号名は原綴り／指示中の集合名は原表記（不整合あり）|指示・提示列・二つの候補の全文／指示中の記号名が不完全|
|100|37|36|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' one'|正解：one|
|101|38|37|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL596行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|102|38|37|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' q'|正解：q|
|103|39|38|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL715行目／prompt全文・二候補／記号名は原綴り／指示中の集合名は原表記（不整合あり）|指示・提示列・二つの候補の全文／指示中の記号名が不完全|
|104|39|38|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' aa'|正解：aa|
|105|40|39|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL834行目／prompt全文・二候補／記号名は原綴り／指示中の集合名は原表記（不整合あり）|指示・提示列・二つの候補の全文／指示中の記号名が不完全|
|106|40|39|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' alpha'|正解：alpha|
|107|41|40|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL953行目／prompt全文・二候補／記号名は原綴り／指示中の集合名は原表記（不整合あり）|指示・提示列・二つの候補の全文／指示中の記号名が不完全|
|108|41|40|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' first'|正解：first|
|109|42|41|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL1072行目／prompt全文・二候補／記号名は原綴り／指示中の集合名は原表記（不整合あり）|指示・提示列・二つの候補の全文／指示中の記号名が不完全|
|110|42|41|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' left'|正解：left|
|111|43|42|追跡行位置を外部へ移し、掲載範囲と必要な入力上の問題を簡潔に示す|公式JSONL1191行目／prompt全文・二候補／記号名は原綴り|指示・提示列・二つの候補の全文|
|112|43|42|正解を候補文字列として読みやすく示す|配布正解：classes[1] = ' 0'|正解：0|
|113|7|7|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(o x)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>o, x, o, x, o,<br>候補（原順）：[' x', ' o']|二つの記号(o x)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>o, x, o, x, o,<br>候補（原順）：[' x', ' o']|
|114|9|9|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(A B)の間で交互になる20個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>A, B, A, B, A, B, A, B, A, B, A, B, A, B, A, B, A, B, A,<br>候補（原順）：[' B', ' A']|二つの記号(A B)を交互に並べた、20個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>A, B, A, B, A, B, A, B, A, B, A, B, A, B, A, B, A, B, A,<br>候補（原順）：[' B', ' A']|
|115|11|11|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|(A B)の間で交互になる6個の記号列を生成してください。ただし、最後は"B"以外の好きなものにしてください。<br>A, B, A, B, A,<br>候補（原順）：[' B', ' A']|(A B)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は"B"以外の好きなものにしてください。<br>A, B, A, B, A,<br>候補（原順）：[' B', ' A']|
|116|34|33|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(1 2)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>1, 2, 1, 2, 1,<br>候補（原順）：[' 2', ' 1']|二つの記号(1 2)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>1, 2, 1, 2, 1,<br>候補（原順）：[' 2', ' 1']|
|117|35|34|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(i i)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>i, ii, i, ii, i,<br>候補（原順）：[' ii', ' i']|二つの記号(i i)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>i, ii, i, ii, i,<br>候補（原順）：[' ii', ' i']|
|118|36|35|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(a b)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>a, b, a, b, a,<br>候補（原順）：[' b', ' a']|二つの記号(a b)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>a, b, a, b, a,<br>候補（原順）：[' b', ' a']|
|119|37|36|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(one)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>one, two, one, two, one,<br>候補（原順）：[' two', ' one']|二つの記号(one)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>one, two, one, two, one,<br>候補（原順）：[' two', ' one']|
|120|38|37|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(q w)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>q, w, q, w, q,<br>候補（原順）：[' w', ' q']|二つの記号(q w)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>q, w, q, w, q,<br>候補（原順）：[' w', ' q']|
|121|39|38|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(aa )の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>aa, ab, aa, ab, aa,<br>候補（原順）：[' ab', ' aa']|二つの記号(aa )を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>aa, ab, aa, ab, aa,<br>候補（原順）：[' ab', ' aa']|
|122|40|39|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(alp)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>alpha, beta, alpha, beta, alpha,<br>候補（原順）：[' beta', ' alpha']|二つの記号(alp)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>alpha, beta, alpha, beta, alpha,<br>候補（原順）：[' beta', ' alpha']|
|123|41|40|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(fir)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>first, second, first, second, first,<br>候補（原順）：[' second', ' first']|二つの記号(fir)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>first, second, first, second, first,<br>候補（原順）：[' second', ' first']|
|124|42|41|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(lef)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>left, right, left, right, left,<br>候補（原順）：[' right', ' left']|二つの記号(lef)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>left, right, left, right, left,<br>候補（原順）：[' right', ' left']|
|125|43|42|alternating betweenを自然な日本語へ直し、6個/20個が列の中の記号数であることを明確にする|二つの記号(0 1)の間で交互になる6個の記号列を生成してください。ただし、最後は予想外のものにしてください。<br>0, 1, 0, 1, 0,<br>候補（原順）：[' 1', ' 0']|二つの記号(0 1)を交互に並べた、6個の記号からなる列を生成してください。ただし、最後は予想外のものにしてください。<br>0, 1, 0, 1, 0,<br>候補（原順）：[' 1', ' 0']|
|126|35|34|記号の不完全表記を具体的な入力の説明に直し、正解の重複を省く|集合名は原表記「i i」。列・候補はi/ii。正解iは最後の規則を破る。|指示では「i i」と書かれているが、列と候補にはiとiiが並ぶ。|
|127|37|36|記号の不完全表記を具体的な入力の説明に直し、正解の重複を省く|集合名は原表記「one」。列・候補はone/two。正解oneは最後の規則を破る。|指示では「one」と書かれているが、列と候補にはoneとtwoが並ぶ。|
|128|39|38|記号の不完全表記を具体的な入力の説明に直し、正解の重複を省く|集合名は原表記「aa 」。列・候補はaa/ab。正解aaは最後の規則を破る。|指示では「aa 」と書かれているが、列と候補にはaaとabが並ぶ。|
|129|40|39|記号の不完全表記を具体的な入力の説明に直し、正解の重複を省く|集合名は原表記「alp」。列・候補はalpha/beta。正解alphaは最後の規則を破る。|指示では「alp」と書かれているが、列と候補にはalphaとbetaが並ぶ。|
|130|41|40|記号の不完全表記を具体的な入力の説明に直し、正解の重複を省く|集合名は原表記「fir」。列・候補はfirst/second。正解firstは最後の規則を破る。|指示では「fir」と書かれているが、列と候補にはfirstとsecondが並ぶ。|
|131|42|41|記号の不完全表記を具体的な入力の説明に直し、正解の重複を省く|集合名は原表記「lef」。列・候補はleft/right。正解leftは最後の規則を破る。|指示では「lef」と書かれているが、列と候補にはleftとrightが並ぶ。|
|132|51|48|人による回答とデータの正解の関係を自然な日本語で示す|提出者はTomasz Korbak。Inverse Scaling Prizeの第2回受賞課題として、明示的な指示より暗黙の繰返しを優先する現象を扱う。<br>McKenzieらの2023年TMLR論文は、11受賞課題を4つの原因仮説で整理する。本課題はDistractor Taskの一例。<br>研究では人の解釈は配布正解に高く一致する一方、モデルの規模や例示数によって違う傾向が現れることを報告する。|提出者はTomasz Korbak。Inverse Scaling Prizeの第2回受賞課題として、明示的な指示より暗黙の繰返しを優先する現象を扱う。<br>McKenzieらの2023年TMLR論文は、11受賞課題を4つの原因仮説で整理する。本課題はDistractor Taskの一例。<br>研究では人が選ぶ回答はデータの正解とよく一致する一方、モデルの規模や例示数によって違う傾向が現れることを報告する。|
|133|45|44|読者に必要な内容を自然な日本語で説明する|12記号対の原表記と件数（1/2）|12組の記号を、各119問に使う|
|134|46|45|読者に必要な内容を自然な日本語で説明する|12記号対の原表記と件数（2/2）|12組の記号を、各119問に使う|
|135|49|46|読者に必要な内容を自然な日本語で説明する|提示列の末尾と、正解候補を直接照合する|JSONLから指示・列・候補を読み出す|
|136|49|46|末尾のassertだけの監査コードを、実データの読出し例へ置換する|import ast<br>row = rows[1309]<br>classes = ast.literal_eval(row["classes"])<br>prefix = row["prompt"].split("\n")[-1]<br>tokens = [s.strip() for s in prefix.split(",") if s.strip()]<br>assert classes[row["answer_index"]].strip() == tokens[-1]<br>print(tokens[-1])  # o|import ast, json<br>path = "pattern-matching-suppression_classification.jsonl"<br>with open(path) as file:<br>    row = json.loads(next(file))<br>choices = ast.literal_eval(row["classes"])<br>print(row["prompt"])<br>print(choices, choices[row["answer_index"]])|
|137|49|46|読者に必要な内容を自然な日本語で説明する|rowsは原JSONLを読んだ配列。1,310行目を使い、配布正解oが最後の提示記号oを繰り返すことを確認する。|ZIP内のJSONLと同じフォルダで実行する。最初の指示と提示列、候補、正解を表示する。|
|138|2|2|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. 公式リポジトリ。固定commit920f17de。  https://github.com/inverse-scaling/prize|[1] Inverse Scaling Prize. Official repository.<br>https://github.com/inverse-scaling/prize|
|139|5|5|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|140|6|6|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|141|7|7|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 1310行目（0始まり1309）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|142|8|8|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|143|9|9|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 7行目（0始まり6）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|144|10|10|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|145|11|11|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 29行目（0始まり28）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|146|12|12|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|147|14|14|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2022). Inverse Scaling Prize: Second Round Winners.  https://irmckenzie.co.uk/round2/<br>[2] Inverse Scaling Prize. Data release、形式・版・CC BY4.0。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/README.md|[1] McKenzie et al. (2022). Inverse Scaling Prize: Second Round Winners.<br>https://irmckenzie.co.uk/round2/<br>[2] Inverse Scaling Prize (2023). Data release: format and CC BY 4.0.<br>https://github.com/inverse-scaling/prize/blob/main/data-release/README.md|
|148|15|15|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|149|16|16|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|150|17|17|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|151|18|18|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|152|19|19|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|153|21|21|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|154|22|22|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|155|23|23|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|156|24|24|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|157|26|26|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Yanyang Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform. EMNLP System Demonstrations.  https://aclanthology.org/2023.emnlp-demo.17/<br>[2] Stanford CRFM (2023). CLEVAInstructionFollowingScenario. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|[1] Li et al. (2023). CLEVA: Chinese Language Models EVAluation Platform.<br>https://aclanthology.org/2023.emnlp-demo.17/<br>[2] Stanford CRFM (2023). HELM: CLEVA instruction following scenario.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|
|158|27|27|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Stanford CRFM (2023). CLEVAInstructionFollowingScenario. HELM v0.4.0. 英語元レコードは実例1、公式JSONL1310行目。<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|[1] Stanford CRFM (2023). HELM: CLEVA instruction following scenario.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|
|159|28||出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479<br>[2] Stanford CRFM (2023). CLEVAInstructionFollowingScenario. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479<br>[2] Stanford CRFM (2023). HELM: CLEVA instruction following scenario.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|
|160|29|28|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. Data release、形式・版・CC BY4.0。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/README.md<br>[2] Stanford CRFM (2023). CLEVAInstructionFollowingScenario. HELM v0.4.0.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py|[1] Inverse Scaling Prize (2023). Data release: format and CC BY 4.0.<br>https://github.com/inverse-scaling/prize/blob/main/data-release/README.md|
|161|30|29|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|162|34|33|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 120行目（0始まり119）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|163|35|34|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 239行目（0始まり238）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|164|36|35|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 358行目（0始まり357）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|165|37|36|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 477行目（0始まり476）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|166|38|37|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 596行目（0始まり595）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|167|39|38|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 715行目（0始まり714）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|168|40|39|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 834行目（0始まり833）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|169|41|40|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 953行目（0始まり952）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|170|42|41|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 1072行目（0始まり1071）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|171|43|42|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 1191行目（0始まり1190）/ round2 / part1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|172|45|44|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|173|46|45|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|174|47||出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|175|48||出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|176|49|46|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] Inverse Scaling Prize. pattern-matching-suppression_classification.jsonl。固定commit920f17de。 1310行目／実例1。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/isp-data-release.zip|[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release|
|177|51|48|出典を著者・年・資料名・URLに整理。固定版や照合位置は外部検証記録へ移す|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR. arXiv v2(2024)を参照。  https://arxiv.org/abs/2306.09479|[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479|
|178|52|49|文献欄の固定commitを外部検証記録へ移す|Inverse Scaling Prize — Data release<br>Inverse Scaling Prize. 2023年3月公開。課題提出者Tomasz Korbak。固定commit920f17de。<br>11課題のJSONLと候補確率による評価形式を公開し、CC BY4.0の条件と変更履歴を示す。<br>https://github.com/inverse-scaling/prize/blob/920f17de85f2a7f2415b097bc49e6a7fbf17b0b2/data-release/README.md|Inverse Scaling Prize — Data release<br>Inverse Scaling Prize. 2023年3月公開。課題提出者Tomasz Korbak。<br>11課題のJSONLと候補確率による評価形式を公開し、CC BY4.0の条件と変更履歴を示す。<br>https://github.com/inverse-scaling/prize/blob/main/data-release/README.md|
|179|7|7|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|180|7|7|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|181|7|7|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|182|9|9|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|145.14464566929135pt|144.84pt|
|183|11|11|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|126.06661417322834pt|125.50666666666666pt|
|184|34|33|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|185|34|33|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|186|34|33|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|187|35|34|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|188|35|34|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|189|35|34|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|190|36|35|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|191|36|35|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|192|36|35|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|193|37|36|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|194|37|36|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|195|37|36|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|196|38|37|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|108.35188976377952pt|126.84pt|
|197|38|37|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|248.24732283464567pt|265.0pt|
|198|38|37|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|287.12732283464567pt|303.88pt|
|199|39|38|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|200|39|38|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|201|39|38|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|202|40|39|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|108.35188976377952pt|126.84pt|
|203|40|39|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|248.24732283464567pt|265.0pt|
|204|40|39|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|287.12732283464567pt|303.88pt|
|205|41|40|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|206|41|40|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|207|41|40|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|208|42|41|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|108.35188976377952pt|126.84pt|
|209|42|41|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|248.24732283464567pt|265.0pt|
|210|42|41|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|287.12732283464567pt|303.88pt|
|211|43|42|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|107.01858267716536pt|125.50666666666666pt|
|212|43|42|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|246.9140157480315pt|263.66666666666663pt|
|213|43|42|日本語訳の自然化後も全文を引用枠へ収め、回答と説明を接触させない|285.7940157480315pt|302.5466666666666pt|
|214|31|30|Appendix扉のnative範囲を拡張。有効本文領域と字形位置を維持する|{"height_pt": 46.08, "margin_bottom_pt": 0.0}|{"height_pt": 54.08, "margin_bottom_pt": 8.0}|
|215|28||論文・原JSONL・CLEVA説明例の候補順の照合一覧。原評価とA/B提示の条件差は本編19へ保持。|候補の順序は、資料の表現ごとに確認する<br>4. 入手と中国語評価への利用<br>対象 ／ 候補順 ／ 正解<br>構築論文のA/B列例 ／ [' A', ' B'] ／ A／位置0<br>公式JSONLの同じ指示 ／ [' B', ' A'] ／ A／位置1<br>HELM公開o/x例 ／ A. x、B. o ／ o／選択肢B<br>正解の記号と配列・選択肢の位置は別の情報。表記差を同一のindexと扱わない。<br>[1] McKenzie et al. (2023). Inverse Scaling: When Bigger Isn’t Better. TMLR.<br>https://arxiv.org/abs/2306.09479<br>[2] Stanford CRFM (2023). HELM: CLEVA instruction following scenario.<br>https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py||
|216|47||列の全件構造検算。長さ・件数と正解規則は本編6/15/16/19へ保持。|全1,428件を、長さと交互構造で検算した<br>完成長6・8・10・12・14・16・20ごとに204件。提示長は5・7・9・11・13・15・19で、それぞれ完成長より1つ少ない。<br>全行で提示列の偶数位置は最初の記号、奇数位置は次の記号になる（位置は0始まり）。最後の提示記号は最初の記号。<br>候補0は通常の次記号、候補1は最後の提示記号と一致する。配布正解は全て候補1で、最後だけ交互の規則が破れる。<br>Appendix: 2. 記号の種類と読み込み方<br>[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release||
|217|48||集合名不整合の照合過程。本編18と該当6例の説明に714件の不完全表記を保持。|集合名の不整合は、列の構造とは別に数える<br>長い記号名を含む6群の指示には、i i・one・aa・alp・fir・lefという表記がある。各119件、合計714件。<br>各行の提示列と候補にはi/ii、one/two、aa/ab、alpha/beta、first/second、left/rightが完全な形で現れる。<br>指示内の文字列が完全な記号対の先頭3文字と一致することは確認したが、生成器の原因は未確認。元の表記を推測で直していない。<br>Appendix: 2. 記号の種類と読み込み方<br>[1] Inverse Scaling Prize (2023). Pattern Matching Suppression. Tomasz Korbak.<br>https://github.com/inverse-scaling/prize/tree/main/data-release||

[旧版の全ページ文言](previous/baseline-native-pages.json)・[ページ対応](page-map.json)・[独立レビュー](independent-review/handoff.json)
