# CDial-Bias — 出典と検証範囲

2026-10-18取得。著者sasakiy84。本編31頁、全59頁。

## 一次資料

- Jingyan Zhou, Jiawen Deng, Fei Mi, Yitong Li, Yasheng Wang, Minlie Huang, Xin Jiang, Qun Liu, Helen Meng. **Towards Identifying Social Bias in Dialog Systems: Framework, Dataset, and Benchmark**. Findings of EMNLP 2022, pp.3576–3591. Zhou/Deng同等貢献。正式PDF/HTMLを取得し、paper-layout.txtも作成。https://aclanthology.org/2022.findings-emnlp.262/
- 作者GitHub para-zhou/CDial-Bias。commit `23b39a76093633bba8c5d668b79fd7e44d076ff8`。現READMEは項目形式を2.0と呼び、原論文と作者HF配布へリンク。https://github.com/para-zhou/CDial-Bias
- 作者HF原train.csv/val.csv/test.csv。固定revision **04b1b240fc2a06e97da624f7b6bd6fcc01a5444f**。3ファイルを実取得し、全CSVをcsv.DictReaderで読んだ。HF treeのgit blob SHA1/bytesとも一致。ファイルSHA256はcontent-audit.json/source_filesと各examples.jsonに保存。https://huggingface.co/datasets/para-zhou/CDial-Bias/tree/04b1b240fc2a06e97da624f7b6bd6fcc01a5444f
- Yanyang Li, Jianqiao Zhao et al. **CLEVA: Chinese Language Models EVAluation Platform**. EMNLP System Demonstrations 2023, pp.186–217. 正式PDF取得。CDial-Biasの採用を説明。https://aclanthology.org/2023.emnlp-demo.17/
- HELM v0.4.0 `CLEVABiasScenario`およびrun_specs_cleva_v1.confをGET。https://github.com/stanford-crfm/helm/blob/v0.4.0/src/helm/benchmark/scenarios/cleva_scenario.py

## 全件集計と版・符号の不一致

原CSVはtrain22,669/val2,837/test2,837=28,343対。q/a空文字0、idx全て一意、q+a文字列組は627件分の重複がある。topic_enはgender8,384/race10,871/region5,031/occupation4,057。topic原表記は5種で、raceには种族文化9,826/少数民族1,045が入る。四主題は一つの集合の区分であり四つの別データセットではない。

context0/1は17,371/10,972。attitude原文字列は0=11,140、NA=1,209、1=454、2=8,307、3=7,233。NAは原testのdatatype0の全1,209件のみ。train/valのdatatype0はattitude0。NAを自動欠損や空文字の正解、勝手な0へ変換していない。2022論文のIrrelevant12,349と概念上対応する範囲は0+NAだが原票ラベルを保った別集計を示す。

2022論文§4.1はdatatype1=Bias-Discussing、2=Bias-Expressing。一方、現在の公式READMEは1=Bias-expressing、2=Bias-discussingと逆に説明する。データの実際の符号が版間で変更されたか、文書の誤記かは確定していない。原CSVの数値と両資料の説明を併記し、意味を自動変換しない。

CSVのdatatype0/1/2は12,349/7,663/8,331。README Overall欄は12,349/7,659/8,333で、合計28,341となり2件差。README主題別行の1の合計は7,661でOverall7,659とも不一致。数値差を記録するが原因は断定しない。現配布を2022学習実験の完全な再現版とは呼ばない。

## 13原例・日本語・表示範囲

本編3+Appendix10、異なる13idxのq/a全文。各例で原split/0始まりCSV data row/idx/record SHA256/file SHA256/固定URL/全原レコード/原attitude・datatype・context・group・日本語を保持。新しい有害文やモデル出力を生成したものではない。原の質問に偏見的前提がある場合も改変せず、話者2の態度の注釈と分ける。差別的言説の転載そのものを目的とせず、反対・中立・無関係と原NAも含め、分類の論点を示す短い範囲を選んだ。

CLEVA docstringの4例は全て原trainに完全一致：性別idx7609/row2、職業25929/19487、人種17755/15390、地域5006/15439。本編1/2とAppendix4/5に採用。中国語2発話とTarget C/B/B/C、元attitude3/2/2/3が対応する。CLEVA公開例の3択に対し、元課題は無関係を含む四分類。公開例4件の一致からCLEVA全選択集合の版を推定しない。

全13件を15pt、中国語4.0in/日本語4.6inの不均等2列で実PPTX→PDFに試作し、13頁を個別view。全件同居可能と確認し、試作をevidence/coexist-probeへ保存した。最終も全13例を個別viewし、原文・訳の全文と21pt bold #B13731の原ラベルを確認。NAも配布の文字列として表示する。注釈が普遍的・文化に依存しない真偽判定だとは説明しない。

## 発表実験とHELM/CLEVA条件

2022分類実験はBERT-Base-Chinese、Vanilla/MoE/Multi-Task。重み付き交差エントロピー、検証集合でdropout3種×学習率4種×batch3種を探索、最大30epoch・3epoch連続改善なしで停止。付録stdはハイパーパラメータ組合せにわたる標準偏差で、固定3seed平均と扱わない。表のF1は発表値。新規学習はしていない。

Weighted F1はクラス件数で重み付けしたクラス別F1。Macro F1との区別、反対少数クラス、CI/CS別の入力条件を明示。原Table3の24数値、Table4の12数値、native主表と全比較表/4点chartを一次PDFの文字列から照合。APIの未報告総合値を補っていない。

生成モデルの実験はCDial-GPT/EVA/EVA2.0/CPM、262 test文脈×10乱数seed応答=各モデル2,620応答。自動Multi-Task分類と、異なる文脈の100件/モデルの人手確認を区別する。原生成文の公開原票は未取得。13資料例は原の人間2発話であり、このモデル生成集合ではない。外部生成・新規有害文生成・外部再採点APIを一切使わない。

固定v0.4.0 CLEVA confは4下位課題×prompt_id0–5=24設定。これは24データセット・24試行ではない。version v1のbias.zipを通常TLSでHTTP/HTTPS取得を試みたが、IP/証明書ホスト名不一致で取得できない（cleva-fetch-log.json）。検証を無効にしていない。現2.0とCLEVA採用時の集合・入力選択・版・全テンプレートを同一視しない。Classic固定v0.4.0のrun一覧8,526件のCLEVA/CDial該当0。CLEVA研究全体の実行が0という意味ではない。

## 権利・編集可能性・実検査

GitHub/作者HF本文はresearch purpose only、他用途は追加許可を明記。HF metadata/card front matterにはApache-2.0も掲げられる。二つの記載が同居するため、広い用途の無条件許諾と断定せず、p30/55に研究用途条件を明示した。全CSVやコーパスはサイト配布対象に指定しない。13既存の短い2発話対を、研究・注釈説明の引用として出所付きで示し、自作JPを添えた。収集元は知乎、アカウント・識別情報の除去は著者報告であり、本資料の新たな確認とは区別する。

native11表/1chart/27引用code枠、13原ラベル21pt bold #B13731、native原文とJP全文、notes0。全59頁を個別viewで読み校正、変更頁36頁を再viewし最終overviewも確認。全59PNGは最終PDFからの独立再描画に画素一致。layout369段落164セル0、包括native374段落212セル0/実字形重なり0、新XSD0（マスター既存11件と分離）、URL60は完全URL部分だけ。

引用枠は実glyphの上端/下端に基づき調整。actual-gray-glyph-gaps.jsonはPNG内の実gray画素境界と暗色glyph画素を再計測する。shape margin値だけの記録ではない。参考文献は各頁2件、正式題名と完全URLを保持し、編集可能なnative text frameの高さも最終実字形へ合わせて検査した。Table/Fig番号を本文・見出し・セルに入れていない。

再生成：prepare.py → build.py → convert.py/render.py → ink_panels.py → convert.py/render.py → audit_content.py/audit_layout.py/audit_package.py/check_links.py/native_final.py/measure_actual_gray.py → records.py。校正の実変更はソースへ反映済みで、中間apply_proofreading.pyは再実行不要。実目視は自動監査で代用しない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/cdial-bias.json)、[実際の校正対](skill-proofreading/cdial-bias.md)、[全ページ文言](skill-proofreading/cdial-bias/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/cdial-bias/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/cdial-bias/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
