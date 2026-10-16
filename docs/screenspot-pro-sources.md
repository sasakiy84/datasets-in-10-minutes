# ScreenSpot-Pro：出典と確認範囲

2026-10-16作成。日本語「datasets in 10 minutes」。本編35枚＋Appendix30枚、計65枚。専門ソフトの画面と操作指示から対象位置を予測するGUI groundingを、実例・採点・作成方法・分布・現在の利用から紹介する。作成者sasakiy84、所属欄なし。本編の黙読・流し読みは、入口30秒、課題と実例175秒、評価145秒、作成と全体像150秒、系列と利用100秒、計600秒を想定する。閲覧時間は未実測。

## 選定と現行モデルでの利用

[OpenAI, GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)の公式ページで、ScreenSpot-Pro（no tools）のGPT-6 Astra 92.7%、GPT-5.6 Sol 76.9%、Claude Fable 5欄87.3%を確認した。脚注17はFableの値について、安全策を減らしたMythosの結果と指定する。スライドのモデル名・表注にこの構成を反映した。APIによるモデルの再評価は実施していない。

この公式ページは同日先行するデータセット調査で取得した保存版を参照した。本作業で同URLを再取得した際はHTTP 403だった。公表値の確認と、今回新たにライブ取得できた資料の範囲を区別する。

当初候補のBrowseCompは、論文が例題のオンライン再掲載を避けるよう求めるため、実例付きで公開する本シリーズには採用しなかった。ScreenSpot-Proは公開データカードにMIT Licenseの表示があり、正解領域と画像の対応を確認できた。

## 一次資料と版

- Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua (2025). *ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use*. [著者公開PDF](https://likaixin2000.github.io/papers/ScreenSpot_Pro.pdf)。同PDFを著者の公開GitHub Pagesリポジトリから取得した。20ページの版で、表紙はPreprint / Under review。
- [公式評価コード](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding)：改訂`dbe00114bc53a32c61c1a267786da85967710da8`。READMEの初公開日は2025-01-04。引用指定の掲載先はWorkshop on Reasoning and Planning for Large Language Models。GitHubの著者名表記と論文・データカードの著者表記に差がある箇所は、論文表紙のZiyang Mengを採用した。
- [公式データ](https://huggingface.co/datasets/likaixin/ScreenSpot-Pro)：改訂`210e78d3844251110bff86c95835ebd37a6930fa`、APIのlastModifiedは2026-03-18。26個のJSON注釈を同じ改訂で取得した。認証・利用申請は不要の公開状態。
- [Cheng et al. (2024), SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)：ScreenSpotの先行研究。arXivの書誌メタデータで正式タイトル・著者を照合した。
- [Wu et al. (2024), OS-Atlas: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)：ScreenSpot-v2。公式OS-Atlas READMEとScreenSpot-Pro論文で、先行データの注釈修正との関係を確認した。

公式GitHubをブラウザーで撮影し冒頭に掲載した。外部CSSの一部は取得できず、標準書式で表示されている。

## 実例：論文画像と公開注釈の対応

画像配布の大容量ストレージへの接続は環境の経路でCONNECT 403になったため、論文PDFに埋め込まれた元解像度のJPEGを取り出した。画像は著者が正解枠・矢印・拡大図を加えた例示画像であり、注釈なしのモデル入力とは呼ばない。スライドにも「論文の例示画像（正解枠・拡大図を含む）」と表示した。画像サイズ・正解座標・指示文・対象種別は公開JSONへ対応させた。左右に元の例示画像と正解位置の拡大を並べ、PPTX内の画像クロップと編集可能な四角形を使った。

|掲載先|注釈ID|画像の出所（論文ページ）|
|---|---|---|
|本編1|`vscode_macos_0`|18|
|本編2|`blender_windows_61`|18|
|本編3|`powerpoint_windows_67`|19|
|追加1|`davinci_macos_10`|18|
|追加2|`fruitloops_windows_4`|18|
|追加3|`unreal_engine_windows_21`|18|
|追加4|`premiere_windows_47`|18|
|追加5|`vmware_macos_26`|19|
|追加6|`macos_common_macos_9`|19|
|追加7|`linux_common_linux_29`|19|
|追加8|`origin_windows_46`|19|
|追加9|`quartus_windows_26`|19|
|追加10|`fruitloops_windows_53`|3|

論文の文末のピリオドなどとJSONの指示文が異なる例は、表示する原文にJSONを使った。全13画像で画面サイズが注釈と一致し、同じ位置の対象を確認した。13件について、公式`eval_sample_positive_gt`関数で中心点・境界点がcorrect、左端の1 px外がwrongとなることを検証した。エージェントを起動したり、実アプリを操作したりしていない。

## 統計とモデル結果

集計対象は固定した公開改訂の全1,581レコード。画像名とIDはいずれも1,581種類。23アプリとOS共通3環境、計26環境である。分野はJSONのgroup、OSはplatform、対象の種類はui_typeを集計した。

- 6分類：Creative 341、Dev 299、CAD 261、Scientific 254、Office 230、OS 196。
- OS：Windows 927、macOS 604、Linux 50。
- 対象：text 977（61.8%）、icon 604（38.2%）。論文のtext 62.6%と現行注釈の比率は一致しないため、資料の分布は公開改訂からの集計と明示した。原因は未確認。
- 画面サイズは14種類。2,560 × 1,440が514件、3,840 × 2,160が270件、3,840 × 1,080が181件、3,456 × 2,234が161件、2,160 × 1,440が99件、残る9種類が356件。Appendixに全14種類と全26環境の件数を掲載した。
- 対象面積比は`(x1-x0)*(y1-y0)/(width*height)*100`。全1,581件の平均0.065084%、中央値0.035494%。VS Codeの例は30 × 36 px、画面の約0.025%。公開座標はそのまま使い、`inventor_windows_60`のy0=-1も黙って補正・除外していない。この例はスライドの実例には選んでいない。
- 初期の直接予測：OS-Atlas-7B 18.9%、UGround-7B 16.5%、GPT-4o 0.8%。英語の指示。
- 探索付き：OS-Atlas-7BのReGround 40.2%、GPT-4oを計画役とするScreenSeekeR 48.1%。OS-Atlasのtext 28.1% / icon 4.0%、ScreenSeekeR 64.1% / 22.4%。中国語のOS-Atlas-7Bは16.8%。いずれもLiらの論文に対応させ、現行モデルの別表と分けた。

## 制作・表示検査

共通SlideMaster.pptxを継承。表紙52 pt太字、英数字Noto Sans、日本語Noto Sans CJK JP、緑帯14 pt太字、コードLiberation Mono。表15個とグラフ2個は編集可能。表罫線は上端・下端1.2 pt、見出し下0.6 pt。発表者ノートなし。

最終65ページを描画し、全ページのコンタクトシートと実例を確認した。段落・セルの文字欠落、ページ外への文字のはみ出し、通常タイトルの折り返しはいずれも0件。全177セルの実文字境界が行・列の領域に収まり、表注との間隔は12 pt以上、本文と出典は8 pt以上。リンク55件はURLのみがリンク領域であることをPDFでも照合した。引用画像の注釈とクロップ、表紙・目次・章扉の配置、参考文献ごとのまとまりも確認した。

ZIP整合性・内部参照・ノート不在・表罫線を確認。PresentationML・DrawingML・図表の82 XMLパーツを未変更のISO/IEC 29500-4 XSDで照合し、`buSzPct`の整数表記に関する既知の字句差133件、その他のエラー0件。全133値は公式Open XML SDKの定義域25000〜400000内。PowerPointデスクトップでの手動編集は未確認。

ギャラリーは初公開年2025、種別「画像」、タスク「エージェント操作」で登録し、新しいラベルは増やしていない。

## ライセンス表示

公式データカードはMITを指定する。公式リポジトリの[LICENSE](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding/blob/main/LICENSE)の表示を以下に保持する。

MIT License

Copyright (c) 2026 Kaixin Li

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
