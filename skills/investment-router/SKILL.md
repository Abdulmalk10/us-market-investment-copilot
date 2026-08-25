---
name: investment-router
description: Routes broad U.S. equity investment research requests across market scanning, company analysis, earnings, recommendation, portfolio risk, thesis monitoring, and data-quality workflows.
---

# Investment Router

Use this as the entry point for broad or multi-step U.S. public-equity requests.

## Routing

- Market overview or ideas: use `market-radar`.
- One ticker or peer comparison: use `stock-deep-dive`.
- Earnings, news, or event setup: use `earnings-catalyst`.
- Buy/hold/avoid framing or trade plan: validate inputs, then use `recommendation-engine`.
- Holdings, sizing, drawdown, or exposure: use `portfolio-risk`.
- Monitor an existing thesis: use `thesis-tracker`.
- Conflicting, stale, or incomplete data: use `investment-data-quality` before conclusions.

For combined requests, establish market regime first, analyze candidates, validate evidence, then form a recommendation. Do not imply that separate skills are independent agents or that consensus exists unless distinct analyses were actually performed.

## Core rules

Read `../../references/evidence-policy.md` and `../../references/output-standard.md`. Read `../../assets/strategy-profile.yaml` unless the user supplies a different mandate.

Use current sources whenever claims may have changed. Separate reported facts, consensus estimates, calculations, and judgment. State the as-of time and market session for live prices. Never fabricate missing prices, filings, estimates, options data, or news. Never promise returns or execute transactions without an explicit supported tool and user authorization.
