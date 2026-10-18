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

## 2026-10-18：正解表示と出典表現の見直し

全44ページを点検。正解表示13か所、出典表現1か所を修正した。Geminiは使用していない。独立した正解表示は12.5ptから22ptの太字にし、答えと評価値は変更していない。図表番号は検証履歴に保持し、スライドではページ下の文献表示へまとめた。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|7|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|8|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|9|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|17|論文Table 3の強制二択。多数決ラベルの一致率96.4%とは別の量。|強制二択で評価。多数決ラベルの一致率96.4%とは別の量。|ページ下の文献表示で出典を特定できるため、本文の図表番号を削除。評価条件は保持。|
|27|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|28|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|29|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|30|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|31|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|32|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|33|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|34|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|35|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|36|正解：上の文（12.5pt）|正解：上の文（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|

[今回の点検・変更と範囲照合](blimp/answer-and-citation-review.json)
