# VQA v2：出典と制作・校正記録

最新改訂：原文・訳の併記と説明文の見直し。現行53ページ。[変更対・ページ対応・検証記録](slide-language-review/vqa-v2.md)を参照。以下は初回制作時の記録を含む。

2026-10-17作成。本編30ページ、Appendix23ページ、合計53ページ。写真と英語の質問から短い答えを生成するVisual Question Answeringのversion 2を紹介する。本編は約10分の黙読・流し読みを想定し、Appendixを含む完全版PPTXと、同じ最終改訂から出力したPDFを収録する。閲覧時間は未実測。

## 一次資料と固定した版

|資料|用途・参照した版|
|---|---|
|[Making the V in VQA Matter](https://arxiv.org/abs/1612.00837)|Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, Devi Parikh, CVPR 2017。質問への偏り、24候補からの補完画像の選定、10人による回答、v1／v2の比較。|
|[公式サイト](https://visualqa.org/)・[配布](https://visualqa.org/download.html)・[採点](https://visualqa.org/evaluation.html)|2026-10-17確認。2017年4月のv2.0公開、各分割の実数、回答形式、画像と注釈の利用条件。公式トップページの実画面を掲載。|
|[公式VQA評価コード](https://github.com/GT-Vision-Lab/VQA)|`a013f0043c1e2cdc995922dfe257f7149aa9af06`。回答正規化とleave-one-outの得点。|
|[BLIP-2](https://arxiv.org/abs/2301.12597)|Junnan Li, Dongxu Li, Silvio Savarese, Steven C. H. Hoi, ICML 2023。Table 3のゼロショット、Table 5の微調整後の比較。|
|[LAVISのVQAタスク](https://github.com/salesforce/LAVIS/blob/main/lavis/tasks/vqa.py)|`05cb670f47296522e24e7727e366b4a997d28582`。2026-10-17に回答保存と検証集合の公式採点ツール利用を確認。|
|[COCO 2014注釈](https://images.cocodataset.org/annotations/annotations_trainval2014.zip)|ZIP中のcaptions_val2014.jsonを取得し、使用した14画像の元URL、寸法、ライセンスを照合。画像はCOCOのval2014から取得。|

公式のval質問、回答注釈、補完ペアを取得した。質問と注釈はquestion_id、写真とはimage_idで照合している。画像URL・SHA-256と14件の質問・回答を[検証データ](data-audits/vqa-v2.json)に保存した。

## 採点と性能値

公式の採点は、10人から1人を外し、残る9人に一致する数mからmin(m/3,1)を求め、10通りを平均する。10人中の一致件数が0／1／2／3／4以上のとき、得点は0／0.3／0.6／0.9／1。公式Python 2評価モジュールをlib2to3でPython 3へ機械変換し、採点ロジックを変更せず、0〜10件が一致する11条件を実行して確認した。

原著Table 1のMCBは、v1学習→v1評価60.36%、v1→v2 54.22%、v1と同規模のv2学習→v2評価56.08%、v2全学習データ→v2評価59.14%。いずれもvalで、学習・評価集合を行ごとに明示した。

BLIP-2論文Table 5では、VQAで微調整したモデルのtest-dev／test-standardを比較した。ALBEF 75.84%／76.04%、BLIP 78.25%／78.32%、BLIP-2 ViT-g OPT-6.7B 82.19%／82.30%。Table 3のゼロショット65.0%はViT-g FlanT5-XXLの別構成であり、同一モデルの微調整前後として扱っていない。testの正解は非公開でサーバ側で採点される。

## 規模と全件集計

公式v2.0の画像数はtrain82,783・val40,504・test81,434で204,721枚。質問数は443,757・214,354・447,793で1,105,904問。公開される回答注釈はtrain4,437,570・val2,143,540で各問10回答。testの正解は公開されていない。原著と現配布のtest概数との差について原因を推測していない。

valの214,354問を全件集計した。answer_typeはyes/no80,541、number28,134、other105,679。質問の単語数は空白区切りのsplit()、文字数は空白・記号を含むlen。母標準偏差はpstdev、分位点は昇順の位置round((n−1)×p)。単語数の階級4以下／5–7／8–10／11–13／14以上は35,103／134,416／37,994／5,662／1,179問。

回答の一致度の表は、各問の正規化前の回答文字列で最頻値の件数を数え、その件数で問題を分類した。1〜3件27,778問、4〜6件47,185問、7〜9件69,163問、10件70,228問。VQA accuracyそのものとは区別した。question_typeの表は公式メタデータの上位5区分で、独自の網羅的分類とはしていない。

## 掲載実例

本編は、落書きの有無を対比する1ペア（2レコード）、人数、視線の3つの問い。追加10問は本編と重複しない。合計14レコード、質問の内容として13例を示した。原文・日本語訳・人の最多回答と、その回答を書いた人数を対応させ、画像も実際に見て照合した。落書きのquestion_id28714002／426166003は、公式の補完ペアに登録されていることを確認した。

|区分|公式の識別子|内容|
|---|---|---|
|本編|28714002／画像 28714|壁の落書き：あり|
|本編|426166003／画像 426166|壁の落書き：なし|
|本編|131089002／画像 131089|人数を数える|
|本編|262148000／画像 262148|視線の向きを答える|
|追加例|393243003／画像 393243|髪の色を答える|
|追加例|393284003／画像 393284|スポーツの種類を答える|
|追加例|132024002／画像 132024|動作を答える|
|追加例|524621008／画像 524621|動物の種類を答える|
|追加例|262284003／画像 262284|部屋の種類を答える|
|追加例|262162016／画像 262162|物がないことを答える|
|追加例|524436003／画像 524436|何の上に座るかを答える|
|追加例|393288000／画像 393288|建物の種類を答える|
|追加例|262682015／画像 262682|場所を答える|
|追加例|200058000／画像 200058|服の模様を答える|

## 注釈・写真の出典と利用条件

質問・回答注釈は[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。出典はVQA TeamとGoyalらの原著。日本語訳と説明を追加した。写真の比率を保ち、トリミング・色変更・合成をせず掲載している。写真は個別のライセンスに従い、VQA注釈のCC BY 4.0を一括適用していない。

下表はCOCO 2014の公式メタデータと、取得できたFlickr oEmbedの作者・題名・URLを合わせたもの。Flickrから作者・題名を取得できなかった3件は、COCOメタデータにある元画像URLを保持し、作者名を推測していない。写真ごとの来歴と取得結果も検証データに残した。

|COCO画像ID|作者・題名（取得できた範囲）|出典|ライセンス|
|---|---|---|---|
|262284|geeksquadthe／Master Bedroom Bathroom Walk-In Shower - Village Lofts|[Flickr](https://www.flickr.com/photos/101095425@N08/9627540643/)・[元画像](http://farm8.staticflickr.com/7396/9627540643_b3ec7096c8_z.jpg)|[CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/)|
|200058|Bananaguay／Snow|[Flickr](https://www.flickr.com/photos/platano/2456758025/)・[元画像](http://farm3.staticflickr.com/2248/2456758025_77d425a95a_z.jpg)|[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/)|
|131089|riz94107／IMG_9593|[Flickr](https://www.flickr.com/photos/riz94107/4866736626/)・[元画像](http://farm5.staticflickr.com/4117/4866736626_297f0b22b9_z.jpg)|[CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)|
|524436|DarkB4Dawn／Istanbul|[Flickr](https://www.flickr.com/photos/darkb4dawn/6981041686/)・[元画像](http://farm8.staticflickr.com/7213/6981041686_5914368e78_z.jpg)|[CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/)|
|393243|取得できず／題名未取得|[Flickr](https://www.flickr.com/photo.gne?id=1562760533)・[元画像](http://farm3.staticflickr.com/2294/1562760533_6893778f46_z.jpg)|[Attribution-NonCommercial-ShareAlike License](http://creativecommons.org/licenses/by-nc-sa/2.0/)|
|262148|Ketil Johansen／Sk8 with boardshop & DC shoe|[Flickr](https://www.flickr.com/photos/litek/4549977479/)・[元画像](http://farm5.staticflickr.com/4028/4549977479_547e6b22ae_z.jpg)|[CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)|
|393288|ell brown／St John's RC Cathedral - Alfred Road, Portsmouth - statue - St John|[Flickr](https://www.flickr.com/photos/ell-r-brown/9324458628/)・[元画像](http://farm3.staticflickr.com/2806/9324458628_01b371c5e9_z.jpg)|[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)|
|393284|BlueLight1990／DCIM_1|[Flickr](https://www.flickr.com/photos/klingele/4872033447/)・[元画像](http://farm5.staticflickr.com/4093/4872033447_176d7158a6_z.jpg)|[CC BY-ND 2.0](https://creativecommons.org/licenses/by-nd/2.0/)|
|262682|J0nny_t／Kitchen|[Flickr](https://www.flickr.com/photos/j0nny_t/7556152056/)・[元画像](http://farm9.staticflickr.com/8022/7556152056_eff00ab722_z.jpg)|[CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/)|
|28714|取得できず／題名未取得|[Flickr](https://www.flickr.com/photo.gne?id=8614354814)・[元画像](http://farm9.staticflickr.com/8100/8614354814_eab96f3727_z.jpg)|[Attribution-NoDerivs License](http://creativecommons.org/licenses/by-nd/2.0/)|
|132024|Trong Ton／End of ski season|[Flickr](https://www.flickr.com/photos/trongton/8653774735/)・[元画像](http://farm9.staticflickr.com/8259/8653774735_470097c4aa_z.jpg)|[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)|
|262162|取得できず／題名未取得|[Flickr](https://www.flickr.com/photo.gne?id=4918042336)・[元画像](http://farm5.staticflickr.com/4136/4918042336_472817e6b6_z.jpg)|[Attribution-NonCommercial-NoDerivs License](http://creativecommons.org/licenses/by-nc-nd/2.0/)|
|524621|Valerio Pillar／DSC_4172.JPG|[Flickr](https://www.flickr.com/photos/vpillar/2873582007/)・[元画像](http://farm4.staticflickr.com/3114/2873582007_36ea66187d_z.jpg)|[CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)|
|426166|Rusty Darbonne／Blue Bike|[Flickr](https://www.flickr.com/photos/rustydarbonne/2319776213/)・[元画像](http://farm4.staticflickr.com/3052/2319776213_ced79b883c_z.jpg)|[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)|

## 日本語校正と表示の確認

日本語の校正には、[日本語校正スキル](../.agents/skills/japanese-slide-proofreading/SKILL.md)をCodexで適用した。Geminiや外部の文章生成APIは利用していない。ページごとの確認は`docs/skill-proofreading/vqa-v2/pages.jsonl`、修正前後の対は同ディレクトリの`changes.tsv`、最終検査とSHA-256は`review.json`に保存する。新規に作成した資料の初稿からの変更であり、既存資料へのGemini提案の再利用記録とは区別した。

共通マスターを保持し、日本語はNoto Sans CJK JP、欧文はNoto Sans、コードはLiberation Mono。長い説明は左揃えの通常文とし、表・グラフ・コード・引用の文字は編集可能にした。写真・公式サイトの画面だけは画像として配置する。

全ページの一覧に加え、各ページを900×506相当の拡大画像で順に確認した。最終の調整ページも再出力して確認。PPTXとPDFのページ数・段落、タイトルの1行表示、ページ外の文字、表セル内の収まり、本文と出典の8pt以上の間隔、引用・コード枠、URLだけへのリンクを検査した。グラフの値は内蔵Excelブックと照合した。

ZIP整合性、XML解析、内部参照、図形IDの重複を検査し、標準OOXML XSDとの照合でマスター由来の既存差分と箇条書き百分率の字句形式差を分離した。整数形式のbuSzPctは25000〜400000の範囲を別途検査した。新規の構造エラーはない。PDFはLibreOfficeで出力した。デスクトップ版PowerPointでの実機確認や、新しいモデルのベンチマーク実行は行っていない。

## 2026-10-18：正解表示と出典表現の再確認

正解の読みやすさ・個人の好みのえんじ色と、本文の図表番号を確認した。原文・訳・正解値・統計値・評価条件・ページ数を保持。Codexによるスキル適用、Gemini使用なし。[変更対と最終版の検査](skill-proofreading/vqa-v2/answer-style-review.json)。
