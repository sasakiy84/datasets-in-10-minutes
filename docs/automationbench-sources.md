# AutomationBench — 出典と制作範囲

制作・校正：`skill_based_codex`。Geminiと外部モデルAPIは未使用。2026-10-21（日本時間）に新規作成。表紙著者はsasakiy84、所属なし。共通SlideMasterを使用し、編集可能なPPTXと、それからLibreOfficeで変換したPDFを作成した。

主題は複数アプリにまたがる業務の実行であり、モデル発表資料そのものの解説ではない。公開課題と別の非公開評価集合、公式の厳密成功率と診断用部分点、APIと別のツール形式を説明した。

## 一次資料

- Daniel Shepard and Robin Salimans (2026), *AutomationBench*, arXiv:2604.18934。背景、課題の構築、採点、初期評価、著者を確認。https://arxiv.org/abs/2604.18934
- Zapier, *AutomationBench*、公開リポジトリのバージョン1.0.6。公開600件、simple200件、模擬環境、採点コード、README、CHANGELOG、LICENSEを照合。https://github.com/zapier/AutomationBench
- Zapier, *AutomationBench AI benchmark leaderboard*、2026-10-21参照。非公開集合の現在の成績、APIモード、fallbackの条件を確認。https://zapier.com/benchmarks
- Anthropic (2026), *Introducing Claude Fable 5.1 and Claude Mythos 5.1*。採用を確認。31.4%はOpus 5 fallbackの寄与を含むことを公式表の注記で確認。https://www.anthropic.com/claude-fable-and-mythos-5-1
- OpenAI (2026), *GPT-6 Astra: A new generation of intelligence*。採用を確認。https://openai.com/index/gpt-6-astra/
- Shuyan Zhou et al., *WebArena: A Realistic Web Environment for Building Autonomous Agents*, ICLR 2024。https://arxiv.org/abs/2307.13854
- Harsh Trivedi et al., *AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents*, ACL 2024。https://arxiv.org/abs/2407.18901

## 原票と確認範囲

公式の公開課題ローダーから6分野各100件とsimple200件を生成し、全件の構造・件数・定義された検査条件の数を集計した。全条件9,612、中央値11、最小3、最大64である。これは条件定義の数であり、実行ごとの部分点の分母と同じものではない。

本編3例と追加9例の、計12の異なる課題を掲載した。依頼のuserメッセージは全文、日本語訳も全文を掲載し、規則・表・メール・投稿は入力内容と期待される更新を追える箇所を抜粋・再構成した。原文の段落間の空行は、必要に応じて段落の余白で表現する。

模擬ツールの既知の正解操作列を手で構成し、会議調整・避難訓練・銀行照合の3課題で、公式の採点対象条件すべてを満たすことを確認した。これはエージェントの評価実行ではなく、モデルAPIを呼ばない参照操作の検証である。実際のメール、Slack、顧客管理サービスは操作していない。閲覧時間は予定600秒で、実測していない。PowerPoint本体での開封は未実施。

課題名とdomainの組で例を識別する。example_id単体は分野間で重複がある。初期状態中のアプリ数、公開資料が挙げる47アプリ、Pythonの状態モデルのfield数を同じ単位として数えない。

## 選定から外した課題

食事の金額と人数条件が期待する検査条件と整合しない経費例と、親会社案件の通知規則が明記されない受注例を除外した。除外の原票と理由はdata-audit.jsonに記録し、スライドに説明を増やす代わりに、明確に対応を追える例を選んだ。

## 実際の確認

全ページのnative文言・表・出典を原票と照合し、機械検査と独立担当の内容・描画レビューを組み合わせる。実際に個別画像を開いたページはvisual-progress.jsonに記録し、描画しただけのページを目視確認済みとはしない。最終承認前の引継ぎ票と独立した最終承認は区別する。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-automationbench.pptx)・[PDF](../slides/datasets-in-10-minutes-automationbench.pdf)。本編41頁、総85頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/automationbench.json)・[校正の修正対](skill-proofreading/automationbench.md)・[全ページ文言](skill-proofreading/automationbench/pages.jsonl)・[最終検証票](skill-proofreading/automationbench/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE.txt](licenses/automationbench/LICENSE.txt)、[ATTRIBUTION.md](licenses/automationbench/ATTRIBUTION.md)。
