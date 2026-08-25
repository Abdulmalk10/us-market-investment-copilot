# US Market Investment Copilot

A Codex plugin for research and decision support in liquid U.S. equities. It combines market regime, fundamentals, valuation, price action, catalysts, and portfolio risk while keeping facts, estimates, and judgments separate.

## Defaults

- Universe: NYSE and Nasdaq mid/large caps
- Horizon: 3–30 trading days
- Style: catalyst-driven swing ideas confirmed by fundamentals and technicals
- Excludes by default: OTC, penny stocks, microcaps, and illiquid securities
- Output: thesis, evidence, scenarios, entry conditions, invalidation, risks, and confidence

This plugin provides research, not personalized financial advice. It never guarantees returns or executes trades.

## Included skills

- `investment-router`: selects and coordinates the correct workflow
- `market-radar`: assesses regime and ranks candidates
- `stock-deep-dive`: complete company and security analysis
- `earnings-catalyst`: earnings, events, news, and expectation gaps
- `recommendation-engine`: converts validated research into a scenario-based view
- `portfolio-risk`: exposure, concentration, correlation, and sizing analysis
- `thesis-tracker`: monitors thesis evidence and invalidation conditions
- `investment-data-quality`: validates freshness, provenance, and consistency

Edit `assets/strategy-profile.yaml` to change the default universe and risk preferences.
