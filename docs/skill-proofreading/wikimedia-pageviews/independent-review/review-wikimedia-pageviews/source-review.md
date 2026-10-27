# Independent source review — Wikimedia Pageviews
Actor: /root/wikimedia_coordinator/review_pageviews. Date: 2026-10-28 JST.

Independently fetched and read, rather than inheriting the creator's checks:
- `Research:Page view` (Meta; current definition, public/private derivation, UTC, exclusions; the current document includes historical fields and change history).
- Current Analytics API homepage, page-view reference, concepts, access policy, and its live OpenAPI JSON specification. The reference HTML itself is a shell for client-rendered specs; the raw official reference source supplies the exact specification URL.
- Current Pageview hourly schema and introduction (private Hive dataset; no implication that its geography/referer fields are exposed by the per-article API).
- Analytics pageviews dump README, pageview_complete README, and dump legal page, in full.
- Privacy policy: inspected passages on aggregated/non-personal public datasets and confidentiality of IP/browsing information; not a claim to full legal-policy review.

Key findings communicated to creator:
1. Current per-article and aggregate `agent` enums are all-agents/user/spider/automated. `bot` is not a valid current parameter. `spider` means self-identified bot; `automated` is other heuristic-detected automated traffic. `user` is a request classification and does not guarantee one person per request.
2. API data begin 2015-07-01; underlying/private table and ordinary hourly dumps go back to 2015-05. Pageview_complete begins 2007-12 using several historical sources, so its whole span is not uniformly the present definition.
3. API and Analytics dump statistics are CC0 1.0. Website documentation has its own CC BY-SA footer; screenshots and quotations must distinguish that from statistical data.
4. API requires an identifiable User-Agent. Serial requests are recommended. Requests without one initially returned 403 for three documentation pages; identifying UA fixed this, with no TLS/proxy bypass.
5. Public per-page aggregates do not expose individual readers or browsing histories. Private pageview_hourly includes country/city/referer/user-agent dimensions; its schema is documentation, not public raw data.
6. Redirect titles and moves matter for title time series; the current concepts explicitly say alternate-spelling redirect requests are not counted toward the actual target's views.

Independent bounded real-data check:
`per-article/ja.wikipedia/all-access/user/富士山/daily/2025090100/2025093000` independently fetched (30 daily records). Exact record equality to creator's raw/fuji.json. Sum 24,611 views, maximum 2025-09-01 = 1,669 views. This is a fixed historical month, not current popularity. Native timestamp field is YYYYMMDDHH, UTC.

No Gemini/external generative API/model evaluation. Normal public HTTP only. Acquisitions saved with status/bytes/SHA, including initial recoverable 403 conditions in the execution log. No giant dumps fetched.
