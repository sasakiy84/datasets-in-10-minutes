# CLEVA：出典と検証記録

対象は2023年の **CLEVA: Chinese Language Models EVAluation Platform**。プラットフォームの資料であり、個別データセットの資料とは分ける。2026-10-18取得・制作。Geminiや外部生成APIは使用していない。

## 一次資料と固定範囲

- 正式刊行版：[Li, Zhao et al., EMNLP 2023 System Demonstrations, pp.186–217](https://aclanthology.org/2023.emnlp-demo.17/)。PDF 32頁、SHA-256 `49412cfeff8d70fd6cae8a77d6d63e4298a51481f05b5e0847e24f9561900fd8`。最初に試したdemo.9は別論文で、採用していない。
- [arXiv公開HTML](https://arxiv.org/html/2308.04813)の説明例を、section/block位置・表示文字列・SHAとともに保持。正式EMNLP PDFの中国語入力・選択肢・回答にも対応する。HTMLに含まれる英訳は日本語訳の代わりに転載せず、中国語から訳した。
- [公式リポジトリ](https://github.com/LaVi-Lab/CLEVA)、固定commit `9b11c68e6321db0aad5d3c571094451884180c78`。固定READMEとLICENSEを直接取得。2023年11月のHELM統合、四つの参照結果、2024–2025年のC²LEVA案内を確認した。
- [HELM v0.4.0 CLEVA実装](https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py)、[v1設定](https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/presentation/run_specs_cleva_v1.conf)。Converter、入力・選択肢・ラベル・テンプレートの変換と条件を確認した。
- [HELM Classic v0.4.0](https://crfm.stanford.edu/helm/classic/v0.4.0/)の固定公開run索引8,526件で、名前・scenario classを検索してCLEVAは0件。実装の存在と公開版の実行結果を分けた。公式READMEのHELM参照値は、この公開索引のrunを再集計した値とはしていない。

## 単位・条件・公表値

31課題＝実務11＋能力20、84収録データセット、約37万テスト事例、複数プロンプトや拡張後の約900万問い合わせ、33.98%の新規収集、1評価集合平均3.95テンプレートは正式論文の報告値。元の評価集合を取得して全件数を数えた値ではない。

固定設定を直接parseし、31課題・65の課題/下位課題組・253記述を数えた。65や253を84の内訳として扱わない。22既存中国語データセットという論文の数も、独立調査の出典系列行数と置き換えない。

公式READMEの4行×2値を照合：対話要約ROUGE-2 0.3045/0.3065、英中SacreBLEU 60.48/59.23、事実確認Exact Match 0.4595/0.4528、地域バイアスMicro F1 0.5656/0.5589。HELM/CLEVA間の乱数・文脈内提示例・ChatGPT版の差を明示した。指標の尺度が違う行を平均して順位を作っていない。

九つの評価軸は本文とAppendix Dを確認。効率の実測指標はD.7のQPS、多様性はD.8のinter/intra-distinct。D.9のPII_matchは、PIIが1件以上検出された生成文を持つ事例数/Nであり、全文字数に占めるPIIの割合ではない。2023年の評価はAzure PII検出を用いた。新たにAzure等へデータを送っていない。

70%は抽出した評価集合によるモデル対の順位付けに関する設計基準で、モデルの正答率ではない。G.4のSeparate/Joint、Chatbot/Completion、8モデル×4課題での提示例数比較を読み、4〜8例付近での頭打ち傾向と文章分類での低下を、31課題共通の最適値として扱わない。

## 13件の公開説明例

本編3件と追加10件は、CLEVA論文で公開された説明例。原評価集合のtest IDや、完全な評価時プロンプトを復元したものではない。`examples.json`に中国語の掲載範囲・参照・日本語訳・出所block・表示文字列SHAを保持した。省略記号を含むChID例は、その省略を保持している。

CLUEWSC、C3、Math23K、CCPM、ChID、OCNLI、分野知識、CHEFの事実確認、EPRSTMT、TNEWS、意見対象抽出、記号の再定義、帰納計算の例を用いた。採用元の不一致があるCSDSのニュース要約例・CrossWOZのテレビ雑談例は、本資料の13例に採らなかった。候補集合やラベル番号を別の版のものに差し替えていない。

13件の原文・設問・全選択肢・回答は、それぞれ1頁に保持。共参照の例は列幅と15.5ptの訳を実描画して同居を採用。C3は会話と設問/全選択肢を同じ頁の二列へまとめ、訳は別頁。長いChID説明例も原文を1頁に保ち、訳を別頁にした。選んだ原文を訳のために分割していない。参照回答は21pt・bold・テーマaccent1 `#B13731`。

## 現在のアクセスと権利

公式オンラインサイトは取得時503。公式のHTTP配布先はHTTPSへ308転送され、そのIPホスト名に証明書が一致せず取得できなかった。ドメイン経由も確認した。TLS検証を無効化せず、取得失敗を記録した。取得できないCLEVA v1原集合の件数・ID・内容は推測していない。

公式GitHubのREADME冒頭をChromiumで描画し、CSS34件・asset failure0、フォント・画像・バッジを読み込んだ画面を単独表示とスライドで確認した。最初のコード一覧画面にはcommit取得エラーがあり、採用せずREADMEへスクロールした。

CLEVAリポジトリの表示はCC BY-NC-ND 4.0。原データの条件と一律に同一視しない。ACL Anthologyは2016年以降のACL刊行物をCC BY 4.0と表示しており、正式論文の公開説明例を帰属を示して引用・翻訳した。日本語は本資料が添えた訳で、CLEVAの公式訳・公式評価ラベルではない。

## 日本語・実描画・native検査

日本語校正はローカルの日本語校正スキルによるCodexのページ単位の確認。`review_mode/method=skill_based_codex`、`gemini_used=false`。実際の修正対は`proofreading-changes.json`、最終の全頁文言は`page-review.json`、組版の試行は`layout-trials.json`と`final-fit.json`に残す。

62頁・本編35頁。全62頁を個別にview_imageし、実際に変更したPNGをSHAで検出して再表示した。8 native表・1 native棒グラフ・1 nativeテンプレート枠、ノート0。全28引用枠の可視字形の上下余白6.67–7.33pt、テンプレート枠は上下8pt。対の参照回答を同じ高さへそろえた。layout 354段落/78表セル問題0、標準XSD新規エラー0（マスター既存11件を分離）、URL-only 53件のPDF文字中心・矩形が一致。独立レビューは別担当へ引き継ぎ、承認後に最終状態を同期する。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/cleva.json)、[実際の校正対](skill-proofreading/cleva.md)、[全ページ文言](skill-proofreading/cleva/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/cleva/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/cleva/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
