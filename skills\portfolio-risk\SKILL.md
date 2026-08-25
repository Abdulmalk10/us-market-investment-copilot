---
name: portfolio-risk
description: Reviews a U.S. equity portfolio for position, sector, factor, catalyst, liquidity, correlation, drawdown, and scenario risk and proposes risk-aware sizing changes.
---

# Portfolio Risk

Require holdings, weights or market values, cash, and base currency; use clearly labeled assumptions if some are absent. Never infer authorization to trade.

Measure concentration by name, sector, industry, factor, catalyst date, and correlated business exposure. Review beta, volatility, liquidity, drawdown, downside scenarios, and aggregate exposure. Flag hidden duplication such as multiple stocks driven by the same commodity, rate, AI-spending, or consumer factor.

Use `../../scripts/position_size.py` for deterministic risk-budget calculations when applicable. Treat volatility and correlation estimates as sample-dependent. Provide current risks, scenario losses, proposed limits or sizing ranges, and the data needed to improve confidence.
