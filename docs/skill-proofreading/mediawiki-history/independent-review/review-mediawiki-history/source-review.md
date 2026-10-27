# Independent source preparation — MediaWiki history
Actor: /root/wikimedia_coordinator/review_pageviews (same actor, separately assigned second review).
Date 2026-10-28 JST.

Independently fetched and actually read: current official MediaWiki history overview, MediaWiki history dumps (including full schema detail and release changes), dump FAQ, page/user history reconstruction explanation, dumps README; Analytics datasets license confirmed separately on the official dump legal page during Pageviews source work (same actor).

Findings:
- These are revision/user/page event records; revision text is excluded. Do not confuse the dataset with full-text revision dumps.
- Monthly snapshots reconstruct the entire historical record. Current fields refer to snapshot time, historical fields to event time. Rename/move/revert information can change old rows, so simple incremental concatenation can be inconsistent.
- Three event entities use one denormalized schema; revision/create is an edit, while page/create and create-page are different creation concepts. User-only rows have no page information.
- Ordered schema detail table has78 fields, despite stale schema-overview prose saying76. Independently parsed exact detailed field order equals creator's schema.json. Change record explicitly says event_log_id and event_user_is_cross_wiki were added in2026-05.
- Public dump initial release2020-01, snapshot2019-12. Internal reconstruction/table history predates public dump release; no assertion that the dataset itself was invented in2020.
- TSV/bzip2 and empty nulls documented. Official old downloads README still describes arrays as array(...), whereas newer full schema page specifies comma-separated escaped arrays. Actual file must control the format explanation.
- Statistics/Analytics dataset CC0 is distinct from CC BY-SA documentation/screenshots.
- Reconstruction documentation explicitly prioritizes correctness over completeness when log histories conflict; the table is a reconstructed resource, not a guarantee of perfect complete histories.

Data check: independently parses all116,372 local records (file acquired by creator, not independently redownloaded); recomputes78-column widths/entity/type/year totals/range and finds all chosen example records by their actual fields. See data-check-summary.json for exact scope and results. Public usernames/IPs are not needed for the field-count/statistics check and are not emitted in this record.

Pending: no deck actual page viewing or final native/technical approval has yet occurred. No Gemini/generative API/model evaluation.
