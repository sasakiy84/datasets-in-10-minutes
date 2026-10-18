# LegalSupport：出典と検証記録

本編33頁・全63頁。米国判決文中の主張と二つの引用判例の説明を比べ、より強い根拠を選ぶデータセットとして紹介する。2022年のHELM初回公開論文に既に記載されている。2023年の論文掲載版・Classic固定実行と、公表年を分けた。

## 一次資料

- Percy Liang et al. (2022/2023), *Holistic Evaluation of Language Models*. [初回公開版](https://arxiv.org/abs/2211.09110v1)・[TMLR掲載版](https://arxiv.org/abs/2211.09110)。LegalSupportの構築と位置づけは本文とE.3.9、担当者は謝辞で確認。CAPの1965年より後の州・連邦判決、異なる引用導入句、候補が多いときの無作為二候補、ラベルの由来を照合した。
- Stanford CRFM, [LegalSupport公開ZIP](https://docs.google.com/uc?export=download&id=1PVoyddrCHChMxYrLhsI-zu7Xzs5S8N77)。3,044,429 byte、SHA-256 `7b6044736a552b788932e79c3a0a20000387c41182cd6620da3b49588c38eb5f`。train/dev/testとparamsを展開し、全20,034行を集計した。
- [HELM v0.3.0のシナリオ](https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/scenarios/legal_support_scenario.py)。contextと二つのparentheticalを入力に変換し、正解文字列と一致する参照すべてへcorrectタグを付ける。
- [HELM Classic v0.4.0：LegalSupport](https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/legal_support)。2023-11-17の固定版。元run suite v0.3.0の公開stats/run_specs/scenario_stateを使用した。
- [HELM Classic公式トップ](https://crfm.stanford.edu/helm/classic/latest/)を2026-10-18にブラウザで描画。CSS・画像・フォントが実際に読み込まれた画面を使用。これはLegalSupport固有の成績画面ではない。独立したデータセット公式サイトは確認できなかった。

## 実例と訳文

本編3例と追加10例はすべて配布testの実際のレコード。0始まりの行番号、case_id、元の引用導入句・識別子・引用文、未変更のcontext/選択肢、ラベル、原行SHA-256を保存した。13例は異なるcase_idと主張を持つ。短く対比が読める例を選んでおり、出現頻度を代表する無作為標本ではない。

選択した入力は主張と二つの選択肢を一枚に保持。6例は英日を同居させ、7例は原文と訳文を別頁にした。原文の句読点・綴りは配布状態を保持し、訳は意味に沿って自然な日本語にした。正解は配布の引用導入句によるラベルに従い、独自の法律判断で変更しない。原文に含まれない説明や訳を、入力本文へ混ぜない。

## 全件集計と公開実行

train13,862/dev3,125/test3,047。主張文字列の一意数は3,472/744/744、選択肢順を除いた入力組は5,983/1,245/1,218。case_idの分割間共通数は83/94/20だが、同じ主張と二選択肢の組の共通数は全組合せで0。case_idの共通だけから評価入力の混入や性能への因果を判断しない。

同一選択肢はtrain8/dev0/test1行あり、シナリオでは両方がcorrectタグになる。確認した公開評価1,000入力では該当0件だった。公開入力はdev511/test489で、原行へ全件対応させ主張・選択肢順・正解タグの完全一致を確認した。

選択した3モデルはmultiple_choice_joint、実提示3、入力切り詰め0、temperature0。OPT-175Bとtext-davinci-003は3試行・出力上限5トークン、Llama 2 70Bは1試行・1トークン。devとtestの正解率は別に表示した。davinciの3,000出力は出力記号をoutput_mappingで元の選択肢に対応させて再採点し、公開値と一致した。

OPTのseparate_original/separate_calibratedは各0例提示・1試行であり、jointの3例提示・3試行とは条件が異なる。方式だけの因果比較とはしていない。固定版公開結果を2026年の最新モデル順位として扱わない。

## 編集・描画・独立レビュー

Geminiを使用せず、日本語校正スキルをCodexが一頁ずつ適用し、実際の修正前後5対を保存した。別担当create_iceが原配布20,034行、公開1,000入力・3,000出力、13原例・訳、run条件、全63頁描画を独立に照合。指摘の`after 1965`を「1965年より後」に修正し、最終描画で再確認した。

全63頁の本文と全表を通読し個別画像で確認。10表はnative編集可能、引用26枠と正解26箇所を保持。正解は21pt以上・太字・テーマaccent1 `#B13731`。引用枠の実字形上下余白は6.67–7.33pt。参考文献は2件ずつ2頁。最終PPTX由来PDFで欠落、枠外、表セル、URL文字範囲だけのリンク、notesなしを監査。標準XSDは変更せず、マスター既存11件を分離し新規エラー0だった。

コードのApache 2.0と元の判例・加工データ全体の利用条件は区別する。取得ZIPに専用LICENSEは確認できなかった。データを全面的にApache/CC0等と記載していない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/legal-support.json)、[実際の校正対](skill-proofreading/legal-support.md)、[全ページ文言](skill-proofreading/legal-support/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/legal-support/review.json)。
