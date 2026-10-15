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
|ImageNet|30|37|67|
|SNLI|29|31|60|
|SQuAD|32|66|98|
|UCF101|32|32|64|

各資料は約10分の本編と、追加例・統計・資料をまとめたAppendixからなる。予定時間であり、音読による測定は未実施。過去の試作や一時制作ファイルは環境内に残しているが、共有スキルの依存ファイルではない。

UCF101の全件集計にはTSN公開実装の配布リストを用い、別の公開実装のコピーと一致することを照合した。動画本体全体の長さは再集計しておらず、平均クリップ長などは原著の値を使う。公式サイトのトップ画面は環境の接続許可が未反映で取得できず、原著のarXiv公開ページの画面を掲載している。原著の公開ページと公式データ配布サイトは区別して表記する。

ImageNetのカテゴリ例はILSVRC 2012の1,000クラスと照合し、重複のない100クラス（10%）であることを確認した。残る900クラスは列挙しておらず、WordNet全体を網羅する一覧でもない。見取り図の10グループは説明のための区分で、WordNetの公式の上位分類ではない。

UCF101の行動例はすべて3コマの連続フレームとし、表示した時点を秒で示した。主例はI3Dの公開入力、追加例はUCF101動画の公開コピー（RichardMinsooGo-ML/5_TF2_UCF101_video_classification）を用いた。追加例のファイル名が配布分割リストに含まれることと、動画のタイムスタンプを照合した。圧縮ZIPの約7 GBという値はTensorFlow Datasetsのチェックサム記録の6,960,400,115 bytesに基づく。素材の取得元や集計元は、利用したページの出典から特定できる。末尾の参考文献は、読後の学習・研究に使う原著、公式教材・実装、評価の限界を調べる資料を選び、何を学べるかを添えた読書案内にしている。

箇条書きは、提供された発表資料のp.7をXMLで確認し、本文プレースホルダー（body、idx=1）と段落のネイティブなレベル・バレットを使う方式にそろえた。第一階層は●・左余白36 pt、第二階層は○・左余白72 pt、ぶら下げは各28 ptとし、本編とAppendixの目次は番号付きリストとした。本文に丸文字を打ち込んでいないことも確認した。バレットは親子とも約13.3 ptとし、LibreOfficeで無視される`buSzPts`を使わず、段落の本文サイズに対応した整数の`buSzPct`と`buFont="Noto Sans CJK JP"`を明示した。本文と番号付き目次のサイズは独立して設定する。これらの値と手順はSKILLとマスターだけで再現できる。

日本語はNoto Sans CJK JP、英数字はNoto SansをPPTXとPDFで共通に使用する。コードはLiberation Monoを使う。フォント本体は同梱・埋め込みしておらず、別端末でのPPTX編集には同じフォントの導入が必要になる。

PowerPointの修復版との比較で特定した、表セルの罫線／塗りの要素順、重複したbuNone、presentationのdefaultTextStyle／extLstの順序の修正は保持している。今回の4資料とマスターのPresentationML・DrawingML全372パーツは、ECMA-376第5版のTransitional XSDで構造を確認した。このXSDの`buSzPct`はパーセント文字列だけを受け付け、LibreOfficeで動作確認した整数形式を拒否するため、その値は公式Open XML SDKの`BulletSizePercentage`定義（整数25000〜400000）に照らして別途検証した。この表記差以外のXSDエラーは0件。スキーマは https://github.com/QtExcel/ecma-376-5th 、SDK定義は https://github.com/dotnet/Open-XML-SDK/blob/main/data/schemas/schemas_openxmlformats_org_drawingml_2006_main.json を用いた。

完全版の全289ページをLibreOfficeでPDFへ再描画し、全ページの目視、本文・表・出典の文字照合、タイトルの一行、出典との間隔を確認した。全355個のバレットはPDF上で13.209〜13.408 pt、Noto Sans CJK JPであることを確認した。本文・図表説明など102テキスト領域を、収まる範囲で拡大した。SQuADのp.9を含む23箇所の引用枠は、全行の描画位置から上下約7 ptの余白を確保し、質問・回答も再配置した。p.12の補足は、公式v1.1 train＋devの全20,963段落を各1回、前後空白除去後の文字数で集計し、500文字未満が2,874段落あるという具体的な記述に置き換えた。原著の収集条件と配布データの実測値の違いの原因は断定していない。ZIPの整合性、内部参照、図形ID、ネイティブなバレット・番号付きリストの構造、発表者ノートがないことも確認した。Linux環境のためMicrosoft PowerPointでの最終開封は未実施。
