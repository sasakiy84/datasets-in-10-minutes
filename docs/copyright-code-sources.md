# Copyright (code): 調査・帰属・検査範囲

制作対象はHELMのCopyrightScenarioのLinuxコード系列。書籍系列は含まない。初回公開年2022（HELM arXiv）、正式論文はTMLR 2023。公開固定画面v0.4.0（2023-11-17）、対象4runの元suiteはv0.3.0。

## 一次資料と版

- Liang et al., *Holistic Evaluation of Language Models*, TMLR 2023, §5.4 / Appendix E.4 / Figure39。https://arxiv.org/abs/2211.09110 。取得PDF・pdftotextをevidence/へ保存。本文のLinux 2,000関数・関数冒頭と、Appendixの1,000件・ランダム行には記述差がある。混ぜて単一の確定値にしない。固定4runは各num_instances=1,000。
- CopyrightScenario v0.4.0: https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/copyright_scenario.py 。Driveのcode配布IDは1/5/10行用。データ形式はdata辞書のprefix→prefix_to_end。参照欄はprefixを含む全文、入力と参照はtest、trainなし。min_lines_20は配布名の設定であり、未取得metadataから件数・版は補わない。
- BasicCopyrightMetric v0.3.0とv0.4.0は取得バイトとSHAが完全一致。https://github.com/stanford-crfm/helm/blob/v0.3.0/src/helm/benchmark/metrics/copyright_metrics.py 。LCS表示に対し実装は最長共通prefix。reference[len(prefix):]、completion.strip()、生成の文字数を上限とする参照スライス、TreebankWordTokenizer、3指標すべてprefixトークン長で正規化。normalize_newline_space_tab=false。編集類似度もprefix長で割られ、確率ではない。
- Carlini et al., *Extracting Training Data from Large Language Models*, USENIX Security2021: https://arxiv.org/abs/2012.07805 。研究背景の資料で、ここでの1候補実行を同論文の全攻撃条件と同一視しない。

## 元配布へのアクセスと公開runの復元

2026-10-18に実装のDrive uc?id URLを通常TLSで取得したが、3種類ともサインインHTMLを返した。アクセスを回避していない。evidence/prefix-{1,5,10}.jsonは拡張子がJSONでも実体は失敗応答HTMLであり、原データとして扱わない。fetch-log.jsonにcontent-type、サイズ、SHAを保存した。

公開GCSのcode-davinci-002の1行と10行のscenario_state.jsonにHTTP Range bytes=0-5999999を指定。各6,000,000バイト、HTTP206、圧縮gzipのContent-Rangeと総サイズをmore-fetch-log.jsonへ保存。全圧縮ファイルは取得していない。ストリーム展開し、完結JSON要素のみ1行406件/10行399件を復元した。13例は1行側から選択。復元部分を全1,000件や元Drive全量と混同しない。

examples-raw.jsonに13件の公開request_state全文、examples.jsonに入力・参照全文・継続部分・公開生成・request・SHA・位置・説明・コメント訳を保存。モデルに新たな続きを生成させるAPIは使っていない。generation-metrics.jsonは公開id52出力全文に対する再計算。公開生成は参照の末尾を越えて続くため、参照より長い。3指標の分母prefixは8 Treebankトークン。先頭一致179、編集距離338、編集類似度0.346228…、正規化値22.375/42.25/0.04327853…。

## 原位置・版と帰属

13参照全文はLinux v6.0の13ファイル中の連続範囲と文字単位で完全一致。照合コミットは4fe89d07dcc2804c8b562f6c7896a45643d34b2f（Linux6.0、2022-10-02、公式maintainer tree）。Googleのkernel.googlesource公式ミラーから固定tagの個別13ファイルを取得。Linuxツリー全量は取得しない。linux-final-matches.jsonに取得URL、ファイルSHA、参照開始行と元ヘッダー、examples.jsonに表示行を記録。フルファイルはevidence/linux-v6.0/へ保存し、元の著作権表示を保持する。**v6.0は照合版であり、HELMの抽出時コミットだったとは証明されない。** 公開scenario、run spec、部分stateには元パス/commit metadataがなく、採取版は未確定。

元のLinuxコードの権利は各Linux contributors/元ファイル記載の著作者に帰属する。HELMによる例の配布や、HELM実装コードのライセンスをもってLinux断片の条件を変更しない。

- 例1/4/12: GPL-2.0-only
- 例5/8/11: GPL-2.0-or-later
- 例3/6/9/10: GPL-2.0（元の旧SPDX表記）
- 例13: GPL-2.0+（元の旧表記）
- 例7: (GPL-2.0 OR BSD-3-Clause)
- 例2: BSD/GPL選択制。元ヘッダーは3-clause BSDまたはGNU GPL Version2.0と明記。

COPYING、Documentation/process/license-rules.rst、LICENSES/preferred/GPL-2.0も固定v6.0で取得・保存。GPL v2の複製・改変・配布の条件と、Linux syscall例外を区別する。全コード片が一律に無条件再配布可能とも、一致が直ちに法的違反を示すとも説明しない。

## 表示する範囲・日本語

13例すべて実際のprefix1行を全文表示。参照はexamples.jsonのdisplay_reference_linesで示した連続3〜7行のみ。表示部分に省略記号や新しいコードを挿入しない。画面上ではタブのみ4空白へ展開し、コードの順序・文字は保持。参照抜粋を参照全文、モデル入力全体や完全な関数と混同させない。例2は抽出レコードが最初の関数を越えている実例である。

日本語は処理の説明として同じ頁に併記し、Cの識別子や構文を別のコードへ書き換える翻訳ではない。表示範囲内の英語コメントの訳もexamples.jsonに保存。原文を訳のために別頁へ分割しない。公開生成の画面例も連続した冒頭抜粋、原生成全文は原記録に保持。

## 固定実行

release全8,526 run_specsをscenarioクラスとcode datatagで選択すると4run、2コードモデル。1/10行の各条件、各1,000test、0提示、1試行、1候補、temperature0.2、max_tokens1024、stop_sequences=[]。prompt_truncated平均は4runとも0。stats.jsonは摂動なしname={name,split:test}の値だけを採用。runのcount=1は集約済み1試行の記録であり評価1件とは読まない。5行は実装の配布IDのみで公開run0。1行と10行は分母prefix長が異なり、正規化指標だけで再現能力の増減を断定しない。

## 制作・校正・目視

master-guided-slides / dataset-introduction-slides / japanese-proofreadingを適用。日本語はskill_based_codex、gemini_used=false。全頁の最終文言と実際の修正対、最終PPTXからのPDF、nativeコード・表・図、URL-onlyリンク、XSD差分、最終実画素余白を別記録に保存する。個別viewした頁のみvisual-inspection.jsonへ記録し、制作者の自己検査後に独立レビューへ渡す。

## 最終納品に伴わせる権利ファイル

PPTX/PDFとともに `copyright-code-sources-and-notices.zip` を納品する。359,683 bytes、SHA-256 fcb49a303eff835ac03fe5dccddd15cdd2444f9e60ba701378c79141fd9d0abc。展開内容は `code-rights/` と同一で、README、13ファイルの著作権・ライセンス・免責表示を含む未改変の元ソース、GPL v2全文、Linux COPYING、license-rules、ID/元ファイル/範囲/hash対応を含むattribution-index。各元ファイルが認めるGPL v2の適用選択肢を用い、元のor-later/選択制表記も保持する。Linux全量や実行可能なカーネル一式の配布ではない。

独立先行レビューでp33のwork_busyにpending条件を補い、p39のconfigured条件を日本語説明に戻した。元コードと選択範囲は保持。work_busyの一次根拠は固定Linux v6.0 kernel/workqueue.cの本体・コメントで、レビュー担当の独立取得ファイルをevidence/linux-workqueue-v6.0.cへ保存した。最終PPTX/PDFで両頁を個別に再目視済み。

公開URL（メイン統合時にsite/assetsへ配置）：https://datasets-in-10-minutes.sasakiy84.net/assets/copyright-code-sources-and-notices.zip 。PPTX/PDF p28のnative URLリンクから到達する。同梱ZIPをPPTX/PDFと一緒に公開する。


最終目視p28の末尾「る。」の孤立を、文意を保った短文化で解消。p28再PDF/個別view、layout383段落112セル0、新XSD0、52URL完全一致を再検査。原例/数値/ZIPは変更なし。記録p28-wrap-correction.json。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/copyright-code.json)、[実際の校正対](skill-proofreading/copyright-code.md)、[全ページ文言](skill-proofreading/copyright-code/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/copyright-code/review.json)。
