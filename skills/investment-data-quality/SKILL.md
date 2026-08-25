---
name: investment-data-quality
description: Validates U.S. equity research inputs for identity, freshness, provenance, period consistency, corporate actions, conflicting values, and suitability for investment conclusions.
---

# Investment Data Quality

Audit before relying on a dataset or conflicting sources.

Check ticker/security identity, timestamps and timezone, regular versus extended-hours prices, units and currency, split adjustments, fiscal periods, GAAP versus non-GAAP definitions, point-in-time availability, survivorship bias, missing observations, and source provenance.

Prefer SEC filings and issuer materials for reported company facts; official macro/regulatory sources for economic and legal claims; exchange or established market-data sources for prices; and clearly identified providers for consensus estimates. Reconcile differences when possible and preserve both values when definitions differ.

Return usable, usable with caveats, or not usable. List blocking issues separately from non-blocking limitations. Never silently fill gaps with invented data.
