# 国土地理院DEM — 一次資料と取得範囲

取得・参照日：2026-10-28 JST。Gemini・外部生成API・モデル評価は使用していない。

- **help**: https://service.gsi.go.jp/kiban/app/help/
  DEM種類、測量方法、角度の格子、精度条件、配布と利用者登録を実読。
- **tile**: https://maps.gsi.go.jp/development/demtile.html
  TXT256×256、東・南方向、単位m、e欠測、PNG復号式を実読。
- **make**: https://maps.gsi.go.jp/development/hyokochi.html
  最大ズーム4点の線形平滑、縮小時4点平均、元DEMとの違いを実読。
- **catalog**: https://maps.gsi.go.jp/development/ichiran.html
  標高タイル節のみ実読。dem=DEM10B、TXT更新停止2024-10を確認。
- **spec**: https://service.gsi.go.jp/kiban/contents/screen/basismap/documents/FGD_DLFileSpecV5.3.pdf
  5.3版のDEM区画・構成点・格子・配列順・欠測と座標参照系の節を実読。
- **height**: https://www.gsi.go.jp/sokuchikijun/hyoko2024rev.html
  標高改定2025-04-01、水平位置、JGD2024と高さの区別の該当節を実読。
- **qa**: https://www.gsi.go.jp/sokuchikijun/hyoko2024rev-QA.html
  Q3-4/3-5を実読。2025-07-31反映、1A/5A/5B/5C対象、10A/10B非対象。
- **history**: https://service.gsi.go.jp/kiban/app/data_update_info_all/
  2008-04-01記録を実読。5mレーザ/写真、24火山10m等の提供開始。
- **terms**: https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html
  PDL1.0適用・出典・加工表示・測量成果等の利用条件を実読。
- **pdl**: https://www.digital.go.jp/resources/open_data/public_data_license_v1.0
  PDL1.0公式本文の取得・保存。

## 実データ

公開TXT18タイルをすべて256行×256列の配列として解析。元の配布GMLは取得していない。GMLの構造は公式仕様5.3の説明であり、取得した原GMLレコードとは呼ばない。fgd.gsi.go.jp旧URLはプロキシCONNECT403だったため迂回せず、現行公式service.gsi.go.jpの公開ヘルプと仕様へ進んだ。

rawと描画コードは制作環境に私有保持。公開記録には範囲・URL・値・方法を残す。map-manifest.jsonの入力bboxと表示crop bboxを区別する。
