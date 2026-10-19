# Numeracy 調査・制作記録

## 対象と主要な結論

日本語53ページ、本編32ページ、予定黙読・流し読み600秒（未実測）。作者sasakiy84、所属なし。共通SlideMaster.pptxからnative editable PPTXを制作し、その最終PPTXをPDF化した。ノートなし。

対象はHELMで導入された多項式帰納の人工生成課題。HELM論文のnumeracy_predictionと、公開コードのnumeracyを対応させた。Numeracy-600Kは別の自然言語データセットであり、ACL 2019の一次資料を取得して違いを確認した。年はHELMの初公開2022年（arXiv:2211.09110）に対応し、参考文献はTMLR掲載2023年を使う。

HELM Classic latest/config.jsを2026-10-18にHTTP200で取得し、latest=v0.4.0を確認。固定版v0.4.0のschemaにはnumeracyグループと主指標absolute_value_difference/testがあるが、run_specs、runs_to_run_suitesには該当runが0件。モデル別成績を作らず、公開runがないことを明記した。0件はモデルの得点0を意味しない。元リリースJSONのURL・ローカル参照・SHAをevidence/release-inventory.jsonに記録した。

## 公式生成器の固定と再現

公式ソースv0.3.0を直接取得。SHA256は73246f52e36508055946e44561c7ab086219e82038fe3a1737736f5a427a5403。キャッシュだけに依存せず取得した同一バージョンを使った。

公式の生成関数とNumeracyScenarioクラスのAST本体を保持し、HELMの基盤importのみ、文字列Input/Output、Reference、Instanceの最小dataclassとScenario基底へ置き換えて実行した。追加したfuture annotationsは型注釈の名前解決を遅延させるもので、係数選択・乱数・サンプリング・計算・文字列化の処理を変更していない。get_test_tokenizer_serviceなど、今回の生成に不要なサービスは呼んでいない。外部のモデル生成APIは利用していない。

固定条件：Python 3.12.14、NumPy 2.3.5、SymPy 1.14.0（正確な値はgeneration-summary.json）、seed=0、overlap=True、sort_vals=False。linear/parabola/plane/paraboloidの4型、example/standard/functionの3モードを実行した。動作する8組は各train100+test100、合計1,600件。functionは4型とも空リストで0件だった。ソースのgenerate_datasetsにはTODOとreturn []が残る。MODE_INFOの各1,000関数という設計値を、実際に得た件数として使わない。

各データセットの完全レコードとSHAをevidence/<type>-<mode>-seed0.jsonへ保存。全1,600件を、記録された式へSymPyで別途代入して再計算し、すべて正解値と一致した。各組のtrain/test入力が重複しないことも確認した。generation-validation.jsonに全件の検査を記録した。

## 実例13件と表示範囲

本編3件、追加10件。すべて公式生成器から得た実レコード。examples.jsonに関数型・モード・seed・配列位置・原レコード・正解・参照式・SHAを記録した。IDはこの資料で付けた識別子で、公式データの既存IDとは呼ばない。

各ページでは、train100件の連続した冒頭4件または6件をCSVの形で表示し、test入力1件を全文で示した。全100例を示した実プロンプトとは扱わない。公開runがないため、実モデルのプロンプト全体を取得したとも扱わない。CSVのヘッダーは公式get_dataset_headerに対応するx,yまたはx,y,z。数値は原データの文字列を保持し、右欄の日本語で入力と予測する変数の対応を説明した。参照式はメタデータと明示し、モデル入力に混ぜていない。

13例のsource_positionと全訓練レコード冒頭を、最終examples.jsonから再照合した。examples-verification.jsonに記録。赤字の正解は生成器が計算した参照値であり、モデルの生成結果ではない。

## 入力領域・係数・統計

linearは整数−100〜100、parabolaは0〜200で各201候補点。planeは2変数とも−10〜10、paraboloidは0〜20で、実装はx≤yを満たす点だけを残すため各231候補点。訓練100点とtest100点を重複なく選ぶ。

p17のnative散布図は、plane/standard/seed0の正確な200入力点。native chartのxVal/yValキャッシュをdomain-chart-data.jsonの100+100点と照合した（chart-audit.json）。軸ラベルはLibreOfficeがXY chartのタイトルを誤表示する挙動を避け、編集可能なnative textとして図の横・下に置いた。チャート本体と数値軸はnative editable。

paraboloidのコメントはaxis-alignedのみとするが、実際の係数範囲ではxy項の係数は0または1。standard/seed0はz=2x²+xy+y²+4となる。この実装とコメントの差をp46で具体的に説明した。x,yの一次項は0に固定される。

p47は、standard/seed0の各200件の実測出力範囲。全係数・全入力の極値ではない。元データからmin/maxを算出し、負数も右揃えにした。6表はbooktabs相当のnative表。

## 採点の検証

既定のexact_match、quasi_exact_match、absolute_value_differenceはrun_specsとBasicMetricで確認した。任意のDistanceMetricはrun_solver=Trueで追加される。defaultのadapterは最大訓練100、評価100、1試行、温度0、最大生成20トークン、改行停止（example/standard）。これらは公開設定で、実モデルをこの制作で実行した結果ではない。

公式の採点関数をASTでそのまま抽出して、説明用の予測文字列に適用した。metric-examples.jsonに正解・予測・3指標の実値を記録した。

- 正解64・予測64.0は、整数変換が失敗して予測0となり、絶対誤差64。
- 正解0・予測errorは、絶対誤差0だがexact_matchは0。
- quasi_exact_matchのnormalize_textは句読点を除去するため、正解64・予測-64を一致とする。絶対誤差は128。p22の表へこの差を明示した。
- 正解64・予測65の直線への幾何学的距離は1/√17≃0.243。数値の差1と区別した。

任意の数値ソルバー実装には失敗時に距離0を返す分岐があり、複数出力ではdistanceを合計している。今回の説明は既定num_outputs=1の線形の正常例だけを使う。モデル性能の集計をこの追加指標から推定していない。

## 出典・利用条件・画面

一次資料：HELM論文、v0.3.0のNumeracyScenario、get_numeracy_spec、BasicMetric、DistanceMetric、公式LICENSE、Classic設定・リリースJSON。区別用にNumeracy-600KのACL論文を取得。正規のURL・bytes・SHA・取得失敗をevidence/acquisition-log.jsonへ記録。mainの旧パスは404だったため、現在のコードの存在や動作を推定せず、固定版v0.3.0を説明した。

生成器コードはApache License 2.0。入力は人工的な整数列で、他者のWeb文章を含むコーパスの再配布ではない。コードのライセンスと生成数値の出所を区別し、公式コードへの帰属を各ページに付した。

独立したNumeracy公式サイトはなく、HELMが導入したシナリオなので、冒頭にHELM Classicの公式トップを置いた。通常TLS検証付き取得の応答をChromiumで描画し、CSS・ロゴ・主要図・フォントをview_imageで確認。CSS1、asset_failures=[]。Numeracyの成績画面と呼ばず、HELM Classicの公式サイトと明示した。

## 校正と最終検査

japanese-proofreadingスキルによるskill_based_codex。gemini_used=false。全53ページの最終文言とページ別確認をpage-review.json、実際の日本語修正対をproofreading-changes.jsonに記録した。データの数値、原文字列、式の符号は文章校正で変更していない。

全ページoverviewと全53ページの個別画像を実際にview_imageで開いた。数値引用の26枠とコード1枠はPDF実字形から余白を調整し、最終行まで確認した。表6、チャート1、文献3、公式画面を個別に検査。最終変更17/21/22/24/45/47ページも再目視した。

最終PPTXから出力したPDFで、layoutは381段落・59セル問題0、textは456段落問題0、native URL専用ラン57件とPDFリンク57件完全一致。標準XSDはマスター既存11件と整数buSzPct字句差を分離し、新規エラー0。内部参照・ZIP・図形ID・native chart200点・notes0を確認した。

独立レビューは自己検査と別にメインが割り当てる。この担当は共有repo/engine/gitを編集していない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/numeracy.json)、[実際の校正対](skill-proofreading/numeracy.md)、[全ページ文言](skill-proofreading/numeracy/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/numeracy/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/numeracy/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
