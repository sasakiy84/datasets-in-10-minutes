# MMLU：スキルによる日本語校正

Geminiは使用していない。Codexが日本語校正スキルを1ページずつ適用した。実際の変更対を示す。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|12|同じ科目から5問を少数例提示用に確保し、開発集合とテスト集合を分けた。特定科目の微調整だけを目標にした大規模学習集合ではない。|各科目で5問を少数例提示用に確保し、開発集合とテスト集合を分けた。特定科目の微調整だけを目標にした大規模学習集合ではない。|各科目に5問ずつあることを明確にする。|
|37|質問：政府は、何を使ってインフレを測定するか。|質問：政府は、何を使って物価上昇を測定するか。|この設問のinflationを自然な日本語で表す。|
|5|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|11|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|12|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|13|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|16|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|17|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|23|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|50|[1] Dan Hendrycks et al. (2020). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|[1] Dan Hendrycks et al. (2021). Measuring Massive Multitask Language Understanding. ICLR 2021.  https://arxiv.org/abs/2009.03300|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|

[全ページの記録](mmlu/pages.jsonl)・[検査とレイアウト変更](mmlu/review.json)・[出典](../mmlu-sources.md)

## 2026-10-18：正解表示と出典表現の見直し

全53ページを点検。正解表示13か所、出典表現1か所を修正した。Geminiは使用していない。独立した正解表示は12.5ptから22ptの太字にし、答えと評価値は変更していない。図表番号は検証履歴に保持し、スライドではページ下の文献表示へまとめた。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|7|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|8|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|9|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|17|論文Table 1の重み付き平均。UnifiedQAは他のQA集合で学習したモデル。|重み付き平均。UnifiedQAは他のQA集合で学習したモデル。|ページ下の文献表示で出典を特定できるため、本文の図表番号を削除。評価条件は保持。|
|27|正解：D（12.5pt）|正解：D（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|29|正解：D（12.5pt）|正解：D（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|30|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|31|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|32|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|33|正解：D（12.5pt）|正解：D（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|34|正解：D（12.5pt）|正解：D（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|35|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|36|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|37|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|

[今回の点検・変更と範囲照合](mmlu/answer-and-citation-review.json)
