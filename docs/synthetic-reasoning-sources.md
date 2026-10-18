# Synthetic Reasoning — 調査・制作記録

制作日: 2026-10-18 JST。sasakiy84、所属なし。日本語native PPTX / 最終PPTXからのPDF。本編29ページ、Appendix29ページ。黙読・流し読み約10分の予定値で、実測していない。

## 対象と一次資料

HELMのSynthetic Reasoning (abstract symbols)とSynthetic Reasoning (natural language)を一つの資料として扱った。抽象版は置換・照合・帰納の3モード、自然言語版はeasy/hardの2難度。自然言語版は抽象例を逐語訳したものではなく、独立した生成器である。

- Percy Liang et al. (2023). *Holistic Evaluation of Language Models.* Transactions on Machine Learning Research. https://arxiv.org/abs/2211.09110
  - reasoningの設計、Appendix E.3.1/E.3.2、貢献者欄を確認。本文のモデル値はこの論文の図から転記せず、Classic v0.4.0の公開runから取得した。
- Yuhuai Wu, Markus Rabe, Wenda Li, Jimmy Ba, Roger Grosse, Christian Szegedy (2021). *LIME: Learning Inductive Bias for Primitives of Mathematical Reasoning.* ICML, PMLR 139. https://proceedings.mlr.press/v139/wu21c.html
  - 取得PDFはarXiv:2101.06223v2（2022-03-16）。掲載年は2021。合成課題による数学的推論向け事前学習の研究で、HELMの評価生成器そのものとは区別した。
- Peter Clark, Oyvind Tafjord, Kyle Richardson (2020). *Transformers as Soft Reasoners over Language.* IJCAI. https://arxiv.org/abs/2002.05867
  - PDFはarXiv v2（2020-05-05）。abstractページのComments: IJCAI 2020も保存して掲載先を照合した。
- Stanford CRFM. HELM v0.4.0公式コード。
  - 抽象版: https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/synthetic_reasoning_scenario.py
  - 自然言語版: https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/synthetic_reasoning_natural_scenario.py
  - 採点: https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/metrics/basic_metrics.py
  - v0.3.0とv0.4.0の両生成器を取得し、バイト単位で一致を確認。LICENSEはApache-2.0。

## 生成と13実例の原記録

未改変の公式v0.4.0 Pythonファイルをimportして実行した。依存するScenario/Input/Output/Reference/Instanceの容器とsplit/tag定数だけをローカルの同等容器で提供し、乱数生成・規則生成・置換・正解生成のロジックは変更していない。ハーネスはgenerate.py、環境はevidence/runtime.json。

各モード/難度は新しく初期化し、seed42でtrain1000 / valid5000 / test5000を生成した。全55,000件をevidence/generated-records.jsonl.gzへ保存。抽象版のRandomStateは初期化時、自然言語版のrandom.seedはget_instances開始時に設定される違いを記述した。

本編はvariable_substitution index6000、pattern_match index6000、hard index6000。追加10件は置換6001/6002、照合6001/6002、帰納6000/6001、easy6000/6001、hard6001/6002。5設定の合計13件で、全てtest分割。index6000がtest内のindex0となる。全入力と公式の参照正解を保持し、自然言語版は原文を1ページに保って訳を次ページに置いた。抽象版の置換文字列は文字列リテラルとして意味を持つため、日本語訳でもその綴りを保ったことをラベルで示した。

examples-raw.jsonは生成直後、examples.jsonは原文・正解・訳・版・seed・index・ID・ソースSHAを含む配布記録。record_sha256は生成直後のindex/family/task/random_seed/input/references/split/id/source_file/source_sha256からなるpayloadのSHA-256。訳や制作上のroleはハッシュの対象外。verify_examples.pyはこのpayloadと公式原記録を照合し、さらに独立した置換処理、正規表現での規則適合、辞書からの属性対応とand/or条件適用で13正解を検証した。

これらは公式生成器のtest例で、公開HELM実行が抽出した515件と同一のサンプル群であるとは主張しない。モデルの実際の入力には、問題に指示と5/3組の提示例が加わる。採点方法を説明する2件の比較用予測は「採点方法の説明例」と明示し、13実例や実測モデル出力に数えていない。

## 採点の精確な意味

- schemaの抽象版主指標はquasi_exact_match/test。normalize_textは小文字化、ASCII punctuation除去、英語のa/an/the除去、空白正規化を行う。したがってASCIIの + - * = も消える。正規化後の一致と、前後空白だけを除くexact_matchを別表にした。
- 自然言語版のschema主指標はf1_set_match/test。論文説明にはIoUが登場するため、現在対象のschemaと実装を確認し、本文はF1、AppendixはIoUと明示した。
- extract_set_from_textはisより後をandで分け、ピリオドを除く。主語は採点集合に含まれず、同義語の統合や小文字化は行わない。Nothing.は空集合。予測は最初の行だけを使う。
- 公式の採点関数だけをASTから抽出して、説明用予測の得点を実行確認した。metric-explanations.jsonに保存。別記号の列がquasi一致=1、主語だけ異なる文が集合F1=1となることも確認した。
- 帰納は生成時の変数名を参照正解とし、名前の付け替えた同値規則を採点上同一視しない。

## HELMの公開実行

Classic latestとして取得したv0.4.0（2023-11-17）のrelease JSONから345実行を抽出。抽象3モードと自然2難度に各69実行。本文はtext-davinci-003（2022）/OPT-175B（2022）/Llama 2 70B（2023）の15実行を比較した。

元run suiteは全てv0.3.0。各試行の最大評価数1000はvalid485 + test515であり、表はtest515のみ。davinci/OPTは各3試行、Llama2は各1試行。実提示数は抽象5/自然3、prompt_truncated=0（全15実行）。出力候補1、temperature0、改行停止、最大出力は抽象50/自然20トークン。正規化一致/厳密一致は例ごとの0/1、自然F1/IoUは例ごとの値を平均し、表では100倍した。2026年の最新モデル順位とは称していない。

stats-helm.jsonは完全run名、suite、scenario/adapter仕様、stats URL・bytes・SHAとtest/validの摂動なし値を保持。元stats JSON15件もevidenceへ保存。schema-groups.jsonには主指標を指定する原schemaの該当項目と元ファイルSHAを保存した。

## 生成品質の集計範囲

seed42のpattern_match test5000例を全件集計。候補文字列に重複がある973件（19.46%）、正解だけが最長となる2826件（56.52%）。後者の長さは空白で区切る列の要素数で、同じ候補文字列は1種類として扱った。全4候補が同一となるtest例は0件。妨害候補が重複変数を除く集合から作られる実装と対応する。

自然言語版のNothing.はtrain/valid/testを合計した各11000例で、easy1899 / hard1910。再抽選の確率パラメータをそのままクラス比率とせず、実際の生成結果から数えた。

## 公式画面・権利・検査

専用のデータセットサイトではなくHELMの公式生成器として公開されるため、冒頭は公式リポジトリの対象タグv0.4.0のREADME画面と正確なURLを提示。通常TLS検証と継承プロキシの応答をChromiumで描画し、CSS・フォント・主要内容を確認。最終画像はevidenceではなくofficial-site.png、取得logはscreenshot-log.json。native cropで画像の縦横比を保った。

短い語彙表とテンプレートから生成し、既存記事や書籍のレコードを転載する資料ではない。公式コードのApache-2.0と論文の著者・掲載先を明示した。

日本語校正スキルで55ページを個別確認。method/review_mode=skill_based_codex、gemini_used=false。実際の修正11対、最終全ページ文言、原文/正解照合、全ページのview_image記録を保存。新規文を機械的に変更せず、変更が不要なページも確認記録を残す。

最終PPTXから専用UserInstallationのLibreOfficeでPDFへ変換。初版58ページの各内容を個別に拡大表示し、統合後の変更17ページを最終描画で再表示。全コード・引用・表・参考文献・公式画面を確認した。標準XSDは変更せず、マスター由来11件と整数buSzPctの字句形式差を分離。新規エラー0、内部参照・shape ID・ZIP整合・native URL-onlyリンクを確認。表9件、コードと原文はnative text、ノートなし。


独立レビュー対応：自然言語5例を15pt・EN4.6in/JP4.0inの不均等2列で実描画し、成立したhard6000/easy6001/hard6001の3例を同居へ変更（最終p10/39/40）。easy6000とhard6002は全文が収まらず別頁を維持。coexist-verification.jsonとレビュー側coexist画像が試験根拠。初版58頁の全内容は個別目視済みで、統合後55頁の変更17頁を再び個別viewした。引用枠20件は最終glyph境界とPNG実画素で上下余白を調整。8枠は4ptを戻し、最終は上6.67〜8.67pt・下6.0〜9.33pt。8変更頁を再度個別viewした。最終PPTX/PDF、監査、校正頁番号、hashは同期済み。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/synthetic-reasoning.json)、[実際の校正対](skill-proofreading/synthetic-reasoning.md)、[全ページ文言](skill-proofreading/synthetic-reasoning/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/synthetic-reasoning/review.json)。
