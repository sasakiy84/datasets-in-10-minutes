# BFCL：スキルによる日本語校正とレビュー

Geminiは使用していない。ローカルの制作・日本語校正スキルで作成し、作成担当とは別の担当が内容・原票・描画を確認した。以下は実際に行った修正の対である。最終版の確認範囲とファイルの対応は検証票に記録した。

|ページ・対象|修正前|修正後|理由|
|---|---|---|---|
|全体|108-page draft with all field text for multi-turn and web tools, including entire region enum|Preserve every user turn, complete initial file, full ground truth; clearly labelled excerpt of relevant tool capabilities/arguments/types/defaults|データセットの概要と使い方に必要な情報へ整理し、細かすぎる仕様列挙を検証記録へ分ける。|
|9,10,11|複数の候補から、由来を調べる関数を選ぶ|仏教の起源を調べる関数を選ぶ|通常タイトルを一行で読める長さにした。|
|71|関数呼び出しの形だけでなく、専用の回答欄に書く国名を採点する。|関数呼び出しの形ではなく、最終的な文章に参照の国名が含まれるかを採点する。|現在の採点コードは専用回答欄を抽出せず、最後の文章を照合する。|
|全体|Function name alone at bottom of page, remaining definition on next page|Keep a complete function definition together where it fits; split only meaningfully at field boundaries|改頁位置で関数と説明の対応が失われるのを防いだ。|
|10|仏教を開いたのは誰で、どこで生まれたのか。|仏教の開祖は誰で、仏教はどこで始まったのか。|仏教の起源を人物の出生地と誤読しないよう主語を明示。|
|69|優れた持久力を持つ選手|持久力に優れた選手|日本語の自然な修飾関係にした。|
|22|ノート整理|個人の予定・タスク管理|一次資料のPersonal To-Do Listに対応する具体的な用途にした。|
|81|BFCL V3 • Multi-Turn & Multi-Step|BFCL V3 • Multi-Turn & Multi-Step Function Calling Evaluation|参考文献の正式な見出しを保持。|
|81|BFCL V4 • Web Search|BFCL V4 • Agentic Part 1: Web Search|参考文献の正式な見出しを保持。|
|82|BFCL V4 • Memory|BFCL V4 • Agentic Part 2: Evaluating Tool Calling for Memory|参考文献の正式な見出しを保持。|
|82|BFCL V4 • Format Sensitivity|BFCL V4 • Agentic Part 3: Evaluating Format Sensitivity for Tool Calls|参考文献の正式な見出しを保持。|
|7|数5の階乗を計算する。|5の階乗を計算する。|自然な依頼文にした。|
|8|出力として求めるのは120という計算結果ではなく、関数名と引数である。numberには整数5を渡す。|階乗を求める関数math.factorialを選び、numberに整数5を渡す。|入力と正解例から分かる否定を削り、動作を直接説明した。|
|21|日々変わる株価ではなく、受賞者や過去の大会結果など、最近の安定した事実を問う。|受賞者や過去の大会結果など、最近の安定した事実を問う。|自明な対比を削り、採用した問題の性質を述べた。|
|全体|単一ターンの関数選択だけでは、総合得点を十分に表せない。||重みの表から分かる注意の繰返しを削った。|
|全体|質問や関数定義を読むだけなら、モデルの応答を生成する必要はない。||公開データの説明から分かる自明な否定を削った。|
|67|find(path=".", name="None") は|find(path=".") は|省略時の挙動を説明する例に、文字列Noneを検索する引数を入れない。|
|9|例2原文を二つの関数ごとに2頁、日本語訳も2頁に分割|原問と全二関数仕様を原文1頁17pt、日本語訳も1頁17ptへ統合|原文を一頁で読むことを優先し、訳のために原文を分割しない。|
|52|中国語の依頼1行だけの原文頁、その次に天気の仕様頁|中国語の依頼全文と最初の関数仕様全文を同じ頁に17ptで表示|余白だけの頁で入力を分断せず、候補関数と依頼を対応させる。|
|57|二都市の天気の依頼だけ1頁、唯一の関数仕様が次頁|原文の依頼と全関数仕様を17ptで一頁に表示|原文のまとまりを一頁で把握できるようにした。|
|10|訳文本文上端1.81in、保守的出典間隔7.10pt|訳文本文上端1.77in、全ページ出典間隔監査問題0|出典との余白を確保した。|
|23|バージョン列の1–4と見出しを左寄せ|バージョン列の数値と見出しを右寄せ|数値列と対応する見出しの組版を統一した。|

[全ページ文言](bfcl/pages.jsonl)・[最終検証票](bfcl/review.json)・[メインの確認](bfcl/main-review.json)
