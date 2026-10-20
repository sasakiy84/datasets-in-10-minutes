# GDPval — 一次資料と取得記録

2026-10-20確認。通常HTTPSは継承proxy/CAを使用し、TLS検証を維持。Gemini・外部生成APIは使用していない。

- OpenAI (2025-09-25), Measuring the performance of our models on real-world tasks. https://openai.com/index/gdpval/
- Patwardhan, T. et al. (2025), GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks. OpenAI / arXiv:2510.04374. https://arxiv.org/abs/2510.04374 （公式記事リンクのPDF: https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf ）
- OpenAI, Dataset for GDPval. https://huggingface.co/datasets/openai/gdpval
- Artificial Analysis, GDPval-AA v2.1 Leaderboard. https://artificialanalysis.ai/evaluations/gdpval-aa
- Artificial Analysis, Intelligence Benchmarking | Artificial Analysis. https://artificialanalysis.ai/methodology/intelligence-benchmarking
- Anthropic (2026), Introducing Claude Fable 5.1 and Claude Mythos 5.1. https://www.anthropic.com/claude-fable-and-mythos-5-1

## 配布版と原票

HF pin: 11e7900cdcac61bc4daf59e65feb238acda98fbf。公開goldは220レコード。train splitは配布上の名称。READMEにはライセンス欄がなく、LICENSEは404。CC等の再配布権を推定していない。スライドの依頼文・入力資料・参照成果物は出典を明示した研究紹介の引用であり、別生成の解答は作っていない。

原票全220: evidence/records.json。選択13: examples.json（提示順番号、rawID、入力/参照成果物パス、英語依頼全文、ルーブリック、職種・産業）。日本語は全文の逐語訳ではなく、入力・作業・提出形式を説明する要点として表示し、その表示テキストを各頁manifestへ保持する。

参照成果物の実配布を確認し、13例すべてで実際の専門家成果物の抜粋を使用した。公開gold全件では35件に成果物ファイルがない。ダウンロードした元ファイルとSHAはevidence/file-fetch.json。解析したPDF/DOCX/XLSX/コードの内容はevidence/file-extracts.json。

## 主要数値と評価条件

OpenAI初版47.6%等: paper p5 Figure5とp6脚注2。gold220、各課題3生成、各生成3専門家比較。wins+ties、人間参照成果物に対する比較。表の公開年はモデル公開年。ClaudeはUI、OpenAIはweb/code enabled。

AA v2の1853/1723/1824/1711: Anthropic記事の列順Fable5.1/Fable5/Opus5/GPT5.6Sol。Fable5.1 max1853はsystem card8.15.3もメイン担当が確認。AA v2.1とは尺度が異なる。

現v2.1: AA methodology主要節はCrowd-BT、DeepSeek V4.1 Flash(max)=1600。250turns、Stirrup、shell/web、3モデルから採点者を選び匿名比較。評価の旧記述が残る箇所はdata-auditへ記録。現時点上位例のモデル名・設定・値はAAページの可視本文に掲載されている1866/1857/1838を転記した。

専門家作業時間: paper Table3 gold median5h/mean9.49hを採用。構築: p2–4、職種選定・4年以上/平均14年・最低3/平均5reviews。公開snapshot分布はdata-audit.jsonに計算法・単位・全件集計を記録。出典の異なる計測値を原著の同条件値として扱っていない。

## 公式画面

official-site.pngは記事トップを実描画して取得。CSS/フォント/ヒーロー本文とURLを目視した。screenshot-log.jsonに200とasset failuresを保存。Cookie bannerはページ表示の一部。

## 最終化引継ぎ

原票全件・13例の入力と参照成果物・35ファイルSHA・論文・Web一次資料の独立読解はreview-gdpval/review.mdから継承。finish_gdpvalが新たに全13依頼の全文照合、native/PDF全文字比較、リンク、schema、表セルを最終候補で再実行。追加のネット取得・外部モデルAPIは行っていない。参照成果物の医学的妥当性、OpenStreetMap queryの実行結果、閲覧時間は新たに検証していない。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-gdpval.pptx)・[PDF](../slides/datasets-in-10-minutes-gdpval.pdf)。本編45頁、総129頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/gdpval.json)・[校正の修正対](skill-proofreading/gdpval.md)・[全ページ文言](skill-proofreading/gdpval/pages.jsonl)・[最終検証票](skill-proofreading/gdpval/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。
