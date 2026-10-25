# BFCL 独立一次資料レビュー

独立担当 `/root/new_three_coordinator/review_bfcl` が、作成担当の保存物を取得元の代わりにせず、固定版GitHub、公式ブログ、ICML論文、公式公開CSVを取得した。原票との機械的比較を実施したうえで、選定された13例の質問、関数仕様、参照呼出・回答を実際に読んだ。日本語訳・完成版の描画は後続レビュー対象であり、この記録の時点では完了扱いにしない。

## 出自・版・構築

初期BFCLは2024年公開、ICML2025論文はPatilほか7著者（全員UC Berkeley）。論文の正式タイトルと著者順、会議/頁はPMLR書誌とPDF冒頭で照合した。論文本文1–5頁とp6–7の初期結果・FC/Prompt・カテゴリ差の説明を読み、課題、構築、単発AST、複数ターンの状態/応答評価、Agentic評価の当時の記述を確認した。全22頁の全文章を読了したとの主張はしない。

公式V1ブログのカテゴリ定義と構築説明、V2ブログの実利用者入力の収集/加工説明、V3ブログのAPI構築・グラフ・人手参照経路・検証・状態/応答採点の該当本文を読んだ。V2は2024-02-26から04-01の64,517クエリを素材とし、重複・既存データとの重なりを除去、関数仕様を標準化する。V1のmultipleは複数候補から適切な関数を選ぶ。現行TEST_CATEGORIES.mdのsequence表現と不一致があるため、元定義・原票・採点コードに従う。

## 現行V4の採点・件数

固定取得版は `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`。公開データ20ファイルを独自取得しレコードを数えた。件数はown-dataset-counts.json。20ファイル数と評価カテゴリ展開数は同義ではない。Web100問は2条件、Memory155問は3バックエンドへ展開される。

公式V4ブログの総合weightはAgentic40%、MultiTurn30%、Live10%、NonLive10%、Irrelevance10%。現行eval_runner_helper.pyの実装と一致。NonLive内部はカテゴリ平均、Live内部は件数重み付き、Irrelevance内部はNonLiveとLiveの正解率を等重みで平均する。AgenticはWebとMemoryの各平均を等重みで平均する。古いHTMLの単純平均という説明と区別した。

ブログのlive irrelevance882/relevance18と固定データ884/16には差がある。実装save_eval_resultsの分母はlen(model_result)、882固定ではない。full評価は入力と回答の件数一致を要求する。細かい差を独立スライドに増やさず、意味のある集合・条件を説明する方針を作成担当へ通知した。

ASTコードは関数名、必要な引数、型、許容値を照合する。parallelとparallel_multipleは順不同で呼出を対応付ける。任意引数の許容値に空文字がある場合は省略を許す。irrelevanceは関数呼出なしを判定し、文章の理由の適切さは採点しない。選定されたmath.factorial(number=5)は提示されたBFCL仕様であり、Python標準ライブラリの実際の引数名を検査した例ではない。

現行Agenticコードは、最後の非関数呼出メッセージを対象に正規化後の参照語を語境界付きで含有照合する。途中の呼出経路は採点対象でない。論文p5の専用answer fieldのstrict exact matchという記述と現行コードは一致しない。現行版に合わせるよう作成担当へ通知済み。コードを読み、ベンチマークの評価やモデルは実行していない。

## 実例と正解

当初選択13から円計算と音量を差し替え、最終13は11単発、1複数ターン、1Web検索。全13原票と参照回答を、担当自身が固定版から取得したデータへ厳密に比較し一致を確認した。irrelevanceには個別goldファイルがないため、採点コードから無呼出条件を確認したという範囲を分けた。multi_turn_base_47の全3ユーザー発言、初期student_record.txtの6人分の点数、参照最小経路を読んだ。関数仕様4件は全APIの抜粋であることを明示する。Webの2仕様は全available仕様に一致する。

Web例web_search_50のSloveniaは、Tour de France公式の2024年勝者記事と、選手本人の公式プロフィールの出生地Klanec,Slovenijaで裏付けた。国籍だけから出生国を推測していない。取得先・HTTP結果はweb-example-primary-acquisition.json。

## 利用条件と結果

GitHubのApache2.0 LICENSEを独自取得し、READMEの公開条件と照合した。2026-10-25取得の公式CSVでOpus4.5 77.47%、Sonnet4.5 73.24%、Gemini3ProPreview Prompt72.51%、GLM4.6 FCthinking72.38%を確認した。公式ページの更新表示は2026-04-12。取得日とモデル公開日/測定日時を混同しない。
