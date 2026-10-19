# OCNLI 調査・制作の出典と検証範囲

対象は Hu, Richardson, Xu, Li, Kübler, Moss (2020), **OCNLI: Original Chinese Natural Language Inference**, Findings of the Association for Computational Linguistics: EMNLP 2020, pp.3512–3526, DOI 10.18653/v1/2020.findings-emnlp.314。正式ACL PDF・書誌HTMLを取得し、arXiv v1だけで制作しなかった。正式書誌ではLarryではなくLawrence S. Moss。元の中国語コーパスを主題とし、CLEVA採用を本編最後の章で区別する。

## 固定した一次配布

- 公式作者リポジトリ https://github.com/CLUEbenchmark/OCNLI、main固定commit `b53efdee17257a5c33993cf6fcf8ffff0497ea0e`。公式README、全6JSONL、baseline data processing/evaluate codeを保存。
- CLUE公式READMEが指す https://storage.googleapis.com/cluebenchmark/tasks/ocnli_public.zip を再取得。ZIPのtrain.50k/dev/testは、固定作者repoの3ファイルとバイト単位で同一。親の既存ZIPだけに依存しなかった。
- train.50k 50,486行（有効50,437、`-`49）、dev 3,000行（有効2,950、`-`50）、test 3,000行（ラベル非公開）。合計56,486行。30k=30,286/有効30,237、10k=10,000/9,985、3k=3,000/2,994。小規模3集合が50kのペア/ラベル部分集合であることを確認。
- train50k/dev共通の前提文字列2,184種類、完全一致ペア0。30k/devは共通前提文字列0、prem_id共通2（news_608/tv_257、同じIDでも文が異なる）。文字列とIDの共有を同じ数にしなかった。
- train50kにはgenre/prem_id nullが3行ある。公開testはgenre/prem_id/5注釈ラベル自体を提供しない。欠測を第6文体と扱わない。
- 5注釈欄には既定3ラベル以外にunknown/unrelatedが現れる。devでそのような票を含む原票は39件。id2092はunrelated3票だが配布正解`-`。それをneutralへ勝手に変換せず保存し、既定3ラベルの多数決・配布ラベルを照合した。これは論文表の件数差39とは別の観測であり、原因を結び付けない。

## 収集と版の意味

正式論文§3とTable1/3/4を参照。前提は政府活動報告、LCMCニュース、劉震雲と王安憶の現代小説、Behind the headlines with Wentao（鏘鏘三人行）、Chinese Callhomeの5文体。前提選択は8–50文字、電話会話の転記記号を削除。145人の言語専攻の中国語母語話者が仮説を作成、約0.3元/ペア。再注釈は独立4人＋作成者の計5票、約0.2元/ペア。

Single=各ラベル1仮説、Multi=各ラベル最大3（最大9）。Multi Encourageは多様性・否定語を含まない矛盾を奨励、Multi Constraintは矛盾3つ中否定語ありを1つまでに制限。easy/medium/hardは同じ前提/ラベルに対する作成順。実測難易度ラベルと断定しない。70%重複制約は指示であり、全原票をその閾値で検査したとの主張はしない。

正式論文Table3の条件別件数11,986+12,328+16,584+15,627=56,525。一方、同表のtotalと公開3分割合計は56,486で、39差。原因は未確認のためいずれも保持した。後続のtrain30kなどはREADMEが提供する規模別配布であり、4作成条件と混同しない。

## 13実例・引用・訳

全13件は固定公式devの原票で、本編3＋追加10。各前提・仮説を全文保持し、原文を訳のために分割していない。全13件でCN/JP同居を実描画した。通常19pt、長い例8/13は17.5pt。例13のみCN3.9in/JP4.6inへ不均等幅とし、字形・回答・footerの間隔で成立を確認。

`examples.json`に0-based row、1-based line、原id、prem_id、5注釈、配布ラベル、raw line SHA256・構造化レコードSHA256、全文・訳・元版・帰属を保存。例2は3C/2Nの多数決で、全員一致と扱わない。追加例の説明は検証記録へ保存し、スライド上の言い換えで原ラベルを変えない。入力にない主体・肯否・比較・義務を足していないか自己校正した。

元OCNLIにA/B/C選択肢はない。p29だけはCLEVA正式論文の実在する多肢選択例を全文表示する。同じ原票を採用形式の比較に再掲し、14件目の独立例として数えない。

## 評価・再計算

公式`ocnli/mnli_code/util/evaluate.py`の`evaluate_classifier`をASTでそのまま抽出し、公開有効ラベルの固定neutral予測に適用（batch_size=1で端数切捨てを避ける）。dev=1,103/2,950=0.37389830508474575を得た。短い掲載再現コードとも一致。学習モデルを新たに実行した成績ではない。

2020年Table5/7の成績は一次論文の引用。testラベル・学習済み予測は公開原票には含まれず、それらの得点を新たな再採点と呼ばない。5学習試行平均±標準偏差。CBOW55.7±0.5、biLSTM59.2±0.5、ESIM59.8±0.4、BERT72.2±0.7、RoBERTa78.2±0.7、neutral38.1。hypothesis-only BERT65.3/64.3、RoBERTa65.7/65.0。全native表値を照合。

人手90.3は追加の学生5人、20練習例、その後test無作為300組。多数決不成立2組は最多のneutralで埋めた。全testモデル成績との分母差を保持。約12.1ポイントという差を百分率の相対改善と混同しない。

## CLEVA / HELMで確認した範囲

正式CLEVA論文 https://aclanthology.org/2023.emnlp-demo.17/ はLi et al. (2023), EMNLP System Demonstrations pp.186–217（書誌HTML確認）。PDF16–17頁（印刷201–202）でOCNLI由来textual_entailmentの多肢選択例を掲載。かご例の前提・仮説がdev row1162/id1162と全文一致し、元entailment、公開選択肢A总是可以/B有时可以/C不可以、正解Aを確認。PDFの文字抽出には一部文字化けがあり、PyMuPDF抽出と原PDFで確認した。

HELM v0.4.0 `cleva_scenario.py`と`presentation/run_specs_cleva_v1.conf`を独立取得。commonsense_reasoning/textual_entailment/v1のprompt_id0〜5が6設定。Converterはchoices→Reference、label index→correct。docstringの「我像南方人…外国人」例は公開論文のかご例と別物。採用全原票や全テンプレート本文を確認したことにはならない。

固定リリースrun_specs8,526件からCLEVA classは0件。設定ファイルの存在と公開実行の存在を区別。2023-11-17固定版での公開実要求・成績・実提示例数を捏造していない。

今回の配布再試行は、コード中のhttp://39.108.215.175/data/v1/commonsense_reasoning.zipがHTTPSリダイレクト後にIP名不一致のTLS検証失敗。公式ドメイン経由 https://www.lavicleva.com/data/v1/commonsense_reasoning.zip は503。TLS無効化はしていない。採用範囲・分割・テンプレート・生成条件は未確定のまま記録。

## 利用条件と帰属

公式READMEは **Creative Commons Attribution-NonCommercial 2.0 Generic (CC BY-NC 2.0)** を掲示。CCサイト本体は今回403だが、権利条件の出典は作者の公式READMEに残る。ライセンスの不存在と解釈しない。news前提はLCMC（ISLRN990-638-120-277-2、ELRA-W0039）からELRAの許可を得たと明記される。各前提の政府報告・ニュース・小説・番組/電話会話の権利は、それぞれの原資料の権利者に帰属する。OCNLI作成者の帰属と、元素材を区別して保存した。日本語訳は本資料の説明のために作成した引用訳。

## 制作・検査

共通マスターからnative PPTXを作成し、同じ最終PPTXを固有LibreOffice profileでPDF化。全57頁とoverviewを実際にview_imageし、変更頁も再view。8native表・全13原文/訳・CLEVA全選択肢・14正解・29引用/コード枠・参考文献3頁×2件・公式ブラウザ画面を個別確認。

日本語校正は日本語校正スキルに基づくCodexによる校正、`method/review_mode=skill_based_codex`、`gemini_used=false`。実際の変更対・各頁最終文言を別JSONへ保存。レイアウト・XSD新規エラー・URL-onlyリンク・本文欠落・ノートを監査。全件の実データ照合は`prepare.py`/`primary_checks.py`、最終native照合は`records.py`で再現できる。制作スクリプトの順序と実行済み検査はhandoffへ記録する。独立レビューはcreate_twitter担当。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/ocnli.json)、[実際の校正対](skill-proofreading/ocnli.md)、[全ページ文言](skill-proofreading/ocnli/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/ocnli/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/ocnli/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
