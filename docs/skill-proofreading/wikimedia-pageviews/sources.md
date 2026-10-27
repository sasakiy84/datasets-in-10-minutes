# Wikimedia Pageviews sources and scope

Creator /root/wikimedia_coordinator/create_pageviews read the official current API home, concepts/page-views, reference/page-views, access-policy and unique-devices documents, Pageviews/hourly Wikitech documentation, dump README, pageview_complete README and legal terms. Sources were acquired by ordinary public HTTP with TLS/proxy preserved. Sources contain HTML and extracted text. The official API homepage screenshot was captured with CSS/fonts loaded and individually inspected. Its text is not claimed as OCR.

The current API reference states availability from 2015-07-01; hourly pageviews README states May 2015 onward. Pageview complete combines sources from December 2007 onward and is separately described in Appendix. The page_title field of hourly dumps is URL-decoded with spaces replaced by underscores; the API article request path is percent-encoded. The dump filename timestamp denotes the end of its UTC hourly window.

Actual data: two 30-day article series for Japanese Wikipedia, September 2025 UTC, all-access/user; three monthly access-method records for 富士山; four 30-day whole-project agent series; monthly top 1000. Values were summed locally and clearly scoped. Five additional article series returned HTTP 429 and were not retried or used; the appendix instead uses distinct records from the already captured top list. All published ranks retain API values, including possible tied ranks.

Hourly format: one compressed 256 KiB prefix of pageviews-20250901-010000.gz fetched with bounded streaming and Range, yielding 30,906 complete lines. The full file was not fetched. The displayed line af.m Adidas 1 0 occurs in that saved prefix. Its record describes the mobile site of Afrikaans Wikipedia during 2025-09-01 00:00–01:00 UTC. A percent-encoded anomalous record in the prefix was deliberately not used to misrepresent the documented normal title format.

Failed source discovery: Pageview_complete Wikitech candidates were 404; the actual official dump README succeeded. A guessed docs-host api-spec.json was 404 and was not used. Initial docs/screenshot HTTP 403 responses due to insufficient client identification were corrected by supplying the policy-compliant User-Agent; TLS verification stayed enabled. API extra1–extra5 429 responses remain raw evidence and are excluded from all analysis.

The minimal final native acquisition and aggregation snippets were executed with a single bounded public GET, substituting only the instructed User-Agent contact field. All 30 records matched the saved original sample. No model evaluations, external generation APIs or Gemini were used.

Analytics data are CC0 1.0, confirmed in access-policy and both dump READMEs; official documentation/screenshot is CC BY-SA 4.0 with attribution and links. Wikipedia article text/images are not relicensed by these statistical-data terms. No individual IP/user/session data were acquired.
