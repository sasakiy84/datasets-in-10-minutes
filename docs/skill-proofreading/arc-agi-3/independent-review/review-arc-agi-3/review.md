# ARC-AGI-3 独立レビュー

担当: /root/review_arc3。作成担当: /root/create_arc3。レビュー用ディレクトリのみに書き込み。Codexによる内容・事実・日本語・技術監査。Geminiおよび外部生成APIは使用しない。

## 読了・環境

AGENTS.md、master-guided-slides、dataset-introduction-slides、japanese-slide-proofreading を読了。cloud-environment-runtime と networking を読了。network-policy.json は unrestricted / vpn_configured:false。environment_status も現在観測 enforced/connected。通常ネットワークshellは追加network権限、proxy/CA/TLS検証を維持。

## 一次資料調査 (2026-10-20)

- 公式ARC3ページ、2026-03-25 launch、arXiv abstract(v2=2026-04-17)、arXiv v2 HTML、benchmarking READMEを独立取得。
- OpenAI記事2件はurllibで403。利用可能なweb tool経由で独立取得し evidence/openai-web.json / settings-web.json に保存。
- 技術論文HTMLを作者の取得物からも別にclean parseして照合。作者HTMLはv1、独立取得はv2であることを全文diffで検出。paper-version-diff.txtを保存。
- launchの標語0.51%と論文Table2最高0.37%が異なる。初期成績は論文表の対象・時点へ固定するよう作者へ助言。

## 制作前の主要照合

- ARC3は静的ARC2と別の対話環境。64x64/16色のframeまたはframe列を見て、離散行動で規則・goalを探る。
- 論文Table1はpublic25、semi-private55、fully-private55=135環境。候補414/486人/2893attemptsは人間実験候補全体であり採用数と別。
- 人間100%は全員100%ではない。各環境10人中少なくとも2人が初見で全レベル成功した採用条件。v1はsecond-best first-run action count、v2はupper-median successful action countが基準。v2は4人または5人成功なら行動数昇順3位を選ぶ。
- 論文v1のRHAEはレベルごと min(1,(human/agent)^2)、未解決0、レベル番号で線形重み、環境を平均。v2はupper-median基準と115%上限・達成重み比率による環境上限へ変更。SDK0.9.7は2026-04-14にlevel cap115%とgame cap変更を公表。v2数式はmin(1.15,h/a)^2で文章115%capと不整合。SDK0.9.9実装scorecard.pyは二乗後min(score,115)であり、説明はこちらへ対応させる。
- 論文v1初期semi-private表: Gemini3.1ProPreview0.37 / GPT5.4High0.26 / Opus4.6Max0.25 / Grok4.20Beta0309Reasoning0.00 (%)。v2初期表へ更新: Opus4.6Max0.50 / Gemini3.1Pro0.40 / GPT5.4High0.20 / Grok0.10 (%)。初期段階の私の『v2旧100%』助言を作者・mainへ即訂正。
- OpenAI GPT6Astra表は99.9%、Sol7.8%、Opus5 30.2%。Astra脚注はResponses API harness。各モデル最大effortの集計。
- July29設定記事のSol13.3→38.3はpublic集合。7.8と同じ列で同条件のように比較不可。推論保持と圧縮の2設定、出力token6分の1。standard175k charactersと独自175k tokensの違いは原票に記録。
- 現行benchmarking READMEはStandard/manual_rolling と Provider Adapter/continuous_conversation の結果を分けて報告するよう明示。論文の初期『no harness』を現状に一般化しない。
- SDK/benchmarkingのMITは確認。環境・game素材等の権利まで一括MITと一般化しない。

## 実例について作者へ連絡済み

13件は別game単位。同一gameのレベル違いで水増ししない。実観測のaction/frameのみ利用し、正解操作列やgoalを推測して作らない。ランダム探索は『観測→操作→変化』として説明し、実成功がないときは成功列と称さない。
collect.pyの選択stepがレベル遷移を跨ぐ場合、最初のresetを基準にlevel名を固定できないことを指摘。pixel_changesにはUI timerの変化も入り得るため、mechanicを示す根拠は実ボードを確認する。

## 現時点の未実施範囲

完成PPTX/PDF未受領。構造・schema・全例照合・日本語・描画・リンク・最終hashの検査は未実施。全頁の独立visualはmain手配の別担当と統合予定。現時点では承認しない。

## 現行公式leaderboard独立取得

`https://arcprize.org/media/data/leaderboard/v3.json`を独立取得。datasetId v3_Semi_Private。Astra standard max=62.7128%、Provider Adapter high=99.9457%、Provider Adapter max=98.5507%。Sol standard max=7.78%、Opus5 high=30.16%。同一条件比較と別条件のprovider adapterは区別するよう作者へ通知。modelReleaseDateを提出日と同義にしない。

## 実データの独立再生

13公開gameの作者random探索全trace（各最大30操作、bp35のみ途中24観測）を、自review内へコピーした環境sourceを使ってSDK OFFLINEで再生。全観測frame/state/levels_completedが一致。全13件の選択PNGもraw最終frameから16色→RGB→nearest512pxで再構成し完全一致。replay-audit.json / replay.py に記録。13件すべて未完了level1のため、これだけでgoal推定・学習の意味を説明するのは不十分とmainに同意し作者へ指摘。

OpenAI設定記事が直接参照するHF human logs mirrorからshard2(14,062,017bytes)/shard5(39,275,328bytes)を取得。各gameでwon=1の最短総行動sessionを選び5game抽出。lp85(238観測/8levels)、ka59(442/7)、cd82(125/6)、ft09(150/6)、ls20(473/7)を独立SDK OFFLINEで全再生し、全frame/levels_completed完全一致。ka59のaction_input旧hashも現行環境における全遷移一致を確認。human-replay-audit.json / replay_human.py に保存。追加取得re86/s5i5は抽出のみでSDK再生未実施。作者へ本編3例の成功feedbackに使えるlp85/ka59と追加改善候補を提供。

human-lp85/ka59-contact.pngを実viewしlevel1完了と次level遷移を確認。ただしこれらは成果物PDFページの独立viewには数えない。

## 初稿技術検査 (最終承認ではない)

初稿PPTX SHA256 b40ba7bdf8eff80ff9d657353babbe9ac7e559db27c566cb1b2d8f5b96ecebe9、43頁。全頁native text/tableを抽出して通読。ZIP/internal rels/unique shape ID問題なし。author=sasakiy84、notes0、native tables10/chart1。59partsの標準XSD検査で新規nonlexical errorなし、整数buSzPct124件はSDK定義域25000–400000を別検証。マスターの既存schema差と字句表現差はpackage-audit.jsonに実数を保存。多数頁sources text frameの下端がslide外へ出ており、作者へ修正依頼。glyph内だけでframe合格にはしない。

最終版待ち。初稿の検査を最終版の検査と扱わない。

## 改訂候補46頁の内容監査

PPTX 6f9d916b6893c48ef12d4e9e0d391f16f5c66614268d4389ac96f05ee0efee28 / PDF 3d8c188e446b048939e9146ca675332467ea92919014b00a906fd8f2e29457baをfinal-candidate/へsnapshot保存。これはfinalという名前の作業snapshotであり、その後さらに章順・組版を直す予定なので最終納品版と扱わない。46頁全native text/tableを通読。表紙AGI展開・v2初期表・成功feedbackへ改善済み。sources枠のslide外は解消、127xml/62schema parts、新規nonlexicalエラー0、notes0、native table10/chart1。

全13例のrawを直前available_actionsと照合。lf52の新target-rawは非提供ACTION5を使用し、作者へ提供内actionへ差替依頼。ft09公開humanログ途中に非提供key actionsがあるが、表示終盤41–43は有効なACTION6のみ。その他12例の表示操作は有効。menu-audit.jsonへ全件保存。

本編の章帯が1→2→1→3→2→4と往復する構成はmainが作者へ整理依頼。最終頁数・順序が変わる予定のため、独立visualは最終SHA固定まで待機。
