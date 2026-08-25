# Opportunity scoring

Score each available factor from 0 to 100, then apply weights:

- Fundamental quality and revisions: 25%
- Catalyst strength and timing: 20%
- Technical and relative-strength confirmation: 20%
- Valuation and expectation gap: 15%
- Market and sector alignment: 10%
- Liquidity and tradability: 10%

Apply explicit penalties after the weighted score: binary-event risk up to 15 points, crowding or gap risk up to 10, accounting/governance concern up to 20, and poor data quality up to 25.

Interpretation: 80–100 strong research candidate; 65–79 watch/conditional; 50–64 mixed; below 50 weak. A high score is not a recommendation. Missing inputs reduce confidence and must not be treated as neutral values. Use `scripts/opportunity_score.py` for repeatable calculations.
