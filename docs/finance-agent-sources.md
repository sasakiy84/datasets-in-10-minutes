# Finance Agent Benchmark — primary sources and verification

2026-10-22収集。外部生成APIと評価実行は使用せず、公開一次資料を読んで作成した。本文30頁は600秒の読了を想定した計画値で、実測ではない。

## Benchmark and versions

- Bigeard et al. (2025), Finance Agent Benchmark: https://arxiv.org/abs/2508.00828
- Vals AI (2025), Finance Agent: Public Validation: https://github.com/vals-ai/finance-agent/blob/main/data/public.csv
- Vals AI, Running Finance Agent Benchmark (2026-10-22参照): https://github.com/vals-ai/finance-agent
- Vals AI, Finance Agent v1.1 (2026-10-22参照): https://www.vals.ai/benchmarks/finance_agent
- Vals AI, Finance Agent v2 (2026-10-22参照): https://www.vals.ai/benchmarks/fabv2
- Vals AI, Finance Agent v2.1 (2026-10-22参照): https://www.vals.ai/benchmarks/fabv2-1

初期537問・公開50問から実例13件を選び、原問・参照回答・rubricの全項目を読んだ。モデルへの入力は質問と共通ツール指示であり、回答に必要な資料を検索して取得する。原問は各1頁に全文を保持し、日本語は翻訳、赤字は配布参照回答の翻訳（AMDは数値を表に整理）として区別した。

初期論文の全537問での分類平均/全問正解率、v1.1のテスト337問の公式Accuracy、v2/v2.1の必須条件付き部分点は区別する。v2は927問、現在のv2.1は926問で、問題・基準・審判の変更があり、版間の数値差をモデルの進歩として扱わない。

## Selected examples and corporate primary evidence

### finance-agent-public-6: Airbnbの財務責任者を調べる
Airbnbの2024年Form 10-Kの署名欄はElinor MertzをChief Financial Officerと記す。
- Airbnb (2025), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm

### finance-agent-public-9: Palantirの売上高成長率を計算する
2024/2023/2022年の売上高は2,865,507 / 2,225,012 / 1,905,871千米ドル。
- Palantir Technologies (2025), Annual Report 2024: https://investors.palantir.com/files/2024%20FY%20PLTR%2010-K.pdf

### finance-agent-public-2: TJXの実績を会社予想と比べる
2024-11-20公表Q3 FY2025 releaseはQ4税引前利益率予想10.8～10.9%。2025-02-26公表Q4 FY2025 releaseの実績11.6%。
- The TJX Companies (2024), Q3 Fiscal Year 2025 Results: https://investor.tjx.com/node/20606
- The TJX Companies (2025), Q4 Fiscal Year 2025 Results: https://investor.tjx.com/news-releases/news-release-details/tjx-companies-inc-reports-q4-and-fy25-results-q4-comp-store

### finance-agent-public-3: AMDの売上高予想の幅を比べる
各四半期の予想の中心値5.7/6.7/7.5/7.1billion、±0.3billion。
- AMD (2024), First Quarter 2024 Financial Results: https://ir.amd.com/news-events/press-releases/detail/1192/amd-reports-first-quarter-2024-financial-results

### finance-agent-public-16: Airbnbの売上高と予約額の比率
2024 revenue11102/GBV81784;2023 revenue9917/GBV73252;2022 revenue8399/GBV63212 (million USD)。
- Airbnb (2025), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm
- Airbnb (2024), Annual Report 2023: https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm

### finance-agent-public-20: Shift4の処理委託先への集中
Concentration Risk節の2文が配布Answerと一致。
- Shift4 Payments (2025), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm

### finance-agent-public-25: Microsoftの海外従業員比率
As ofJune30 2024 full-time228000 / US126000 / international102000。
- Microsoft (2024), Annual Report 2024: https://www.microsoft.com/investor/reports/ar24/index.html

### finance-agent-public-30: Dutch Brosの粗利益を予測する
2024 revenue1,281,015 / cost of sales940,886 / derived gross profit340,129 (thousand USD)。Projected2026grossprofit466.5722425million→467million。
- Dutch Bros (2025), Annual Report 2024: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001866581/75aa60bb-5c3f-4f9d-83fe-01d599729f46.html

### finance-agent-public-33: Cloudflareの販売チャネルを読む
2024 channelpartners337394thousand /20%; direct1312332 /80%。
- Cloudflare (2025), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1477333/000147733325000043/cloud-20241231.htm

### finance-agent-public-34: Uberの調整後EBITDAへの調整
2024 Form10K AdjustedEBITDA reconciliationの2023列 stockbasedcomp1935million。
- Uber Technologies (2025), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm

### finance-agent-public-40: Floor & Decorの既存店売上高
2024Q4 Comparable store sales decreased0.8%。
- Floor & Decor (2025), Fourth Quarter and Fiscal 2024 Financial Results: https://ir.flooranddecor.com/sec-filings/content/0001507079-25-000012/fnd-2024earningsreleaseex9.htm

### finance-agent-public-44: Airbnbの株式報酬費用を確認
2024 AdjustedEBITDAreconciliation Stockbasedcomp1407million。
- Airbnb (2025), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm

### finance-agent-public-19: Oracleの実効税率の変化
2024/2023 effective tax rate10.9%/6.8%。
- Oracle (2024), Annual Report 2024: https://www.sec.gov/Archives/edgar/data/1341439/000095017024075605/orcl-20240531.htm

AMDの四つの予想は各発表の翌四半期予想から照合した。追加一次資料:
- https://www.amd.com/en/newsroom/press-releases/2024-7-30-amd-reports-second-quarter-2024-financial-results.html
- https://ir.amd.com/news-events/press-releases/detail/1224/amd-reports-third-quarter-2024-financial-results
- https://ir.amd.com/news-events/press-releases/detail/1236/amd-reports-fourth-quarter-and-full-year-2024-financial-results

## Rights and scope
初期公開50問は論文のDataset SplitおよびAppendix BでCC BY 4.0とされる。コードのMIT Licenseとは別に記録した。新公開27問の条件へ一般化しない。LICENSE-DATA-CC-BY-4.0.txt、LICENSE-CODE-MIT.txtとATTRIBUTION-FINANCE-AGENT.txtを添付する。企業資料とサイト画像はそれぞれの発行元に帰属する。

原問・参照回答・rubricは固定CSVと完全一致を機械確認した。数値の根拠となる企業資料の該当節を読んで計算を再確認したが、全企業資料の全頁を読んだとは主張しない。選定候補0/42/45の時間依存・符号・参照回答不一致はdata-audit.jsonに残し、架空の例や黙ったgold修正で穴埋めしなかった。

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-finance-agent.pptx)・[PDF](../slides/datasets-in-10-minutes-finance-agent.pdf)。本編30頁、総62頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/finance-agent.json)・[校正の修正対](skill-proofreading/finance-agent.md)・[全ページ文言](skill-proofreading/finance-agent/pages.jsonl)・[最終検証票](skill-proofreading/finance-agent/review.json)。作成担当の引継ぎ票は独立確認前の記録として保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-DATA-CC-BY-4.0.txt](licenses/finance-agent/LICENSE-DATA-CC-BY-4.0.txt)、[LICENSE-CODE-MIT.txt](licenses/finance-agent/LICENSE-CODE-MIT.txt)、[ATTRIBUTION-FINANCE-AGENT.txt](licenses/finance-agent/ATTRIBUTION-FINANCE-AGENT.txt)。
