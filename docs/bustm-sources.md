# BUSTM 一次資料・制作記録

対象はOPPO XiaoBu Conversational-AI Centerの2021年 **BUSTM: OPPO XiaoBu Dialogue Short Text Matching Dataset**。公式公開元 https://github.com/xiaobu-coai/BUSTM の固定commit `4e80d7fe23d56d7e8680d6565f02a7c46253dad4` をAPIから確認。READMEは中国語名「小布助手对话短文本匹配数据集」、FewCLUE配布リンク、2021引用、32/32/1772/2000/4251を明示。展開名に略称の各文字を推測して加えていない。別のBQ financial questionコーパスやCLEVA全採用集合とは統合しない。

## 一次取得と固定版

FewCLUE固定commit `62a02c6f31cf32814cfe522f78ef088228840f8d` の公式15ファイル、8,663配布行（小集合とallの重複配布を含む）、811,648 bytes。初回の原ファイルGETはメインがcleva-origin-review/fewclue-fetch-log.jsonへ記録し、本専有dirへ移譲したもの。制作担当は公式固定Git treeを別GETし、全15ファイルのGit blob SHA1をローカルbytesから再算出して全件一致を確認した。再取得したかのようには記録しない。URL/SHA256/bytes/blobはstats.json/data-audit.jsonへ保持。公式README/固定tree/commit/CLEVAコードとconfig/4baseline実装の追加取得はfetch-log.json、fetch-more-log.json。通常TLS/proxy使用、証明書検証無効化なし。

OPPO公式GitHubをChromiumで実描画。HTML200/CSS/フォント表示と画面本文を実際にviewし、official-site.png採用。取得手順とasset結果はscreenshot-log.json。別コーパスのカードを公式トップと呼ばない。

## 論文と内容

Liang Xu, Xiaojing Lu, Chenyang Yuan, Xuanwei Zhang, Huilin Xu, Hu Yuan, Guoao Wei, Xiang Pan, Xin Tian, Libo Qin, Hai Hu (2021), **FewCLUE: A Chinese Few-shot Learning Evaluation Benchmark**, arXiv:2107.07498v2。初出2021-07-15、v2 2021-09-29。取得PDF SHA256 `a868c5eea19f5f2ab00a30c0205c759d330610ee0975328c007bd6514073d971`。11ページを個別表示し、本文・統計表・結果表・人間評価・書誌を確認した。arXivメタデータで刊行会議/雑誌なし。NLPCC2021コンテストへの利用を論文のNLPCC正式刊行と混同しない。原データ公開年も2021で公式引用に直接根拠がある。

目的は小布助手の意図認識に使う対話短文意味照合。スマートフォン/IoTの発話から来る口語的な二文の同意味判定。原サービス全データ数・注釈人数/同意/詳細ガイドライン・各対の理由・全作成期間は確認できず、32件や公開全件から推定していない。FewCLUEは9課題、n_label<=3は合計32例、複数train/devと未ラベル対を提供する。ここで32は各クラス32ではない。

## 完全集計と13例

prepare.pyは15ファイルの全行を解析。0/1は文字列。test2000/unlabeled4251にはlabel欄がない。test_public1772は0=886/1=886。train_all160は0=90/1=70、dev_all160は0=82/1=78。各小集合32は各32種類。all160はそれぞれ156種類、重複追加行4。allは各0〜4小集合の連結と、順序付き発話対＋labelのmultisetで完全一致。全ファイルを通じ同一順序付き発話対に非欠損ラベル競合なし（元research.py再実行済みではなく、移譲研究結果を初期根拠とし、制作側prepareは集約一致・各原例照合を追加）。

train_all/dev_all/test_public/test/unlabeledの10組合せは順序付き発話対の完全一致0。語の重なりや意味の近さまで否定する検査ではない。IDだけでは集合をまたぎ一意でない。文字長はUnicode文字数、空白・句読点込み、各発話別計測。公開テスト最短2/最長25/平均7.37文字（トークン数ではない）。全内訳はstats.json。

13独立原例、本編3＋追加10。examples.jsonに元ファイル/1始まり行/id、原行（改行込み）/SHA256/byte offset、原票の正準JSON SHA256、source全bytesSHA、四つの言語対応欄と配布labelを保持。原票にないIDは作らない。train_all36行はCLEVA紙面、train_1の4行と同じ対（IDは異なる）。train_0の3行はHELM docstring。近い表現でも配布0を保持し、注釈理由を捏造しない。

本文は原CN2発話＋JP全文＋0/1正解を一頁に保持。原文の文法崩れ/反復も直さない。日本語は新規の意味訳で既存訳の転載ではない。例13「阿伟死了」は語句使用とネット表現についての質問の違いのみ説明し、元が単独発話のため発話者が特定のミームを意図したと断定しない。13例は8負/5正、選定例の比率でコーパス比率を代替しない。

公開対象13例のemail/電話を確認し不掲載。元test_public13行にはemailがあり、本資料例には選んでいない。原データ全JSONL・論文・HTMLはローカル調査用、公開用原記録は選んだ13短対に限定する。権利・個人情報監査で原文全件を不要にログへ印字しない。

## 評価・結果の範囲

Accuracy。公開test_publicの一定ラベルは886/1772=50%。これは制御した定数予測の算術で、モデル実行ではない。モデル再実行なし。2021 FewCLUE結果表のBUSTM値：Majority50.0、Human88.0、FineTuningR60.7(9.1)、Zero-shotR50.6、Zero-shotG50.0、PET56.0(5.0)、LM-BFF57.6(3.4)、P-tuningR60.9(2.9)、EFL71.8(0.8)、FineTuningERNIE60.4(5.7)、PETERNIE58.4(3.4)、P-tuningERNIE60.8(5.3)、EFLERNIE54.6(8.1)。本文表は中心値を引用し、括弧の意味・集約試行数が当該表で明示されないためSD/5試行平均等とは断定しない。

公式READMEは比較数値がtest_publicの結果と明記し、PET公式コードもtest_publicを使用。論文とREADMEで時点や全課題の結果が異なるので、本資料のモデル値は論文v2を優先、集合の役割はREADMEを併用する。コンテストは別test2000へ提出、第二段階0〜4/allの6学習条件。現在の公開リーダーボード最新性能とは呼ばない。

基盤RoBERTaはchinese_roberta_wwm_ext、ERNIE1.0比較。EFLはCMNLIで先行学習した後、下流少数例に微調整するため追加データの条件を保つ。PETテンプレートはコードの「意思锟同」の锟位置をMASK化し1→相/0→不。元テンプレート例は実装方式であり未実行のモデル出力ではない。コードはtrain指定条件/dev_few_all/test_public、一般説明の各32devと全く同じではない。ADAPET読込にはクラス番号の内部変換1→0/0→1があるが、元データlabelは維持。

人間評価88.0はFewCLUEの公表値。新3課題の手順はdev30〜50問の練習・照合・議論、各人テスト100問。人数・BUSTMの評価問題ID・全1772に対する評価とは断定しない。READMEはdev100/投票との別記載があるため手順は正式論文v2を優先し、この差を保持する。

## CLEVA / HELM

Yanyang Li et al. (2023), **CLEVA: Chinese Language Models EVAluation Platform**, EMNLP System Demonstrations。PDF/txtは自分のCCPM調査からbytes不変でコピー（再GETと偽らない）。Paraphrase Identification記述はCLUE/FewCLUE由来、二択・Accuracy、公開CN例「你的火气大吗／你火气大不大／是」。原train_all36行と一致。HELM v040 CLEVAParaphraseIdentificationScenarioのshort_utterance例はtrain_0の3行、A不是/B是、Target A。financial_questionは別下位課題で本資料BUSTMへ混ぜない。

configはparaphrase_identification/short_utterance/v1、prompt_id0〜5。HELM Converterはテンプレートからchoicesとlabelを作りReferenceへ変換する。六つは元データ六コーパスではない。Classic v040の公開全8526 run_specsを集計しCLEVA0、元manifestSHA256 `ef94fb6d3d234ef3193ed043b4a718cd75e0cf2aaf94f0439693cf46a4ff6f62`。helm-audit.jsonに実コードSHA/設定/説明例確認/ZIP再試行を保存。HTTP/HTTPSの公式IP配布は証明書IP名不一致、正常TLSで取得不能。無効化せず、全採用集合・prompt全体・得点・max_tokens/実提示例数を推測しない。

## 権利・限界

OPPO固定リポジトリはREADMEのみ、LICENSEなし、GitHub metadata license=null。FewCLUE固定treeにも全体データLICENSEなし（baseline BERTのコードLICENSEをデータ全体に適用しない）。README Licenseは「正在添加中」。MIT/CC/商用可を推測せず、元発話と収集データの条件を公開元へ確認して使う。13短対は出典を付して課題説明の範囲で引用。原配布元の公開と、複製・再配布の包括許諾は区別する。

最終自己検査：54頁を全て個別view、overview確認、修正箇所を再view。全13原CN＋JPは不均等3.8/4.8inch・19ptで同居。正解14箇所は21pt bold B13731。引用/コード30枠の実字形上下差最大0.06666666666664867pt。360段落104セルlayout0/newXSD0/55URL完全一致/notes0。日本語スキルの実修正10対・全頁文言記録を保存。全15ファイルのラベル付き順序対にラベル競合0も制作担当が全件再確認。正式本文へのモデル再実行なし。

独立レビュー対応：p7の给我を日本語でも「私に」と明示し、给我们との単複を保持。原CN/label/解説は維持。元例/native/manifest/実校正11対へ同期、p7実view・全監査/records再合格。最新hash {'pptx_sha256': 'c7db7898202992100984a4d23224146fb9b6cda9c3d1a745804fc26e5af73102', 'pdf_sha256': 'd26ac83b6a5dde302da4144f6019a721449e085551dcff51fc012e29f0b6b58e'}

Pile独立レビュー承認・残件0。全54頁・原15ファイルの別GET/8663行/13例/訳/条件/全画像同期/技術監査/最終c7db7898…/d26ac83b…確認。review-bustm/review.jsonに実範囲と最終hashを保存、canonical passed同期済み。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/bustm.json)、[実際の校正対](skill-proofreading/bustm.md)、[全ページ文言](skill-proofreading/bustm/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/bustm/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/bustm/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
