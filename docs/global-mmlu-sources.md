# Global-MMLU：出典と制作記録

2026-10-21制作。日本語、学部4年〜修士1年向け、黙読・流し読みの予定600秒。本編とAppendixの枚数はbuild-info.json参照。閲覧時間は未実測。作成者sasakiy84、所属なし。共通SlideMaster.pptxに沿った編集可能PPTXと、そのPPTXから出力するPDFを制作する。

## 一次資料

- Shivalika Singh et al., **Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation**, arXiv:2412.03304 (2024)、v2 2025-02-19。https://arxiv.org/abs/2412.03304 。raw/arxiv.htmlとpaper.txtを保存。工程、200人による文化注釈、科目別50問、CS/CA、5-shot評価、モデル群平均の本文値を確認。
- **Global-MMLU Dataset Card**, Cohere Labs、Hugging Face（2026-10-21参照）。https://huggingface.co/datasets/CohereForAI/Global-MMLU 。HFの現在の表示組織はCohereLabs、旧CohereForAI URLは正規配布へリダイレクトする。revision 0e619dbeb34206cd48705a1a0ea7fb21cae09993。raw/README.md、hf.jsonを保存。
- **MMMLU Dataset Card**, OpenAI (2024)。https://huggingface.co/datasets/openai/MMMLU 。既存資料docs/mmmlu-sources.mdでも対象と出所を確認。Global-MMLUはMMMLUの10言語を取り込み、独自専門修正4言語、コミュニティ修正11言語、機械翻訳16言語、英語を組み合わせた別研究。元のMMLU問題を共有していることを本文で明記。
- Hendrycks et al., **Measuring Massive Multitask Language Understanding**, ICLR 2021。https://arxiv.org/abs/2009.03300 。57科目の元データMMLU。
- Anthropic, **Claude Fable 5.1 & Mythos 5.1 System Card** (2026)。https://www.anthropic.com/claude-fable-and-mythos-5-1 。親担当の取得済み/tmp/fable-card.txt §8.18.1を通読。GMMLU=Global MMLUの42言語平均でFable5.1=94.0、Fable5=93.6、Opus5=92.5、Sonnet5=89.0%。adaptive thinking/max effort、各1試行。MILUは別の11言語評価であり、直後の5試行平均をGMMLUへ転用しない。

## 規模と範囲

公式カードは42言語、test各14,042問（589,764レコード）、dev各285問（11,970レコード）。英・日・仏・西・スワヒリ・ヒンディー・ヨルバのtestを取得・読込、すべて14,042問。アラビア語testも取得したが掲載例に使用しない。原問題単位と翻訳レコード単位を区別する。

英語testの独立再集計は57科目。is_annotated=trueが2,850問、CS792、CA2058、未注釈11192。CSの定義は文化・地域・方言のいずれかの知識が必要という人手判断で、安全上の有害性のラベルではない。200人が参加し、各問を最低3人、半数以上の賛成を使って判定。英語につけた注釈を41翻訳言語へ引き継いでいる。全問を文化注釈済みとは扱わない。

6分野内訳はdata-audit.json、掲載表のCS/CAは独立レビューでも再計算済み。研究本文のSTEM CS30/950という記述と表の23/950に差があるため、配布実体と一致する表の23を採用。資源分類はpaper high18/mid11/low13とcard20/9/13が違うため、主題に不要な資源別内訳はスライドに使用しない。Global-MMLU Liteの初版は英語を含む15言語、CS200+CA200、計6,000レコード。現行3.0（2026年5月）は23言語・test9,200レコードであり、初版と現行版をAppendixの1頁で説明する。

## 実例と翻訳

examples.jsonに本編3問・Appendix10問、計13独立問題を保存。同じ原問題の異言語訳を追加問題として数えない。7言語を使用。各問に元ファイル・sample_id・言語・viewer行URL・全設問・全選択肢・配布正解・CS/CA、英語対照と本資料の日本語訳を記録する。原文は配布の全文で、改変しない。併記が狭い場合は原文全文1頁と日本語訳頁へ分ける。日本語原文例は公式配布日本語をそのまま示す。

独立レビューで発見した2点を修正した。例6のスペイン語Bは英語secretary of defenseとは異なりel Ministerio de Defensaなので、日本語を「国防省」にした。例12のヒンディー語D की अवहेलना करने は英語overrideとは異なるため、日本語を「無視する」にした。配布原文やラベルは変更しない。

## 取得・掲載条件

公式配布はgated:false、Apache-2.0。設問の引用・翻訳は、原データへのリンクと作者・配布元を各実例に対応させ、変更（日本語訳）が分かる表示にした。Apache2.0本文をLICENSE-Global-MMLU-Apache-2.0.txtへ保存。初期候補MILUは公式HFが自動gateかつ未認証401で、13独立実例を確保できず、申請や認証を行わず候補から外した。調査物は../alternatives/miluへ保存。

## 画面・制作・検証

公式プロジェクトサイト https://cohere.com/research/globalmmlu をCSS付きで撮影し、p2に掲載した。公式サイトのTry Global MMLU LiteはCohereLabs/Global-MMLU-Liteの現行配布へリンクする。画面はofficial-site.png、取得記録はscreenshot-log.json。以前のHF画面はbefore-project-lite-updateに保存した。

フォントはNoto Sans/Noto Sans CJK JP、ヒンディー語はNoto Sans Devanagari、コードはLiberation Mono。ヒンディー語原文は全ランのLatin/EA/CSをDevanagariに指定して描画を確認する。独立担当による原文/訳/事実と全頁の描画レビューを実施し、実施済範囲だけを最終handoffへ記録する。Gemini・外部モデルAPIは使用しない。

最終独立レビューの指摘により、グルと二本の剣、Arkansas toothpick、格率の意味を、それぞれの実例の正解直下に一文で補った。参考文献は1頁2件を保ち、項目間の実文字間隔を24.516pt／25.054ptへ調整した。表紙副題・Appendix扉・文献の計7文字枠も高さを補正した。修正前後の全55頁のrawpixel比較では、実例3頁と文献2頁以外の50頁が完全一致した。

公式サイト・Lite更新前の55頁の独立canonicalレビューはapproved、残件0。全辺のglyph輪郭監査で文字枠外・頁外0、構造・表・URL検査も合格した。URL4枠の最小補正では1080px描画で全55頁が一致し、独立144dpi比較ではp28・30だけにサブピクセル差があったため両頁を再目視して承認した。本文・表・原文などのnative文字は55頁すべて不変。

## 公式プロジェクトとLite現行版の追加確認

Cohere Labs, Global MMLU（2026-10-21参照） https://cohere.com/research/globalmmlu 。現行Liteカードは https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite 、revision36c2fd756f19ccf13a9a96c8e53ccecc02192b8b。版履歴は1.0（2024年12月）15言語、2.0（2025年12月）アルバニア語・ビルマ語・ウェールズ語を追加、3.0（2026年5月）チェコ語・ハンガリー語・オディア語・スロバキア語・タジク語を追加し、既存イタリア語を更新。現カードの23言語・各test400問・CS/CA各200問・全9,200レコードは、独立reviewer /root/review_global_mmlu が全23testを取得して再集計した。記録は../review-global-mmlu/lite-v3-source-audit.json。作者側の値は取得した公式API/cardのメタデータ観測であり、独立再集計と区別する。

公式サイトには23言語と6,000samplesの併記があるが、現行件数には配布カードと全件再集計が一致する9,200を用いた。原因は断定しない。論文のLite結果は初版15言語の評価であり、現3.0の評価結果として転用しない。スライドの変更は公式画面p2、Lite補足p51、最新Liteカードを2件目に加えた参考文献p55の3頁に限定する。

公式プロジェクト・Lite更新後のpairは独立source/deltaレビュー、全構造・表・URL・全辺glyph検査に合格し、canonical approved／残件0となった。独立144dpiの全55頁比較でも変更頁は2・51・55のみで、残り52頁が完全一致した。作者は変更3頁を拡大して再確認した。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-global-mmlu.pptx)・[PDF](../slides/datasets-in-10-minutes-global-mmlu.pdf)。本編33頁、総55頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/global-mmlu.json)・[校正の修正対](skill-proofreading/global-mmlu.md)・[全ページ文言](skill-proofreading/global-mmlu/pages.jsonl)・[最終検証票](skill-proofreading/global-mmlu/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-Global-MMLU-Apache-2.0.txt](licenses/global-mmlu/LICENSE-Global-MMLU-Apache-2.0.txt)、[ATTRIBUTION-Global-MMLU.md](licenses/global-mmlu/ATTRIBUTION-Global-MMLU.md)。
