# Market Investment Copilot

Personal investment-research plugin for U.S. and Saudi equities. It combines market regime, fundamentals, valuation, earnings and catalysts, technical context, and portfolio risk while keeping facts, estimates, and judgments separate.

## Default strategy

- Primary universe: liquid U.S. mid-cap and large-cap equities
- Secondary universe: Saudi equities and Saudi market monitoring
- Typical horizon: roughly 1 month
- Style: catalyst-driven opportunities confirmed by fundamentals, valuation, market context, and technical structure
- Priority: risk-adjusted upside rather than maximum theoretical upside
- Excludes by default: OTC, penny stocks, microcaps, and illiquid securities unless explicitly requested

## What it does

- Scans and ranks stock opportunities
- Performs full single-stock deep dives
- Analyzes earnings, guidance, catalysts, valuation, and technical context
- Reviews portfolio concentration and risk
- Explains Saudi-market drivers and material disclosures
- Builds bull / base / bear scenarios
- Defines entry logic and thesis invalidation
- Treats social-media stock ideas as leads requiring independent verification

## Tracked idea sources

Ideas from tracked social accounts are labeled by source and independently verified before they influence a conclusion.

Examples include:
- @BinDollarSign
- @TriggerTrades
- @shabancrypto
- @Badr9577
- @TrendSpider
- @OpSniper_11
- @chartFBM
- @alawall99
- @BullTrader0
- @dahayyan1
- @hoo0t_p

## Plugin structure

- `.codex-plugin/plugin.json` — plugin metadata and ChatGPT/Codex interface definition
- `skills/market-investment/SKILL.md` — core investment-research workflow, scoring, risk framework, and response behavior

## Opportunity scoring

The core skill can rank opportunities on a 100-point framework covering:
- Fundamental quality
- Earnings / estimate momentum
- Catalyst strength and timing
- Valuation / upside asymmetry
- Technical setup
- Market / sector alignment
- Risk quality / downside control

This plugin provides investment research and decision support. It does not guarantee returns or conceal material downside risks.
