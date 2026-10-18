# LegalBench 調査・制作記録

日本語、著者sasakiy84、所属なし。制作日2026-10-18 JST。本編36ページは黙読・流し読み約10分の予定で、閲覧時間は未実測。全84ページ、編集可能なnative PPTXと最終PPTXから出力したPDF。ノートなし。

## 一次資料・固定版

- Guha et al. (2023), *LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models*. arXiv:2308.11462v1（2023-08-20）。https://arxiv.org/abs/2308.11462 。取得paper.pdfとpaper-v1.pdfは同一内容。六つの推論形式、36データ源、40寄稿者、20モデル、0〜8提示例、温度0、分類/抽出/複数回答/人手採点、初期成績を照合した。
- 公式 https://hazyresearch.stanford.edu/legalbench/ 。ChromiumでCSS・フォントが反映されたトップ画面を取得しview_imageで確認。screenshot-log.jsonに記録。
- https://github.com/HazyResearch/legalbench 。固定改訂 `b46bf4ffae90524b2b72aaa30e7745fe9db64481`。tasks.py、evaluation.py、162課題のREADME、13課題の公開trainとbase_promptを取得。GET URL/bytes/SHAはevidence/*fetch-log.json。ファイル追加取得は固定SHAをURLへ指定した。
- https://huggingface.co/datasets/nguha/legalbench 。取得時HEAD `daec8237410aa23e3faf4bc41ad8b3a7e1696826`。API info/treeメタデータを保存。TSV一覧合計82,311,731 bytesは掲載sizeの合計であり、全test本文のダウンロード実測ではない。
- HELM Classic v0.4.0（2023-11-17）と同タグのLegalBench scenario。公開run_specsをクラス名・シナリオ名で絞り、LegalBench実行0件を確認。legal_supportの87実行は別データセットなので加算しない。現行コードも別取得し、五つの対応課題とHF固定revisionを確認した。

## 課題の単位と版差

TASKSには162の異なる識別子。コードの五つの群は17/5/12/118/10で重複なし、すべてのTASKSが一度ずつ所属する。法規範の適用を説明するapplication_promptは12課題に併設されており、これを追加12データセットとして数えない。六つの概念的推論形式と五つのデータ分類を区別した。

系列別にはCUAD38、MAUD34、Learned Hands16、ContractNLI14、Supply Chain Disclosure10、OPP-115 9、その他41で計162。系列名と個別課題名は違う単位。編集可能なAppendix一覧には162識別子を全件掲載した。

論文の推論群別件数には節間の不一致がある（争点16/17、解釈119等）。構成図の件数は固定コードの列挙を全件集計した。2023年の入力/出力形式35/7/112/8は論文の公表分類として年と出典を付け、現在のREADME Task type分類と同一の軸として再計数していない。

2026-03-29の公式CHANGELOGに、MAUD7課題の問いと文章の対応修正、OPP-115全9課題の短い注釈スパンから段落への変更が記載される。2024-06-30にはrule_qa/scalrの提示例用train削除とunfair_tosのラベル修正。2023年公表成績と修正後データの新成績を同条件として比較していない。GitHub修正の存在と、特定HF改訂への反映の有無は同一視しない。

## 13実例とプロンプト

本編3件・追加10件は異なる13課題の公開trainから1件ずつ。出所/課題名/train/indexを各頁に表示し、examples.jsonへ原レコード、全入力、参照ラベル、訳、元ファイルと原レコードのSHA、固定改訂URLを保存した。入力の原文は全文。ユーザー指定の原文優先を守り、原文を訳のために分割していない。長いsuccessor_liabilityだけEN/JP別頁、それ以外はレイアウト・文字サイズを調整して同居した。

表示範囲は原レコードの入力欄に課題の問いを添えたもの。ベースプロンプトに含まれる固定ルール・他の提示例を、すべてモデル入力の全文として載せているわけではない。最初の実例の前にこの範囲を説明し、各課題の完全なbase_promptも保存した。データレコードに含まれる原文の誤字・引用符・大文字等は保持した。原入力と問いの対応、文字欠落、ラベルの一致は原TSVと再照合した。train提示例の成績をtest得点として扱っていない。

選定課題のREADMEはdefinition_extractionがCC BY-SA 4.0、他12課題がCC BY 4.0。引用と日本語訳の帰属は各課題の元作者/LegalBench、同一ライセンスに従う。definition_extractionの訳部分にもCC BY-SA 4.0を適用する。全162課題の利用条件を一律CC BYに変更しない。162課題の個別出所・ライセンスをevidence/task-registry.jsonへ保存。

## 評価・モデルの根拠

2023年Table2の群別平均とTable3の適用課題の人手評価を再掲。GPT-3.5はtext-davinci-003、Claude-1はv1.3、GPT-4は2023年モデル。Flan-T5-XXLも異なる系列として掲載。OpenAIの取得は2023年5〜8月、Claudeは7月。分類/抽出は改行停止、rule_qaおよび適用課題の多くは150トークン、diversity_jurisdiction_6は300トークン。理由の評価は商用3モデルのみで、法律の訓練を受けた1人が採点。6種類のdiversity課題は各30例、他の適用課題は全例。

自動採点は課題別。分類では小文字化・句読点除去・前後空白除去後の一致とbalanced accuracy。definition_extractionは語幹化を加えた用語一致。successor_liabilityは4例外の選択集合に対するF1。本文生成の説明を分類ラベルのEMと混同しない。2023年の実験記録はHELM Classicの得点ではない。公開run0件なのでHELMモデル得点や試行平均は作っていない。

## 検査

master-guided-slides、dataset-introduction-slides、日本語校正（name:japanese-proofreading）を適用。Gemini/外部生成APIは使用せず、method/review_mode=skill_based_codex、gemini_used=false。各ページの最終文言・校正記録、実際に行った修正対、個別view_imageのページは別JSONに記録する。

最終PDFの実文字境界で引用枠の余白を調整し、可視画素の上下間隔を確認する。標準XSD、整数buSzPct、元マスター既存11エラーとの差、内部参照、図形ID、ZIP、native表、ノート0、URL-onlyリンクを確認。個別問題の元データ照合と全ページの文字欠落検査を行う。最終handoffには独立レビュー待ちを明示する。

最終検査完了：84頁の最終PNGを全頁個別にview_imageで確認し、全体overviewも確認。全577段落・89表セルの描画境界検査は問題0、PPTX段落とPDF文字の欠落0。原典13レコード一致、21pt太字えんじ正解26run、参考文献は各2件。引用26枠の実可視画素による上下余白は6.67〜7.33pt、表下注記は12.54pt。独立レビュー待ち。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/legalbench.json)、[実際の校正対](skill-proofreading/legalbench.md)、[全ページ文言](skill-proofreading/legalbench/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/legalbench/review.json)。
