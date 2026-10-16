# τ²-bench：出典と確認範囲

2026-10-16作成。日本語「datasets in 10 minutes」。本編39枚＋Appendix30枚、計69枚。作成者sasakiy84、所属欄なし。顧客と担当者がツールを使って問題を解くτ²-benchを中心に、τ³-benchの文書検索・音声への拡張を紹介する。本編は入口30秒、課題と実例175秒、評価135秒、作成と全体像135秒、系列と利用125秒の計600秒を想定し、閲覧時間は未実測。

## 一次資料と固定した版

- Victor Barres, Honghua Dong, Soham Ray, Xujie Si, Karthik Narasimhan (2025). *τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment*. [arXiv:2506.07982v1](https://arxiv.org/abs/2506.07982v1)、2025-06-09。取得したPDFはPreprint / Under reviewの表記。
- Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan (2024). *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*. [arXiv:2406.12045v1](https://arxiv.org/abs/2406.12045v1)、2024-06-17。
- Quan Shi, Alexandra Zytek, Pedram Razavi, Karthik Narasimhan, Victor Barres (2026). *τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge*. [arXiv:2603.04370v1](https://arxiv.org/abs/2603.04370v1)、2026-03-04。
- Soham Ray, Keshav Dhandhania, Victor Barres, Karthik Narasimhan (2026). *τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains*. [arXiv:2603.13686v1](https://arxiv.org/abs/2603.13686v1)、2026-03-14。
- [公式リポジトリ](https://github.com/sierra-research/tau2-bench)：今回取得したHEADは`96a3ef92329baf908ffe9dfe188cea34e8701d2a`。現行README、公開提出JSON、ライセンスを参照。
- τ²の課題・評価コード：タグ[v0.2.0](https://github.com/sierra-research/tau2-bench/tree/v0.2.0)、コミット`f8de30c298689cbe0117d76a378e7315a17e5bd8`（2025-10-06）。`data/tau2/domains`および`src/tau2`を参照。
- τ³の銀行課題・商品文書：タグ[v1.0.1](https://github.com/sierra-research/tau2-bench/tree/v1.0.1)、コミット`fc0055dc4e0a316c3f83133267fbd6faaa770992`（2026-07-16）。`data/tau2/domains/banking_knowledge`とリリースノートを参照。シリーズ名のτ²／τ³と、ソフトウェアのv0.2.0／v1.0.1を区別した。

冒頭の実画面は[Hugging Faceの論文紹介ページ](https://huggingface.co/papers/2506.07982)。公式サイトtaubench.comはこの環境からCONNECT 403となったため、見出し・出典を「論文の紹介ページ」として掲載した。ChromiumでCSS・本文フォント・主内容の反映を確認し、スタイルが効いた実画面を使った。

## 実例と評価コード

公開課題の顧客シミュレーター向け設定を英語で抜粋し、日本語で課題内容と完了条件を説明した。実行済みの対話ログとしては扱っていない。原文は空白の正規化だけを行い、全14件について元レコード内の文字列との一致と課題の一意性を検査した。

|掲載ページ|系列|領域|課題ID|
|---|---|---|---|
|8|tau2|retail|`0`|
|10|tau2|telecom|`[mobile_data_issue]data_mode_off&#124;data_usage_exceeded[PERSONA:None]`|
|12|tau2|airline|`7`|
|33|tau3|banking_knowledge|`task_001`|
|43|tau2|retail|`2`|
|44|tau2|retail|`3`|
|45|tau2|retail|`6`|
|46|tau2|airline|`0`|
|47|tau2|airline|`3`|
|48|tau2|telecom|`[service_issue]airplane_mode_on&#124;unseat_sim_card[PERSONA:None]`|
|49|tau2|telecom|`[mms_issue]bad_network_preference&#124;user_abroad_roaming_disabled_on[PERSONA:None]`|
|50|tau2|telecom|`[mms_issue]break_app_sms_permission&#124;data_mode_off[PERSONA:None]`|
|51|tau2|telecom|`[service_issue]airplane_mode_on&#124;break_apn_settings[PERSONA:Hard]`|
|52|tau3|banking_knowledge|`task_074`|

小売の交換商品・返品対象、航空予約の取消・運賃変更・金額、通信端末の初期化・参照操作・終了時assertion、銀行の商品条件・返金額をそれぞれデータとコードへ対応させた。銀行task_001のGold Rewards Cardは年会費0、還元率2.5%、Rho-Bank+資格を商品文書`doc_credit_cards_gold_rewards_card_001.json`で確認した。task_074はv1.0.1の参照返金額27.00、14.50、4.75、3.70を採用した。

`src/tau2/metrics/agent_metrics.py`の`pass_hat_k`を読み、純粋関数を抽出して4試行・3成功の場合のpass¹=.75、pass²=.5、pass⁴=0を確認した。式はC(成功数,k)/C(試行数,k)。DB・伝達・アクション・環境assertionの採点経路を読み、参照アクションと必須の操作順序を混同しない説明にした。モデルAPIの呼出しや全ベンチマークの再実行はしていない。

## 構成と集計

固定したv0.2.0の公開課題はretail 114、airline 50、telecom 114の計278件。論文のretail 115とは一致しないため、スライドでは固定タグの公開課題数を採用した。差の原因は未確認。

通信の全組合せは論文の2,285件、原子的な小課題は15種類、選抜された公開課題は114件。IDから集計した主問題はMMS 49、mobile data 36、service 29。personaはNone 40、Easy 38、Hard 36。小課題数2〜9の件数は順に25、26、21、13、11、8、4、6件。

ツールのREAD／WRITEは固定タグのデコレーターを集計し、小売6／7、航空6／6、通信担当者6／6、通信顧客15／15とした。GENERICを除くREAD／WRITEの数である。論文の通信READ 7とは数え方が一致しないため、コードに対応する数と見出しを採用した。銀行v1.0.1は課題97件、商品・手続き等の文書JSON 698件。

## モデル結果と取得時点

- 初期の通信結果はBarresらの2025年論文。GPT-4.1約34%、o4-mini約42%、Claude 3.7 Sonnet約49%。顧客GPT-4.1、4試行、temperature 0。顧客のツール操作を外す比較はGPT-4.1が18ポイント、o4-miniが25ポイント低下。
- [Google DeepMind, Gemini 3.1 Pro公式比較](https://deepmind.google/models/gemini/pro/)を2026-10-16にライブ取得。τ²のretail／telecomはGemini 3.1 Pro Highが90.8／99.3%、Claude Opus 4.6 Maxが91.9／99.3%、GPT-5.2 xhighが82.0／98.7%。High／Max／xhighを推論設定として示した。
- τ³銀行は現行リポジトリの`web/leaderboard/public/submissions`以下の提出JSON。`claude-opus-5_sierra_2026-08-04`はpass¹ 48.7113402%、pass⁴ 31.9587629%。`gpt-5-5_sierra_2026-05-05`は44.5876289／29.8969072%。`gemini-3-1-pro-preview_sierra_2026-05-05`は26.03／9.28%。4試行、AllTools、v1.0.1。AllToolsの語句検索・意味検索・シェルを説明した。GPT-5.5の現行提出JSON値44.59%とリリースノートの再採点値46.39%には差があり、掲載表は現行提出JSONを採用した。
- τ³音声は`grok-voice-3-0_xai_2026-10-14`。公開2026-10-14、評価2026-10-08、telecom 82.4561%。1試行、顧客GPT-5.5 xhigh、regular speech、200 ms ticks、1200秒上限の提出。コード改訂`4ce7c0397c1eb65c9bbe59aeacfe1ca44a1cd699`。テキスト結果とは別のページで条件を添えた。

## 制作と検査

共通SlideMaster.pptxを継承。表紙52 pt太字、英数字Noto Sans、日本語Noto Sans CJK JP、緑帯14 pt太字、コードLiberation Mono。編集可能な表16個・グラフ2個。表上端と下端1.2 pt、見出し下0.6 pt、縦罫なし。発表者ノートなし。

全69ページをレンダリングしてコンタクトシートを目視確認。表176セル、14件の引用枠、本文と出典の間隔、全62件のURLリンク範囲、ページ外要素・見出しを検査した。本文と出典の最小間隔9.03 pt、引用枠の上下余白6〜10 pt。PPTXのZIP・内部参照・86 XML部品を検査し、既知のbuSzPct字句判定132件以外のスキーマエラーは0。値は仕様の範囲内。PDFとPPTXは同じ改訂。

ギャラリーに11件目として追加し、タイトル検索（tau2、τ²、全角文字）、既存の種別・タスク・年フィルタと年順、全PDFリンク、デスクトップと390 px幅の表示を検査し、全項目を通過した。公開年はτ²の初公開2025年、種別「言語」、タスク「エージェント操作」とし、新しい分類ラベルは増やしていない。

## ライセンス

公開課題の抜粋・商品条件等の出典はSierra Researchの公式リポジトリ。MITライセンスの著作権表示と許諾文を以下に保持する。

```text
MIT License

Copyright (c) 2025 Sierra Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 54〜56ページの説明改訂

54〜55ページは「1課題に組み合わせた不具合の数」と「該当する課題の件数」に改め、通信OFFとデータ容量超過の組合せ、各行の読み方、通信114課題との対応を加えた。56ページは担当者・顧客それぞれの読取・更新を独立した列にし、契約照会・端末確認・データ容量追加・通信ONの具体例を添えた。追加ページなし。PDFの文字と描画を旧版と比較し、変更が54〜56ページだけであることを確認した。全69ページの再描画検査と表176セルの検査、PPTX構造検査を通過し、変更した3ページを目視確認した。
