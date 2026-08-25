#!/usr/bin/env python3
"""Calculate a transparent opportunity score from JSON input."""
import argparse
import json

WEIGHTS = {
    "fundamentals": 0.25,
    "catalyst": 0.20,
    "technicals": 0.20,
    "valuation": 0.15,
    "regime": 0.10,
    "liquidity": 0.10,
}

def calculate(payload):
    factors = payload.get("factors", {})
    missing = [key for key in WEIGHTS if key not in factors]
    if missing:
        raise ValueError("Missing factors: " + ", ".join(missing))
    invalid = {key: value for key, value in factors.items() if key in WEIGHTS and not 0 <= float(value) <= 100}
    if invalid:
        raise ValueError("Factor scores must be between 0 and 100")
    gross = sum(float(factors[key]) * weight for key, weight in WEIGHTS.items())
    penalties = payload.get("penalties", {})
    penalty_total = sum(max(0.0, float(value)) for value in penalties.values())
    net = max(0.0, min(100.0, gross - penalty_total))
    tier = "strong" if net >= 80 else "watch" if net >= 65 else "mixed" if net >= 50 else "weak"
    return {"gross_score": round(gross, 2), "penalties": round(penalty_total, 2), "net_score": round(net, 2), "tier": tier}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="JSON file containing factors and optional penalties")
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as handle:
        print(json.dumps(calculate(json.load(handle)), indent=2))
