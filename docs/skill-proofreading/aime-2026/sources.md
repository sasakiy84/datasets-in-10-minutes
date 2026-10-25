# AIME 2026：資料と掲載範囲

2026-10-25参照。作成者 sasakiy84。日本語の文言はローカルの日本語校正スキルに従ってCodexが確認・修正した。Geminiや外部生成APIは利用していない。モデル評価は実行しておらず、公開資料の取得・数学の直接計算・静的な全列挙を行った。

## 問題の出自と配布元

- Mathematical Association of America, **Invitational Competitions**. https://maa.org/maa-invitational-competitions/ — AIMEの正式名称American Invitational Mathematics Examination、AMC10/12から進む招待制競技であることを確認した。この現行MAAページは2027年の新しい方式も説明しているため、そこにある新方式を2026年の構成の根拠にはしていない。
- MathArena, **AIME 2026**. https://huggingface.co/datasets/MathArena/aime_2026 — 問題と整数の参照回答30件、データ項目、ライセンスの一次配布。固定版d61f486805306e6e6b5913504c07763a99e1b112、全30件を取得。MAAが競技問題を作り、MathArenaが既存問題を抽出・整形して評価用に公開するという役割を区別した。配布のtrainという分割名を、学習用問題の構築や別のテスト集合の存在の意味には解釈していない。
- Jasper Dekoninck et al. (2026), **Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs**. https://arxiv.org/abs/2605.00674 — Abstract/introduction、最終回答の構築・採点、飽和、Appendix A.1–3など関連箇所を読んだ。全57ページの精読を主張しない。AIME I/II各15問、AoPSからの抽出とLaTeXへの変換・確認、標準4試行、SymPyパーサーと判定の照合の根拠。パーサーとの不一致1%未満は最終回答を採点する評価全体の報告であり、AIME2026単独の値ではない。HMMTに記されたOCRの手順をAIMEへ転用していない。
- Mislav Balunović et al. (2025), **MathArena: Evaluating LLMs on Uncontaminated Math Competitions**. https://arxiv.org/abs/2505.23281 — 第一著者・書誌、Abstractを確認。公開直後の競技問題による汚染対策という出発点の資料。2026年版の構成や現行スコアをこの2025年資料から推測していない。

## 現行の成績と評価設定

- **MathArena公式サイト**. https://matharena.ai/?comp=aime--aime_2026&view=model — 実CSSとフォントを読み込んだ公式画面を撮影し掲載。取得時の表はAIME2026を旧評価の区分に置く。現在の高得点と著者による飽和の説明を示す。
- 公式テーブル取得先 https://matharena.ai/competition_tables/aime--aime_2026 。GPT-5.5 (xhigh)100.00%、Gemini3.1ProPreview98.33%を掲載。いずれも実測行で、モデルが大会公開後に登場した印を持つ。推定行を混ぜていない。
- 公開トレースの試行選択肢だけを3モデル×30問で取得した。GPT-5.5とGeminiは各問Run1–4、Claude-Opus-4.8(max)は全問Run1–2だった。論文の標準手順を現行全モデルに無条件で適用せず、成績の掲載は同じ4試行の2モデルに限った。公開モデルの推論本文は転載しない。根拠はcurrent-trial-check.json。モデルや評価器を実行した記録ではない。
- SRI Lab, ETH Zurich, **MathArena**. https://github.com/eth-sri/matharena — README、競技設定、関連パーサー実装とライセンス。取得時のコミットe921f1aa8bd09394a1506886a5d8b032ff591655。READMEの一覧と現行UIの旧評価区分の更新差は、現行UIと2026年論文に基づいて扱った。

## 13例と数学の確認

本編は問題1・2・3。Appendixは4・6・7・8・16・19・20・22・29・30。固定データの問題番号がIDであり、異なる問題13件である。すべて原文全文、数式を表示用の編集可能な記号へ直した版、日本語全文、配布された整数の正解、作成した短い解説をexamples.jsonに保存した。原文を訳文のために分割せず、13例とも全文を1ページに載せた。短いものは訳文と同じページ、長いものは訳文を別ページにした。

作者は13件の原文・訳・正解・解説を読み、直接計算と有限全列挙で正解13件を検算した（check_math.py / math-check.json）。πの6回合成は置換720件、特殊演算は正の整数列2048件、7項組の合同条件は2187件などを列挙した。これはモデル評価ではない。ルート担当者による独立の数学確認は../root-aime-mathにあり、作者自身の検算と区別する。別担当による全ページ独立レビューは../review-aime-2026に記録される。

## 権利と配布

固定したデータカードはCC BY-NC-SA4.0を示す。取得した実際のライセンス本文をLICENSE-AIME-data-CC-BY-NC-SA-4.0.txtに置く。日本語訳・表示用の数式整形・解説はその改変として帰属情報をATTRIBUTION-AIME-2026.mdに記し、同じ条件で共有する。評価用コードのMIT Licenseは別物で、実際の本文をLICENSE-MathArena-code-MIT.txtに保持する。コードのMITを問題データの権利として扱っていない。

## 読み時間と監査の範囲

本編31ページは読み飛ばしを含む600秒の予定配分で、実測はしていない。全63ページを作者が個別画像で読んだ。最終変更のないページは、作者が実見したdraft1と最終版の生RGBの一致でつなぎ、変更ページは再度個別に読んだ。原文・訳・正解のネイティブテキスト、PDFへの反映、字形の枠内、表、URL、XMLの監査は別JSONに記録する。OOXMLスキーマでは、python-pptxの既知のbuSzPct数値字句109件を明示しており、厳密な例外なしのスキーマ適合とは主張しない。
