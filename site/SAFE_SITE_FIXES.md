# Safe Site Fixes — 2026-08-26

This branch records the data-integrity and mobile reliability changes for the US Market Investment Copilot site.

## Critical fixes

- Live quote and analysis levels are treated as separate data with separate timestamps.
- A stale or inconsistent analysis cannot appear as Buy, Best Opportunity, or Second Best.
- Long setups must satisfy `Stop < Entry Low <= Entry High < T1 <= T2`.
- Analysis is invalidated when price diverges materially from the analysis anchor or entry zone.
- HPE's legacy ~$24 entry is intentionally invalidated rather than mechanically rescaled to the current ~$54 price.
- Quote freshness, source, and timestamp are visible.
- Failed quote refreshes are marked stale; last-known/cached prices are never silently labeled live.
- Finnhub API tokens must not be committed to source. They are stored only in browser local storage.
- Refresh requests are concurrency-guarded and use per-symbol error handling.
- Auto-refresh runs every five minutes while the page is visible.
- Manual refresh has loading/error state.
- Mobile navigation is fixed to the bottom, respects safe-area insets, and has real click handlers.
- Price alerts persist locally, request browser notification permission, and are checked after quote refreshes.
- The UI states clearly that reliable closed-browser background push requires a backend/push service.
- If no candidate passes all gates, the correct output is No Trade rather than recycling an old recommendation.

## Release artifact

The tested self-contained replacement is maintained as `pre-move-copilot-fixed.html` in the ChatGPT work output for this repair cycle. It contains no API secret.

## Validation performed

- JavaScript syntax check passed with Node.
- Mobile fixed-navigation guard present.
- Notification permission flow present.
- Five-minute refresh loop present.
- Stale-analysis gate present.
- HPE legacy entry is absent from executable recommendation data.
- No-Trade fallback present.
