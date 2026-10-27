# UniDic2025.12 — 出典と確認範囲

対象は国立国語研究所の「現代書き言葉UniDic ver.2025.12 解析用軽量版パッケージ」。UniDicの設計と用途を紹介したうえで、この版の実際の解析出力と配布形式を説明する。カタログ年2025は紹介版の公表年で、系列全体の初公開年を推測したものではない。

- [UniDic公式サイト](https://clrd.ninjal.ac.jp/unidic/)：全文と2025年12月31日の更新情報を確認。CSS・ロゴ・画像が読み込まれた画面を撮影し実見した。
- [UniDicとは](https://clrd.ninjal.ac.jp/unidic/about_unidic.html)：設計方針・所内データベース・配布解析用辞書の関係と、CSJ/BCCWJでの用途を確認。2019年の説明・2021年の利用一覧を2026年の利用調査とは扱わない。
- [用語集](https://clrd.ninjal.ac.jp/unidic/glossary.html)：短単位、階層的な見出し、品詞、語彙表IDと語彙素IDの各節を確認。書字形と発音形は語形の下の並列の情報。細かなビット表現や図そのものは転載しない。
- [FAQ](https://clrd.ninjal.ac.jp/unidic/faq.html)：全文を確認。特徴列、語種、ID、語彙の数え方と利用条件に対応させた。
- [現代語用ダウンロード](https://clrd.ninjal.ac.jp/unidic/download.html)：現代書き言葉・話し言葉の対象と条件を確認。[2025.12公式ZIP](https://clrd.ninjal.ac.jp/unidic_archive/2512/unidic-cwj-202512.zip)を実取得・全13ファイル展開した。README・BSD/COPYING・dicrc・rewrite.defの特徴列・feature.defの関係部分を確認。語彙全エントリの精読やlex.csv全件集計はしていない。この軽量配布にはlex.csvは含まれない。
- [全種類のダウンロード](https://clrd.ninjal.ac.jp/unidic/download_all.html)：古文・方言用の対象説明を参照。全種類を実行したり、現代語用の利用条件を全辞書へ拡張したりしていない。
- [商用利用について](https://clrd.ninjal.ac.jp/unidic/commerce_use.html)：全文を確認。使用版は修正BSDを選び、原文と帰属を保存した。
- 伝康晴ほか（2007）[コーパス日本語学のための言語資源：形態素解析用電子化辞書の開発とその応用](https://doi.org/10.15084/00002185)：リポジトリ書誌情報と日英抄録を確認し、単位の斉一性・見出しの同一性・変異を扱う目的に対応させた。論文全23頁を通読したとは扱わない。
- 工藤拓 [MeCab: オリジナル辞書／コーパスからのパラメータ推定](https://taku910.github.io/mecab/learn.html)：辞書の特徴情報と未知語候補、学習・配布形式の関係部分を確認。
- Paul McCann（2020）[fugashi, a Tool for Tokenizing Japanese in Python](https://aclanthology.org/2020.nlposs-1.7/)：書誌と抄録、[公式README](https://github.com/polm/fugashi)を確認。fugashi1.5.2を実導入し、表示コードを実行した。READMEが案内する旧版unidic/unidic-liteを、公式2025.12版として使ったことにはしていない。

11入力は本資料で用意した短い文字列。コーパスから抜いた実例と偽らず、公式辞書から実際に得た解析出力を記録した。本編6入力と補足の異なる5入力の対応はexamples.jsonに残す。Gemini・外部生成API・ベンチマークのモデル評価は使用しない。ローカルMeCabの解析は実行した。

制作・校正は3ローカルスキルに従った。実際の初稿PPTXからの前後対はproofreading.json、表示・構造・コードの確認は各監査票へ記録する。作成者自身の確認と、別担当の独立確認は区別する。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-unidic.pptx)・[PDF](../slides/datasets-in-10-minutes-unidic.pdf)。本編28頁、総41頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/unidic.json)・[校正の修正対](skill-proofreading/unidic.md)・[全ページ文言](skill-proofreading/unidic/pages.jsonl)・[最終検証票](skill-proofreading/unidic/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-UNIDIC-BSD.txt](licenses/unidic/LICENSE-UNIDIC-BSD.txt)、[ATTRIBUTION-UNIDIC.md](licenses/unidic/ATTRIBUTION-UNIDIC.md)。
