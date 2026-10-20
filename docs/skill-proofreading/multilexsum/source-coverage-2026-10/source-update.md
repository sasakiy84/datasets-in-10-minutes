# Multi-LexSum：要約の元入力表示の点検

判定：今回問題になった、入力を冒頭1文だけのproxyにする不備はない。現63頁の13実例は、公式のShort要約全文を入力とするShort→Tiny課題であり、28–52語という短さは配布入力自体の長さである。13のTiny参照全文・各日本語訳も保持されている。PPTX/PDFは変更しない。

正式NeurIPS2022本文§3.1は、元文書群からL/S/Tへ要約する3課題に加え、正解要約を入力にして短い要約へ写す3課題を定義し、S→Tを明示する。§4の要約間圧縮の実験もS→Tを扱う。原訴訟文書群を表示していないことを、この独立課題の入力欠落とは判定しない。スライド6/7に課題と表示範囲が既に説明されている。

Tinyの全事実がShortに含まれるという判定ではない。全13の参照を事実単位で読み、Shortで確認できる内容、Longで補える具体情報、Shortにも保存Longにも明示のない内容、登録・更新を知らせる告知表現、主体の表現差をreference-fact-coverage.jsonへ記録した。例2の1,697人・裁判所、例6の仮差止め/判事の引用、例12のCOVID-19などはShortにない。Tinyは事件の特定時点を紹介するTwitter用の文でもあり、登録告知やSNSハンドルを含む。これらは原Shortをスライドで省略したために失われた事実ではない。現14/58頁にもShort外の情報が含まれる例が説明されている。

資料全体は元文書群→3粒度も紹介するが、元訴訟文書群そのものを見せる実例はない。既存資産には公開要約と文書IDはある一方、原文書本文は取得していない。今回は主担当の指示に従い、この同種不備の修正に範囲を絞り、原文書群の新規取得・追加スライド作成は行わない。

## 実施した検証

全13の入力をsummary/shortと、参照をsummary/tinyと比較し、固定test JSONLの原行/原記録SHA/ファイルSHAへ一致を確認。63頁のnativeから全EN入力・参照・JPが欠けずに載る頁を検索し、元文と訳を実際に読み比べた。before-after.tsvとpage-map.jsonは、全文範囲維持と63頁の恒等対応を示す。

現repoファイルは、既存の独立レビューが全63頁を個別目視・監査した版とSHA完全一致する。今回は変更頁0であり、新たな画像目視を実施したとは記録しない。前回の全頁描画承認を、同一ファイルであることに基づき継承する。今回の新規検証は入力表示範囲と参照事実の対応である。Gemini/生成APIは使用していない。

## 一次資料

- Shen et al. (2022), Multi-LexSum: Real-World Summaries of Civil Rights Lawsuits at Multiple Granularities. NeurIPS2022. https://arxiv.org/abs/2206.10883 。正式本文保存：/workspace/artifacts/helm-parallel/multilexsum/evidence/paper-final.txt。
- 公式配布 https://huggingface.co/datasets/allenai/multi_lexsum 。固定release v20220616、固定HF改訂055f5fa5300a5fdefb5b691c4d6c1e58f485b379、test908事件。今回のコピーtest.jsonlと原13記録はexamples.json。
- 旧調査/生成記録は /workspace/artifacts/helm-parallel/multilexsum と /workspace/artifacts/helm-editorial-revision/multilexsum を変更せず保持。
