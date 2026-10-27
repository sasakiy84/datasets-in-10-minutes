# WLSP — 一次資料と読解範囲

参照・取得日：2026-10-28 JST。制作手法：skill_based_codex。Gemini・外部生成API・モデル評価は未使用。

- **official**：https://clrd.ninjal.ac.jp/goihyo.html
  全文実読。意味分類・1964書籍初版・2004増補版由来・CSV形式・関連資源。公式総101070は語数ではなくレコード数。

- **repo**：https://github.com/masayu-a/WLSP
  masterのcommit固定。readme.txt全文を実読し、v1.0.1、2004電子DB配布、2018版日付、CC BY-NC-SA3.0、引用指定を確認。

- **manual**：https://github.com/masayu-a/WLSP/blob/e809cf8203f8ab2ab2adef60d2fd0b2f643ac524/kaisetsu.txt
  同梱解説全文をShift_JISで読了。2004-02-25/Version1.0の仕様資料。分類階層、15列、A/B/数値種別、区切り＊と99、逆読みを照合。

- **book**：https://www2.ninjal.ac.jp/past-publications/publication/catalogue/bunruigoihyo_2ed/
  書籍紹介全文を実読。現代語とのずれ、コンピューター処理への応用、増補対象と分類見直し、2004年1月の刊行情報。旧ninjal URLは刊行物一覧へ転送されたため現行アーカイブを取得。

- **english**：https://www.ninjal.ac.jp/english/resources/search/
  該当資源項目のみ実読し、Word List by Semantic Principles / WLSPの正式名を確認。資源一覧全体を全読したとは扱わない。

- **mapping**：https://github.com/masayu-a/wlsp2unidic
  README全文実読。分類語彙表情報とUniDic語彙素IDの対応、ヘッダ付きTSV、配布credit2020/v1.0.2。対応表本体の実解析や結合実行は未実施。

- **familiarity**：https://github.com/masayu-a/WLSP-familiarity
  README全文実読。v4.0/2024-06-30、クラウドソーシングに基づく推定、親密度・位相情報、列仕様とCC条件。評定全データの取得・再推定は未実施。

- **CC**：https://creativecommons.org/licenses/by-nc-sa/3.0/deed.ja
  共有・翻案と表示/非営利/継承の条件を実読。公式legalcode.enも取得し原文を保存、全条文の個別法的解釈をしたとは扱わない。

## 原データと公開記録

データ本体は指定公開リポジトリの固定Git blobを実取得し全101067行を15列として解析。生データ・全行dump・スクリプトは制作環境に保持し、公開記録には選定例と集計範囲、取得URL、入力SHAだけを残す。別版の公式紹介値と取得版の実測値を混ぜない。
