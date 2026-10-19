# ICE 調査・制作記録

- 制作日: 2026-10-18 JST。作者 sasakiy84。日本語、native editable PPTXと最終PPTXから出力したPDF。49枚、本編28枚、予定黙読時間600秒（実測なし）。
- 公式名称: International Corpus of English。1990年開始。26チームという値は取得時の公式トップページの記載。
- 標準設計: 500×約2,000語、話し言葉300・書き言葉200。1990年以降、18歳以上、英語による教育などの採用条件。公式designページとNelsonの2002年manualで照合。
- 公式ページ: https://www.ice-corpora.uzh.ch/en.html 。ChromiumでCSS 2件・画像を読み込み、実画面を取得・個別目視。asset_failures=[]。

## 実例と版

本編3件、追加10件。India 12件は正規の公開GCS `crfm-helm-public/classic/benchmark_output/runs/v0.3.0/ice%3Asubset%3Dind%2Cmodel%3Dtogether_opt-175b/scenario_state.json` の実入力から、連続した短い冒頭範囲を選択した。HTML画面のrunリンクも各ページに表示。原コーパスのファイル名は公開runにないので推定しない。run IDとJSONパス、文字範囲、原文・訳、全文と抜粋のSHA-256をexamples.jsonに記録。空白のみ正規化して表示した。JSON内のrequest_statesの位置はリクエスト分割のためIDと一致せず、元JSONの実位置に照合済み。

USA 1件はHELM v0.3.0 ICEScenario docstringに公開された造幣局の実テキスト例。コード内の原範囲を抽出して照合。元ファイル名や全文は未提示なので推定しない。公開例の地域には偏りがあり、13件はコーパス全体の無作為標本ではない。

## ライセンスと取得制約

公式のGetting Accessは申請と教育機関メールによる資格確認を要求する。ライセンスPDFは “The Corpus must be used for non-profit academic research purposes only.”、著作権は原権利者に残ること、コーパス再配布禁止を明記する。出版物の短い引用は “only in a way which would be permitted under the fair dealings provision of copyright law” とする。ICEはCCライセンスのデータセットではない。公開HELM runも、元の利用条件から独立した自由再配布許諾とは扱っていない。

制限されたダウンロード領域、認証、パスワードや申請者資格を使わず、Stanfordの公開runと公開公式資料をHTTP200で取得した。本資料はInternational Corpus of EnglishとHELMに帰属する短い引用のみを含む。examples.jsonには全文を含めず、元JSONの位置とハッシュを残す。ローカルの `evidence/scenario-state.json`（約545MB）と `evidence/india-inputs.json`（500件全文）は検証用であり、repo・公開納品へコピーしない。資料全体や抽出500件を元コーパスの再配布物として公開しない。

他の正規公開例も調査した。UCL ICE-GBサンプルはHTTP403。Uganda公式ページは現配布窓口をBergenの担当者メールとして案内。Trinidad and Tobagoは非営利学術用途・再配布禁止の同意付き配布、Nigeriaは公式リンク先SourceForgeの公開配布一覧を確認。これらのコーパス本体は取得せず、HELM公開例の説明を優先した。manualの説明用例を実コーパスの独立レコードとして数えていない。

## HELM の条件と結果

Classic表示固定版v0.4.0（2023-11-17）、run suite v0.3.0。2系列: OPT-175B（2022）、text-davinci-003（2022）。地域はea/hk/ind/usa。stats.jsonのname={name:metric,split:test}のみを使用し、摂動条件なし。各1試行。language_modeling、max_train_instances=0、max_eval_instances=1000、max_tokens=0。本文はtest、references=[]。India 500、Hong Kong 500、East Africa 625、USA 200件。bits_per_byte値はstats.json、12本の元statsはevidence、exact specsはevidence/run-specs-selected.jsonに保存。

例: IndiaはOPT 0.793974...、davinci 0.895481...。スライドは小数第3位に丸めた。全runのprompt_truncatedも保存。長い文書の分割により、文書数とリクエスト数は異なる。2026モデル順位とはしない。

v0.3.0コードとキャッシュは一致。説明文の当初7地域に対して列挙は9地域。split=written/spokenの説明に対し実引数はcategory=S/W/...。HDRの性別処理はall、XLSはanyで、説明文の一律allと一致しない。これらはAppendixに具体的に説明。

## 検査

日本語校正: japanese-proofreading skillを各ページに適用。method/review_mode=skill_based_codex、gemini_used=false。実修正対4件、数式の符号・訳の編者注・料理の語注の内容修正も別記した。変える必要のない文に修正対は作っていない。

全49ページoverviewを確認し、全49ページを個別view_imageで拡大して目視した。原文・訳・表・公式画面・参考文献を全件確認。引用枠2件の不足をPDF文字境界で検出し、全26枠の上下余白を実描画に合わせた。変更後の7/9/11/20/28/38/40とタイトル変更6ページを再目視。

layout-auditは289段落・57セルの本文照合と境界を確認しissues=[]。標準XSDはマスター由来11件と整数buSzPctの既知差を分離し、新規エラー0。内部参照・図形ID・ZIP正常。native table 5、chart 0。URL-only runとPDFリンク47件は完全一致。notesなし。

独立レビュー（MS MARCO担当）でp39の称賛への応答の訳を指摘され、受けた称賛に値するかという意味へ修正した。原文は保持し、再PDF化・引用枠再調整・各監査・個別目視で確認した。

独立再計算でp21のEast Africa / text-davinci-003の丸め1件を修正（0.7635297830374674 → 0.764）。他7セルは元値との丸め一致を確認。

## 年のメタデータ

`year=1990`は公式トップページの “began in 1990” に基づくプロジェクト開始年であり、全地域共通のデータセット初公開年を意味しない。ICEは地域別の編纂・公開が続く共同計画で、単一の初公開年は今回確定していない。ギャラリーの項目名が「データセット公開年」である場合、1990を公開年と断定する表示は避け、共同計画の開始年という意味をdescription・注記に明記する。複数地域の公開年を架空の単一年へまとめていない。

## リポジトリの検証記録

[原レコード・出典・実行条件](data-audits/ice.json)、[実際の校正対](skill-proofreading/ice.md)、[全ページ文言](skill-proofreading/ice/pages.jsonl)、[自己検査・独立レビュー](skill-proofreading/ice/review.json)。


## 読者向け説明の改訂

[日本語・情報量の問題点と修正](skill-proofreading/ice/editorial-2026-10/findings.json)。細かな再現条件・原レコードの照合情報は従来の検証記録に保持し、紹介スライドから整理した。
