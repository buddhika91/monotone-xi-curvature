#!/usr/bin/env python3
import argparse, csv
from pathlib import Path
import mpmath as mp
from monotone_xi_curvature.xi import K
from monotone_xi_curvature.derivatives import derivative

def K3(r):
    return derivative(K, mp.mpf(r), 3)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", default="0.001")
    parser.add_argument("--b", default="10")
    parser.add_argument("--h", default="0.01")
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--csv", default="data/K3_scan.csv")
    args = parser.parse_args()

    mp.mp.dps = args.dps
    a = mp.mpf(args.a)
    b = mp.mpf(args.b)
    h = mp.mpf(args.h)
    n = int(mp.ceil((b - a) / h))

    min_val = mp.inf
    max_val = -mp.inf
    min_r = None
    max_r = None
    rows = []

    for j in range(n + 1):
        r = min(a + j * h, b)
        val = K3(r)
        rows.append((j, r, val))
        if val < min_val:
            min_val = val
            min_r = r
        if val > max_val:
            max_val = val
            max_r = r

    print("=" * 88)
    print("SCAN K3(r)")
    print("=" * 88)
    print(f"dps: {args.dps}")
    print(f"interval: [{a}, {b}]")
    print(f"h: {h}")
    print(f"min K3: {mp.nstr(min_val, 40)} at r={mp.nstr(min_r, 30)}")
    print(f"max K3: {mp.nstr(max_val, 40)} at r={mp.nstr(max_r, 30)}")
    print(f"all negative on grid: {max_val < 0}")

    csv_path = Path(args.csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["j", "r", "K3"])
        for j, r, val in rows:
            writer.writerow([j, mp.nstr(r, 30), mp.nstr(val, 50)])

    print(f"wrote {csv_path}")
    print("=" * 88)

if __name__ == "__main__":
    main()
