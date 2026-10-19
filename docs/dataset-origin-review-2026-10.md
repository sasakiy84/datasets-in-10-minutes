# データセットの出自と説明範囲の確認（2026年10月）

対象47資料のうち、最新方針での改訂・独立レビュー・統合を終えた41資料を記載する。未完了の資料を確認済みとは扱わない。

選定に使った一覧の説明ではなく、各データセットや課題の目的、実例、構築、評価、使い方を主題に改めた。元データの作成、既存素材の利用、後続研究の加工・採用を、一次論文と公式配布に照合した。採用先の固有設定や検証用の細部はスライド外の記録へ移した。

Numeracyの多項式課題やWikiFactのように、選定元の研究で実際に新規構築されたものもある。作成主体を他の研究へ付け替えず、素材や同名データとの関係を明確にする。CLEVAは依頼に従い、プラットフォーム自体を独立した資料として扱う。

今回の改訂と確認はCodexとローカルスキルによる。Geminiは使用していない。文言の修正対、削除した詳細、ページ対応、作成者・独立レビュアー・メインの確認範囲は各資料の記録に残す。

| 資料 | 出自と説明範囲 | 根拠・変更記録 |
|---|---|---|
| EPRSTMT | 北京師範大学ICIP Labのレビューを、FewCLUEチームが少数例評価へ整備した。 | [一次資料の照合](skill-proofreading/eprstmt/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/eprstmt/editorial-2026-10/changes.md) |
| AFQMC | Ant FinancialのATECに由来する質問照合データを、CLUEが中国語理解評価へ整備した。 | [一次資料の照合](skill-proofreading/afqmc/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/afqmc/editorial-2026-10/changes.md) |
| OCNLI | Huらが中国語の前提文と母語話者の仮説・再注釈から構築した。 | [一次資料の照合](skill-proofreading/ocnli/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/ocnli/editorial-2026-10/changes.md) |
| Math23K | Wang・Liu・Shiが2017年に構築。2019年のGTSは別の新手法であり、追試という旧説明を訂正した。 | [一次資料の照合](skill-proofreading/math23k/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/math23k/editorial-2026-10/changes.md) |
| NarrativeQA | KočiskýらのDeepMind/Oxford研究。作品・要約・人手質問と二つの参照回答からなる読解データ。 | [一次資料の照合](skill-proofreading/narrativeqa/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/narrativeqa/editorial-2026-10/changes.md) |
| Natural Questions | Google Researchを中心とするKwiatkowskiらが、実検索質問とWikipedia全HTMLの長短回答を注釈した。 | [一次資料の照合](skill-proofreading/naturalquestions/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/naturalquestions/editorial-2026-10/changes.md) |
| QuAC | Choiらの共同研究。質問者には本文を見せず、教師が節を読んで範囲を選ぶ対話型読解として構築した。 | [一次資料の照合](skill-proofreading/quac/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/quac/editorial-2026-10/changes.md) |
| CNN / DailyMail | Hermannら2015年のニュース読解から、Nallapatiら2016年のハイライト要約、Seeら2017年の非匿名版へ発展。ニュース素材と加工・課題の作成主体を区別する。 | [一次資料の照合](skill-proofreading/cnn-dailymail/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/cnn-dailymail/editorial-2026-10/changes.md) |
| cMedQA2 | Zhangらが自らの中国語医療回答選択データを拡張したもの。元の100候補評価を紹介する。 | [一次資料の照合](skill-proofreading/cmedqa2/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/cmedqa2/editorial-2026-10/changes.md) |
| COLD | Dengらが中国語の攻撃的表現を収集・注釈し、検出器COLDDetectorとともに公開した。 | [一次資料の照合](skill-proofreading/cold/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/cold/editorial-2026-10/changes.md) |
| MS MARCO | MicrosoftがBing質問・Web文章・人手回答から構築。TREC2019の段階的関連度判定は追加の評価資料。 | [一次資料の照合](skill-proofreading/msmarco/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/msmarco/editorial-2026-10/changes.md) |
| LegalSupport | Liangらの研究で新規作成。CAPの既存判例が素材で、課題設計・実装はNeel Guhaの担当と確認した。 | [一次資料の照合](skill-proofreading/legal-support/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/legal-support/editorial-2026-10/changes.md) |
| LSAT | ZhongらがLSAT試験由来の分析的推論問題を整備したAR-LSAT。試験問題・研究データ・ARM手法を区別し、現配布と論文件数差を明示した。 | [一次資料の照合](skill-proofreading/lsat/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/lsat/editorial-2026-10/changes.md) |
| LexGLUE | Chalkidisらが七つの英語法律課題を整理したベンチマーク。SCOTUSは判決文とSCDBの争点情報から新規構築し、ほかの法律データも入力・ラベル・分割・評価方法を整えて収録した。 | [一次資料の照合](skill-proofreading/lexglue/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/lexglue/editorial-2026-10/changes.md) |
| CCPM | Li・Qi・Sun・Yi・ZhangのTHUNLP-AIPoet研究。古典詩句と現代語訳の対を集め、四択課題に構成した。 | [一次資料の照合](skill-proofreading/ccpm/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/ccpm/editorial-2026-10/changes.md) |
| BUSTM | OPPOの小布会話AIチームが公開した短文意味照合。FewCLUEは少数例学習評価へ整備して採用した。 | [一次資料の照合](skill-proofreading/bustm/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/bustm/editorial-2026-10/changes.md) |
| ChID | Zhengらの中国語成語穴埋めデータ。CLUEの候補共有形式は元形式との違いを保つ。 | [一次資料の照合](skill-proofreading/chid/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/chid/editorial-2026-10/changes.md) |
| WMT2020（英中） | WMT2020ニュース翻訳の英中・中英テスト。運営の元評価と公式テスト配布を紹介する。 | [一次資料の照合](skill-proofreading/wmt2020-enzh/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/wmt2020-enzh/editorial-2026-10/changes.md) |
| TwitterAAE | Blodgettらが位置付き投稿と地域人口構成から構築したコーパス。人口統計による言語的関連と個人の人種を区別する。 | [一次資料の照合](skill-proofreading/twitter-aae/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/twitter-aae/editorial-2026-10/changes.md) |
| BillSum | Kornilova/EidelmanのFiscalNote Research研究。連邦議会・California議会の法案と専門家要約を対応付けた。 | [一次資料の照合](skill-proofreading/billsum/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/billsum/editorial-2026-10/changes.md) |
| EUR-Lex-Sum | Aumiller・Chouhan・GertzがEUR-Lexの法令と専門家要約を収集し、最大24言語へ対応付けた。 | [一次資料の照合](skill-proofreading/eurlexsum/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/eurlexsum/editorial-2026-10/changes.md) |
| Multi-LexSum | Shen・LoらとCivil Rights Litigation Clearinghouse等の協力で構築。法律実務の文書群と専門家要約を三つの粒度で提供する。 | [一次資料の照合](skill-proofreading/multilexsum/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/multilexsum/editorial-2026-10/changes.md) |
| CLUEWSC2020 | CLUEチームが36作品から中国語の照応判定を構築。先行WSCの着想と本データの作成を分けた。 | [一次資料の照合](skill-proofreading/cluewsc2020/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/cluewsc2020/editorial-2026-10/changes.md) |
| The Pile | EleutherAIが22資源を組み合わせた言語モデル学習用コーパス。構成素材ごとの由来・権利も区別した。 | [一次資料の照合](skill-proofreading/the-pile/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/the-pile/editorial-2026-10/changes.md) |
| WikiFact | Liangらの研究で新規に構築した事実補完データ。Wikidata 2022年1月版は素材で、先行LAMAの形式とも区別した。 | [一次資料の照合](skill-proofreading/wikifact/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/wikifact/editorial-2026-10/changes.md) |
| Dyck Language | 形式言語としてのDyck、Suzgunら2019年の次記号予測研究、BIG-bench固定Dyck4、Stanford CRFMの補完生成器を区別。紹介する生成器の2022年公表と先行研究年を混同しない。 | [一次資料の照合](skill-proofreading/dyck/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/dyck/editorial-2026-10/changes.md) |
| Numeracy（多項式の規則推論） | Liangらの研究で設計した多項式規則推論の生成課題。Reuters由来のNumeracy-600Kとは別であり、題名にも範囲を明示した。 | [一次資料の照合](skill-proofreading/numeracy/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/numeracy/editorial-2026-10/changes.md) |
| MATH | HendrycksらがAMC/AIME等の競技問題とAoPSの解説から構築した2021年データ。別の数学事前学習データAMPSと区別する。 | [一次資料の照合](skill-proofreading/math/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/math/editorial-2026-10/changes.md) |
| CrossWOZ | 清華大学のZhuらが収集・注釈した中国語の複数領域対話。元対話・状態・行為と元評価を紹介する。 | [一次資料の照合](skill-proofreading/crosswoz/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/crosswoz/editorial-2026-10/changes.md) |
| Redefine | 課題提出者はXudong Shen。Inverse Scaling Prizeによる公開・評価と、後続の採用を区別した。 | [一次資料の照合](skill-proofreading/redefine/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/redefine/editorial-2026-10/changes.md) |
| Pattern Matching Suppression | 課題提出者はTomasz Korbak。Inverse Scaling Prizeによる公開・評価と、後続の採用を区別した。 | [一次資料の照合](skill-proofreading/pattern-matching-suppression/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/pattern-matching-suppression/editorial-2026-10/changes.md) |
| ICE — International Corpus of English | Sidney Greenbaumの提案を起点とする各地域チームの国際共同コーパス計画。1990年は開始年。 | [一次資料の照合](skill-proofreading/ice/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/ice/editorial-2026-10/changes.md) |
| Data imputation — Buy / Restaurant | 素材は既存のBuy/Restaurant照合用表。2021年のMeiらIPMと、2022年に公表された二表の言語モデル補完課題を区別し、題名と年の意味も明示した。 | [一次資料の照合](skill-proofreading/data-imputation/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/data-imputation/editorial-2026-10/changes.md) |
| エンティティ照合（DeepMatcherデータ） | Mudgal・Liらの2018年DeepMatcher研究で使った照合用データ集。元表、候補生成・ラベル、属性を移動するDirty変換と公開13設定を区別する。 | [一次資料の照合](skill-proofreading/entity-matching/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/entity-matching/editorial-2026-10/changes.md) |
| コードの再現（Linuxソース） | Liangら2022年研究の既存文字列再現課題。素材はLinuxソースで、コードの作成者・採取版・課題の設計を区別し、再現の一致と実用性・法的判断を混同しない。 | [一次資料の照合](skill-proofreading/copyright-code/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/copyright-code/editorial-2026-10/changes.md) |
| CHEF | Huらが構築した中国語の根拠付きファクトチェック。主張・根拠・真偽判定の元課題を説明する。 | [一次資料の照合](skill-proofreading/chef/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/chef/editorial-2026-10/changes.md) |
| CDial-Bias | Zhouらが構築した中国語会話と偏見態度のデータ。元注釈と元研究評価を中心にした。 | [一次資料の照合](skill-proofreading/cdial-bias/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/cdial-bias/editorial-2026-10/changes.md) |
| C³ | Sunらによる中国語読解問題データ。元の会話/文章、選択肢と知識注釈・評価を説明する。 | [一次資料の照合](skill-proofreading/c3/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/c3/editorial-2026-10/changes.md) |
| CLEVA | Li・Zhaoらの独立した中国語評価プラットフォーム。ユーザー指定に従い、基盤自体の設計と採用データ・独自構築を紹介する。 | [一次資料の照合](skill-proofreading/cleva/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/cleva/editorial-2026-10/changes.md) |
| Disinformation | CSETの2021年研究が原型。投稿継続にはその11入力を使用し、主張反復の見出し群と主張文はCRFM研究チームがMRFから構築した。 | [一次資料の照合](skill-proofreading/disinformation/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/disinformation/editorial-2026-10/changes.md) |
| RealToxicityPrompts | GehmanらのUniversity of Washington/AllenAI研究。OpenWebTextの文から入力と元の続きを作成し、検出器で採点。後続公開生成は元continuationと区別する。 | [一次資料の照合](skill-proofreading/realtoxicityprompts/editorial-2026-10/origin-attribution-check.json) / [変更対](skill-proofreading/realtoxicityprompts/editorial-2026-10/changes.md) |

確認した成果物と確認方法は、各記録のファイル照合値とページ範囲に対応する。旧版の全頁確認を継承した場合は、現行版との一致範囲と変更頁の再確認を明記している。
