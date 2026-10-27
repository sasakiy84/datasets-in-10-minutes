# UniDic 独立確認の範囲

新担当 `review_unidic_final` が確認した範囲。旧担当が消失する前の実見や技術票は、今回の本人の実施として継承していない。

公式トップ・UniDicとは・現代語ダウンロード・商用利用のページを独自HTTP取得し全文を読んだ。用語集の短単位と見出し階層・可能性に基づく品詞・語彙表ID/語彙素IDの定義、FAQの出力列・名称対応・ライセンス・語彙数の数え方、古文・方言ページの対象と別利用条件を読んだ。aboutの説明は2019年、所外利用例は2021年という範囲を保ち、2026年の全利用調査とはしない。

- https://clrd.ninjal.ac.jp/unidic/
- https://clrd.ninjal.ac.jp/unidic/about_unidic.html
- https://clrd.ninjal.ac.jp/unidic/glossary.html
- https://clrd.ninjal.ac.jp/unidic/faq.html
- https://clrd.ninjal.ac.jp/unidic/download.html
- https://clrd.ninjal.ac.jp/unidic/download_all.html
- https://clrd.ninjal.ac.jp/unidic/commerce_use.html

実使用パッケージのREADME、COPYING、選択された修正BSD原文を全文読んだ。GPL/LGPL/BSDの選択可能性は公式ページとCOPYINGに照合したが、GPL/LGPL全条文を逐語精読したとはしない。rewrite.defの出力列、dicrcの該当設定を読み、29特徴の実出力・語彙素等の対応を独自実行と照合した。辞書エントリ数と語彙素数を同じ単位にしていない。

MeCab一次文書の辞書形式・dicrc・char.def/unk.defの未知語処理を読み、p21/35の説明を確認。fugashiのACL書誌と抄録を読んで、正式題名・会議名・著者・頁とPythonラッパーという位置付けを照合した。2007論文の正式題名・著者・巻頁は国語研一次ページの書誌で確認したが、論文全23頁を通読したとはしない。

- https://taku910.github.io/mecab/learn.html
- https://aclanthology.org/2020.nlposs-1.7/

公式696MB ZIPは作成担当が取得したものを再利用。自分で全ファイルSHA-256、ZIP全13メンバーCRCと容量/一覧を確認し、公式URLの先頭末尾64KiBを別HTTP取得して一致を確認した。全ZIPを別途再取得したとは記録しない。独自にfugashi1.5.2を導入し、11入力のsurface/feature/未知語flagを再実行し、表示に使う出力すべてが一致した。p25は最終PPTXのnative codeを取り出し、辞書パスだけ変更して実行一致した。外部生成API・Gemini・ベンチマークモデル評価は使用していない。
