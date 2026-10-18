# BLiMP：スキルによる日本語校正

Geminiは使用していない。Codexが日本語校正スキルを1ページずつ適用した。実際の変更対を示す。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|5|文法的に許容される文と、特定の規則に違反する文を対にした英語の評価集合である。1対を1問として扱う。|文法的に許容される文と、特定の文法規則に違反する文を対にした英語の評価集合である。1対を1問として扱う。|規則の対象を明示する。|
|34|対立点：名詞を省略した後のthreeに、形容詞roughだけを続けている。|対立点：名詞を省略したthreeの後に、形容詞roughだけを続けている。|語の位置関係を、誤解のない語順で説明する。|
|5|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|11|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|12|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|13|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|16|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|17|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|23|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|41|[1] Alex Warstadt et al. (2019). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|[1] Alex Warstadt et al. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. TACL 8, 2020.  https://aclanthology.org/2020.tacl-1.25/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|8|対立点：単数の女性を指すherselfと、数の一致しないthemselvesを対比する。|対立点：この生成設定ではJodiを単数・女性として扱い、herselfとthemselvesの数の対応を対比する。|生成設定で想定した数・性の対応を説明する。|
|13|Hugging Faceのsplit名|公開ミラーの分割名|表セルの末尾1文字だけの折返しを解消する。|
|35|対立点：hideは自動詞として使えるが、この用法のseeには目的語が必要になる。|対立点：生成テンプレートではhideを自動詞、seeを目的語が必要な他動詞として扱っている。|英語のすべての用法へ一般化せず、配布ラベルが前提とする用法を明示する。|

[全ページの記録](blimp/pages.jsonl)・[検査とレイアウト変更](blimp/review.json)・[出典](../blimp-sources.md)
