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
