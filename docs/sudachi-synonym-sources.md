# Sudachi 同義語辞書の出典と確認範囲

主対象はSudachiDictの同義語CSV（2026-10-15更新、commit 830bf9e1313f6f75235ba87ee041e144dbcad8c1）。形態素解析辞書本体と別のファイルを扱う。

- [公式の列仕様](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)：11列、語形・略語・表記・展開制御。
- [配布CSV](https://github.com/WorksApplications/SudachiDict/blob/830bf9e1313f6f75235ba87ee041e144dbcad8c1/src/main/text/synonyms.txt)：取得した固定版。
- [2020年の設計・作成報告](https://www.anlp.jp/proceedings/annual_meeting/2020/pdf_dir/P4-14.pdf)：人手収集、階層的な関係と代表形、非対称な展開。
- [2019年の同義語辞書追加](https://github.com/WorksApplications/SudachiDict/commit/e32387bbc0913fd4352e571faa0954605dcf077c)：同義語ソースの初追加。
- [chikkarpy](https://github.com/WorksApplications/chikkarpy)：検索とSudachiPy連携。ライブラリ自体は今回実行していない。
- [yamaMomo](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/PT2-3.pdf)：同義関係と分野情報から日本語分散表現の評価用データを作成した研究。

再開担当がCSV・仕様・ライセンスを別HTTP取得し、全レコードを構造解析した。人間として通読した範囲は公式仕様、初期論文3頁、利用文書、ライセンス、選定した13群のレコード等であり、全CSVの人間通読とは扱わない。最終42頁の作成担当の個別実見と技術検査は本人の記録に対応する。旧担当の取得や初期版確認は継承範囲として分けた。

[原データ確認](data-audits/sudachi-synonym.json)・[形式と実表示](skill-proofreading/sudachi-synonym/data-manifest.json)・[修正前後](skill-proofreading/sudachi-synonym/proofreading.json)・[全頁文言](skill-proofreading/sudachi-synonym/pages.jsonl)・[技術検査](skill-proofreading/sudachi-synonym/technical-summary.json)・[帰属](licenses/sudachi-synonym/ATTRIBUTION-Sudachi-Synonym.md)・[Apache License 2.0](licenses/sudachi-synonym/LICENSE-SudachiDict-Apache-2.0.txt)。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-sudachi-synonym.pptx)・[PDF](../slides/datasets-in-10-minutes-sudachi-synonym.pdf)。本編32頁、総42頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/sudachi-synonym.json)・[校正の修正対](skill-proofreading/sudachi-synonym.md)・[全ページ文言](skill-proofreading/sudachi-synonym/pages.jsonl)・[最終検証票](skill-proofreading/sudachi-synonym/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-SudachiDict-Apache-2.0.txt](licenses/sudachi-synonym/LICENSE-SudachiDict-Apache-2.0.txt)、[ATTRIBUTION-Sudachi-Synonym.md](licenses/sudachi-synonym/ATTRIBUTION-Sudachi-Synonym.md)、[NOTICE-Sudachi-Synonym.txt](licenses/sudachi-synonym/NOTICE-Sudachi-Synonym.txt)。
