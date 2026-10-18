# COLD — 出典・版・実データ検証

2026-10-18取得。公開元COLDの独立資料。COLDはChinese Offensive Language Detectionであり、同名の別データを扱わない。native PPTX60頁、本編31頁、本編3例＋追加10例。著者sasakiy84。黙読600秒を予定（未実測）。CLEVA版の未取得部分、モデル出力のない部分を原データで埋めていない。

## 一次資料

- Jiawen Deng, Jingyan Zhou, Hao Sun, Chujie Zheng, Fei Mi, Helen Meng, Minlie Huang. **COLD: A Benchmark for Chinese Offensive Language Detection.** EMNLP2022, pp.11580–11599. DOI10.18653/v1/2022.emnlp-main.796. https://aclanthology.org/2022.emnlp-main.796/ 。正式PDF `evidence/paper.pdf`、本文 `paper.txt`。§3の収集/注釈、Tables2/3/5/6、Appendix B.3を照合。arxiv初公開も2022年であり、year=2022。公式READMEのBibTeXは著者が5名のみなので、正式PDFの7名を優先した。
- **COLDataset official repository**, https://github.com/thu-coai/COLDataset 。固定commit `a0c55a945497ab58e94aef491180e1cf88ffb864`。公式3 CSVをこのcommitのraw URLから取得。READMEに二値ラベルと詳細4分類の意味がある。READMEの現行検出モデルへのリンクはroberta-base-coldだが、論文§4.1のCOLDDetectorはbert-base-chinese。両者を同じ重みや成績としない。
- 公式repoの `LICENSE` はApache License2.0。https://github.com/thu-coai/COLDataset/blob/a0c55a945497ab58e94aef491180e1cf88ffb864/LICENSE 。この出所の条件をCLEVA全体の共通ライセンスとみなさない。
- Yanyang Li et al. **CLEVA: Chinese Language Models EVAluation Platform.** EMNLP2023 System Demonstrations, 186–217. https://aclanthology.org/2023.emnlp-demo.17/ 。付録Toxicity節はCOLDから標本を採用し、Chinese sentenceの二値選択をaccuracyで測ると説明する。元のデータ全体と、CLEVAで選ばれた成員は別。
- Stanford CRFM. **CLEVAToxicityDetectionScenario / Converter**, HELM v0.4.0. https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py 。class/taskはtoxicity_detection。入力例、候補、正解タグ、変換済みデータを読む方法を確認した。
- 同 **CLEVA v1 run configuration**, https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf 。toxicity_detectionのprompt_id0〜5。full_functionality_text/textはモデル区分の設定で、6実モデルの実行結果ではない。
- **HELM Classic v0.4.0**, release2023-11-17. https://crfm.stanford.edu/helm/classic/v0.4.0/ 。8,526 runとsuite索引の検索ではCOLD/CLEVAの対象run0。2026年の最新モデル順位とは扱わない。

`fetch-log.json`と`fetch-fixed-log.json`に取得URL、bytes、SHA-256。`evidence/repo-commit.json`に固定commit。正式CLEVA PDFは同じ作業環境の既取得一次資料から自分のevidenceへコピーし、そのSHAをinventoryに保存。外部生成APIは不使用。

## 実データの全件集計

UTF-8 BOMを含むCSVを`utf-8-sig`/`csv.DictReader`で読み、TEXTを変更せず集計。ヘッダー先頭列は空文字、TEXTは大文字。空欄名index列はtrain/devで一意でない。

|ファイル|label1|label0|行数|異なるTEXT|
|---|---:|---:|---:|---:|
|train.csv|12723|13003|25726|25659|
|dev.csv|3211|3220|6431|6430|
|test.csv|2107|3216|5323|5320|

計37,480行、異なるTEXT37,325種類。二値0と1の両方が付くTEXTは25種類。内部の同文重複行はtrain67/dev1/test3で、各ファイルの同文最大出現回数2。ファイル間の共通TEXTはtrain–dev30、train–test39、dev–test15種類。空白/句読点/大小文字を正規化しない比較。生成経緯・重複の原因・誤ラベルとは断定しない。

内部split列はtrain.csv全25726がtrain、test.csv全5323がtest。dev.csvはdev3216/train3215。この資料の分割件数はファイル所属。内部列に従って再分割しない。`stats.json`、`duplication-and-split-audit.json`、`analyze.py`に再集計を保存。

testの詳細0=other non-offensiveが2548、1=attack individualが288、2=attack groupが1819、3=anti-biasが668。全5323行で詳細0/3→二値0、詳細1/2→二値1を確認。詳細×topic表は正式論文Table3と一致。公開topicは1値、論文Table4の複数キーワード組合せの分類とは別。

Table2の平均文字数は報告値として全体48.77/offensive53.69/non-offensive44.20。現在CSVのPython len(TEXT)の平均は47.8571504803/52.9051050385/43.1722310818であり、同じ値としない。前処理等の原因を推測せず、数え方を分離した。

## 13原例と日本語

全13件のTEXT全文、中国語原文と日本語訳を同居。source file/0起算行/物理行/元index/全生レコード/二値・詳細ラベル/topic/internal split/URL/commit/ファイルと生CSV行のSHA/JSON再直列化SHAを`examples.json`へ保存。元indexをSNSの一意IDとしない。canonical hashは `json.dumps(ensure_ascii=False,sort_keys=True,separators=(',',':'))` のUTF-8。物理行のhashは元CSVの改行込みバイト範囲。

実例1はtrainの0起算240、物理242行、元index6374。TEXTはHELM公式docstringの公開例と完全一致し、原label0とTarget A（A非冒犯/B冒犯）を照合。残12例は公式testから、全4詳細カテゴリ、全3topic、皮肉・否定・反差別を含む発言を選んだ。13例をCLEVAの採用成員とみなさない。二値の表示は非攻撃的/攻撃的、原語safe/offensiveと対応。配布判断を翻訳者が再注釈せず、訳は否定・数値・括弧・対象を保持した。

`verify.py`が全13原位置/全hash/配布正解/native原文と訳/PDF/21.5pt bold accent1の独立正解を照合。p49のコードは同じ原レコードへ実行して一致。全13同居を実描画、引用枠を元の全文に合わせた。原文の分割や省略はない。

## 評価条件と未取得範囲

論文Table5の正答率とmacro F1、Table6の類型別正答率は正式PDFの報告値。図の6値と表20採点セルを照合。全5323予測は取得しておらず、独自再採点した成績とは呼ばない。多数派予測の60.42%だけは実件数3216/5323から計算。論文の検出器学習、収集時の反復分類器（Appendix B.3）、生成モデル出力を検出器で評価する実験を分離。収集の学習率等をCLEVAのinfer_paramsへ代入しない。

Classicのrun_specs8526とsuite索引の該当run0を`helm-index-check.json`に保存。public predictions/actual request/得点がないため、HELMの5-shot、温度、生成数、切詰め、採点後処理を確定しない。新規モデル問い合わせ0。

公式実装のCLEVA_DATA_URL＋`v1/toxicity_detection.zip`はHTTP→HTTPSを含む通常TLSで証明書のIP不一致となり未取得。`cleva-endpoint-probes.json`。検証を無効にしない。変換済みtrain/test、具体的prompts/infer_params、全採用成員/件数は未確定。元COLD3CSVで代用していない。

## 校正・描画・監査

3スキルmaster-guided-slides/dataset-introduction-slides/japanese-slide-proofreadingを適用。method/review_mode=skill_based_codex、gemini_used=false。全60頁とoverviewを実際に個別viewし、変更16頁を再view。実校正23対と全頁確認を記録。本文20pt、原文/訳18pt、独立正解21.5pt bold/accent1。9native表、1native chart、26引用枠、1code枠、notes0。全27枠の実画素上下余白6.67–8pt。

最終PPTX→PDFを同期。layout381段落124セル問題0、native全396段落162セルのPDF本文一致、標準XSD新規0（マスター既存11件を分離）、native/PDF67 URL-only範囲完全一致。公式画面は通常TLSで取得したHTML/CSSをChromiumで描画、asset失敗0、実見済み。

再現は`analyze.py`→`prepare.py`→`build.py`→`convert_local.py`→`render.py cold`→`ink_panels.py`→PDF/render→必要に応じ`fit_revised_quotes.py`→PDF/render→監査/verify/check_text→記録。`final_proofread.py`は既反映の一度限りの変更履歴で、再実行しない。共有repo/Gitは担当が変更していない。

メイン追検査のp11訳末尾孤立を解消し、再描画・独立再承認へ同期する。原CNとラベルは保持。


独立レビュー最終承認：create_cnndmがp11の原文忠実性・全引用/正解・最終描画を再確認。変更はp11のみ、残59頁PNG不変。最終PPTX e9bc65df69a741752d906433c5fc4b0ae2ec10a83820c9ec4bc16f4751fb2677、PDF 979ebbb131436c71f114fdae422312ff0173be415fd1e86ae1ddbee6b1e66fb0。本文の少数字折返しを禁止条件として扱っていない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/cold.json)、[実際の校正対](skill-proofreading/cold.md)、[全ページ文言](skill-proofreading/cold/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/cold/review.json)。
