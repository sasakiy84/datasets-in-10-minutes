# EUR-Lex-Sum：出典と検証記録

本編34頁・全66頁。2022年発表の24言語の法令要約データセットを紹介する。EU法令本文と人手の参照要約を組にし、同言語要約・言語間要約を扱う。Celex IDを共通に持つ文書と、言語別ペアの件数を区別した。本編約10分の読解を想定して設計しており、読了時間は未実測。

## 一次資料と固定版

- Dennis Aumiller, Ashish Chouhan, Michael Gertz (2022), *EUR-Lex-Sum: A Multi- and Cross-lingual Dataset for Long-form Summarization in the Legal Domain*. EMNLP, 7626–7639。[正式掲載版](https://aclanthology.org/2022.emnlp-main.519/)を取得。PDF SHA-256 `8d3c7a5eda347dcbaf0da016fbfa3243b14506ce5514af8dda645d17a46b1208`。収集・フィルタは§3、評価は§5、公表数値はTable 2–5とAppendix Bへ照合した。表番号は照合記録用で、スライド本文へ不要な出典番号を足していない。
- [公式GitHub](https://github.com/achouhan93/eur-lex-sum)、確認した先頭commit `ab44866958`（2024-02-27）。README、分析コード、保存済み統計、baselineコードを固定commitで取得。共同第一著者のAumiller/Chouhan、Gertzの所属と役割は正式論文・配布カードへ照合。
- [公式Hugging Face配布](https://huggingface.co/datasets/dennlinger/eur-lex-sum)、revision `33ecb2d630298e3f912d067aaaa71aaf4ee92404`。英語train/validation/testと、フランス・ドイツ・スペイン・イタリア・アイルランド・ギリシャ・マルタ語のtestを取得。取得したのは10 JSONLであり、全24言語・全分割を取得したと記載しない。ファイルごとのURL・byte数・SHA-256を保存。
- [HELM v0.4.0のLegalSummarizationScenario](https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/legal_summarization_scenario.py)。`EurLexSum`はHFの`english`設定を読み、`reference`→入力、`summary`→参照。空白整形・任意の先頭語数切り詰め・train長フィルタをコードで照合した。
- Classic v0.4.0公開run_specs全8,526件に、データ名とシナリオ引数を照合して該当0件。HELMの実行スコアを作らず、研究で公表された2022年のbaselineを明確に区別した。
- [EUR-Lex現行の利用条件](https://eur-lex.europa.eu/content/legal-notice/legal-notice.html)を取得して確認した。

## 公開画面

公式HF配布のトップ画面をChromiumで描画し、CSS4件・実際のフォントや画像・本文を確認した。取得時asset失敗0。Dataset Viewerが旧Pythonローダーのため無効である表示も、実際の公開状態の一部である。JSONLファイルは通常のURLから取得できた。最初に試したGitHubトップ画面はcommit情報の読み込み失敗があったため最終採用せず、取得結果を記録として残した。

## 実例と表示範囲

13例は8言語・13の異なるCelex IDの実在testレコード。本文と参照要約の連続した範囲を表示し、文字開始・終了位置、0始まりの行、原行hash、配布ファイルhash、全文の原レコード、訳文を保存。表示範囲を全文と呼ばず、各例に入力/要約の全文語数を明記した。本文は主として条文の一段落、参照は要約の目的を説明する段落を選んだ。例9の要約は三つの構成要素を含む連続した節を保持した。

原文の選択範囲を一枚で示すことを優先してから、幅と文字サイズを変えて日本語の同居を検討。原文だけでも全幅15.5ptで枠を超える例3/6/9は、入力と参照という意味単位で分けた。訳を併記するために原文を分割したものではない。成立する同居案と不成立の試行範囲をbuild-infoのlayout_trialsへ記録した。

生成課題の参照要約であり、唯一の正解として独自の正解ラベルを付けない。本文は法令の一部分、要約は複数の法令や他の節も含む全体を説明するため、短い抜粋だけが要約全体の根拠であるとはしない。元の空白、句読点、綴り、脚注記号も原文の一部として保持した。

## 件数・長さ・分布

2022年の24言語公表値を転記し、合計31,987ペアを再計算。共通375法令をvalidation187/test188へ分け、言語ごとのtrainは全ペアから375を除いて算出した。英語はtrain1129/validation187/test188で全1504件。取得した8言語testの全188 Celex IDと行順が一致し、英語の分割間ID共通は0。

現在の固定配布の長さはPythonの`len(str.split())`で計数し、母標準偏差・中央値・極値・対応IDを保存した。英語train本文平均12,882.96語、中央値4,818語、最大1,087,217語。参照要約平均783.05語・最大2,930語。本文の階級別文書数は183/394/279/140/92/41で、全1129件を含む。native棒グラフのキャッシュとも照合する。

公表Table 2/5は同一とは限らない処理・配布状態での分析であり、英語train本文平均12,206、要約799、test本文最大403,319、要約最大2,987。今回の固定配布と混ぜず、Appendixに両方を提示した。異なる原因を推測で版変更や計数方式と断定していない。現在の英語trainで本文より要約の空白区切り語数が多い組は1件。すべてが必ず短くなるという説明は避けた。

## 公表評価と実装条件

2022年の改良LexRankの言語別test ROUGE F1と、英語→スペイン語のLED/LexRank/参照翻訳条件を正式論文の表へ照合。188法令のtestを対象とし、stemmingなし。英語の人手参照を翻訳する比較条件は、法令だけから要約を生成する方式とは利用情報が異なる。

論文§5.1の目標段落数の記述はaverage圧縮率。一方、保存された`lexrank_baselines.py`の`compute_median_character_compression_ratio`は段落数比を`np.median`で集約して使う。スライド本文では「trainの段落圧縮率」とし、この差をここに記録した。埋め込みはparaphrase-multilingual-mpnet-base-v2、追加要約学習なし。論文の主張とコードの実装を一律の平均値と呼ばない。

言語間baselineは実際には英語の要約を作ってからOPUS-MTで翻訳する手順。論文にあるtranslate-then-summarizeという表現を、そのまま処理順として採用しない。保存コード`cross_lingual_baselines/lexrank_baseline.py`も英語出力を読み、500 subword単位で翻訳する。ただし現スクリプトにはvalidationをskipしtest index<177をskipする再開用の条件があり、そのまま188件を再実行したとはしていない。LEDはBillSum学習済み、入力約4096トークンの区間を生成して連結する2022年の実験で、現在のモデル順位ではない。公表得点を今回再実行したと記録しない。

## 配布条件の表記差

現在の公式READMEはデータCC BY 4.0、コードMIT。元のEUR-Lex現行条件もCC BY 4.0の対象を記載する。HFカード先頭メタデータはcc-by-4.0だが本文はCC BY-SA 4.0、固定旧ローダーはCC BY-NC-SA 4.0と記載が異なる。古い単一の表記を全配布へ断定的に当てはめず、各一次表記と取得版を記録した。`usedStorage`は履歴を含む指標のため、現在の配布容量として転記していない。

## 校正と検証

Geminiを使用せず、Codexが日本語校正スキルを一頁ずつ適用。実際の訳語・文言の修正前後を保存し、最終ページ番号へ対応させる。主担当による個別描画確認と、別担当create_msmarcoによる独立の原記録・数値・日本語・組版確認を分けて記録する。確認範囲・最終hash・未解決の有無はhandoffとreview記録を参照。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/eurlexsum.json)、[実際の校正対](skill-proofreading/eurlexsum.md)、[全ページ文言](skill-proofreading/eurlexsum/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/eurlexsum/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/eurlexsum/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
