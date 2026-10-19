# LEXTREME 調査・制作記録

日本語資料、著者sasakiy84。2026-10-18調査。共通マスター、dataset-introduction-slides、japanese-slide-proofreadingを適用。外部生成API・Gemini不使用。

## 範囲と版

- 正式論文：Joel Niklaus, Veton Matoshi, Pooja Rani, Andrea Galassi, Matthias Stürmer, Ilias Chalkidis (2023), **LEXTREME: A Multi-Lingual and Multi-Task Benchmark for the Legal Domain**, Findings of EMNLP 2023, pp.3016–3053, https://aclanthology.org/2023.findings-emnlp.200/ 。取得した正式ACL PDFを基準とする。最初に取得した.257は別論文（Speculative Decoding）であり、出典に使っていない。arXiv 2301.13126v3も取得し比較。
- 2023年スイートは11構成データ・18設定（SLTC8/MLTC5/NER5）。HELM v0.3.0と取得時mainのTASK_CODE_MAPPINGはいずれも18設定。主資料はこの範囲。
- HFの2023-02-07ローダー`65f6046b8083`を固定取得。構成辞書とクラス順をASTから抽出。新しいローダーには追加設定があるので、現行コードの全構成数を18とは記載しない。
- 現在HFのIDはjoelniklaus/lextreme（旧joelitoからredirect）。コミット73271418f8710e672618fa05f727c9aee239c24bのカードはウクライナ3時期追加後、12データ/21設定/25言語と記載。READMEの概要はローダーの全追加設定を網羅していない。取得した現行ローダーのBUILDER_CONFIGSは32件（トルコ・スイス関連の追加も含む）をASTで数え、2023固定版は18件と照合した。HELM実装と現在カードの範囲を混同しない。
- 言語別集約は論文Table6の24 EU言語。C19データにはノルウェー語nbもあり、論文Table3と脚注6が明記。24を「全構成データ内の異なる言語の厳密な一意数」と解釈しない。Table3 EU24一覧は文字脱落があるので、その行を言語リストとして転記せず、Table6のヘッダーを参照。正式ACL Table3はMEU/MAPを24と表記するが、Table9の収録欄ではMEUはgaなしの23、MAPはhr/pl/slなしの21。固定ローダーもMEUを23 official EU languagesと説明する。個別データに一律24を主張せず、p15を複数EU言語、p21を全言語へ修正した。
- 法域はBR/DE/GR/CH/RO/EUやC19の国別範囲。言語と法域の一対一対応を仮定しない。法域別総合集約は論文の対象外。

## 実データと13例

6つの構成データの固定コミットtest.jsonlを通常TLSで取得。全取得URL・bytes・SHA-256はevidence/fetch-log.jsonと各*-api.json。1始まりの行番号、原レコード全体、入力・正解の変換値、原行SHA-256をexamples.jsonに保存。

GAM test3078、OTS4297、C19 418、LegalNERo907、Greek Legal NER4017、BCD405レコードを取得。これは6配布ファイルの行数であり、18設定をすべて読込・実行した件数ではない。元スイートの分割数は正式論文Table2から別途転記した。

本編3/追加10、de/en/ro/it/fr/nb/el/ptの8言語。目的抽出であり無作為代表標本ではない。選んだinputフィールドは全文、NERはトークン配列全文。大きなメタデータレコード全文はexamples.jsonに保存するが、モデル入力には混ぜない。日本語は意味の訳で、原語トークンのBIOを訳へ付け替えない。元注釈や大文字・句読点・スペース・誤記を保持。

select_examples.pyは元ファイルと2023ローダーのクラス順から13例を構築する。verify_data.pyはHELM v0.3.0の公式メソッド本体を変更せず実行する。インフラimportsだけを除き、最小dataclassとdatasets interfaceを代入し、選んだ実レコードをクラス整数へ符号化して渡した。入力と全正解参照が13件とも完全一致。モデル推論・プロンプト実行はしていない。wrong refsは公式処理の結果をhelm_instanceとして保存したが全train分割を通したときの乱数状態とは異なるので、この参照順を公開runの実順序とは主張しない。

OTS-CTのクラス順a/ch/cr/j/law/ltd/ter/use/pincをHELMは0〜8へ変換。例2 use,pincは7,8。C19 event1〜event8は0〜7で、例8 event4は3。NERは`"token" "token"`とBIO列を文字列化。クラス語彙は2023ローダー、NER順はHELMで照合済み。

OTS-ULはuntaggedを除外し3クラス、BCD-Uはnot_determinedを除外し2クラス。HELMの指示文に余分な候補があってもローダーで有効になるとは限らない。13例は全て有効ラベル付き。空MLTC参照や全18設定の読込成功は未検証。

## 原スイートとHELM評価

原基準実験は各設定fine-tuning、3 seeds（1–3）、学習率1e-5、batch64、validation loss早期停止patience5、macro-F1、GLCを除くSLTCの過剰サンプリング、長文の階層モデル。データ別・言語別集約をそれぞれ多段調和平均し、最終も両者の調和平均。p20の10数値は正式ACL PDF Table5/6の集約値そのまま。丸めた構成値から総合集約を再計算し直していない。arXiv abstract/古いGitHub READMEの61.3を最終正式論文の集約値と混ぜない。

HELM v0.3.0 get_lextreme_specはgeneration adapter。最大提示例1〜5、最大出力5〜788を設定別に保存。classification_macro_f1/micro_f1はSLTC/MLTCに追加し、MLTC delimiterは`, `。ClassificationMetricのdocstringに未対応との旧文言があるが実装はMultiLabelBinarizerを使用する。NERには分類指標が追加されず、BasicMetric(names=[])にも正解一致指標はない。原スイートのNER評価がそのまま実装されていると主張しない。

MultiEURLEXではレコード内の非None言語からrandom.choice。乱数42はwrong referenceのshuffleと共用し、処理順に依存。全24言語を各レコードで走査する方式ではない。

## 公開run

latest/config.jsを再取得しv0.4.0（2023-11-17）を確認。公開schemaはlextremeをmain metric classification_macro_f1/testで登録。共通保管のrun_specsとruns_to_run_suitesを独自にフィルタし該当0件。ファイルSHAはstats.json。モデル別得点、実提示数、応答、試行平均は存在を確認できないため掲載しない。0件は0点ではない。p20はHELM順位ではなく原スイートの基準実験。

## 権利と引用の帰属

現HFスイートカードはCC BY4.0。HELMとローダーコードはApache2.0。ただし構成データの文章・注釈条件へ一律適用しない。各固定版カードではGAM CC BY4.0、OTS CC BY-NC2.5（YAMLはother、本文に明記）、C19 CC0、LegalNERo CC BY-NC-ND4.0、Greek Legal NER CC BY-NC-SA4.0。BCDカードはライセンス情報提供なし・ブラジル法に従う旨。短い原例の出所明示引用と意味の訳を示し、コーパス全体の再ライセンスを主張しない。独立した利用は構成配布物の条件を確認する。

構成元著者は2023ローダーにあるcitationと、各カードに保存。GAM: Urchs/Mitrović/Granitzer (2021)。OTS: Drawzeskiほか(2021)。C19: Tziafasほか(2021)。LegalNERo: Păișほか(2021)。Greek Legal NER: Angelidis/Chalkidis/Koubarakis (2018)。BCD: Lage-Freitasほか(2022)。正式タイトル・著者・年・掲載先を参考文献頁に載せた。

## 描画と品質

公式トップ画面をChromiumで通常TLSの応答から描画し、CSS・フォントと内容を実際にview_image。現カードの12/21をそのまま写す。本文は2023スイートとの差を説明する。native text/tablesを使い、notesなし。最終PPTXから専用LibreOffice profileでPDF化し、全頁画像化。引用枠は実PDF字形を用いて上下余白を調整し再PDF化。最終の個別目視範囲と監査結果はviewed-pages/page-review/*audit.jsonに保存する。見ていないページを閲覧済みに記録しない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/lextreme.json)、[実際の校正対](skill-proofreading/lextreme.md)、[全ページ文言](skill-proofreading/lextreme/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/lextreme/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/lextreme/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
