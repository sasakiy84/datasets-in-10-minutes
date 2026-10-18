# WMT2020（英中）出典・範囲・権利記録

本資料の主題は2020年のNews Translation Taskの公開テストnewstest2020の英語→中国語・中国語→英語。WMT14やWMT2020の学習コーパス全体、CLEVAの未取得選定集合とは別。本文29頁・全60頁、原文書13件から独立した1区間ずつを選び、区間全文・対応参照全文・各々の新規日本語意味訳を表示する。原記事全文の引用ではない。外部の翻訳生成API、新たなモデル出力の生成は使用していない。

## 一次資料

- Loïc Barraultほか21名 (2020), **Findings of the 2020 Conference on Machine Translation (WMT20)**. Proceedings of the Fifth Conference on Machine Translation, pp.1–55, DOI 10.18653/v1/2020.wmt-1.1. [正式ACL書誌](https://aclanthology.org/2020.wmt-1.1/) / [PDF](https://aclanthology.org/2020.wmt-1.1.pdf)。evidence/acl.html・paper.pdf・paper.txt。会議名はConference、開催年2020。収集/原言語/段落分割は§2、評価は§3、英→中の歴史的人手評価は印刷p24の公式表。対象年とニュースの日付を混同しない。
- [WMT20公式ニュース翻訳タスク](https://www.statmt.org/wmt20/translation-task.html)。evidence/official-site.html。CSSを読み込んだ実画面をofficial-site.pngへ保存、表示を個別確認。11言語対22方向、英→中のparagraph-split、データ配布、利用条件を確認。
- [公式公開test.tgz](https://data.statmt.org/wmt20/translation-task/test.tgz)。独立取得5302245bytes、SHA256 `22b23a6e59d77d0987b8a01b5dbc3794feccdb5e37bfc5c6094df6bdbe943f6e`。取得HTTP状態/bytes/hashはfetch-log.json。evidence/test.tgzと対象8SGMを保持。analyze.pyにより、docid+segid一致でsource/refを結合。通常版英→中1418区間/130文書、原言語en；中→英2000区間/155文書、原言語zh。空入力/空参照0、各方向の入力と対は一意。英→中の区間は複数文を含み得るため一律に「1文」と呼ばない。
- Kishore Papineni, Salim Roukos, Todd Ward, Wei-Jing Zhu (2002), **BLEU: a Method for Automatic Evaluation of Machine Translation**, ACL. [書誌](https://aclanthology.org/P02-1040/)。evidence/bleu-paper.pdf/txt。修正n-gram適合率の幾何平均、brevity penalty、コーパス集計。
- Matt Post (2018), **A Call for Clarity in Reporting BLEU Scores**, WMT Research Papers, pp.186–191. [書誌](https://aclanthology.org/W18-6319/)。evidence/sacrebleu-paper.pdf/txt。BLEUの処理条件・報告条件。
- [SacreBLEU 2.5.1](https://github.com/mjpost/sacrebleu/tree/v2.5.1)。PyPIから専有metric-depsへ版固定インストール。実際に使用したBLEU・zh/13a tokenizer・配布METADATAをevidence/sacrebleu-2.5.1へhash付き保存（sacrebleu-installed-sources.json）。コードのライセンスはニュース原文へ拡張しない。
- Li et al. (2023), **CLEVA: Chinese Language Models EVAluation Platform**, EMNLP System Demonstrations. [正式書誌](https://aclanthology.org/2023.emnlp-demo.17/)。evidence/cleva-cleva-paper.pdf/txt。Appendix B.2 Translationは過去WMTの英中翻訳とSacreBLEUを記載、全選定版をnewstest2020だけと断定していない。このPDFと次のscenario/confは先行担当c3内で取得した固定一次ファイルの読取コピー（独立再GETを装わない）。
- HELM v0.4.0 [CLEVATranslationScenario](https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py)、[CLEVA設定](https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf)、[run_specs.py](https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/run_specs.py)。evidence/cleva-scenario.py・cleva-run_specs_cleva_v1.conf・helm-run-specs.py。run_specs.pyは本制作で独立GET、hashはfetch-metrics-log等へ保存。translationのprompt_idはen2zh各0–2、zh2en各0–2、合計6設定。生成既定値の提示上限5/1候補/20token/温度0等はinfer_paramsに上書きされるため、未取得の実行条件とはみなさない。

## 通常配布とB配布、公開例とCLEVA全体

newstestB2020は対象全区間の入力文字列が通常配布と同一。sourceファイルはsetid等が異なるためbytesは同じではない。参照文字列は英→中1416/1418、中→英1997/2000で異なる。配布ファイル名A/Bを、論文のHUMAN-A/Bとの厳密な対応と断定しない。B参照の公開性は確認できるが、中→英B参照の作成経緯までは確定していない。別の入力実例として水増ししない。

本編3例は公開CLEVA紙面/公式docstringの入力・参照とnewstest2020が完全一致。位置はexamples.json（英→中global0 index910/1411、中→英18）。CLEVA公開例の元位置が判明したことと、未取得の選定集合の全年度/全件数が確定することを区別。13例は13独立docid、英→中7・中→英6。source/ref/Brefの元SGM行、行番号、byte offset、doc metadata、segid、原行/ファイルSHA、全文をexamples.json/all-pairs.jsonへ保存。SGMのHTML実体参照だけをhtml.unescapeして表示、原行も保持する。例6はsourceのeast of Caribbeanと中国語参照の加勒比海东部を、日本語でも「東」「東部」と分けた。

## 固定公開実装の確認範囲と限界

translation.zipはHTTP/HTTPS両URLを通常の証明書検証で取得試行したが、IPアドレスと証明書の不一致で失敗（fetch-cleva-translation-log.json）。証明書検証は無効化していない。実選定、templates、infer_params、実際の最大出力長や提示数は未確定。

Classic v0.4.0の公開run索引8526件にCLEVA名称0、suite mappingも0。公開索引一次ファイルは既存調査 `/workspace/artifacts/helm-classic-remaining/helm-release-*.json` から本専有evidenceへコピーし再走査、全bytes/hashとコピー元はhelm-index-check.jsonに記録。WMT一般の翻訳run全般の不存在を意味しない。

get_cleva_machine_translation_metric_specsは `helm.benchmark.metrics.machine_translation_metrics.CLEVAMachineTranslationMetric` を指定するが、同v0.4.0公開ディレクトリには配置先machine_translation_metrics.pyが存在しない。公式GitHub API一覧を独立取得（fetch-metrics-tree-log.json）、対象rawの404試行も記録。クラス名とモジュール名を区別。したがってCLEVA採点のtokenizer/集計法を推測で補わず、公開版の接続先の欠落として記述した。

## 説明用BLEUと歴史的評価

reference-bleu.json / metric-recheck.json / validate.py。通常配布の公開参照を出力側、B配布参照を参照側へ置いた説明用計算。モデル成績でもCLEVAの再現でもない。SacreBLEU2.5.1、参照1本、大小文字保持、exp smoothing、effective order no。英→中全1418区間はzh tokenizerで36.85247953081421、中→英全2000区間は13aで25.168576390598655。counts/totals/BP/長さ/4適合率/完全signatureを記録。zhは漢字等を1字ずつにし、非漢字部分にも区切り処理。PPTX内2コードを抽出してそのまま実行し、見出し原入力と全1418区間BLEU/signatureの出力一致をevidence/code-check.jsonへ保存。

2020年のDAは論文による歴史報告値。英→中 HUMAN-B80.6/z.568、HUMAN-A82.5/.529、OPPO80.0/.447、Tencent-Translation79.0/.420、Huawei-TSC77.3/.415。選んだ3機械は提供資源制約内（公式表の白地を実画像evidence/paper-p24.pngでも確認）。0–100のDAは正答率ではない。平均評点と評価者ごとの標準化平均zは別。統計的な同順位群を無視した微差の順位化を避ける。英語からはsource-based、英語へはreference-based中心で、文脈提示にも差がある。二方向zをそのまま同一絶対尺度として比較しない。

## 利用条件・帰属

公式タスクページのLicensingは、overview論文の引用と個別データの追加引用条件を守る研究利用を認め、それ以外は元の著作権者への相談を求める。CC等の包括ライセンスや商用自由利用とは記さない。ニュース原文/参照訳の権利とコードのライセンスは別。表示は13件の短い連続SGM区間と対応参照に限定し、footerにWMT20/配布元とdocid/segidを保持。ニュース記事の作者名・byline・訳者名が配布にない場合は推測しない。元全文アーカイブは調査原記録として保持し、資料への全記事転載や公開配布sidecarは作らない。日本語は本資料による新規意味訳で、既存公開日本語訳ではない。

## 校正・描画・技術検査

三技能の適用、ネイティブPPTX/表12/図表1、notes0。全60頁とoverviewを個別目視、最終変更8頁を再確認。13件全文+JP同居は15pt・不均等幅を含む39頁の実PDF試験後に採用（coexist-*.json）。引用26/コード2の28枠は最終PNGの実画素余白を測定、上下差を確認。タイトル/表セルの少数字孤立は自然な短文化で調整し、本文引用の少数字行だけを理由に強制改行はしない。頁別校正と実before/afterはpage-proofreading.json/proofreading-changes.json。最終PNG全60件は新規PDFラスタとbytes一致。layout/package/links/execution/pixel監査と最終hashはhandoff.jsonに集約。


## 独立レビュー承認

create_twitterが全60頁/原8SGM/6836対/13独立原例/二方向BLEU/DA/固定条件/native/最終hashを独立照合し、未解決0で承認。review-wmt2020-enzh/review.jsonを参照。最終PPTX2830f1327b68d91a709043ab16c9f8705f1b9271b1be233156b2fb1150a0bcb3、PDF4605132b59b2b6c767056f01243a69363fb230c070e1bd1fdf1c31d78f2ada08。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/wmt2020-enzh.json)、[実際の校正対](skill-proofreading/wmt2020-enzh.md)、[全ページ文言](skill-proofreading/wmt2020-enzh/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/wmt2020-enzh/review.json)。
