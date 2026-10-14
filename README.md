# マスターに沿った日英スライド制作

共有スキルは次の2ファイルだけで構成する。

- `.agents/skills/master-guided-slides/SKILL.md`
- `.agents/skills/master-guided-slides/SlideMaster.pptx`

このフォルダを利用するプロジェクトの`.agents/skills/`へコピーし、材料と発表条件を与える。研究発表、成果物発表、紹介、授業などに対応し、参考スライド・配布Pythonスクリプト・別添設定ファイルを必要としない。読者の疑問から情報を設計し、一次資料の確認、構成、組版、描画・照合までをSKILL.mdで説明する。編集と描画は利用環境のPowerPoint、LibreOfficeなどを使う。

日本語の依頼例

> $master-guided-slides を使い、添付の研究の問い、方法、結果から学会発表のスライドを作って。発表時間は15分。PPTXとPDFを付けて。

English request

> Use $master-guided-slides and its master to present this project's goal, workflow, demonstration and evaluation in ten minutes. Deliver an editable PPTX and a PDF.

## datasets in 10 minutes

`slides/`には、sasakiy84によるデータセット紹介シリーズの完全版PPTXとPDFを保存する。本編だけの版や発表者ノートは含めない。ファイル名は`datasets-in-10-minutes-${dataset_name}.pptx`と`.pdf`。表紙左上は`datasets in 10 minutes (2026-10-15)`とし、所属欄を設けない。

|対象|本編|Appendix|合計|
|---|---:|---:|---:|
|ImageNet|29|35|64|
|SNLI|28|30|58|
|SQuAD|32|66|98|
|UCF101|30|30|60|

各資料は約10分の本編と、追加例・統計・資料をまとめたAppendixからなる。予定時間であり、音読による測定は未実施。過去の試作や一時制作ファイルは環境内に残しているが、共有スキルの依存ファイルではない。

UCF101の全件集計にはTSN公開実装の配布リストを用い、別の公開実装のコピーと一致することを照合した。動画本体全体の長さは再集計しておらず、平均クリップ長などは原著の値を使う。公式サイトのトップ画面は環境の接続許可が未反映で取得できず、原著のarXiv公開ページの画面を掲載している。原著の公開ページと公式データ配布サイトは区別して表記する。
