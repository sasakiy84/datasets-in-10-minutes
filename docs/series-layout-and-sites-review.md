# 2026-10-17 多言語事例・配置・公式画面の横断レビュー

## 対象と確認方法

全25資料、改訂後計1,717ページを俯瞰した。22資料の189ページを変更し、変更したページは最終PDFを1440×810で個別に拡大して確認した。同形式の実例ページも対象に含め、原文から訳・正解・解説への順序、背景内の余白、表の行内位置と注記の間隔を確認した。PDFはそれぞれの最終PPTXからLibreOfficeで出力した。

Global PIQAは52ページから64ページへ拡張（本編29ページ）。独立した13問題を12言語で示す。日本語・英語に偏っていた追加例を、スペイン語、フランス語、ドイツ語、ポルトガル語、インドネシア語、スワヒリ語、アラビア語、ヒンディー語、韓国語、中国語に変更した。原文・全選択肢と、対応する日本語訳・正解・文化語の説明を対のページへ配置。公式TSVの追加10レコードについて、ID、設問、全候補、labelの完全一致を確認した。出典とページ対応は[Global PIQAの調査記録](global-piqa-sources.md)を参照。袋のparallel問題は日英で選択肢の順序が違うため、日本語A・英語Dを保持している。

## 配置の変更箇所

ページ番号は改訂後。公式画面の差し替えも含む。

|資料|変更ページ|
|---|---|
|arc-agi-2|2|
|charxiv|2, 9, 11, 13, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52|
|facts-grounding|2, 7, 8, 9, 10, 11, 12, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50|
|fineweb|28, 41, 68, 69, 70, 71, 72, 73|
|global-piqa|2, 7, 8, 9, 10, 12, 13, 14, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 56|
|gpqa|52, 56, 71, 74|
|hle|2|
|mcp-atlas|2, 8, 10, 12, 38, 40, 42, 44, 46, 48, 50, 52, 54|
|mmmlu|8, 9, 10, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44|
|mmmu-pro|2|
|mrcr-v2|2, 9, 11, 14, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40|
|omnidocbench|2, 8, 12, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51|
|osworld-verified|2, 9, 11, 12, 14, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53|
|scicode|2, 8, 10, 12, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46|
|screenspot-pro|2|
|simpleqa-verified|2, 8, 9, 10, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43|
|squad|20|
|swe-bench-pro|2|
|swe-bench-verified|2, 8|
|tau2-bench|2|
|terminal-bench|2|
|ucf101|6|

OSWorld-Verified p.12は2列の数値表を適切な横幅へ縮め、数値と項目の対応を追いやすくした。p.41を含む13件の指示ページは、原文・日本語の説明・採点方法を文量に応じてまとめ、中央だけに空白が残る配置を解消した。

CharXiv、FACTS Grounding、GPQA、MCP Atlas、MMMLU、MRCR v2、OmniDocBench、SciCode、SimpleQA Verified、SWE-bench Verifiedの同形式ページも調整した。引用背景は描画した最終行まで覆い、上下余白を確保。SciCodeの追加10例とOmniDocBenchのHTML例は、コードを編集可能な文字のまま残し、背景を独立した図形にして上下10 pt、影なしとした。SQuAD p.20、UCF101 p.6は表セルの上下余白を修正。FineWeb p.28・41の短いセル改行、p.68–73の表と注記の間隔、GPQA p.56の表と正解の間隔も修正した。

## 公式画面

全25資料の冒頭画面を再確認。以前の接続失敗時に配布画面や論文へ代替していた資料も再試行し、17資料で実ブラウザによる公式画面へ更新した。CSS・フォント・主要な本文が表示されたスクリーンショットを用いた。今回の取得日は2026-10-17。画面上のランキングは撮影時点の表示で、既存のモデル評価表を更新したものではない。

|資料|採用画面|URL|
|---|---|---|
|mmmu-pro|公式サイト|https://mmmu-benchmark.github.io/|
|osworld-verified|公式サイト|https://osworld-v1.xlang.ai/|
|hle|公式サイト|https://lastexam.ai/|
|terminal-bench|公式サイト|https://www.tbench.ai/?version=2.0|
|screenspot-pro|公式サイト|https://gui-agent.github.io/grounding-leaderboard/|
|arc-agi-2|公式サイト|https://arcprize.org/arc-agi/2|
|scicode|公式サイト|https://scicode-bench.github.io/|
|charxiv|公式サイト|https://charxiv.github.io/|
|global-piqa|公式リポジトリ|https://github.com/mrlbenchmarks/global-piqa#readme|
|omnidocbench|公式リポジトリ|https://github.com/opendatalab/OmniDocBench#readme|
|facts-grounding|公式サイト|https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/|
|swe-bench-verified|公式サイト|https://www.swebench.com/|
|swe-bench-pro|公式サイト|https://labs.scale.com/papers/swe-bench-pro|
|mcp-atlas|公式サイト|https://labs.scale.com/papers/mcp-atlas|
|tau2-bench|公式サイト|https://taubench.com/|
|simpleqa-verified|公式サイト|https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified|
|mrcr-v2|公式リポジトリ|https://github.com/google-deepmind/eval_hub/tree/master/eval_hub/mrcr_v2#readme|

- OSWorldは従来、接続できなかった公式ページの代わりに公式軌跡配布画面を使っていた。今回はOSWorld-Verifiedの告知がある公式v1サイトへ更新し、見出し・緑帯・URLも合わせた。
- Terminal-Benchは公式サイトで2.0を選択し、選択を保持するURLを掲載。MMMU-ProはProへのリンクも載るMMMUシリーズの公式トップ、τ²-benchは該当する公開履歴が見える公式シリーズサイトを掲載した。
- OmniDocBenchの独立サイト `https://opendatalab.com/omnidocbench` は再試行してもヘッダーのみで本文が描画されなかったため、公式GitHubのREADMEを採用した。Global PIQA・MRCR v2も開発元の公式READMEを掲載し、データファイル一覧を冒頭に使わない。
- ImageNet・COCO・SNLI・SQuADは既存の公式サイト画面を維持。
- GPQAは既存の著者公式リポジトリ、FineWebは著者による公式Hugging Face記事を維持。MMMLUはOpenAIの公式データカードを維持し、存在を確認できない独立サイトへ差し替えていない。
- UCF101は公式の `https://www.crcv.ucf.edu/data/UCF101.php` と `https://www.crcv.ucf.edu/research/data-sets/ucf101/` を再試行したが、上流の証明書検証エラーによる503で本文を取得できず、既存の原論文画面を維持した。

## 整合性と再発防止

全22改訂PPTXのZIP、内部参照、XML、スライド数とPDFページ数、ノートなしを確認。描画した文字のページ外逸脱、タイトルの折り返し、表セルからの文字逸脱、本文と出典・表と注記の接近は修正後の検査で検出なし。PDFの描画順による文字照合の未一致2件（MCP Atlas p.18の不等号、MMMU-Pro p.11の数式・箇条書き）は拡大画面で全内容の表示を確認した。既存マスター由来の `buSzPct` の整数字句表現だけは従来の既知項目で、今回その他のスキーマエラーは検出していない。

変更のないページはスライドXMLとPDFピクセルを旧版と比較した。Global PIQAの挿入に伴うページ番号更新は緑帯右上だけを除外。ほかの資料の未変更ページはピクセル一致。Global PIQAの33ページも一致し、p.24・61は同一XML・同一本文だが段落内の一部字形の描画差があったため、別途拡大して確認した。

共通SKILLに、公式サイトを優先して再試行すること、実際の文量に応じて関連要素をまとめること、多言語データで言語・文字・地域に広がりを持たせ日本語訳を添えることを明記した。調査・調整・検査用スクリプトは作業用ディレクトリだけに置き、スキルやリポジトリには追加していない。

公開ビルドは25資料、113,587,988 bytes（108.33 MiB）。全25表紙の読み込み、タイトルの大小文字・全角半角検索、種別・タスク・年の絞り込み、年順ソート、カードの1行省略、PDF/PPTXの取得、390 px幅での横はみ出しなしを実ブラウザで確認した。ブラウザエラーなし。22資料のPPTX/PDF計44ファイルは、確認済み作業ファイル・配布元・公開ビルドの3か所でSHA-256が一致した。

## 最終配布ファイル（SHA-256）

|資料|PPTX|PDF|
|---|---|---|
|arc-agi-2|`b435a6d6f348ea3c1c27f3e6a87667e6c91f615ee7dbb868a5cacb8b7f9f4d1b`|`6bf0a8f54a2b26d5e6a65f5ceb4c7ca06765796c934dc1df5f3b5823af5701d6`|
|charxiv|`35f8dcd5a5d295a7dd6f8aa0897d4583c3c4287bfc0feaef577d2529d2c156f2`|`2c34553c3e19aaa40c4cfe602ed41fa771ee65467493a464a8bf7efeb17f10d9`|
|facts-grounding|`9be06d38d2901a9a7a6462afd7c4788b766765ab03fe849bc4e69838b47b8e1d`|`a8284c803cd131015ddc0b008d5fe3459bbd582fac95eb6801dbcb01f6d2c94a`|
|fineweb|`ba257b75751e1f11d32501a9bc497b80371f95f36ee705c2df5995813a40f2ad`|`cfdc9dae51ecc80ad86aec8001c092e94a2ca1913985b934f0e32f0c99c4894b`|
|global-piqa|`8016cda8a9bb7b2c4381dccb2e576ffb1a283dbb86e5585382be5245eb7b1dac`|`d914e8ddddc6575b5a9db5825af93b2a4cd2f169138684fdeb92d34300d90c44`|
|gpqa|`d093e340ab95fc8d6126c2e073d8032ad8939c42bbe1f91ed03c1266b845e6d5`|`28aa023d4f88a23f1473fa5d08b75273515fb5c92cf9cf50c6c69f398c610e2d`|
|hle|`20cfba46764f9a4bdd10e1e504bbaeb8e5e36003a968fa7df66e67650f97141d`|`0895133a449703531fe7f1fff1851bdfb7785ab762aca4d5629c37ea2b967a22`|
|mcp-atlas|`f06450590a3bc04721e2e878f7fcc3fc32e1f94e6a827aa04cb079558bc0420a`|`693460a993be3a7ff4ac37583ce11816b8158d6a8b7d99a45e03048cbff31f8c`|
|mmmlu|`3cf8f3a26f5ea0e96effa751cde08eb774356697d055d417f5b9d4e6752db2f8`|`aaae89c58f2d8f6aa7fe59c7d43dbb75df6a2952be73262f83f07c4773bbd524`|
|mmmu-pro|`e0f6b1e4fd060b242389ca38864af5f852a4cd153a2c3c41449c35df2906d0d7`|`33083b617248132d623148a439bcba1a986cb83d0ee4fad93ba515e7ac9d75a9`|
|mrcr-v2|`72d3b6f785629b1356358addcb8fb20347d87aa88242abaf04d5f907a0cb4cb6`|`345775cd5b966adab9991452c60d19937c22d9b816faedf75eb795c717aadcf9`|
|omnidocbench|`61d0037a1430daf0e15f52c1d513f9c9afc74957d44adafc4d5e5581be9f9b0f`|`46a86e7ff1ca068745561c940c2bea3cc4d6f343da67f3f60ee31e25d88d3159`|
|osworld-verified|`b61afb0c24ea34c6c6b7ae6a028b33a59e5fadad2225084f62ccdbf423cc527c`|`ca7b87f1cbae18bae7c62f91ff6be4ee05d3f0839e1f56bb5d9792bd44b52cec`|
|scicode|`b68fba5863b8414b6cb207f656553e4c32d5d112b0d6b509c485a02099a0c803`|`761ff38e86d9b46703c31d95121e2e41b5e2725091c63d3dcab318fe11157bc5`|
|screenspot-pro|`b3469589fe4d26aeccbb30ed57b880d2ea07338d449292fe77ba8a0fd9f28caf`|`fd5aad715572c979ee379245d4cff4f5f4203999e29d857ece0172b03a31e144`|
|simpleqa-verified|`1a2a5e10bd6570860a7045e8ad3528c64747587a161dfd379cc966551b8b0a16`|`af4d3b93b3a14b94acdc9bef3d9b433f7a93da0fb05e6ee878cf1c9eb59ef8fa`|
|squad|`95d14eecebb322309a31aeaf4d2d6b5b35f4e3ba2b7319c2c2a3b6f2c697494d`|`b5c199b30887f7c9f10eb726dd3fbc008e67bbb20bfd6b0c4423122446b7d904`|
|swe-bench-pro|`9e533b4eb13f81f97bfd665c507fd9df3be08e68779ab0171c0518ccf43e448f`|`0c2f0dedec9a91019a1f8e24e77c05718ee037edfe941c4395a298e5b20fb28e`|
|swe-bench-verified|`e86d27f7c5606d9c9c095ca1aa018bbd090cf3a3cec263d4839ce2394fd12be9`|`452ae134872925617f597b4023b7c8aeb6f42862c35e9415b3f1cd1217562f90`|
|tau2-bench|`fa43aa14084a75b36aa3710b0271eaa422a6cfdf4314584d93368fa648fa8e86`|`842746c87e9852d540c008c665e3dba73efd4faefd90e1df65ca221476360528`|
|terminal-bench|`f2996dc0bfc8d0d90b2c8d25100269bc131cbce576b776fcaf254b17d950ff1b`|`5bd5fb0bd23ea311000490d26c2742a59a746ac8a0868dc85d7d6162d408fcd4`|
|ucf101|`9f6f9639f08d85e77709a0f3aeafce60db7b7deb34e909fa8fc6e8197257bd78`|`acc65394183185b49c185d1603540993b15da054ef5b5a0a450dd64fa006f5df`|
