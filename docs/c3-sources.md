# C³ — 出典・調査範囲・検証記録

公開C³全体を主題とする日本語資料。作成者sasakiy84。CLEVAプラットフォーム資料とは別の資料であり、C³全体、CLUEの配布版、CLEVAの採用部分を区別する。本文32頁、計65頁。初公開年2019、正式論文刊行2020、CLEVAによる後続利用2023。

## 一次資料と版

- Sun, Kai; Yu, Dian; Yu, Dong; Cardie, Claire. **Investigating Prior Knowledge for Challenging Chinese Machine Reading Comprehension.** Transactions of the Association for Computational Linguistics 8 (2020), 141–155. DOI:10.1162/tacl_a_00305. https://aclanthology.org/2020.tacl-1.10/ 。正式PDF `evidence/acl.pdf`、本文 `evidence/acl.txt`。元arXiv v3と区別し、数値・収集・分析・学習条件は正式版§3–5、Tables4–7を優先した。
- 同著者の初期版題名は **Probing Prior Knowledge Needed in Challenging Chinese Machine Reading Comprehension**。初回投稿は2019-04-21。https://arxiv.org/abs/1904.09679v1 。初回題名と日付を保存済みHTMLのcitation metadata/履歴で確認。現行arXivページ・PDFだけから初期版の題名を推測していない。
- 公式repo https://github.com/nlpdata/c3 。固定commit `1f41682ebb684d63afe7c583c8f38e137fc8a826`（2022-04-20）。元6JSON、4注釈、README、licenseを個別取得。取得URL/bytes/SHA256は `fetch-original-log.json`。正式論文と配布データの文書数/質問数を再計算して一致。
- CLUE公開ZIP https://storage.googleapis.com/cluebenchmark/tasks/c3_public.zip 。親が取得したZIPを自分の `evidence/c3_public.zip` へコピーし、元のfetch-clue-logも保存。ZIP内READMEはCLUE1.1でtest1.1を追加しtrain/dev不変と説明する。ZIPの取得日時を、その内容が初公開された日時と混同しない。
- Yanyang Li et al. **CLEVA: Chinese Language Models EVAluation Platform.** EMNLP 2023 System Demonstrations, 186–217. https://aclanthology.org/2023.emnlp-demo.17/ 。付録B.2がC³採用とaccuracy、父子会話例を記す。保存PDF/textは `evidence/cleva-cleva-paper.*`。
- HELM v0.4.0 `cleva_scenario.py` と `run_specs_cleva_v1.conf`。原URLは `build-info.json` と元fetchログ。scenario SHA `c61c19eb5ea2cf408dddf6087eb5c7715d5795c4508f23d2ccc2fc7eaf03de5e`、config SHA `062bed783973956ebcde2b875c9d76905eb3696fee25be4710bee9fc4fbe0e59`。読み込むtrain/test、prompts.json、infer_params.json、Converterの候補と正解indexタグ、metaによるadapter切替をコードで確認した。

## 件数・集合の検証

元6ファイルは13,369文書、19,577問。Mixedは5,229文書/10,006問、Dialogueは8,140文書/9,571問。各splitの値を `stats.json` に保存。候補数は2候補894、3候補2,389、4候補16,294。正解は候補にある唯一の文字列。

CLUE train/dev4ファイルは元repoとSHAまでバイト一致。CLUE test1.0の2,672文書/3,892問は、元testに対し（文書の文字列配列、質問、候補配列）キーが全問一致。CLUE配布ではanswerがなく、提出用id0–3891がある。test1.1は1,080文書/1,625問で、元全6ファイルとの一致は学習2問/開発0問/テスト1問。残1,622問はこのキーで一致しない。候補の順序や全文の正規化をせず比較した。「一部の話題が似る」等の緩い一致ではない。

4注釈ファイル各150問を元IDと1起算questionIndexでjoinし、600問を確認。事前知識521/600=86.8%、言語239/600=39.8%、専門5/600=0.8%、一般常識344/600=57.3%。支持範囲は1文220/複数文372/独立8。これらは抽出600問の性質であり、全19,577問への全数注釈ではない。

注釈 `c3-m-dev` の文書m12-174、questionIndex4には `c-p||c-i||1` という区切りの表記揺れが1件ある。原値は変更せず保存。再集計では最後の`||`を支持範囲として分け、前半を1個以上の`|`で分けてc-p/c-iの両方を保持した。`example-audit.json` に原値と解釈を残した。13選択例にはこの例を使っていない。

構築時の非抜出し率80.4%、平均文書長、モデル/人の正答率は正式論文の報告値。これらを独自の不明なトークン化や文字列正規化で再定義していない。人96.0%は注釈テスト部分で、モデル全3,892問との母集団差をp25に明記。BERT系は学習率0.00002、batch24、max sequence512、8epochs。長すぎる場合は文書/質問/候補の最長列を切り詰める。READMEの複数seedで開発最良を選ぶ推奨を、正式表の全モデルが固定回数試行したという主張へ変えていない。

## 13独立例・全文・訳

`examples.json` に本編3件、追加10件。Dialogue6、Mixed7。元ファイル・固定commit・元documentID・0起算document_index/question_index・file SHA・生レコード・原文・質問・全候補・正解・JPを保存。raw_record_sha256は生レコードを `json.dumps(ensure_ascii=False,separators=(',',':')).encode('utf-8')` で再直列化したcanonical値。元ファイルのraw bytes SHAも別に保存し、二つを混同しない。

各表示は、文書全文＋選んだ一問の質問/全候補。文書が共有する兄弟質問は表示範囲外であり、その範囲をp14で説明する。文書や選択肢の抜粋はしていない。中国語は改変せずnative text。空行を1行詰めるレイアウト調整だけを行った。選択肢ラベルA/B/C/Dは配布の配列順に表示した説明用ラベルで、元データのanswer文字列と対応させた。

父子会話はd-train配列941、文書ID37-153、question0。CLEVA紙面とも全文・質問・選択肢・正解が一致するが、CLEVA評価データ全体の成員や件数を推測していない。`verify_data.py` は13原例の原位置、SHA、全候補、正解文字位置、native原文/訳、赤字bold21.5pt答えを最終PPTXと照合する。p57の読み出しコードを実行し、同レコードへ一致した出力を `evidence/code-check.txt` に保存。

## CLEVA公開runと未取得範囲

Classic v0.4.0の公開run_specs8,526件とruns_to_run_suitesキーを独立に検索し、C3/CLEVAを名に含む公開runは0件。`helm-index-check.json`、`index-helm-release-runs_to_run_suites.json`。一方、同梱configにはreading_comprehensionのprompt_id0–5がある。full_functionality_text/textは設定上のモデル区分であり、6実モデルの実行結果とは説明しない。実装docstringの冒頭「coreference resolution」はコピーされた説明の誤りで、class/taskのreading_comprehensionを優先した。

CLEVA v1の変換済みreading_comprehension.zipは、HTTP→HTTPS遷移先を含め通常TLS検証で証明書IP不一致となり未取得。検証を無効にしない。`fetch-additional-log.json`。このためCLEVAの全採用成員/実train-test件数/具体的prompt本文/推論パラメータは確定していない。公開元C³の分割/全問数や、HELM他課題の5-shot既定を代入していない。新規モデルAPI/外部生成APIは呼び出していない。

## 権利・帰属

C³公式 `license.txt` は **“C3 dataset is intended for non-commercial research purpose only.”**。保存原文 `evidence/license.txt`。CCやMITとみなさない。試験問題が公開されていることから無制限な再配布権を推定しない。本資料は元研究と公式配布へ帰属を示した13問題の紹介と日本語訳で、公開元データ全量の再配布ZIPは納品しない。証拠用raw/dataは担当作業ディレクトリに保存し、公開対象の資料PPTX/PDFと分ける。各実例footerは固定commitの該当ファイルへリンクする。

## 描画・校正・監査

3スキル（master-guided-slides / dataset-introduction-slides / japanese-slide-proofreading）を適用。method/review_mode=skill_based_codex、gemini_used=false。全65頁を個別に実viewし、変更頁14/18/23/24/27/28/30/50も再view。公式画面は通常TLSで取得したHTML/CSS/フォントをChromiumで描画し実見済み。

15ptで原文/訳の列幅4.0/4.6、3.5/5.1、4.5/4.1inを39頁実描画。初期17頁の試験も保存。8例は同居、5例（1/2/5/8/12）は原文全文とJPを別頁。実例4は灰枠を実glyph余白へ詰めた最終形で同居可。`coexist-decision.json` に最終選択、実画像、座標を記録する。原文を訳のために分割していない。

27native引用/コード枠の実画素の上下余白は6.67–8.00pt、上下差最大1.34pt以内。表11、native chart1、native図1、ノート0。正答値は独立した21.5pt bold/accent1。グラフは全7モデル名が省略されない高さとラベル寸法へ調整し最終描画で確認。レイアウト490段落/150セル問題0、標準XSD新規0（マスター由来11件を分離）、66native URL-onlyとPDFリンク矩形の文字範囲が全て完全一致。最終PPTXからPDFを同期している。


独立レビュー：create_msmarcoが全65頁・原19,577問・600注釈・13原例/訳/正解・CLUE版差・技術監査・最終hashを照合し承認。未解決0。記録 ../review-c3/review.json。最終PPTX71b9f819…/PDFee25a739…は変更なし。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/c3.json)、[実際の校正対](skill-proofreading/c3.md)、[全ページ文言](skill-proofreading/c3/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/c3/review.json)。
