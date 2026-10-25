# DeepSearchQA：出典と確認範囲

制作：sasakiy84、2026-10-25。日本語校正はローカルの日本語校正スキルに従う Codex による。Gemini・外部生成 API・モデル評価は実行していない。本編28頁の600秒は計画値で未実測、全52頁、実データ13例（本編3・補足10）。

## データ・論文・採点

- Google DeepMind, [DeepSearchQA](https://huggingface.co/datasets/google/deepsearchqa)。固定 revision `b2623f8653065c2672de6d941fc5434cd652376c` の README と CSV。全900行を取得し、型・17分野の件数を再集計。採用13問の原文と参照回答の全項目を固定CSVと照合した。全900問を人が精読したという意味ではない。ライセンスは公式メタデータの Apache 2.0。[全文](licenses/deepsearchqa/LICENSE-DeepSearchQA-Apache-2.0.txt)・[帰属と翻訳変更の説明](licenses/deepsearchqa/ATTRIBUTION-DeepSearchQA.txt)を保存。
- Nikita Gupta et al. (2026), [DeepSearchQA: Bridging the Comprehensiveness Gap for Deep Research Agents](https://arxiv.org/abs/2601.20975)。2025-12-11公開のGoogle PDFと現arXiv版を取得・比較。制作者が読んだ範囲は本文1–10頁と採点プロンプトの付録15–16頁。書誌一覧11–14頁を全精読したとは主張しない。
- Lukas Haas & Shrestha Basu Mallick (2025), [Build with Gemini Deep Research](https://blog.google/technology/developers/deep-research-agent-gemini-api/)。公開時期と公式紹介。Kaggleの紹介画面はHTTP200でもクライアントのトークンエラーが発生したため有効な紹介画像として使わず、CSSのあるGoogle公式公開記事を実画面で確認して使用した。失敗ログと採用画面を区別して保存。
- [DeepSearchQA Starter Code](https://www.kaggle.com/code/andrewmingwang/deepsearchqa-starter-code)。独立レビュアーが公開コードを取得し、制作者も採点プロンプト・`aggregate_ratings` の該当箇所を静的に読んだ。実行していない。論文は単一回答を二値と述べる一方、公開実装には回答型の分岐がなく、共通の集合P/R/F1を使うため、スライドは一般の集合指標で説明する。無効な判定・空の判定・空のモデル回答は集計対象から除かれる。論文本文の完全正解率66.09/65.18の逆転表記は表と公開資料に照合し、表の対応を採用した。
- Moonshot AI, [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3)（2026-10-25取得）。DeepSearchQA F1 95.0（max）を採用例として示す。個別の試行回数・harness条件が明示されないため、他社を同一条件の順位表に並べない。公開時の論文実験とは分離。

## 13例の根拠

固定CSVの行番号は0始まり。[原文・訳・正解・対応頁](skill-proofreading/deepsearchqa/examples.json)、[集計と読了範囲](data-audits/deepsearchqa.json)、[実際の修正対](skill-proofreading/deepsearchqa/proofreading.json)を保存。原文の問題設定と参照回答は変更していない。

|例|行|権威ある参照先と確認内容|
|---:|---:|---|
|1|123|[SSA州別全データ](https://www.ssa.gov/oact/babynames/state/namesbystate.zip)。制作者が1975年のME/TX/CA各上位5件を抽出し、共通3件を再計算。独立担当も別取得して一致。|
|2|364|[JMLR v1](https://jmlr.org/papers/v1/)、[v2](https://jmlr.org/papers/v2/)、[v3](https://jmlr.org/papers/v3/)。制作者が全著者一覧の積集合を算出し3名を照合。独立担当も別取得して一致。|
|3|10|[NWS Natural Hazard Statistics](https://www.weather.gov/hazstat/)。制作者が2017–2021年の各洪水PDFを読み、死者が出た州数18/23/24/18/22、死者合計136/80/92/57/146を比較。個別PDFは `https://www.weather.gov/media/hazstat/flood17.pdf` から `flood21.pdf`。独立担当も別計算。|
|4|29|[NHS肩痛](https://www.nhs.uk/symptoms/shoulder-pain/)と[関節過可動性症候群](https://www.nhs.uk/conditions/joint-hypermobility-syndrome/)。制作者が症状とリンク先の平衡・協調運動の記述を読解。医学的な個別診断を行ったものではない。|
|5|55|[ArcBest SEC 10-K](https://www.sec.gov/Archives/edgar/data/894405/000155837024001622/arcb-20231231x10k.htm)、[Saia SEC 10-K](https://www.sec.gov/Archives/edgar/data/1177702/000095017024019368/saia-20231231.htm)、[Matson年次報告](https://investor.matson.com/static-files/01e585c3-1f4f-47ab-8f9b-a0a74eaef883)。制作者が該当する2022/2023営業費用表を読み、減少額ArcBest379.658百万ドル、Matson237.6百万ドル、Saiaは99.368百万ドル増を確認。報告書全体を読了したとは主張しない。|
|6|80|[Scott本人Teaching](https://www.johnhgscott.com/teaching.html)と[Publications](https://www.johnhgscott.com/research--publications.html)。独立担当が2015/2017年人工言語授業・ドイツ語授業・2012年共著を別取得して確認。制作者による大学学科トップの弱い出典は本人ページへ修正。|
|7|219|[BIE](https://www.bie-paris.org/site/en/all-world-expos)。独立担当がWorld ExpoとSpecialised Expoの区別を保って1929/1992を確認。|
|8|229|[Art Institute of Chicago](https://www.artic.edu/collection)。独立担当が美術館の出版した図録を載せるA&AePortalの個別作品メタデータで2作品の所蔵・年・油彩を照合。美術館本体の403は本文取得成功と扱っていない。ニューメキシコは「制作地」でなく描かれた場所。|
|9|286|[Lehman 2022–23](https://lehmanathletics.com/sports/mens-basketball/roster/2022-23)と[2023–24](https://lehmanathletics.com/sports/mens-basketball/roster/2023-24)。独立担当が全ロスターを読み上位2人の身長を合計。79+77=156インチ、79+79=158インチ。|
|10|828|[RFK Human Rights](https://rfkhumanrights.org/)と[Nobel Prize](https://www.nobelprize.org/)。独立担当がRipple of Hope受賞者とノーベル平和賞の年を照合。制作者のNobel直接取得403は成功と主張しない。|
|11|109|[FSU本人紹介](https://religion.fsu.edu/person/matthew-goff)、[公式CV](https://religion.fsu.edu/sites/default/files/media/files/faculty/cv/2024-09_goff_cv.pdf)、[SBL Society Report 2023](https://www.sbl-site.org/wp-content/uploads/2024/05/2023.SocietyReport.pdf)。独立担当はFSU現行紹介を直接取得してChicago PhD2002・教員を確認。リンク先2024公式CVは404、SBL報告の直接取得は403だったためSBL公式検索索引の抜粋で編集委員を確認し、本人公開2015年CV（https://fsu.academia.edu/MatthewGoff/CurriculumVitae）のweb本文でDuke共著2014年論文を照合した。|
|12|852|[Smithsonian Libraries Unbound](https://blog.library.si.edu/)。独立担当が2023年9月の公式アーカイブのbylineと著者アーカイブ最終26頁を読み、最初の記事を直接取得して題名・時系列を確認。Yellowstone個別記事は403であり、本文を取得したとは扱わない。|
|13|14|[ACT 2023全州公式表](https://www.act.org/content/dam/act/unsecured/documents/2023-Average-ACT-Scores-by-State.pdf)。制作者が全州の対象条件を読み、Minnesota68%/20.8/41%、South Dakota59%/21.1/41%を確認。受験率の分母は卒業者、理科基準到達率の分母はACT受験者と区別。独立担当も再計算。|

外部独立担当の個別取得URL・読解範囲・失敗は独立レビュー記録が正本。制作者自身が全外部ページを取得・精読したとの主張ではない。FBI行844は現在の公式一覧に参照回答から漏れた適合例があり除外した。ほかの不採用候補と取得失敗は [除外記録](skill-proofreading/deepsearchqa/excluded-candidates.json) に区別して記録する。

## 検証と制作記録

全52頁を制作者が1600px幅の個別画像で実読。candidate2全52頁から最終変更頁を再実見し、未変更頁は自分の全頁raw RGB比較で継承した。OOXML、URL、PDFとの本文対応、実グリフ輪郭、表、改頁を自分で検査。独立承認は別担当が独自取得・全頁実見・自前検査を行う。Microsoft PowerPointでは動作確認していない。最終SHAと範囲は [制作者確認](skill-proofreading/deepsearchqa/creator-visual-review.json)、外部独立承認は別のreview.jsonに記録する。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-deepsearchqa.pptx)・[PDF](../slides/datasets-in-10-minutes-deepsearchqa.pdf)。本編28頁、総52頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/deepsearchqa.json)・[校正の修正対](skill-proofreading/deepsearchqa.md)・[全ページ文言](skill-proofreading/deepsearchqa/pages.jsonl)・[最終検証票](skill-proofreading/deepsearchqa/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-DeepSearchQA-Apache-2.0.txt](licenses/deepsearchqa/LICENSE-DeepSearchQA-Apache-2.0.txt)、[ATTRIBUTION-DeepSearchQA.txt](licenses/deepsearchqa/ATTRIBUTION-DeepSearchQA.txt)。
