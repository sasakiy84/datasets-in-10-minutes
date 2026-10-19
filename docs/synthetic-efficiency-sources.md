# Synthetic efficiency — 調査・出典・制約

対象はHELMのSyntheticEfficiencyScenario。HELM初稿2022年（arXiv:2211.09110v1、2022-11-16）を成立年とし、2023年の効率研究・Classic v0.4.0公開版と区別した。作成者sasakiy84。2026-10-18参照、native日本語66頁（本編31頁）。本編は約10分の説明を想定するが実演時間は未計測。

## 一次資料

- Liang et al. (2022), **Holistic Evaluation of Language Models**, arXiv:2211.09110v1. https://arxiv.org/abs/2211.09110v1 — `evidence/helm-paper-v1.pdf/txt`。謝辞にKeshav SanthanamによるSynthetic efficiencyの設計・実装への貢献を確認した。
- Deepak Narayanan, Keshav Santhanam, Peter Henderson, Rishi Bommasani, Tony Lee, Percy Liang (2023), **Cheaply Estimating Inference Efficiency Metrics for Autoregressive Transformer Models**, NeurIPS 2023. https://papers.nips.cc/paper_files/paper/2023/hash/d1a14493e5f84d6c6129414f0cd1a7c6-Abstract-Conference.html — `efficiency-paper.pdf/txt`, `efficiency-neurips.html`。公式PDFの題名・著者と、入力処理/自己回帰生成を分ける時間モデル、idealized/denoisedの議論を読んだ。全モデルの論文表を独自再現したという主張はしない。公式repo READMEの見出しは「Evaluating」だが、正式論文・BibTeXは「Estimating」。正式題名を採用。
- Stanford CRFM, HELM Classic **v0.4.0 (2023-11-17)**, https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/synthetic_efficiency — 公開run spec、stats、scenario_stateを取得。データsuiteは`v0.3.0`。表示版・suite・コードtagを混同しない。公式サイト画面はCSS/font読込後に実取得した画面 (`screenshot-log.json`)。
- HELM tag v0.3.0 `src/helm/benchmark/scenarios/synthetic_efficiency_scenario.py`、`metrics/basic_metrics.py`、`scripts/efficiency/generate_instances.py`、`generate_run_specs.py`。ソース/取得ログはevidence、URLはbuild-info.json。v0.4.0シナリオも別保存。
- https://github.com/stanford-crfm/helm-efficiency commit **c31b8fcc2b990b629173d7c898f1cdfae929c9a4**。README/tree/commit/profiling関連コードとJSONを取得した。Megatron-LM、A100/V100プロファイル、回帰・分析の構成を確認。全プロファイル再実行はしていない。repo LICENSE URLは404なので独自にライセンスを推定しない。

## 対象集合と生成・入力

固定run-specs全1365件=39モデル×35条件。各モデルが入力長1/256/512/1024/1536と出力上限1/2/4/8/16/32/64の全35組を持つことを`registry-audit.json`で検査。各runはnum_instances=10、num_train_trials=1、max_train_instances=0、max_eval_instances=1000。入力10件を1000件とは数えない。コード定数にはこれより広い入力長10種があるが、固定版の実際の5種と区別した。

生成コードは5作品を半角スペースで分割し先頭2048要素を飛ばす（厳密な単語数でもモデルtoken数でもない）。tokenizerごとに連続領域を取り、decode/再tokenizeで長さを調整する。`__main__`は長さごと30入力を生成する一方、固定runはid0〜id9の10入力を評価する。原配布CodaLabと追加id10は取得時503。したがって「生成済み入力は全部で10件だけ」とは主張しない。

今回の条件比較は3モデル×入力長1/256/1024×出力上限1/16/64=27stats。完全なscenario_stateは5条件50request：davinci-003の3入力長（出力上限16）とAI21 J1-Jumbo/OPT-175Bの256→16。全50で入力=prompt、学習例0、非truncated、温度0、max_tokens16、num_completions1、stop_sequences=[]、保存出力16tokenを確認。

公式GPT-2 encoderを取得し、固定efficiency repoのvocab/mergesで30davinci promptをtokenize→decode。各入力の指定token数と文字列roundtrip一致を確認。GPT2のMIT LICENSEを同梱した。regexは自身の`.deps`にのみ配置。AI21独自tokenizerはローカル再実行していない。AI21入力長256は公開statsのmin/max/meanで確認し、この限界を`input-and-metric-audit.json`へ明記した。

## 時間指標と検証

`prepare.py`は歴史的basic_metrics.pyの推定関数をASTで抽出して実行。全50のraw/idealized/denoised平均を公開値と照合（一致、1e-10以内）。27statsは各10入力。公開runの採用値はstats.jsonに保存。

- Rawはrequest_time。ただしbatch_request_timeとbatch_sizeがあればバッチ時間を優先。OPT 256→16はraw **12.289206266403198秒**、batch_size12。評価用10入力という数とは別の実行情報であり、残る2件の来歴を推測しない。
- オフラインdenoisedはraw/batch_sizeへ上書きされ、OPTは **1.0241005222002664秒**。OPT idealized **1.324秒**。
- AI21 256→16はraw **1.207363224029541**、denoised **0.996**、idealized **1.057秒**。
- davinci256→16 raw **2.018578314781189**、入力1 **1.6247077465057373**、入力1024 **1.6600937843322754秒**。このモデルは両係数JSONに登録なしなので推定値は欠測（—）、0ではない。
- 推定はP(n_input)+beta×(actual_output_tokens−1)+overhead。0出力では生成項なし。Pは最小の登録入力長k≥nから比例補間、超過時最大kで比例拡張。AI21/OPT係数をp54で具体的に再計算。
- davinci出力上限64の実生成平均59.4/55.7/55.9token。上限と実生成数を同一視しない。nativeグラフは保存された平均を示す。入力が長いほど速いという因果やモデル能力の順位は主張しない。
- 全50はcached=true。公開保存結果の読解であり新規API計測ではない。davinci/AI21に2022年11〜12月の日時が残る。今のサービス速度・価格のランキングとして使わない。

## 10実例と原文・訳

`examples.json`はdavinci-003の256→16条件の全10入力（本編3+Appendix7）を保持。13件へ長さ違いを水増ししない親指示に従った。生成コード30件とrun10件の差、原配布503をp58/59に明記。10入力は文字列一意で、5作品各2断片。統計的独立性は主張しない。

例順とHELM ID：1=id0 Alice、2=id2 Holmes、3=id4 Crime、4=id1 Pride、5=id3 Monte Cristo、6=id5 Alice、7=id6 Pride、8=id7 Holmes、9=id8 Monte Cristo、10=id9 Crime。

各例に元state相対パス/全ファイルSHA-256/ID/原record、入力UTF-8 SHA-256、256token検証、生成出力/16token/秒、原作品出所、独自日本語訳を保持。原ファイルの個別CodaLabバイト列は取得不能なので、SHAは公開stateファイルとJSON input文字列のものである。空referenceはスキーマ上のplaceholderで、正解ではない。出力は実際のモデル生成であり、原作の正しい続きを意味しない。生成出力表は空白・改行のみ整形し、その旨を見出しへ明記。文が途切れる出力もそのまま保持。

原入力はEN頁に全文、独自訳は次頁。原文を訳と同居するために分割していない。表示は段落を維持し改行・空白を整形（ラベルに明記）。原入力中の`0027m`、underscore、途中で切れたPorto-Ferra、開き引用符も保持した。訳も断片として示し、原作で未提示の続きや正解を補わない。訳の文学的調子、否定、話者、皮肉、人物の修飾、supercargo=船荷監督、honour/discretion=誠実/分別等を確認した。

Gutenberg eBook：Alice11 (Lewis Carroll)、Pride1342 (Jane Austen)、Holmes1661 (Arthur Conan Doyle)、Monte Cristo1184 (Alexandre Dumas、当該英語版の訳者は断定しない)、Crime2554 (Fyodor Dostoyevsky、Constance Garnett英訳)。全5作品の取得本文と公式生成器のURLを保存。8断片はNFKC/空白・case正規化後に全文一致、Pride2断片は冒頭/末尾各100文字が一致するが句読点・語順等の版差あり。キャッシュURLと元生成器の/files/N/N-0.txtを両方取得してもPrideの全文差は残る。HELM原入力を現在版へ書き換えない。電子版公開年と小説初版年を混同しない。

## 公開範囲・権利

HELMは素材をpublic domain sourcesと説明し、Gutenbergは作品ごとの公開条件を示す。国・版を問わず無条件に全世界で自由と断定しない。公開資料は出所付きの10短断片と新規日本語訳、表・グラフ。現在のGutenberg全文、論文PDF、公開全state/全raw、依存パッケージはローカル調査証跡であり、統合リポジトリへ一括再配布しない。PPTX/PDFのテキスト・図表はnative。公式サイト画面のみ出所付き画像。

## 校正・自己検査

`proofreading-changes.json`に実際に変更した日本語16対を記録。skill_based_codex、gemini_used=false。全66頁を個別拡大表示し、原文/訳・数字/単位・見出し/表/脚注・URLを確認、overviewも確認した。p41/45/47の訳見出し2行化を24ptへ調整し、3頁を個別再表示。引用枠は実PNG暗画素で上下余白を計測・調整し最終値を`visual-review.json`へ保存。`page-review.json`にはnative全文と頁ごとの実検査範囲、最終PNGhash。

`records.py`は66頁native→PDF全テキスト、20原文/訳頁、原input/原state SHA、39×35全組合せ、27stats各n10、notes0を検査。`audit_layout.py`/`shape_gaps.py`/`audit_package.py`/`check_links.py`で余白・接触・XML・native図表・URL範囲を確認。最終独立レビューはreview_decks担当。承認前の状態はhandoff.jsonへ正直に記録する。

## 独立レビュー修正（承認待ち）

生成出力にも独自JPを追加し、native訳表3頁（p15/49/51）を直後に挿入した。原16token出力全文/実測値は維持。output_jaをexamplesへ保存し、Dr. Watsonで切れる文・開き引用符・jo?の語尾断片などを補完しない訳へ校正。追加3頁と後続重要頁を個別再表示した。既存63頁は前版で個別表示済み、最終66頁への頁対応をoutput-translation-response.jsonに保存。15pt・不均等二列の同居実描画は制作時未試行で、独立レビューコピーで検証中。

p17の入力/出力ヘッダー、p22のRaw説明の単字折返しを意味境界の改行へ修正し、該当2頁を再目視した。全監査を再実行。

## 独立承認

review_decksが最終66頁を個別表示、50原request・27stats・10原入力/訳/出力/訳・9chart値を独立確認し、未解決0で承認。記録 `/workspace/artifacts/helm-parallel/review-synthetic-efficiency/review.json`, `review.md`, `handoff.json`。15pt不均等5.1/3.5in二列を全10入力で実描画・個別表示し、最短id5を含め日本語の溢れ/全文欠落が生じたため、原文/訳の分離を妥当と確認した。これは制作時の試行ではなく独立レビューの検証である。最終PPTX61099a3addd0f7b996b961de9bf8ce8b74c002af373167dc6e0783f8f52bd42d、PDF291500fcd01dc116a37e542ff7a9dd268eb023b4cde2818e0f4acb7ef61d1663。承認後成果物の変更なし。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/synthetic-efficiency.json)、[実際の校正対](skill-proofreading/synthetic-efficiency.md)、[全ページ文言](skill-proofreading/synthetic-efficiency/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/synthetic-efficiency/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/synthetic-efficiency/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
