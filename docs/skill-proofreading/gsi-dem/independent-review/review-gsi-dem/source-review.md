# 国土地理院DEM 独立一次資料・データ確認

Reviewer: /root/maps_coordinator/review_gsi_dem. 2026-10-28 JST. Gemini/外部生成APIは未使用。

自分で AGENTS.md、BRIEF.md、master-guided-slides、dataset-introduction-slides、日本語校正スキル全体、および指示127/128を読了。

## 独立取得・実読範囲

- demtile.html: 本文全体。TXT 256行×256列、東X/南Y、単位m、小数第2位、e欠測。RGBは符号付き24bitの0.01m、RGB128,0,0欠測。仕様上のTXT/PNG同値説明はあるが、root観測の別tile不一致を受け現行全tile同値保証へ一般化しない。
- hyokochi.html: 本文全体。地表面で建物/高架橋の高さではない。水部の欠測/値の性質。最大zで最寄4標高点の線形平滑化、小zで上位4画素平均。基盤GML元格子とは異なる。DEM1A/5A/5B/5C/10B/DEMGM、地理院地図の精度優先参照。
- 基盤地図情報ダウンロードサービスhelp: 利用登録、DEM説明、種類表、更新、schema/仕様リンクの各節。DEM1A/5Aレーザ0.3m（点なし2m）、5B写真20cm/0.7m、5C写真40cm/1.4m、10A火山等高線2.5m、10B全国等高線5m。基盤元格子間隔は1/5/10m程度の経緯度格子。
- FGD_DLFileSpecV5.3.pdf: 全60頁取得、実読はDEM区画p15–18/PDF21–24、座標p46/PDF52および改訂表の該当項目。最新仕様2026-07-31。DEM範囲/low-high/配列開始と省略/Linear +x−y/データなし−9999。GML座標JGD2024 (B,L)=緯度経度、fguuid:jgd2024.bl。全60頁読了とはしない。
- height.html: 概要/標高改定背景、衛星測位による標高/東京湾平均海面、成果表変更、登録情報を実読。2025-04-01測地成果2024改定、水平値は変更なし。DEMタイルが全版一律改定済みとは断定しない。サイト全文は取得済みで、すべての連結先PDFは未読。
- terms.html: 2025-11-20改正のコンテンツ利用条項全体を実読。PDL1.0、出典・加工表示、第三者条件、測量法による個別制約。地図画像帰属は加工表示とURLを含む。

## 独立データ取得

rawcheck.pyを自分で作成実行し、creatorの取得一覧にある京都z14=9tiles、富士z13=9tilesのすべてを再取得。18/18でcreator raw bytesが一致。各256²、valid65536、今回欠測0。raw-check.jsonに個別hash/headers/min/max/中央点/bboxを記録。原データ18枚から配列を解析済み、図はまだこの時点で実見していない。

## 描画コード読解（最終版確認前）

render_maps.pyを自分で読解。3×3mosaicしてからgradient、NaN保持、中心緯度cosでWebMercator距離を近似地上m化。北が上、断面は表示範囲最高値の行。tileごとgradient/0埋めはない。局所距離近似の誤差は狭い描画範囲内の緯度差に対応し、正確投影と誤称していない。

追加実読: 公式 hyoko2024rev-QA.html A3-1–A3-5。標高改定反映DEMは2025-07-31提供、改定対象1A/5A/5B/5C、10A/10B/50mは許容精度から改定しない。全QA全文読了とはしない。creatorへAppendixを対象固有の差へ整理する提案を送付。

mapcheck.pyを自分で作成実行。独自18raw組立とcreator保存npyが全要素一致。mosaic全域最高値は富士3772.96m(row459,col465)、京都241.93m(row524,col739)。中心緯度cos近似の緯度変化による最大距離尺度差は富士0.067%、京都0.033%。人工的な0埋めやtile別gradientはコード上なく、seamの隣接変化は全域通常隣接変化の最大値以下。raw/map-manifestの図SHAもその時点で全6件一致。最終図とスライドの一致は別途確認予定。

公式ichiran.htmlの標高タイル節4643–4670行相当を自分で実読。dem/TXTはDEM10B由来、標高タイル提供開始2013-10-30、TXTは2024-10以降更新停止。元基盤DEMシリーズの開始年は独立取得updates.htmlの2008-04-01節で確認（航空5m京都等/写真5m/10m24火山/50m全国）。一覧全文や更新履歴全文を読了したとはしない。
