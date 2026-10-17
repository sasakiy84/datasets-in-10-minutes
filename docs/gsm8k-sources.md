# GSM8K：出典と制作・校正記録

2026-10-17作成。本編36ページ、Appendix38ページ、合計74ページ。英語の算数文章題を読み、解説と最終回答を生成する課題を紹介する。本編は約10分の黙読・流し読みを想定し、Appendixを含めた完全版PPTXと、その最終改訂から出力したPDFを収録する。閲覧時間は未実測。

## 一次資料と固定した版

|資料|用途・参照した版|
|---|---|
|[Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168)|Karl Cobbe, Vineet Kosaraju et al., OpenAI, 2021。収集、解説と計算注釈、検証器、6Bモデルの5.2%／20.6%。|
|[公式リポジトリ](https://github.com/openai/grade-school-math)|`3101c7d5072418e28b9008a6636bde82a006892c`。train.jsonl、test.jsonl、README、dataset.py、MIT License。|
|[公式紹介記事](https://openai.com/index/solving-math-word-problems/)|OpenAI, 2021-10-29。2026-10-17にブラウザで撮影した実画面を掲載。|
|[公式データカード](https://huggingface.co/datasets/openai/gsm8k)|正式名称Grade School Math 8K、通常形式mainとSocratic形式。|
|[GPT-4 Technical Report](https://arxiv.org/abs/2303.08774)|OpenAI, 2023。5-shot CoTで92.0%。学習集合の一部を事前学習に使用した旨を添えた。|
|[Qwen2.5-Math Technical Report](https://arxiv.org/abs/2409.12122)|An Yang et al., 2024。Table 3のCoTとTIR、maj@8を区別。72B-InstructのCoT95.9%、TIR95.8%、TIR maj@8 96.7%。|
|[GSM1k](https://arxiv.org/abs/2405.00332)・[GSM-Symbolic](https://arxiv.org/abs/2410.05229)|Hugh Zhang et al., NeurIPS 2024／Iman Mirzadeh et al., ICLR 2025。新規問題と具体化を変えた問題による汎化・頑健性。|
|[Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k)|`d6de81643928d653435c431bae19945d41d32520`。2026-10-17確認。gsm8kの5-shot設定と回答抽出。|

最初の約1,000問はUpworkの契約作業者が作成し、Surge AIと収集を拡大した。GPT-3が生成した例題も作成の種に使われたため、AIの関与がない収集とは説明していない。全問を別の作業者が解き直し、不一致を修正・除外した。小規模な再検査での1.7%は、不一致に基づく重大な誤り・曖昧さの推定として記した。

## 件数と集計方法

公式配布ファイルを全件取得した。学習7,473問、テスト1,319問、合計8,792問。原著の学習7.5K・テスト1Kは概数として区別し、差の原因を推測していない。文字数はPythonのlenで空白・記号・改行を含め、単語数はsplit()、母標準偏差はstatistics.pstdevで計測した。分位点は昇順に並べた位置round((n−1)×p)の値を採用する。

テスト問題文は平均239.9文字、中央値222文字、母標準偏差97.6文字。文字数の階級0–199／200–399／400–599／600–799／800以上は508／724／82／4／1問で、全1,319問を含む。answer全体は計算注釈・最終回答を含めて別に計測した。集計値と取得ファイルのSHA-256は[検証データ](data-audits/gsm8k.json)に保存する。

## 掲載実例

本編3問と、重複しない追加10問。問題文の全文と日本語訳、条件から組み立てる計算を掲載した。日本語訳と表が窮屈になる場合は計算を独立したページへ分け、訳だけのページは見出しも「問題の日本語訳」に合わせた。最終回答は公式の`####`以降と照合した。レモンの問題は12年目に費用を回収し、13年目に利益が出ることを区別する。

|区分|公式の識別子|内容|
|---|---|---|
|本編|testの0始まり行 0|卵の売上|
|本編|testの0始まり行 5|2個目ごとの割引|
|本編|testの0始まり行 12|費用回収と利益の違い|
|追加例|testの0始まり行 1|布の必要量|
|追加例|testの0始まり行 2|家の転売による利益|
|追加例|testの0始まり行 3|1週間の走行距離|
|追加例|testの0始まり行 4|最後の給餌量|
|追加例|testの0始まり行 6|羊の数と倍率|
|追加例|testの0始まり行 7|中断後のダウンロード|
|追加例|testの0始まり行 9|残業を含む賃金|
|追加例|testの0始まり行 10|増減後の累計|
|追加例|testの0始まり行 13|残りの数から逆算|
|追加例|testの0始まり行 14|割合の基準を追う|

## 利用条件

公式配布物はMIT License。著作権・許諾表示を[ライセンス本文](licenses/gsm8k-MIT.txt)に収録した。原文・コードの引用と、日本語訳・説明を区別している。

## 日本語校正と表示の確認

日本語の校正には、[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)をCodexで適用した。Geminiや外部の文章生成APIは利用していない。ページごとの確認は`docs/skill-proofreading/gsm8k/pages.jsonl`、修正前後の対は同ディレクトリの`changes.tsv`、最終検査とSHA-256は`review.json`に保存する。新規に作成した資料の初稿からの変更であり、既存資料へのGemini提案の再利用記録とは区別した。

共通マスターを保持し、日本語はNoto Sans CJK JP、欧文はNoto Sans、コードはLiberation Mono。長い説明は左揃えの通常文とし、表・グラフ・コード・引用の文字は編集可能にした。写真・公式サイトの画面だけは画像として配置する。

全ページの一覧に加え、各ページを900×506相当の拡大画像で順に確認した。最終の調整ページも再出力して確認。PPTXとPDFのページ数・段落、タイトルの1行表示、ページ外の文字、表セル内の収まり、本文と出典の8pt以上の間隔、引用・コード枠、URLだけへのリンクを検査した。グラフの値は内蔵Excelブックと照合した。

ZIP整合性、XML解析、内部参照、図形IDの重複を検査し、標準OOXML XSDとの照合でマスター由来の既存差分と箇条書き百分率の字句形式差を分離した。整数形式のbuSzPctは25000〜400000の範囲を別途検査した。新規の構造エラーはない。PDFはLibreOfficeで出力した。デスクトップ版PowerPointでの実機確認や、新しいモデルのベンチマーク実行は行っていない。
