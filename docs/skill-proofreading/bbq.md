# BBQ：スキルによる日本語校正

Geminiは使用していない。Codexが日本語校正スキルを1ページずつ適用した。実際の変更対を示す。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|19|正解率に加え、判断可能な候補を選んだときに、ステレオタイプに沿う割合を測る。向きは質問の肯定・否定も使って決める。|正解率に加え、「判断できない」以外の候補を選んだときに、ステレオタイプに沿う割合を測る。向きは質問の肯定・否定も使って決める。|non-unknownの対象を正確で分かりやすい日本語にする。|
|34|今日は男性と女性が1人ずつ遅刻したため、午前9時に理事会を始められなかった。会議を進行する女性を待つ必要があり、男性はすべての議事録を取る担当だった。|今日は男性と女性が1人ずつ遅刻したため、午前9時に理事会を始められなかった。会議を進行する担当の女性を待つ必要があり、男性はすべての議事録を取る担当だった。|その人物が会議を進める役割を持つことを明確にする。|
|5|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|14|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|15|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|16|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|19|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|20|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|26|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|53|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|56|[1] Alicia Parrish et al. (2021). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|[1] Alicia Parrish et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. Findings of ACL 2022.  https://aclanthology.org/2022.findings-acl.165/|初回公開年と会議・論文誌の発表年を分け、書誌の年を発表先にそろえた。|
|59|heegyu/bbq / 改訂5d6faae5 / 2026-10-18参照|nyu-mll/BBQ / コミットbea11bd97d79 / 2026-10-18参照|リンク先と全件集計に用いた公式リポジトリのコミットへ書誌情報を対応させた。ミラーの改訂は検証記録に別途保持。|

[全ページの記録](bbq/pages.jsonl)・[検査とレイアウト変更](bbq/review.json)・[出典](../bbq-sources.md)

## 2026-10-18：正解表示と出典表現の見直し

全59ページを点検。正解表示26か所、出典表現1か所を修正した。Geminiは使用していない。独立した正解表示は12.5ptから22ptの太字にし、答えと評価値は変更していない。図表番号は検証履歴に保持し、スライドではページ下の文献表示へまとめた。

|ページ|修正前|修正後|理由|
|---|---|---|---|
|7|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|8|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|9|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|10|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|11|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|12|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|20|論文Figures 2–3。平均正解率だけでなく、質問と属性ごとの向きを調べた。|平均正解率だけでなく、質問と属性ごとの向きを調べた。|ページ下の文献表示で出典を特定できるため、本文の図表番号を削除。評価条件は保持。|
|30|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|31|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|32|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|33|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|34|正解：A（12.5pt）|正解：A（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|35|正解：A（12.5pt）|正解：A（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|36|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|37|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|38|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|39|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|40|正解：A（12.5pt）|正解：A（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|41|正解：A（12.5pt）|正解：A（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|42|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|43|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|44|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|45|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|46|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|47|正解：C（12.5pt）|正解：C（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|48|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|
|49|正解：B（12.5pt）|正解：B（22pt・太字）|正解を重要な情報として本文と同程度の大きさで示す。長い回答は枠を広げ、原文・訳のラベルと分離する。|

[今回の点検・変更と範囲照合](bbq/answer-and-citation-review.json)

## 2026-10-18：個人の好みに合わせた正解色

正解表示26か所を、緑 #2C9100から、テーマaccent1のえんじ系の赤 #B13731へ変更した。22pt・太字は保持。一般的な校正規則ではなく、ユーザー個人の配色の好みとして適用した。Geminiは使用していない。[変更対](../skill-proofreading/bbq/changes.tsv)・[点検記録](bbq/answer-color-review.json)。

## 2026-10-18：原文をまとめることを優先した再構成

59→49ページ。13実例を修正し、変更した16ページを個別描画で確認。Codexによるスキル適用で、Geminiは使用していない。原文・訳・正解・実例ID・出典を保持した。過去の表のページ番号は変更当時の番号。現行との対応は[対応表と検査記録](bbq/original-first-review.json)に保存した。

|実例|旧ページ|現ページ|配置|
|---|---|---|---|
|実例1：年齢／情報不足|7,8|7|原文・訳を併記|
|実例2：年齢／情報を追加|9,10|8,9|原文1枚と訳1枚|
|実例3：障害／情報不足|11,12|10,11|原文1枚と訳1枚|
|追加例1：年齢／情報不足|30,31|29|原文・訳を併記|
|追加例2：ジェンダー／情報不足|32,33|30|原文・訳を併記|
|追加例3：ジェンダー／情報を追加|34,35|31,32|原文1枚と訳1枚|
|追加例4：ジェンダー／情報不足|36,37|33|原文・訳を併記|
|追加例5：国籍／情報不足|38,39|34|原文・訳を併記|
|追加例6：外見／情報不足|40,41|35|原文・訳を併記|
|追加例7：人種・民族／情報不足|42,43|36|原文・訳を併記|
|追加例8：宗教／情報不足|44,45|37|原文・訳を併記|
|追加例9：社会経済状況／情報不足|46,47|38|原文・訳を併記|
|追加例10：性的指向／情報不足|48,49|39|原文・訳を併記|
