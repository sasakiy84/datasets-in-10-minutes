# EPRSTMT — 出典・版・実データの検証記録

原コーパスの感情分類を独立して説明し、FewCLUE公開版、CLEVA採用、HELMの公開説明例・設定・実行索引を分けた資料。原文13件は全て実在する異なるレビューで、同文の別分割・別IDを例数へ追加していない。原文と訳は13件とも同一ページ、全中国語文字列を保持。Gemini/APIによる例の生成・補完は行っていない。

## 一次研究

Liang Xu, Xiaojing Lu, Chenyang Yuan, Xuanwei Zhang, Huilin Xu, Hu Yuan, Guoao Wei, Xiang Pan, Xin Tian, Libo Qin, Hai Hu (2021). **FewCLUE: A Chinese Few-shot Learning Evaluation Benchmark**. arXiv:2107.07498v2, 29 September 2021. https://arxiv.org/abs/2107.07498v2

参照版はv2、11著者。会議採録・正式掲載頁の裏付けを取れていないため、プレプリントとして記す。本文PDF `evidence/paper.pdf` と抽出テキストを保存。p3 §3.2/§4.1 は32件の抽出とICIP Labによる収集・FewCLUEのフィルタ/検査/再構成を記す。p4 Table1はtrain32/dev32/public610/private753/unlabeled19565、二値・Acc。p6 Table2の包装の傷/試聴レビューは原train0行23 Positiveと全文一致（紙のlabelは小文字positive）。p9 Table3のEPRSTMT列は次のとおり。表番号はスライド本文から省いた。

| 方法 | 中心値 | 括弧内の原表値 |
|---|---:|---:|
| Majority | 50.0 | — |
| Human | 90.0 | — |
| FineTuning_R | 65.4 | 7.7 |
| Zero-shot_R | 85.2 | — |
| Zero-shot_G | 57.5 | — |
| PET | 86.7 | 1.0 |
| LM-BFF | 85.6 | 0.9 |
| P-tuning_R | 88.3 | 0.7 |
| EFL | 84.9 | 0.4 |
| FineTuning_ernie1.0 | 66.5 | 6.3 |
| PET_ernie1.0 | 84.0 | 4.8 |
| P-tuning_ernie1.0 | 80.6 | 5.3 |
| EFL_ernie1.0 | 76.7 | 6.3 |

括弧内の統計定義・試行数を表から推定しない。スライドでは中心値を引用。学習済みモデル予測・非公開正解は未取得のため再採点ではない。§6.1の人手評価はdev30–50件で練習/正解との比較/討議後、各注釈者がtest100件を注釈。原データのラベル作成法や、モデルの全件スコアと同じ分母ではない。全課題ScoreとEPRSTMT列を混同しない。

## 公式配布と全件解析

CLUE team. **FewCLUE official repository**. https://github.com/CLUEbenchmark/FewCLUE
固定commit `62a02c6f31cf32814cfe522f78ef088228840f8d`（2022-09-21）。`fetch_fixed.py` と `fixed-fetch-log.json` は固定15 JSONを取得したURL/bytes/SHA-256を記録。原文権利は各出所に帰属し、FewCLUE配布を収集元ICIPの全コーパスと同一視しない。

`analyze.py` が全15ファイルをパースし、文字列を正規化せず完全一致で集計。`stats.json` に全行数/ラベル数/一意ID・文/同文異ラベル/交差共有/ハッシュを記録。各train/devは32行だが、各クラス32件ではなく各組の内訳は異なる。公開test610は305/305で一意文610、test753にはlabelなし、unlabeled19565にもlabelなし。unlabeledの一意文は18744。

重要なREADMEとの差：READMEはfew_allを「合并去重」と記すが、固定train/dev集約版は各160行であり、IDを除く全項目が0〜4の分割の順序連結と完全一致。train一意文131/重複分29、dev135/重複分25。同じ番号train_i/dev_iの同文共有は5組とも0だが、別分割・同じファイル内には再出現がある。無ラベル資料との共有文はtrain集約6/dev集約4/publictest45/privatetest47。公式ルールは無ラベル資料利用を認めるため、文字列共有の検出を未確認の因果的漏洩と呼ばない。

IDはローカルであり、原レコードIDと0起算行を別項目として記録。test_publicのIDは行番号ではない。`examples.json` の全13件に原ファイル、行、ローカルID、原レコード、原行SHA/ファイルSHA、CN全文、JP全文、配布label、出典を保存。主3件はtrain4行7（CLEVA紙電話Negative）、train0行29（HELMモールPositive）、train0行23（README/FewCLUE紙包装Positive）。追加10件はtest_public行0,1,3,16,7,12,18,22,24,27。全体Positive7/Negative6。

## 実装を使った再計算

固定コードは `evidence/baselines--...`、取得経路は `more-fetch-log.json`。`primary_checks.py` は公式関数をAST抽出して実行し、`primary-source-checks.json` へ結果を保存する。外部学習・生成は行わない。

- EFL `clue_compute_metrics.py`: eprstmt分岐はsimple_accuracy、F1ではない。公開610正解に全Negative/全Positiveを与えると、両方305/610=0.5。
- PET `pet_eprstmt.py`: 原load_dataを全15ファイルに実行。Positive→1、それ以外のlabel→0、label欠損も0。欠損test753/unlabeled19565が全0になっても配布正解ではない。ラベル語は[不,很]。公開実装はdev0〜4の連結を使用し、原文32件の課題説明と全baselineの実条件を同一視しない。
- EFL `EprstmtProcessor`: entail/not_entailへ変換する原関数を実行。ratio1ではtrain0〜4の原32レビューがそれぞれ62/64/60/60/62文ペアになる。公開test610は1220ペア。原レビュー数と変換ペア数を区別。
- スライドnativeコードをそのまま実行し、305 610 0.5を確認。これは公開原ラベルの定数予測で、研究のモデル性能の再現ではない。

## CLEVA / HELMの採用範囲

Li et al. (2023). **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations. https://aclanthology.org/2023.emnlp-demo.17/ . 正式PDFは `evidence/cleva-paper.pdf`、独立GET証跡は `cleva-paper-fetch-log.json`。PDFp20（掲載頁205）のSentiment AnalysisはFewCLUEを採用元とし、Accuracyを使う。公開例の電話レビューCN全文がtrain4行7に一致し、紙の負面/Negativeが原ラベルに対応する。

Stanford CRFM. **CLEVASentimentAnalysisScenario / Converter**, HELM v0.4.0. https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py
クラスdocstringのモールレビューはtrain0行29（他の再出現もあり）と全文一致、A负面/B正面/TargetB。元label Positiveと、公開説明例の選択肢付き正解を別に記す。説明例の候補順を全テンプレートへ一般化しない。

**CLEVA v1 configuration**. https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf
sentiment_analysisのprompt_id0〜5を実コードから抽出確認。**HELM Classic v0.4.0 public index**, https://crfm.stanford.edu/helm/classic/v0.4.0/ （2023-11-17固定）。原run_specs8526件を検索し、CLEVA対象0件。全CLEVA採用集合・選び方・全プロンプト本文・infer_paramsは未取得。設定6通り、公開実行0件、原分割15ファイルを別の数とする。

## 収集元・利用条件の限界

原収集全体、元ICIP配布経路・byte同一性、注釈者/注釈手順・星からの変換・収集した具体サイトは未確認。`research-log.json` は検索経路と失敗/未確定点を記す。Googleのchallengeページや、検索の一般大学ページを出典とはしない。

固定repo-treeにはデータ全体の包括ライセンスを特定できず。BERTサブディレクトリのApache2.0はコードのものとして保存し、レビュー本文全体への許諾へ広げない。原レビューの出所、ICIP収集、FewCLUEの再構成・配布、引用原文/日本語訳/説明を区別する。公開されていることだけで無条件の再配布権を主張しない。

## 制作と検査

日本語native編集可能PPTX/PDF。主30頁、付録を含む全58頁。13例は全CN/JP同一頁で、元文を訳のために分割しない。13正解21pt bold B13731。native10表、26引用枠、1コード枠。全58頁の個別実目視・overview・最終変更頁再確認を実施。レイアウト/全文/URL/標準XSD新規0、master由来既存XSD11は別記。URLは表示文字列とリンク先の範囲が一致。参考文献は2件/頁、URLを短い別ラベルへ置き換えない。固定commit12桁URIも参照版の同じprefixである。ノートなし。

実際の校正対は `proofreading-changes.json`、頁別本文は `page-text-and-proofreading.json`、原票/表/実glyph余白/リンク/検証コードは各audit JSON。`visual-inspection.json` は実際に見た頁を記録。最終hashと監査要約は `handoff.json`。独立レビューはcreate_iceへ依頼する。主30頁の10分は黙読・流し読みを想定した計画であり、実測とはしていない。

独立レビュー承認：create_ice。全58頁/全15JSON/13票・CNJP/2正式PDF/公式関数/native表/監査/hashを独立確認、未解決0。文献枠7件の高さ不足は実字形下端+3ptへ拡張済み。記録 ../review-eprstmt/review.json。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/eprstmt.json)、[実際の校正対](skill-proofreading/eprstmt.md)、[全ページ文言](skill-proofreading/eprstmt/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/eprstmt/review.json)。
