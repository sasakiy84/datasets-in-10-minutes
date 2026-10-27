# Sudachi 同義語辞書の出典と確認範囲

主対象はSudachiDictの同義語CSV（2026-10-15更新、commit 830bf9e1313f6f75235ba87ee041e144dbcad8c1）。形態素解析辞書本体と別のファイルを扱う。

- [公式の列仕様](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)：11列、語形・略語・表記・展開制御。
- [配布CSV](https://github.com/WorksApplications/SudachiDict/blob/830bf9e1313f6f75235ba87ee041e144dbcad8c1/src/main/text/synonyms.txt)：取得した固定版。
- [2020年の設計・作成報告](https://www.anlp.jp/proceedings/annual_meeting/2020/pdf_dir/P4-14.pdf)：人手収集、階層的な関係と代表形、非対称な展開。
- [2019年の同義語辞書追加](https://github.com/WorksApplications/SudachiDict/commit/e32387bbc0913fd4352e571faa0954605dcf077c)：同義語ソースの初追加。
- [chikkarpy](https://github.com/WorksApplications/chikkarpy)：検索とSudachiPy連携。ライブラリ自体は今回実行していない。
- [yamaMomo](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/PT2-3.pdf)：同義関係と分野情報から日本語分散表現の評価用データを作成した研究。

再開担当がCSV・仕様・ライセンスを別HTTP取得し、全レコードを構造解析した。人間として通読した範囲は公式仕様、初期論文3頁、利用文書、ライセンス、選定した13群のレコード等であり、全CSVの人間通読とは扱わない。最終42頁の作成担当の個別実見と技術検査は本人の記録に対応する。旧担当の取得や初期版確認は継承範囲として分けた。

[原データ確認](../../data-audits/sudachi-synonym.json)・[形式と実表示](data-manifest.json)・[修正前後](proofreading.json)・[全頁文言](pages.jsonl)・[技術検査](technical-summary.json)・[帰属](../../licenses/sudachi-synonym/ATTRIBUTION-Sudachi-Synonym.md)・[Apache License 2.0](../../licenses/sudachi-synonym/LICENSE-SudachiDict-Apache-2.0.txt)。
