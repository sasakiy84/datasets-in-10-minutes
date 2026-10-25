# LiveBench：出典・実例・利用条件

## 対象

2024年に登場した更新型評価系列LiveBenchを紹介する。本編とAppendixの13例は、2024年6月24日・7月26日公開の1.0系列の公開問題である。原文・参照値・公開条件を実際に読み、日本語訳と解説を加えた。一部の問題は後の更新で除外されており、公開アーカイブの累積行数を現在の評価問題数とは扱わない。

2026年10月14日公開の2.0は、長いエージェント課題119件と短い単答問題352問を七区分で評価する。旧1.0の公開例と2.0の成績は混ぜず、課題の変化を明示した。2.0の新規原票は、確認した公式導線からは特定していない。未公開問題の推測や再構成は行っていない。

## 一次資料

- Colin White et al. (2025). **LiveBench: A Challenging, Contamination-Limited LLM Benchmark.** ICLR 2025. 正式会議版の題名を保持。旧arXivメタデータのContamination-Freeとは題名の版が異なる。構築、六分野・18課題、初期と更新後の規模、採点・集計、掲載時の比較を参照。読んだ範囲は関連する本編の節と掲載表で、全37頁読了とは主張しない。https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf
- **LiveBench 2.0** / **Methodology**（LiveBench / Abacus.AI、2026-10-25参照）。公開日・更新表示、七区分の件数、実行と集計の条件、現在の比較。公式Web画面はCSS・フォントを描画して撮影した。https://livebench.ai/ / https://livebench.ai/#/methodology
- **LiveBench official repository**, **Changelog**, **Datasheet for LiveBench**。課題ごとの採点コード、更新履歴、配布・保守・利用条件。https://github.com/LiveBench/LiveBench
- **livebench**公式Hugging Face配布。reasoning / math / language / data_analysis / instruction_following / codingの固定リビジョンから実例を選んだ。https://huggingface.co/livebench

## 実例と表示範囲

13例の原票、固定リビジョン、行、参照値、翻訳、表示範囲はexamples.jsonに保持する。6分野を含み、本編3例・Appendix10例は互いに重複しない。選定前に映画あらすじの候補を読んだが、元の長文の出典を固定できなかったため採用しなかった。NYT Connectionsの原文の例示にあるfounderという綴りは、原票どおり保持する。

原文は問題と全選択肢・表の値・出力形式を省かず、1頁で読める配置を優先した。属性推理は意味上の改行を保つため16pt、ほかの長い設問は17ptを基本にした。二つのCSV表は左右に置き、列名と全行を保持する。TSV表は原票のタブを表示用の空白へ展開したことをラベルに明示する。コードの問題文と全公開例は1頁に集約し、共通の生成・出力形式の指示を別の対応頁に保持した。誤字訂正ではliteral $n$を変更せず、表の値を訳文に重複掲載しない場合や意味説明の訳は、その範囲をラベルで示した。

数学の参照ラベルCと、設問が要求する出力CCCCCは区別した。指示追従例には一意の参照文を創作せず、指定形式と機械判定条件を説明した。コード例は唯一の正解実装とせず、公開サンプルの期待出力を示した。

## 採点・成績の照合

1.0の掲載時は六分野の課題平均を均等に集計した。更新後にはエージェント型コード修正も加わったため、六分野という説明を登場時に限定した。2.0は値のある区分の平均で、推理とデータ分析は下位課題群の均等平均、ほか五区分は課題平均である。公式CSVから4モデルの総合値を再計算し、表示した区分得点も照合した。

静的に読んだ公開コードには一部の数式問題のLLM補助判定があるが、実際の公式評価での使用率は調べていない。モデルによる解答生成、外部生成API、モデル評価・採点の実行はしていない。資料作成と静的検証・描画だけを行った。

## 利用条件と記録

データ配布のApache License 2.0は公式Datasheetを根拠とする。コードの複合LICENSEはFastChatのApacheとLiveCodeBenchのMITを併記するため、文字どおりの原本を別に保持した。日本語訳・説明の追加、元資料への帰属、未採用候補の扱いはATTRIBUTION-LiveBench.mdに記す。

Geminiは使用せず、ローカルの制作・日本語校正スキルを使った。実際の修正前後はproofreading.json、選定・出典・成績・範囲はdata-audit.jsonに記録した。作者の実見と、別担当から継承した確認を区別する。各600秒は本編の予定で、閲覧時間は未実測。Microsoft PowerPointでは確認していない。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-livebench.pptx)・[PDF](../slides/datasets-in-10-minutes-livebench.pdf)。本編32頁、総63頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/livebench.json)・[校正の修正対](skill-proofreading/livebench.md)・[全ページ文言](skill-proofreading/livebench/pages.jsonl)・[最終検証票](skill-proofreading/livebench/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-LiveBench-repository.txt](licenses/livebench/LICENSE-LiveBench-repository.txt)、[LICENSE-data-Apache-2.0.txt](licenses/livebench/LICENSE-data-Apache-2.0.txt)、[ATTRIBUTION-LiveBench.md](licenses/livebench/ATTRIBUTION-LiveBench.md)。
