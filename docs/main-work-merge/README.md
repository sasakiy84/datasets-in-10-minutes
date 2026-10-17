# mainとworkの統合記録

統合元：`main` の `1d01310` と `work` の `edf3337`。元の校正記録は各コミット時点の成果物に対応し、本統合の最終ファイルは下記JSONのハッシュで識別する。

main側の追加実例・公式サイト画面・配置調整を基に、work側の文言校正、段落順、表の行順、図の差替え、左揃えを反映した。ページとPPTX内部パーツは本文で対応付けた。Geminiを含む外部生成APIの追加呼出しは0回。

Global PIQAでは、mainの実例差替えに伴い説明が更新済みのため、旧日本語例のLLM補助フラグに関する校正1件を適用しない。FineWebのサンプル説明は両側の同義の変更を短い表現に統合した。

| 資料 | ページ数 | 適用した文言変更対 | 検証記録 |
|---|---|---|---|
| arc-agi-2 | 71 | 23 | [JSON](arc-agi-2.json) |
| charxiv | 65 | 29 | [JSON](charxiv.json) |
| coco | 82 | 16 | [JSON](coco.json) |
| facts-grounding | 60 | 26 | [JSON](facts-grounding.json) |
| fineweb | 85 | 22 | [JSON](fineweb.json) |
| global-piqa | 64 | 15 | [JSON](global-piqa.json) |
| gpqa | 87 | 11 | [JSON](gpqa.json) |
| hle | 61 | 20 | [JSON](hle.json) |
| imagenet | 74 | 23 | [JSON](imagenet.json) |
| mcp-atlas | 68 | 28 | [JSON](mcp-atlas.json) |
| mmmlu | 57 | 2 | [JSON](mmmlu.json) |
| mmmu-pro | 66 | 18 | [JSON](mmmu-pro.json) |
| mrcr-v2 | 51 | 25 | [JSON](mrcr-v2.json) |
| omnidocbench | 63 | 19 | [JSON](omnidocbench.json) |
| osworld-verified | 65 | 13 | [JSON](osworld-verified.json) |
| scicode | 59 | 11 | [JSON](scicode.json) |
| screenspot-pro | 65 | 13 | [JSON](screenspot-pro.json) |
| simpleqa-verified | 53 | 17 | [JSON](simpleqa-verified.json) |
| snli | 72 | 25 | [JSON](snli.json) |
| squad | 109 | 37 | [JSON](squad.json) |
| swe-bench-pro | 66 | 27 | [JSON](swe-bench-pro.json) |
| swe-bench-verified | 62 | 11 | [JSON](swe-bench-verified.json) |
| tau2-bench | 69 | 13 | [JSON](tau2-bench.json) |
| terminal-bench | 71 | 12 | [JSON](terminal-bench.json) |
| ucf101 | 72 | 16 | [JSON](ucf101.json) |

全25資料で最終PPTXからPDFを出力し、ページ数・変更文言の存在・ZIP/XML・内部参照・表の文字領域・新規スキーマエラーを検査した。PowerPointデスクトップでの開封は未実施。
