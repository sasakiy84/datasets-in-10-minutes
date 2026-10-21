# DRACO 調査・制作記録

確認日: 2026-10-21。Gemini、モデルAPI、APIキーの読み取りは実施していない。公開HTTP取得には既存proxyとCAを保持した。

## 一次資料

1. Joey Zhong, Hao Zhang, Clare Southern, Jeremy Yang, Thomas Wang, Kate Jung, Shu Zhang, Denis Yarats, Johnny Ho, Jerry Ma (2026). *DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity*. arXiv:2602.11685v1, 2026-02-12. https://arxiv.org/abs/2602.11685
   - `raw/paper.html`, `raw/paper.txt`。最新HTML endpointも同内容だった。
   - §3: 2025年9～10月の高難度依頼1,000件→100課題。否定的反応/低評価を難度の代理に使用。PIIを除去してから人が確認。
   - §4: 専門家26人、4軸、3,934基準、うち負415。飽和テスト90%超で差戻し約45%、最終確認で約10%差戻し。
   - Table 8: 初期normalized score 70.5/67.2/59.0/52.1/41.9/59.8/46.7。Table 9: pass rate 72.8/70.9/62.7/56.9/48.0/63.1/50.2。
   - 初期採点: Gemini 3 Pro、100課題、各5回の採点平均。これは既報値の引用であり今回APIは使用しない。
   - 論文はCC BY-NC-ND 4.0。論文の図や翻訳本文は再配布せず、事実を日本語で説明して表を独自作成する。
2. Perplexity AI (2026). *DRACO Benchmark*. https://huggingface.co/datasets/perplexity-ai/draco
   - HF APIメタデータ、tree、README、test.jsonl、LICENSEを公開URLからHTTP200で取得。
   - `private=false`, `gated=false`, `disabled=false`。申請や認証を経ず取得できる公開データ。
   - revision `ce076749809027649ebd331bcb70f42bf720d387`、lastModified 2026-02-20。
   - `test.jsonl`100行を解析し、100独立UUID、10領域、3,934基準・負415を確認。
   - データの`answer`はJSONに符号化されたrubricであり、模範回答ではない。
   - MIT、Copyright 2026 Perplexity AI, Inc.。原文LICENSEを`LICENSE-DRACO.txt`へ複写。設問と基準の再掲・翻訳はこの公開配布の許諾に基づく。
   - 配布ページ画面は旧候補で使用したが、最終版では下記の公式紹介記事へ差し替えた。旧取得記録は`site-screenshot-log.json`に保持する。
3. Anthropic (2026-09-01). *System Card: Claude Fable 5.1 & Claude Mythos 5.1*.
   - 既取得公開PDF: `/workspace/artifacts/frontier-benchmarks-2026-10/fable-5-1-system-card.pdf`。親タスクの取得記録を継承。本文抽出 `/tmp/fable-card.txt`も使用。
   - 公開PDF URL: https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf
   - 公式紹介URL: https://www.anthropic.com/claude-fable-and-mythos-5-1
   - 今回は紹介URL/PDF URLともHTTP403。認証や制限の回避はせず、親が以前公開取得したPDFを根拠として使用。403理由はHTTPレスポンス以上は未特定。
   - §8.12.2 p178–179を通読。Web search/fetch、programmatic tool calling、code execution、1M token limit。Opus 4.6を採点者として5回平均、提出報告ファイルだけを採点する設定。
   - p179図を144dpi相当で描画し作者が確認。Fable 5.1のnormalized scoreはlow84.6、med85.3、high85.4、xhigh87.1、max87.7%。図の予算は980k-token。主にlow/med/maxを独自表へ転記。費用の読み取り/推定はしない。
   - 図自体をスライドへ転載せず、事実の数値を独自の編集可能表で示す。

## 実例の選定

原本の配布順index: 本編2,16,0。追加8,38,35,53,5,3,43,77,83,9。13件すべて異なるUUIDで、全10領域を覆う。

各実例の依頼文は全文を掲載。原文を1ページに保つことを優先し、日本語訳が収まらなければ別ページに配置する。各課題の採点基準2件を原文・重み・日本語訳で示す。全基準や報告回答を掲載したとは表示しない。別のCNC減点例では負の実基準`accepts-impossible-hours` −15を示す。

`examples.json`に原文、全文訳、UUID、rubric_id、原本の行、採用基準2件、全rubricを保存。独立担当は別途公開HFを取得して、13原文・rubric・UUIDと26採用基準の一致を確認した。日本語の指摘は`proofreading.json`に記録し反映する。

## 制作条件

日本語、B4～M1相当、fast skim本編予定600秒。著者sasakiy84、所属なし、日付2026-10-21。共通SlideMaster.pptxを使用し、編集可能PPTXからLibreOfficeでPDFを出力。ノートは付けない。予定時間は実測閲覧時間ではない。

repo/Git・共有スクリプトは変更しない。raw本文、HTTP取得物は`raw/`に分離。実行スクリプトは専用ディレクトリ内へ複写した。

最終候補: 本編37頁、全91頁、予定600秒。PPTX SHA256 `00608668983c09fea9703c0c093c22f889cfeba95718ae376055e2922947dbd3` / PDF SHA256 `bbe6a534146fce4969e510a20bd79a2d014c780770b439ec952792394ac41205`。全頁文字・ページ境界・URL範囲・表・出典間隔の自動検査で指摘0。13例の原文全文と各PDF表示部分を空白正規化で照合した。作者は17要所を拡大・全頁一覧を確認。独立全頁目視はhandoff記載の担当が最終確認中。

最終参照文献の修正: p90第2文献を22pt、p91第2文献を14pt下へ移動。全91頁rawpixel比較で変化は90/91のみ。両頁を作者が再度拡大して確認し、全頁の文字欠落・ページ外・URL・表・出典間隔検査は指摘0。

## 公式画面の最終選択

Perplexity Research (2026-02-04), *Evaluating Deep Research Performance in the Wild with the DRACO Benchmark*. https://www.perplexity.ai/hub/blog/evaluating-deep-research-performance-in-the-wild-with-the-draco-benchmark

2026-10-21の再試行で、default版とen-GB版の両URLがHTTP200。HTMLはraw/official-blog-1.html、raw/official-blog-2.htmlへ保存。公式紹介記事を配布データカードより優先する方針に従い、p2を記事のhero/冒頭へ差し替えた。Chromiumの1440×1100画面の上部650pxを標準clipで撮影し、CSS適用・主要資源・タイトル・公開日・著者表示を作者が目視確認。stylesheet2、資源取得例外0。本文やCSSの改変、TLS検証の無効化は行っていない。最新の画面選定は取得成功した公式紹介記事であり、Hugging Faceへのfallbackではない。取得記録はofficial-blog-access.json、撮影記録はofficial-blog-screenshot-log.json。

公式記事差替後の最終pairは上記SHAに同期済。全91頁rawpixel比較の変更はp2のみ（blog-pixelbridge.json）。13件の実例を含む残り90頁は不変。最終PDFのp2を作者が拡大確認し、全頁文字欠落・ページ外・URL範囲・表・出典間隔は指摘0。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-draco.pptx)・[PDF](../slides/datasets-in-10-minutes-draco.pdf)。本編37頁、総91頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/draco.json)・[校正の修正対](skill-proofreading/draco.md)・[全ページ文言](skill-proofreading/draco/pages.jsonl)・[最終検証票](skill-proofreading/draco/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-DRACO.txt](licenses/draco/LICENSE-DRACO.txt)。
