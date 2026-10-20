# Toolathlon-Verified：出典と制作記録

公開一次資料と課題ファイルを調べ、日本語の紹介資料を作成した。対象は2026年6月30日に最終公開されたToolathlon-Verifiedであり、2025年の研究・2026年2月の論文改訂で示された構築方法と初期評価は、その時点の結果として扱う。Geminiや外部モデルAPIは使用していない。

## 一次資料

- Junlong Li et al., *The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution* (2025; v2, 2026-02-26; ICLR 2026). https://arxiv.org/abs/2510.25726
- 公式プロジェクトとリーダーボード。2026-10-21日本時間に確認。 https://toolathlon.xyz/
- hkust-nlp/Toolathlon公式公開リポジトリ。課題108件の依頼文・設定、選んだ課題の初期ファイル・参照成果物・評価コードを確認。 https://github.com/hkust-nlp/Toolathlon
- Anthropic, *Claude Fable 5.1 & Claude Mythos 5.1 System Card*, §8.15.5, pp.194–195. Fable 5.1での継続利用と社内実行基盤の条件を確認。 https://www.anthropic.com/claude-fable-and-mythos-5-1
- Toolathlon-Verified実行履歴の公開メタデータ。申請付き配布・評価等に限定した利用・生の履歴の再配布禁止という条件を確認。履歴ファイルは取得していない。 https://huggingface.co/datasets/hkust-nlp/Toolathlon-Verified_Trajectories

## 課題と実例

本編では、Canvas上の課題採点、メモリ中の取引を使った帳簿更新、倉庫SQLiteとWooCommerce間の在庫同期の3件を扱う。補足では、論文探索、メールからの予定登録、実験ログの集計、非公式実装探索、Kubernetes監査、Notion更新、文書のマスキング、表の変換、A/B分析とクラウド操作、領収書と未払い連絡の10件を追加した。

モデルが実際に操作したログとして提示せず、公開された依頼・初期資料・参照成果物・評価条件の対応として説明した。原文は必要な全文を保持し、長いものは意味上の区切りで分けた。コード区切りのbackticksはファイル名と隣接語の境界を保つため保持し、空の段落による改行を整理した。翻訳と参照値は原文と区別する。

帳簿の120件の保持と5件の追加、在庫の6都市・3地域・商品IDごとの集計、A/Bの20分野の平均、表変換の参照データ、文書の入力27件と参照27件を照合した。公開評価コードの一部には、依頼された項目のすべてを直接検査しないものや、判定の許容値がある。実際に呼ばれる検査範囲を確認し、すべての条件を完全一致で検査するとは記載していない。

## バージョンと結果

論文の32アプリ・604ツール・16ローカルツール・72/108課題での初期化という公表値を使う。現行設定ファイルのサーバ名33種類との細差は、検証記録で区別した。研究の分野別図の割合と108件から得られる内訳は、研究で示された対象の分布として掲載し、Verified全件を独自に分野分類し直したものとはしていない。

2026-10-21確認時の公式サイトはDefaultエージェントの7モデルを掲載している。本編では4系列の結果を選んだ。Fable 5.1の77.8%は別ページで、社内実行基盤・max effort・3試行・安全分類器と代替モデルの条件を示した。324試行のうち11でOpus 4.8の代替実行、別の4が終了して失敗、という内訳を省略せず、公開ボードと同一条件の順位表には混ぜなかった。

## 入手・利用条件

公開GitHubでは、確認した時点のルートにLICENSEを見つけられず、GitHub APIにも包括的なライセンス名がない。MIT・Apacheなどを推測して付与していない。課題ファイルの短い引用や参照データには作成元と個別課題のURLを付け、原票全体や環境データ一式を再配布する資料にはしていない。

Hugging Faceの実行履歴は申請付きで、学習・蒸留・評価を解くための検索コーパスへの利用と、生の履歴の公開再配布を禁じる条件がある。その履歴はダウンロード・実行・再配布していない。

## 制作と確認

共通SlideMasterを使った編集可能なPPTXからPDFを出力する。マスター、ネイティブの表・図、引用・出典、URLのみのリンク、著者sasakiy84、発表者ノート0件を確認する。スキルによる校正前後の対、全頁文言、原票照合、描画・パッケージ監査、実際に個別画像を開いた範囲と独立確認の範囲を別々に記録する。

本物の外部アプリ、メール送信、課金API、添付された提出プログラムの実行は行っていない。PowerPoint本体での開封、閲覧時間の実測も未実施。本編の流し読みは600秒の予定である。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-toolathlon-verified.pptx)・[PDF](../slides/datasets-in-10-minutes-toolathlon-verified.pdf)。本編35頁、総80頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/toolathlon-verified.json)・[校正の修正対](skill-proofreading/toolathlon-verified.md)・[全ページ文言](skill-proofreading/toolathlon-verified/pages.jsonl)・[最終検証票](skill-proofreading/toolathlon-verified/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。
