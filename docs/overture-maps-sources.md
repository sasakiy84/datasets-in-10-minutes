# Overture Maps — sources

Release 2026-10-21.0; accessed 2026-10-28 (JST). Initial dataset publication: 2023-07-26, separately from foundation establishment 2022.

- **client**: Overture Maps Foundation, n.d., Python Client. https://docs.overturemaps.org/getting-data/overturemaps-py/
- **site**: Overture Maps Foundation, n.d., Overture Maps. https://overturemaps.org/
- **catalog**: Overture Maps Foundation, 2026, Accessing the Overture Catalog. https://docs.overturemaps.org/getting-data/cloud-sources/
- **stac**: Overture Maps Foundation, 2026, Release 2026-10-21.0. https://stac.overturemaps.org/2026-10-21.0/catalog.json
- **gers**: Overture Maps Foundation, n.d., What is GERS?. https://docs.overturemaps.org/gers/
- **license**: Overture Maps Foundation, 2026, Attribution and Licensing. https://docs.overturemaps.org/attribution/
- **duckdb**: Overture Maps Foundation, n.d., DuckDB. https://docs.overturemaps.org/getting-data/duckdb/
- **initial**: Overture Maps Foundation, 2023, First World-Wide Open Map Dataset. https://overturemaps.org/announcements/2023/overture-maps-foundation-releases-first-world-wide-open-map-dataset/
- **schema**: Overture Maps Foundation, n.d., Schema Reference. https://docs.overturemaps.org/schema/
- **geo**: GeoParquet, n.d., GeoParquet Format Specification v1.1.0. https://geoparquet.org/releases/v1.1.0/

## Actual distribution and interpretation

The exact cloud files used are recorded in [data-audit.json](data-audits/overture-maps.json) and [map-manifest.json](skill-proofreading/overture-maps/map-manifest.json). The raw STAC and original Parquet metadata are kept privately in the creator workspace. We queried and inspected only the Kyoto subset; world totals come from STAC, not a local all-world scan. Source records retain their own update times, separate from release dates.

GeoParquet 1.1 CRS default confirmed with the actual file metadata; the raw geometry is WKB and local map drawing reprojects to EPSG:3857. The dataset collection defines geographic feature data, not a task or benchmark.

## Reproduction

`extract.py` selected actual published GeoParquet files by their STAC spatial extents, then filtered their bbox fields. `render_maps.py` drew the fetched geometries and attributes with Shapely, pyproj and Matplotlib, preserving polygon holes. No generative image tool, Gemini, or external generation API was used.

Official top screenshot has rendered CSS, branding, navigation and hero text; media/video/analytics resources were omitted. Screenshot and log succeeded before the 90-second process-close timeout; the image was opened and inspected.

## 最終配布物と確認記録

[PPTX](../slides/datasets-in-10-minutes-overture-maps.pptx)・[PDF](../slides/datasets-in-10-minutes-overture-maps.pdf)。本編31頁、総41頁。本編の流し読みは600秒の予定で、閲覧時間は未実測。

[原票・集計・出典の検証](data-audits/overture-maps.json)・[校正の修正対](skill-proofreading/overture-maps.md)・[全ページ文言](skill-proofreading/overture-maps/pages.jsonl)・[最終検証票](skill-proofreading/overture-maps/review.json)。作成担当の引継ぎ票と独立レビューの記録を保持し、最終承認は最終検証票に集約した。

同梱ライセンス・帰属情報：[LICENSE-ODbL-1.0.txt](licenses/overture-maps/LICENSE-ODbL-1.0.txt)、[LICENSE-CC-BY-4.0.txt](licenses/overture-maps/LICENSE-CC-BY-4.0.txt)、[LICENSE-CDLA-Permissive-2.0.txt](licenses/overture-maps/LICENSE-CDLA-Permissive-2.0.txt)、[LICENSE-Apache-2.0.txt](licenses/overture-maps/LICENSE-Apache-2.0.txt)、[LICENSE-CC0-1.0.txt](licenses/overture-maps/LICENSE-CC0-1.0.txt)、[NOTICE-Foursquare.txt](licenses/overture-maps/NOTICE-Foursquare.txt)。
