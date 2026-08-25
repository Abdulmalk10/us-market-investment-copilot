#!/usr/bin/env python3
"""Calculate position size from portfolio risk budget and stop distance."""
import argparse
import json

def calculate(portfolio_value, risk_pct, entry, stop):
    values = [portfolio_value, risk_pct, entry, stop]
    if any(value <= 0 for value in values) or entry == stop:
        raise ValueError("Values must be positive and entry must differ from stop")
    risk_budget = portfolio_value * risk_pct / 100
    risk_per_share = abs(entry - stop)
    shares = int(risk_budget // risk_per_share)
    return {
        "risk_budget": round(risk_budget, 2),
        "risk_per_share": round(risk_per_share, 4),
        "shares": shares,
        "position_value": round(shares * entry, 2),
        "position_pct": round(shares * entry / portfolio_value * 100, 2),
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--portfolio-value", type=float, required=True)
    parser.add_argument("--risk-pct", type=float, required=True)
    parser.add_argument("--entry", type=float, required=True)
    parser.add_argument("--stop", type=float, required=True)
    args = parser.parse_args()
    print(json.dumps(calculate(args.portfolio_value, args.risk_pct, args.entry, args.stop), indent=2))
