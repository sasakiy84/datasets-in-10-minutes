# 原文・日本語訳の併記と説明文の見直し

更新日時：2026-10-17T15:34:43Z。全28資料を確認し、15資料を修正した。Geminiは使用せず、日本語校正・スライド制作・データセット紹介の各スキルをCodexが適用した。

本文枠80件と表セル14件、計94件の文言を修正した。全28資料の本文・表・グラフのXMLで「原著」の残存は0件。正式な文献タイトル、著者、出典URL、権利帰属、数値、引用原文を保持した。

39組の分離例を検討し、36組で原文と訳を同じページに配置した。21組は計算表・入出力例・解説も含めて統合し、15組は解説を別ページに残した。長文3組（GSM8K旧46–47、Global PIQA旧13–14、OSWorld旧14–15）は分割を維持した。既に原文と訳を併記していた例や、段落本文と質問など対象が異なる例は統合していない。

GSM8K旧40–41は新38に統合した。原文・日本語訳を18pt、計算表を19ptで保持し、出典との間隔を確認した。旧19の見出しは新17の「公開時の実験では解答を検証器で選んだ」に変更した。検証器のモデル実験を、問題データの作成工程と混同させない表現とした。

## 資料別の変更

|資料|ページ数（前→後）|文言変更|原文・訳の併記|記録|
|---|---:|---:|---:|---|
|charxiv|65→65|3件|0組|[変更対・ページ対応](charxiv.md)・[検証データ](charxiv.json)|
|coco|82→82|3件|0組|[変更対・ページ対応](coco.md)・[検証データ](coco.json)|
|facts-grounding|60→60|1件|0組|[変更対・ページ対応](facts-grounding.md)・[検証データ](facts-grounding.json)|
|fineweb|85→85|27件|0組|[変更対・ページ対応](fineweb.md)・[検証データ](fineweb.json)|
|global-piqa|64→53|3件|11組|[変更対・ページ対応](global-piqa.md)・[検証データ](global-piqa.json)|
|gsm8k|74→65|8件|12組|[変更対・ページ対応](gsm8k.md)・[検証データ](gsm8k.json)|
|hle|61→61|10件|0組|[変更対・ページ対応](hle.md)・[検証データ](hle.json)|
|humaneval|64→63|5件|13組|[変更対・ページ対応](humaneval.md)・[検証データ](humaneval.json)|
|imagenet|74→74|6件|0組|[変更対・ページ対応](imagenet.md)・[検証データ](imagenet.json)|
|osworld-verified|65→65|2件|0組|[変更対・ページ対応](osworld-verified.md)・[検証データ](osworld-verified.json)|
|snli|72→72|5件|0組|[変更対・ページ対応](snli.md)・[検証データ](snli.json)|
|squad|109→109|7件|0組|[変更対・ページ対応](squad.md)・[検証データ](squad.json)|
|terminal-bench|71→71|1件|0組|[変更対・ページ対応](terminal-bench.md)・[検証データ](terminal-bench.json)|
|ucf101|72→72|11件|0組|[変更対・ページ対応](ucf101.md)・[検証データ](ucf101.json)|
|vqa-v2|53→53|2件|0組|[変更対・ページ対応](vqa-v2.md)・[検証データ](vqa-v2.json)|

## 検証

15資料の全ページでPPTXとPDFの文字を照合し、変更した130ページを個別画像で拡大確認した。原文・訳・表・コード例の保持、見出し、本文と出典の間隔、編集可能なグラフとワークブック、利用中の画像、URLだけに付いたリンクを確認した。各資料のJSONに成果物と適用スキルのSHA-256を記録する。

既存のGemini校正記録・日本語校正記録は過去の版に対応する履歴として保持する。今回の改訂はそれらを上書きせず、このディレクトリに分けて記録した。旧→新ページ対応は統合した3資料の各記録にある。

## 確認した全資料

arc-agi-2、charxiv、coco、facts-grounding、fineweb、global-piqa、gpqa、gsm8k、hle、humaneval、imagenet、mcp-atlas、mmmlu、mmmu-pro、mrcr-v2、omnidocbench、osworld-verified、scicode、screenspot-pro、simpleqa-verified、snli、squad、swe-bench-pro、swe-bench-verified、tau2-bench、terminal-bench、ucf101、vqa-v2。
