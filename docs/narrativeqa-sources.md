# NarrativeQA：出典と制作記録

2026-10-18作成。本編37ページ、Appendix25ページ、計62ページ。本編は約10分の黙読・流し読みを想定し、閲覧時間は未実測。共通マスターを用いた編集可能なPPTXと、その最終版から出力したPDF。発表者ノートなし。

## 一次資料と版

|資料|URL|
|---|---|
|Kočiský et al. (2018), The NarrativeQA Reading Comprehension Challenge. TACL 6:317–328.|https://aclanthology.org/Q18-1023/|
|Google DeepMind, NarrativeQA. 公式配布CSV（2026-10-18取得）。|https://github.com/google-deepmind/narrativeqa|
|Liang et al. (2023), Holistic Evaluation of Language Models. TMLR.|https://arxiv.org/abs/2211.09110|
|HELM Classic v0.4.0, NarrativeQA. 2023-11-17の固定版。|https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/narrative_qa|
|Stanford CRFM, HELM NarrativeQA scenario. 2026-10-18確認。|https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/narrativeqa_scenario.py|
|NarrativeQA, Wikipedia summaries: LICENSE / ATTRIBUTION.|https://github.com/google-deepmind/narrativeqa/tree/master/third_party/wikipedia|

配布元 `google-deepmind/narrativeqa`、固定改訂 `904246f6d1fe99a99a08a03501fe3e619af2cee5`。取得CSV3ファイルは合計22,638,273 bytes。物語全文は未取得。作品1,572件・質問46,765件を全件集計した。論文本文の1,567作品と、表の分割合計・配布CSVの1,572作品との不一致は、原因を推測せず検証記録へ残した。

[検証データ](data-audits/narrativeqa.json)には取得物のSHA-256、集計方法、13実例の作品ID・QA位置・原レコード・全文要約・連続抜粋の文字オフセット・原文・訳を保存した。本編3例、追加10例はすべて別の作品。原文は選んだ抜粋・質問・2つの参照回答を1枚に保ち、訳が収まる7例では併記、それ以外は訳を次ページに置いた。原文の綴り・大文字・空白・誤記は保持した。

## 評価の照合

2018年の要約条件と全文条件は、入力と方式を分けた。人の回答同士のROUGE-Lを、物語全文を読む人の成績として扱わない。HELM v0.4.0のcanonical実行3モデルを、元のv0.3.0スイートのstats.jsonで確認。test・摂動なしのF1、完全一致、実際の平均提示例数を記録。OPT・text-davinci-003は3試行平均、Llama 2は1試行。最大5例という設定値と実際に入力へ入る例数を区別した。2026-10-18に公開HELMコードも取得し、現在も要約入力を読む実装があることを確認した。これは最新順位の調査ではない。

## 校正と描画確認

**Geminiは使用していない。** Codexが[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)をページごとに適用。[実際の修正前後](skill-proofreading/narrativeqa.md)、[全ページ文言](skill-proofreading/narrativeqa/pages.jsonl)、[検査記録](skill-proofreading/narrativeqa/review.json)を保存した。

全62ページを描画して一覧を確認し、引用・訳・表・グラフ・参考文献・公式画面を個別に拡大した。初稿で長い回答と出典が重なったため、回答を21ptのまま横並びにし、短い実例では原文と訳を左右に配置。長文では訳を独立させた。最終変更ページも再出力して個別確認。文字欠落・枠のはみ出し・出典との重なり0件、リンク52件はURL部分のみ。ネイティブ表8件、グラフ1件。標準XSDで新規エラー0件、マスター由来の既存11件と整数buSzPctの字句形式差は分離した。PowerPointでの手動開封は未実施、LibreOffice変換と構造検証を行った。

## 要約の出典と利用条件

リポジトリはApache 2.0、配布Wikipedia要約は[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)。以下の要約抜粋とその日本語訳にもCC BY-SA 3.0を適用する。要約の元記事URLはdocuments.csv由来。本文を連続抜粋し、日本語訳を追加した。質問・回答はNarrativeQAの公開注釈から取得した。元の物語本文の権利は別に確認する。

- 実例1：Wikipedia contributors, [A Voyage to Arcturus](http://en.wikipedia.org/wiki/A_Voyage_to_Arcturus)。連続抜粋と日本語訳。
- 実例2：Wikipedia contributors, [Arcade (film)](http://en.wikipedia.org/wiki/Arcade_(film))。連続抜粋と日本語訳。
- 実例3：Wikipedia contributors, [The Marriage of William Ashe](http://en.wikipedia.org/wiki/The_Marriage_of_William_Ashe)。連続抜粋と日本語訳。
- 実例4：Wikipedia contributors, [Lisbeth Longfrock](http://en.wikipedia.org/wiki/Lisbeth_Longfrock)。連続抜粋と日本語訳。
- 実例5：Wikipedia contributors, [The Old Wives' Tale](http://en.wikipedia.org/wiki/The_Old_Wives'_Tale)。連続抜粋と日本語訳。
- 実例6：Wikipedia contributors, [The Mystery of a Hansom Cab](http://en.wikipedia.org/wiki/The_Mystery_of_a_Hansom_Cab)。連続抜粋と日本語訳。
- 実例7：Wikipedia contributors, [Tancred (novel)](http://en.wikipedia.org/wiki/Tancred_(novel))。連続抜粋と日本語訳。
- 実例8：Wikipedia contributors, [Le Bal de Sceaux](http://en.wikipedia.org/wiki/Le_Bal_de_Sceaux)。連続抜粋と日本語訳。
- 実例9：Wikipedia contributors, [12 (2003 film)](http://en.wikipedia.org/wiki/12_(2003_film))。連続抜粋と日本語訳。
- 実例10：Wikipedia contributors, [The Sessions (film)](http://en.wikipedia.org/wiki/The_Sessions_(film))。連続抜粋と日本語訳。
- 実例11：Wikipedia contributors, [Broadcast News (film)](http://en.wikipedia.org/wiki/Broadcast_News_(film))。連続抜粋と日本語訳。
- 実例12：Wikipedia contributors, [The Hebrew Hammer](http://en.wikipedia.org/wiki/The_Hebrew_Hammer)。連続抜粋と日本語訳。
- 実例13：Wikipedia contributors, [A Dry White Season](http://en.wikipedia.org/wiki/A_Dry_White_Season)。連続抜粋と日本語訳。

## 独立レビュー後の最終版

作成者と別のサブエージェントが元の固定配布レコードと数値条件を独立照合。実例の原文・質問・参照回答を保持しつつ、幅と余白を調整して原文・訳の併記を追加した。全引用枠の可視字形上下余白は各6.67〜7.33pt。現在は本編37、全62ページ。改訂前の校正対・ページ番号は履歴として保存した。[独立レビュー](skill-proofreading/narrativeqa/independent-review/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/narrativeqa/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
