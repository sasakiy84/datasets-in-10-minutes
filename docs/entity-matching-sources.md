# Entity Matching 調査・制作記録

2026-10-18制作、著者sasakiy84。日本語、本編31頁・全59頁、native PPTXと最終PPTX由来PDF。原文13実例（本編3、追加10）、正例6・負例7。公開データを保存実行と照合し、モデルを新たに実行していない。

## 一次資料と紹介範囲

- Mudgal, S., Li, H., Rekatsinas, T., Doan, A., Park, Y., Krishnan, G., Deep, R., Arcaute, E., & Raghavendra, V. (2018). **Deep Learning for Entity Matching: A Design Space Exploration**. SIGMOD 2018. DOI: https://doi.org/10.1145/3183713.3196926 。著者配布PDF https://pages.cs.wisc.edu/~anhai/papers1/deepmatcher-sigmod18.pdf （evidence/paper.pdf、paper.txt）。正式題名・著者順・所属・23課題・3:1:1分割・P/R/F1・学習方式を確認。Table3 Beer Hybrid72.7/Magellan78.8、Table5 Abt-Buy47.7/33.0、Table6 Dirty iTunes74.5/46.8をp26へ掲載。本文で図表番号は繰り返さず、原論文レベルfooterを使用。
- DeepMatcherの公式一覧 https://github.com/anhaidgroup/deepmatcher/blob/master/Datasets.md 。2026-10-18 APIのmaster=a89ffe6cd246f690afd2772e47eb071741160f16、commit date2021-06-13。固定版本文も取得して一致確認（evidence/Datasets-fixed.md）。公開はStructured7/Textual2/Dirty4の13設定。研究23課題のうち、企業由来Clothing/Electronics/Home/Tools等を含む非公開構成を公開13設定へ混ぜない。表のSizeはラベル付き候補ペア数で、表の行数・異なる実体数ではない。
- HELM v0.3.0 EntityMatchingScenario https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/entity_matching_scenario.py 、固定乱数状態、get_entity_matching_specを取得。v0.4.0/mainも比較用に保存。HELMは13設定を登録し、公開一覧と同じ7+2+4の構成。DBLP_GoogleScholarは配布名DBLP-Scholarに対応。
- HELM Classic公開固定版 https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/entity_matching （2023-11-17）。8,526 run_specsを絞るとEntityMatchingScenarioは201、Beer/Abt_Buy/Dirty_iTunes_Amazon各67モデル。最新版の2026年順位として扱わない。代表はOPT-175B、text-davinci-003、Llama2 70Bの9保存runで、実保存suiteはすべてv0.3.0。selected-runs.jsonとfetch-log.jsonに各完全run名・URLを保存。

## 収集・正解・Dirty・分割

BeerはUW–Madison CS784授業（2015年秋）の学生がBeerAdvocate/RateBeer HTMLを収集、表抽出、blocking、候補標本を手動match/non-match注釈。iTunesも同手順。Fodors/Abt等は候補生成後、既存golden matchesに含むペアを正例、それ以外を負例にする。公開資料から人数・一致率を推測しない。CompanyはWikipedia企業ページと企業homepageを対応付け、BM25上位の別homepageを負例とし、冒頭20tokenを除去する。

Dirtyはtitle以外の各属性値を50%で同じtupleのtitleへ移し元欄を空にする人工変換。iTunesのtitle相当はSong_Name。空欄にnanが現れても、情報が消えたとは限らず曲名欄に残ることがある。BeerのABV「-」はリテラル文字列で、pandasの欠測nanと区別。

候補ペアを3:1:1に分割。3対象の原CSVではtrain/valid/testにペア重複0だが、片側のtable IDは共有する。train/test共有はBeer A27/B36、Abt A674/B650、Dirty A24/B15。未知実体だけの評価とは呼ばない。配布説明にはtableA/Bが元サイト表そのものと直接対応しない場合があり、配布をコンパクトにするためleft/right tuple集合を格納するとある。表行数を独立実体数へ読み替えない。

## 配布と取得

原zipをHTTPSで取得した（元HELMコードURLはHTTP）。

- Beer: https://pages.cs.wisc.edu/~anhai/data1/deepmatcher_data/Structured/Beer/beer_exp_data.zip 、163456 bytes、SHA256 13bf56f9ef8c55b6ec4a3dedb0f621b0ac6e0ae353b2a39109081c66129b8da4。
- Abt-Buy: https://pages.cs.wisc.edu/~anhai/data1/deepmatcher_data/Textual/Abt-Buy/abt_buy_exp_data.zip 、147291 bytes、SHA256 cd806d925aca21e6ab942b239353a10ee88904c59d3d3e3da6a74e364e9200a1。
- Dirty iTunes-Amazon: https://pages.cs.wisc.edu/~anhai/data1/deepmatcher_data/Dirty/iTunes-Amazon/dirty_itunes_amazon_exp_data.zip 、1670825 bytes、SHA256 b62294f9a3c51d3779f749783f127d63992c0110381f5ec525b353c7242529b5。

各zipにtableA.csv/tableB.csv/train.csv/valid.csv/test.csv、独立ライセンスファイルなし。全5 CSVの件数・正負・属性・欠測・ID共有はstats.jsonへ全件集計した。配布13設定の規模は公式公開表から採った値で、Companyを含む他10設定を全量取得したとは書かない。

all13-download-status.jsonは13個のloader生成URLをHEADで確認。Fodors_Zagatsは実装fodors_zagats対配布fodors_zagat、DBLP_GoogleScholarは実装dblp_googlescholar対配布dblp_scholar、Dirty版も同じ相違で3件404。他10件200、CompanyはContent-Length91237002のみ確認し全量未取得。初回README.mdは404、正しいREADME.rstへ解決。エラー取得もfetch-logへ保存。

## HELMの実入力と再採点

公式serialize_rowをASTから変更せず実行（pandas2.2.3）。id列を除外して元列順で「name: value」を'. 'でつなぎ、Product A is ... Product B is ... Are A and B the same?へする。空欄を補完せずnan表示、元の文字化け・句読点も保持。read_blocked_pairsの結合と一致させ、3対象9run全9,800 requestのvalid/test入力と参照を原CSVペア/二表へ全件照合した。train提示49,000回も元train入力と正解へ照合（check_demos.py/demo-count-audit.json）。固定乱数状態のCodaLab URLは503であり、そのseedから全抽出を再実行したとの主張はしない。公開保存状態の入力・提示例を再現根拠とした。

- trainで正例数nを求め、正例n件/負例n件をsample。学習プールはBeer80/Abt1232/Dirty156。valid/testの比率は変更しない。
- 9実行すべて：最大提示5→実提示5、温度0、max_tokens設定/実request5、num_outputs/num_completions/実生成1、stop改行、入力切詰め0。OPT/davinciは3trial、Llama2は1trial。モデル別num_outputs差はこの9runにはない。
- max_eval_instances1000はvalid/test結合に適用。Beer全valid91/test91、Dirty全109/109。Abtは配布1916/1916に対し保存valid507/test493、testは正62/負431。3モデル・試行の対象一致は最終recordsで照合。
- 準完全一致quasi_exact_matchの全valid/test18セルを保存出力から再算出しstats.meanと一致。Yes/No以外0。exact/prefix系の公開値とも同値。testは各ペア0/1平均後、OPT/davinci3trialを等重み平均、Llama1trial。stats.countをペア数と誤読しない。
- test成績（Beer/Abt/Dirty%）：OPT34.065934/35.835024/42.201835、davinci90.476190/92.021636/96.636086、Llama92.307692/71.196755/55.963303。表示は小数第2位へ丸め。常時No基準は84.615385/87.423935/75.229358%。
- OPT trial1は3対象とも全Yes。これは公開保存出力の観測であり、温度0でも提示例が異なる。原因をモデル内部へ推定しない。試行ごとの正解率もp25へ掲載。
- 2018年F1は教師あり学習/調整testの正例precision/recallの調和平均。HELM生成正解率と同じランキングに並べない。現在モデルの再実行なし。

## 13実例・翻訳・native構造

examples.jsonは元testペアの論理row（0始まり）、tableA/B ID、3ファイルSHA、raw CSV dictionary、物理行範囲と原レコードbytesのSHA、HELM instance ID/run stateファイル、入力SHA、全文二レコード＋質問、Yes/Noと日本語訳を保存。全13は公開Llama2 testにも存在し、goldは6Yes/7No。Beer4/Abt5/Dirty4。型番・容量、価格差、度数差/欠測、Organic/Non-Organic、セット/単体、曲名欄への情報移動、カラオケ版を含む。楽曲の歌詞や書籍本文は含めない。

原文はHELMの属性列から作ったモデル入力全文。二レコードと質問の途中省略・原文分割なし。JPは同じ二レコード/質問を訳し、nan、数、型番、正解範囲を保つ。初回の20/18.5〜18.5/17.5ptの推定では同居困難だったが、独立レビューで15pt、原文4.9in/訳3.7in、左右margin9.36pt、行送り17.55ptの実描画を追加検査。Beer/Abt9例は同居成立のため採用し、Dirty4例は全文を別頁に維持した。manifest.layout_trialsと独立レビューcoexist-probeへ記録。最終はBeer/Abt9例の原文/訳15pt同居、Dirty4例は全文原文18.5pt＋JP16–17ptを別頁、独立正解17枠は21pt bold accent1 B13731。

10 native tables、引用・コードも編集可能テキスト、ノート0。公式画面はGitHub Datasets.mdの実Chromium描画、CSS/フォント読込を目視確認、架空の再構成画像ではない。初回repo READMEの古いbadgeが欠けたため、画像を要さない公式Datasets.mdへ替えて取得した。screenshot-log.jsonを保存。

## 校正・検証

master-guided-slides / dataset-introduction-slides / japanese-proofreadingのローカル技能に従う。method/review_mode=skill_based_codex、gemini_used=false。実際のbefore/after/reason/pageはproofreading-changes.json。自然な文を変更したと偽装せず、主述・数量対象・助詞・範囲を保つ。全頁に最終native文言・頁別校正記録を作る。原文の字形/JP訳/表/出典/URL/コード/画面/ページ番号を個別目視する。実行した確認のみrecordsへ記録する。

layout/text/package/links、各ページ検査、13例と全公開出力・提示例・表の再照合を記録。独立レビューはcreate_cnndm、先行13例訳確認create_twitter。完了前に合格とは書かない。共有repo/Git・他担当dirは編集しない。

再生成手順はprepare.py→translate.py→enrich.py→build.py→convert.py→fit_panels.py→convert.py→render.py→ink_panels.py→convert.py→render.py→audits→全変更頁目視。固定乱数状態取得失敗のため、公開runの同一抽出を生成器から再実行したとは扱わない。最終版はpanel-fitとfooter変更を反映したファイルでhashを保存する。

可視字形余白を最終PNGの暗色画素から別途測定し、27引用/コード枠を上下8pt目標へ補正した。最終ラスタの丸めを含む実測は上7.33–8.0pt、下8.0–8.67pt（visible-ink-audit.json / panel-ink-fit.json）。PDFのglyph bboxはフォントascenderを含むため別記録（panel-ink-audit.json）。55native URL-only runsと55PDFリンクを検査。2件は文字bboxの接触による隣行抽出があるが、native run範囲とPDF文字中心はURLのみで、リンクの実範囲違反は0。

独立レビューで実例13の見出しを「発売年」から「年の表記」へ修正。BのReleasedはnanで2004日付はSong_Name内にあるため、日付の元属性を見出しで断定しない。日本語訳の欄対応と原文は保持。

create_cnndm独立レビュー承認（未解決0）：原zip/9公開runのfreshGET hash、9800要求/49000提示/18集計/13例、全59頁＋変更18頁、native10表、27枠、17正解、全監査と最終hashを確認。記録は review-entity-matching/review.json。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/entity-matching.json)、[実際の校正対](skill-proofreading/entity-matching.md)、[全ページ文言](skill-proofreading/entity-matching/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/entity-matching/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/entity-matching/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
