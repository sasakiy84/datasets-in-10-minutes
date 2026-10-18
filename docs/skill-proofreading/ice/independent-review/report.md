# ICE 独立レビュー

結論：修正後合格。未解決の指摘なし。レビュー担当create_msmarco。元成果物とrepoは編集せず、作者が修正して最終PDFを再出力した。

## 具体的な指摘と確認結果

1. p21、East Africa / text-davinci-003のbits_per_byte。元statsの0.7635297830374674を小数第3位で四捨五入すると0.764だが、初版表は0.763だった。作者が0.764へ修正。最終native表と元statsを独立スクリプトで比較し、8セルすべて丸め一致を確認。変更後p21を個別view_imageで確認した。
2. p39、`I don't know how much I deserve them` の訳。初版「そんなに褒めていただけるのか分かりませんが」は、今後褒められる可能性の意味に読めた。作者が「コーリ教授に素晴らしいお言葉をいただきました。私がどれほどそれに値するかは分かりませんが。」へ修正。原文を保持し、変更後p39の訳と描画を個別view_imageで再確認した。

## 独立して照合した対象

- 公式design/access/annotation HTML、ライセンス本文、HELM ICEScenario v0.3.0の実装とdocstring。
- India 12例は、検証用公開scenario-state.jsonの先頭64MBを逐次JSONデコードし、該当request_states位置から原文を直接再取得した。元ID、本文全文SHA、連続範囲、抜粋SHA、空白正規化表示をすべて照合。抜粋以外の全文をレビュー成果物へ複製していない。
- USA 1例は公開公式コードのdocstringにoriginal_rawがそのまま存在することとSHAを照合。Indiaの別runやUSAコーパス全文を取得した扱いにしていない。
- raw statsのname={name:bits_per_byte,split:test}を8runで選択し、native表へ対応させた。すべてcount=1。12runのmethod=language_modeling、訓練0件、max_tokens=0、最大評価1000件、1試行も直接照合。
- 標準500テキスト構成と、HELM公開runのEA625/HK500/IND500/USA200件の違いが本文に示されている。USAは書き言葉のみという条件も表にある。
- 世界の英語の比較資料とHELMの言語モデル評価を混同していない。公開run入力が元コーパスの自由な再配布許諾を意味するとは書いていない。handoffがscenario-state.jsonとindia-inputs.jsonを公開取り込み対象から除外している。
- masterとのXSD差を独自に再比較し、新規エラー0。ZIP・内部参照・図形ID検査も合格。作者のlayout/text/links監査を確認し、最終変更後も問題0。

## 目視範囲

overviewを実際に開き、公式画面、13実例の全ページ、5表、3参考文献、指標・実行条件・ライセンス・実装差・引用範囲を1ページずつview_imageで拡大確認した。対象ページはreview.jsonに明記。修正後のp21/p39を再度開いた。原文の最終行、灰色枠の上下余白、訳、引用範囲、罫線、出典・リンク範囲、glyph欠落を検査し、残る問題は見つからなかった。一般本文49ページすべてを個別拡大したとは記録していない。
