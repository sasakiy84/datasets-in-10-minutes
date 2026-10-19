# Dyck Language 調査・制作記録

## 範囲と版

- 48ページ。本編31、予定黙読時間600秒（実測なし）。日本語、作者sasakiy84、所属なし。native editable PPTXと、その最終版から出力したPDF。ノートなし。
- 対象はHELM ClassicのDyck Language生成シナリオ。表示固定版はv0.4.0（2023-11-17）、公開run suiteはv0.3.0。括弧は3種類。参照する2019年の研究、BIG-benchの固定選択式課題、HELMの生成式課題を区別した。
- `year=2022`はHELM版Dyckシナリオが同年の公開コードに存在することに基づく。資料で扱うrun固定版は2023年だが、その年を初登場年には使わない。Dyck言語の提唱年や2019年の参照研究発表年とは区別する。
- 公式の独立したデータ配布トップは用いず、著者の公式実装 https://github.com/suzgunmirac/marnns のREADME画面を冒頭に掲載した。CSS・画像が読み込まれたChromium画面を取得し、view_imageで確認。screenshot-log.jsonに取得結果を保存。

## 一次資料

Suzgun, Gehrmann, Belinkov, Shieber (2019), *Memory-Augmented Recurrent Neural Networks Can Learn Generalized Dyck Languages*, arXiv:1911.03329v1。本文・PDFのTable 2、§4.1、§5.1を確認した。各時点の次の記号集合の予測と、全時点での成功判定を用いる。Dyck-2の10回の実験におけるテスト成功率平均はVanilla RNN 0.00%、Vanilla LSTM 1.39%、Stack-RNN+Softmax 99.99%。学習5,000列（2〜50記号）、評価5,000列（52〜100記号）。この課題の値をHELMの補完得点と同列の順位表にしていない。

HELM v0.3.0のdyck_language_scenario.py、metrics/basic_metrics.pyと、Apache License 2.0を取得。基本指標の最初の誤ったパスへの取得は404だったが、正しいmetrics配下のパスからHTTP200で取得した。原応答のSHA-256・bytes・URLはevidence/retrieval-log-complete.json、全ファイルはevidence/file-manifest.json。

著者repoのREADMEはcommit `63ac24dc029201a9cf0f6fb77510aca7b0791727`、BIG-benchのREADMEとtask.jsonはcommit `092b196c1f8f14a54bbc62f24759d43bde46dd3b`で再取得し、main/master取得分とbytes一致を確認。固定URL・SHAはevidence/pinned-sources.json。BIG-benchのtask.jsonはmultiple_choice_grade、append_choices_to_input=false、Dyck-4、1,000例。参考文献のBIG-bench文書に推定の公開年を付けず、参照日を記した。

## 公式生成器・実例

v0.3.0シナリオの生成処理を変更せず、HELMデータ型のimportだけを同形のローカルdataclassへ差し替えて実行した。外部API生成は使用していない。Python 3.12.14、NumPy 2.3.5、Python randomとNumPyの両方にseed42を指定。

- num_parenthesis_pairs=3、parenthesis_pairs=( )/[ ]/{ }、p=0.5、q=0.25。
- num_train_instances=3、num_test_instances=500、max_recursive_depth=100、max_output_size=3。
- 切り出す前の生成列長: train4〜50、test52〜100記号。
- 生成した503件をevidence/generated-corpus-seed42.jsonへ保存。test500件は公開text-davinci-003のscenario_stateの入力・正解と全件一致した。別のスタック実装でも503件すべての正解を検証。
- 13件（本編3、追加10）はその生成済みtestの独立したレコード。架空の例を加えていない。examples.jsonにID、生成位置、原文、正解、試行0の実予測、SHA、元JSON位置を保存。
- 入力は全文を1ページに保持し、半角空白はそのまま、表示上の改行だけを追加した。括弧記号は日本語でも変わらないため、ラベルと説明を日本語にしている。英語指示は全文と日本語訳を同居させた。

get_inputは末尾側の深さを走査して入力を切り出す。切り落とす側に既に対応した部分列が入る場合もあり、test入力の実測は45〜99記号、平均71.418、中央値71。入力の最大入れ子深さは6〜30。正解長の全500件内訳は1記号168、2記号151、3記号181。生成前の長さ条件と、切り出した入力の統計を区別した。

全1,500公開要求のプロンプトに、生成器で得た3訓練入力+正解の完成列がそれぞれ存在することも照合した。

## 採点の重要な相違

公開runのmetric_specは`exact_match_indicator`。v0.3.0の関数の既定indicatorは半角空白であり、`pred.split(indicator)[-1].strip()`とgold側の同じ処理の後、末尾の要素だけをexact_matchへ渡す。したがって、公開値を括弧列全体の完全一致率と呼んでいない。

実在するid9・試行0はgold=` } ) ]`、prediction=` ] } ) ]`。公開指標は末尾`]`が一致して1点だが、予測全体は余分な`]`を含むので全列一致は0点。この入力全文は実例3にも掲載した。

公開text-davinci-003の全1,500出力へ、取得した元の指標関数を適用して公開値を再現した。試行0: 0.732、試行1:0.760、試行2:0.760、平均0.7506666666666666。前後の空白を除いた列全体のexact_matchで独自再採点すると、0.406／0.492／0.492、平均0.4633333333333334。この独自集計はHELMの公開指標と明確に分けて記載した。generation-audit.jsonに計算結果がある。

## 公開run条件と数値

run名 `dyck_language_np=3:model=...`、suite v0.3.0。正確なrun_specはevidence/run-specs.json。全てgeneration、max_train_instances=3、max_eval_instances=1000、num_train_trials=3、temperature=0、max_tokens=5、stop_sequences=[newline]。実評価は500件で、確認した3モデルはいずれも平均提示例3、prompt_truncated=0。

公開statsのname={name:exact_match_indicator,split:test}、摂動なしを採用。Anthropic内部ID `anthropic/stanford-online-all-v4-s3`をAnthropic-LM (2022)と表示し、84.86666666666666%→84.87%。text-davinci-003 (2022)は75.06666666666666%→75.07%。OPT-175B (2022)は49.4%→49.40%。metric-display-audit.jsonで3表示値を元の数値へ照合。2026年のモデル順位とはしない。

## 配布と帰属

資料はHELMのApache License 2.0の実装から生成した人工的な括弧列を主な実データとする。原研究と著者の実装、BIG-benchの文書、HELMの生成・採点コードと公開出力にそれぞれ帰属を示す。HELMのライセンスを元研究repoのライセンスへ流用していない。著者repoのLICENSEは今回の取得パスで404だったため、独自のライセンスを推定していない。BIG-benchの選択肢レコードを本資料の実例へ転用していない。

## 校正と検査

ローカルjapanese-proofreadingを各ページに適用。method/review_mode=skill_based_codex、gemini_used=false。実際の修正対3件をproofreading-changes.jsonへ、各ページの最終文言と確認をpage-text-and-proofreading.jsonへ保存。架空の修正対は作っていない。

全48ページのoverviewを確認し、全48ページを個別view_imageで拡大した。13入力全文と正解・実予測、原文指示、指標コード、7 native表、1 nativeグラフ、公式画面、参考文献2件×2頁を確認。引用枠をPDFの実字形境界に合わせ、入力改行を均等にし、脚注の行間とURL範囲を修正した。変更した5・6・7・8・9・12・18・30頁と全追加例を最終描画で再確認した。

最終監査: layout/textは306段落・60セル、問題0。package新規XSD0、マスター由来11件と整数buSzPct差を分離。内部参照・ZIP・ID正常、native tables=7/charts=1。URL-only run48件とPDFリンク48件は文字列が完全一致し、隣接文字の混入・glyph overhangなし。ノートなし。実測した目視範囲はvisual-review.jsonに保存。

## HELM版の初登場年の確認

GitHub APIで現パスの全9コミットと、改名前パスの全3コミットを取得。2022-11-16のcommit `c2ee966d79df97f5005d4352b13ddc1730c1f02f`は `src/benchmark/scenarios/dyck_language_scenario.py` から現パスへのrenameであり、このcommitの固定rawソースを取得してDyckLanguageScenarioの実体を確認した。改名前の履歴は2022-08-01のcommit `0c8738c8c5c5d355fb856d126589c86ba636f5e2`までさかのぼる。取得記録はevidence/scenario-commit-history.json、scenario-prerename-history.json、scenario-rename-commit.json、scenario-earliest-confirmed-2022.py。公開のHELM版実装が2022年に存在する根拠としてyear=2022を採用する。最初の内部作成日や形式言語自体の成立日を確定したものではない。固定URL: https://github.com/stanford-crfm/helm/blob/c2ee966d79df97f5005d4352b13ddc1730c1f02f/src/helm/benchmark/scenarios/dyck_language_scenario.py

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/dyck.json)、[実際の校正対](skill-proofreading/dyck.md)、[全ページ文言](skill-proofreading/dyck/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/dyck/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/dyck/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
