# MS MARCO 調査・制作記録

## 範囲と主要な結論

日本語61ページ。本編33ページを黙読・流し読み約10分の予定で設計（実測した読了時間ではない）。MS MARCOの質問応答としての成立からpassage ranking v1への展開を説明し、HELM ClassicのregularとTRECを1資料にまとめた。著者sasakiy84、所属なし。共通SlideMaster.pptxから制作し、文字・引用・表はnative editable。ノートなし。

HELM Classic v0.4.0は2023年の公開スナップショットであり、使用した6件のrun suiteはv0.3.0。最新モデルの順位ではない。モデルはopenai/text-davinci-003、together/opt-175b、anthropic/stanford-online-all-v4-s3。スライドのAnthropic-LMは最後の内部モデルIDを指す。

- regularは公開dev.smallを使い、公開runは1,000質問。TRECは2019年の判定が付いた43質問。いずれも3試行で、平均提示訓練質問数2.0、prompt_truncated=0.0。各訓練質問に正例・負例の2文章を選ぶため、典型的なプロンプトには4組の訓練ペアがある。
- HELMの文章配布元はCodaLabの前処理済みコレクション。v0.3.0シナリオのDATA_URIS[(documents,)]とdocstring Notes(1)はMacAvaney et al. (2021), arXiv:2103.02280で導入された版を使うと明記する。元のMicrosoft collectionを未加工で直接読んだ条件とは異なり、p19で前処理済み配布元を明示した。
- 候補はBM25上位30文章とqrelsの全文章の和集合。通常のRR/NDCGと「topk=30」付きの指標は違う候補集合を採点する。regular text-davinci-003のRR@10は通常0.36773716931216915、topk=30は0.1992456349206349付近（正確値はstats.json）。後者には、上位30外にしか正例がない質問で得点0になる効果もある。
- TRECの二値指標は関連度1を0へ落とし、2・3を関連とする。NDCGは0〜3の元の値を使う。HELMのRankingMetricとgeneral.binarize_dictを取得して照合した。
- qrelsには未判定の関連文章もある。mainのメガネグマの例では、ラベル付きpassage7967212のほかに、体重を説明する未判定の5047774が候補にある。卸売価格への質問に小売の体験談が関連とされる例、利息への質問に改修費用の文章が関連とされる例もそのまま示した。

## 一次資料と公開実例

主要一次資料はBajaj et al. (2016)、Microsoftの公式サイトとPassage Ranking README、Craswell et al.によるTREC 2019概要、Nogueira/Jiang/LinのT5再ランキング論文、HELMの公開コード・run入力・stats。2026-10-18にSentence Transformersの公開学習READMEを取得し、現在もMS MARCOの正例・負例を用いる複数の学習例が公開されていることを確認した。最新版の最高性能を網羅した主張はしない。

13件の実例はHELMが公開するtext-davinci-003の元のrequest_statesから取得した。regular12質問、TREC1質問（本編regular2+TREC1、Appendixregular10）。各質問について、原文の質問・候補1文章の全文と元の関連タグを使い、日本語訳を付した。各例の元instance全体（候補の全参照を含む）をevidence/example-XX-record.jsonへ保存し、SHA256をexamples.jsonで対応させた。HELMのinstance IDは元のMS MARCO query IDと異なることをp57で説明した。passage IDは元コレクションのIDである。摂動を別例として数えていない。

実際のプロンプトでは、訓練例に続いて質問・候補文章を提示し、候補ごとに別々の要求を送る。スライドには1候補の全文を示すため、候補集合全体・訓練例は省かれる。この範囲をexamples.jsonとp57に記録した。存在しない生成回答を正解として作っていない。

公開scenario_state全体は巨大なのでHTTP Rangeで先頭2,000,000 bytes（gzip形式）を取得し、逐次展開・JSONデコードで完全な先頭レコードを抽出した。prefixの元URL、bytes、SHA、抽出位置と個別の完全レコードを保持した。全runの取得・全件解析とは扱わない。最初の無範囲取得で巨大なregularファイルを取得したが、容量を抑えるため削除し、検証可能なprefixと抽出レコードに置き換えた。

公式blob.core.windows.netのqrels直取得はproxyの403で失敗。NISTの直取得も完了せず、公開HELM入力の正解タグおよび公式概要の定義を照合に使った。公式の全コレクション2.9 GBや全質問集合を手元で測定した主張はしていない。取得失敗をevidence/*fetch-log.jsonへ記録した。調査・根拠がある13例を確保済みで、例数不足はない。

## 版、配布条件、引用元帰属

Microsoft公式サイトは、非商用のAI・関連分野研究目的での利用を対象とする。データの配布は元文書の知的財産権のライセンスを追加するものではない。ここではデータの説明・分析に必要な13件の文章を引用し、公式配布元・HELM公開入力への帰属を示す。公開runも元のWeb文章を含む。研究用データセットの全面的な再配布や商用利用の許諾があるとは扱わない。

公式トップ画面はhttps://microsoft.github.io/msmarco/を通常のTLS検証付きurllibで取得した応答をChromiumへ渡して描画。CSSとロゴが表示された画面をview_imageで確認した。screenshot-log.jsonにCSS枚数と失敗アセット、URLを記録した。代替のデータカードではない。

## 検査と校正

日本語校正はローカルjapanese-proofreadingスキルによるskill_based_codex、gemini_used=false。全61ページの最終文言とページ別確認をpage-review.jsonへ、実際に修正したbefore/after/reason/pageをproofreading-changes.jsonへ記録した。原文・固有名・数値・関連度タグを校正によって書き換えていない。

最終PPTXからPDFを生成し、全61ページのoverviewと、全ページの個別画像をview_imageで実際に開いた。引用26枠、native表4ページ、参考文献3ページ、公式画面を含む。引用枠はPDFの実文字境界から上下余白を調整し、再出力した最終ページを確認した。最終変更20・30・59〜61ページも個別再確認した。

- package-audit.json: 全XML/内部参照/IDを検査。新しいXSDエラー0。マスター既存11件と整数buSzPctの字句形式差を分離。native tables=4。
- layout-audit.json: 350段落と43セル、問題0。
- text-audit.json: 385段落の描画文字照合、問題0。
- links-audit.json: nativeのURL専用ラン68件、PDFリンク68件。URL文字列が完全一致、余分な文字なし。
- examples-verification.json: 原文・docid・質問・注釈・SHAを13例すべて照合。

独立レビューはこの自己確認とは別にメインが割り当てる。納品と取り込みはメインが行い、この担当は共有repo/engine/gitを変更していない。

独立レビュー完了：create_iceが全61ページ、13例、12成績セルと6runを確認。CodaLab前処理済みコレクションをp19に追記し、再出力・再監査・独立再目視後に合格。記録は /workspace/artifacts/helm-parallel/review-msmarco/review.json。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/msmarco.json)、[実際の校正対](skill-proofreading/msmarco.md)、[全ページ文言](skill-proofreading/msmarco/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/msmarco/review.json)。
