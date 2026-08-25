---
name: market-radar
description: Assesses the current U.S. equity market regime and screens liquid mid- and large-cap stocks for catalyst-driven opportunities over roughly 3–30 trading days.
---

# Market Radar

Read `../../references/evidence-policy.md`, `../../references/scoring-framework.md`, and the strategy profile.

1. Timestamp the analysis and identify whether the market is open, premarket, after-hours, or closed.
2. Assess index trend, breadth, volatility, rates, dollar, credit conditions, sector leadership, and the near-term event calendar.
3. Build candidates from liquid NYSE/Nasdaq mid- and large-caps. Apply user constraints before ranking.
4. For each candidate, verify liquidity, upcoming catalysts, relative strength, earnings trend, valuation context, and major risks.
5. Rank with the scoring framework. Do not hide missing factors inside a numerical score.
6. Return a short ranked list, why now, trigger, invalidation, catalyst date, key risk, and confidence. Include a watchlist tier for promising but unconfirmed names.

Avoid selecting only recent winners. Include crowdedness, gap risk, and regime sensitivity. A scanner result is a research shortlist, not a recommendation.
