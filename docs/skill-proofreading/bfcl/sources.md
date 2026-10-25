# BFCL — 一次資料・例・利用条件

2026-10-25参照。固定Git revision: 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8。

- **The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models** — Shishir G. Patil et al. (2025), ICML 2025, PMLR 267:48371–48392.
  関数呼び出しのデータ構築と、構文・実行・状態を使った採点を報告する。
  https://proceedings.mlr.press/v267/patil25a.html

- **Berkeley Function Calling Leaderboard (BFCL) V4** — Gorilla Team (n.d.), UC Berkeley. 2026-10-25参照。
  バージョン4の課題別成績と、モデルの呼び出し設定を公開する。
  https://gorilla.cs.berkeley.edu/leaderboard.html

- **Berkeley Function Calling Leaderboard** — Gorilla Team (2024), Gorilla Blog 8.
  単一ターンの関数選択、複数回の呼び出し、ASTによる採点を導入する。
  https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html

- **BFCL V2 • Live Dataset** — Gorilla Team (2024), Gorilla Blog 12.
  実際の利用者の依頼を収集・選別した、Liveデータの構築と内訳を示す。
  https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html

- **BFCL V3 • Multi-Turn & Multi-Step Function Calling Evaluation** — Gorilla Team (2024), Gorilla Blog 13.
  会話の各ターンで、APIの状態と実行結果を確認する評価へ拡張する。
  https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html

- **BFCL V4 • Agentic Part 1: Web Search** — Gorilla Team (2025), Gorilla Blog 15.
  検索とページ取得で答える課題を導入し、総合得点の構成も説明する。
  https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html

- **BFCL V4 • Agentic Part 2: Evaluating Tool Calling for Memory** — Gorilla Team (2025), Gorilla Blog 16.
  利用者の情報を保存・更新する課題と、三つの記憶方式を比較する。
  https://gorilla.cs.berkeley.edu/blogs/16_bfcl_v4_memory.html

- **BFCL V4 • Agentic Part 3: Evaluating Format Sensitivity for Tool Calls** — Gorilla Team (2025), Gorilla Blog 17.
  指示や関数定義の書式を変えて、関数呼び出しの頑健性を調べる。
  https://gorilla.cs.berkeley.edu/blogs/17_bfcl_v4_prompt_variation.html

- **Berkeley Function Calling Leaderboard: Code and Data** — Gorilla Team (n.d.), GitHub, Apache License 2.0. 2026-10-25参照。
  質問、関数定義、参照条件と、応答の生成・採点に使う実装を公開する。
  https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

- **Sublime Pogačar seals third Tour victory in Nice** — Tour de France (2024), Amaury Sport Organisation.
  2024年の優勝結果を報じ、Web検索の実例が参照する選手を確認できる。
  https://www.letour.fr/en/news/2024/stage-21/sublime-pogacar-seals-third-tour-victory-in-nice/1324643

選定は本編3例とAppendix10例。単発11例に加えて、全3ターンと初期ファイルを読める複数ターン例、出生国を調べるWeb検索例を含めた。同じ仕様の類似例だけに偏らないよう、Java/JavaScript、引数なし、中国語、関数不適合、候補選択、複数呼出を扱う。全質問と訳、単発の全仕様フィールドを示す。複数ターン/Webの仕様は読者の理解に必要な要点を抜粋と明記し、完全原票・全仕様・全goldはexamples.jsonとselected-raw.jsonへ保持した。

論文の構築・歴史的成績、公式ブログの版別説明、固定コードの現在の採点、公式CSVの現在の成績を区別した。current codeと古い論文のAgentic照合記述の差、Liveカテゴリ2件の差はdata-audit.jsonへ記録し、細かい再現条件として本文を増やさない。

ライセンス原文と改変・翻訳の帰属はLICENSE-BFCL-Apache-2.0.txt、ATTRIBUTION-BFCL.md。公開データ/統計についてREADMEのApache 2.0記述とroot LICENSEを読んだ。コードやモデル評価は実行せず、公開データの静的読解・照合だけを行った。校正はskill_based_codexで、Geminiを使っていない。

Web例の出生国は参照goldに加え、選手本人公式プロフィール https://tadejpogacar.com/about-me/ の出生地Klanec,Slovenijaと、大会公式の2024年勝者記事で独立レビュー担当が照合した。この追加確認はreview-bfclの独立記録に属し、creator自身による一次取得とは区別する。
