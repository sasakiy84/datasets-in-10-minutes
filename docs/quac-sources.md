# QuAC：出典と制作記録

2026-10-18作成。本編35ページ、Appendix31ページ、全66ページ。本編は約10分の黙読・流し読みを想定し、閲覧時間は未実測。編集可能な共通マスターのPPTXと、最終PPTXから変換したPDF。著者sasakiy84、ノートなし。

## 一次資料とデータ

- Choi et al. (2018), [QuAC: Question Answering in Context](https://aclanthology.org/D18-1241/), EMNLP, pp.2174–2184。
- [公式サイト](https://quac.ai/)。CSS・画像・フォントが読み込まれた画面を確認し、トップ画面を掲載。
- [train_v0.2.json](https://s3.amazonaws.com/my89public/quac/train_v0.2.json)と[val_v0.2.json](https://s3.amazonaws.com/my89public/quac/val_v0.2.json)を全件取得・集計。
- [公式scorer.py](https://s3.amazonaws.com/my89public/quac/scorer.py)。回答不能の票整理、leave-one-out、低一致質問の除外、HEQを確認。
- [HELM固定版v0.4.0](https://crfm.stanford.edu/helm/classic/v0.4.0/#/groups/quac)、[公開シナリオ実装](https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/quac_scenario.py)、v0.3.0の公開statsとscenario_state。

元ファイルのURL・bytes・SHA-256、取得結果、全件集計、実例の原文・訳・ID・文書位置・質問位置・回答開始位置・全文・全参照回答をdata-audit.jsonに保存した。13件はすべて異なる記事・対話で、本編3件と追加10件。配布元の元レコード、回答範囲、連続抜粋の文字位置を再照合した。断片的な正解や原文の不自然な質問も、別の答えへ置換していない。

本文は連続抜粋、会話は直前の1往復と対象質問を掲載。抜粋を実際の全文入力と混同させず説明し、記事名・節名も添えた。質問のsemiconductorは文脈上会社を指しており、訳では設立年を尋ねる表現にした。John Hartson例の原文の通貨表記PS2.5 millionは、訳では250万ポンドとした。原文は変更していない。

## 集計・評価の区別

学習は11,567対話・83,568問、開発は1,000対話・7,354問。開発の参照回答は元回答を含む1〜5件（5件3,953問、4件2,086問、3件1,175問、2件132問、1件8問）。教師の回答不能は学習14,459問17.3%、開発1,486問20.2%。論文の学習20.2%とは差がある。論文の集合別件数の和と全体欄も異なるため、原因を推測せず補足した。非公開テスト1,002対話・7,353問は論文値。

公式QuACは参照回答を1件ずつ除いた最大F1の平均を使い、参照の回答不能票を整理する。人同士のF1が40未満の質問は主指標から除外し、HEQ-Q/Dも報告。HELMは重複除去した参照との最大token F1で、同じ除外や対話全体のHEQ評価は行わない。説明用のCannot answer出力の採点例は、実モデルの生成と混同させない。

HELMは開発の1,000対話から1問ずつ評価。学習・開発の処理順と乱数seed0を再現した入力・順序付き参照が、公開scenario_stateの摂動なし・第1試行1,000件と全件一致した。実装は対象の直前1往復を履歴から外す。省略の成績への因果影響は測っていない。

OPT-175B、text-davinci-003は3試行平均、Llama 2 70Bは1試行。最大5例・出力100トークン・temperature0。実提示例平均0.9443／3.4383／3.204、切り詰め率1.6%／0%／0%。F1と完全一致を公開statsから照合した。2023年11月の固定版であり2026年のモデル全体の順位ではない。公式サイトの2022年掲載モデルも日付を添えて別に紹介した。

## 日本語校正と検査

**Geminiは使用していない。** Codexが日本語校正スキルをページごとに適用し、実際の修正対、全ページ文言、校正・描画・構造記録を保存した。原文を1枚に保つことを優先し、列幅とフォントを調整して同居を検討。2例を併記し、11例は原文と訳を別ページにした。独立した教師の回答は21pt・太字・テーマのえんじ色。

全66ページを一覧で確認し、引用・訳・表・グラフ・公式画面・参考文献をすべて個別に拡大。変更ページは最終再描画後に確認した。引用枠はPDF字形の境界から下余白8ptを確保。文字欠落・枠はみ出し・出典との重なり0件。native表11・グラフ1、URLだけのリンク57件。標準XSDの新規エラー0。マスター由来11件と整数buSzPctの字句差を分離し、XSDは変更していない。PowerPointでの手動開封は未実施、LibreOffice変換と構造検査を実施。

## 利用条件・帰属

[公式サイト](https://quac.ai/)はデータを[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)で配布している。QuAC作成者および元記事のWikipedia contributorsに帰属する。資料では本文を連続抜粋し、日本語訳を加えた。抜粋・翻訳の該当部分にも同ライセンスを適用する。元記事のタイトル・節は各例と検証記録に保持している。著者名の推測や現時点のWikipedia本文への差し替えは行っていない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/quac.json)、[実際の校正対](skill-proofreading/quac.md)、[全ページ文言](skill-proofreading/quac/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/quac/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/quac/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
