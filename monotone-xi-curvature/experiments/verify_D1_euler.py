#!/usr/bin/env python3
import argparse, csv
from pathlib import Path
import mpmath as mp
from monotone_xi_curvature.euler_region import scan_D1, D1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", default="1.000001")
    parser.add_argument("--b", default="2.067")
    parser.add_argument("--h", default="0.001")
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--csv", default="data/D1_euler_scan.csv")
    args = parser.parse_args()

    result = scan_D1(args.a, args.b, args.h, args.dps)

    print("=" * 88)
    print("EULER REGION: VERIFY D1(s)>0 ON 1<s<=2.067")
    print("=" * 88)
    print(f"dps: {args.dps}")
    print(f"interval: [{args.a}, {args.b}]")
    print(f"h: {args.h}")
    print(f"positive on grid: {result['positive']}")
    print(f"minimum D1: {mp.nstr(result['min_D1'], 40)}")
    print(f"at s: {mp.nstr(result['min_s'], 30)}")

    print("endpoint checks:")
    for s in ["1.000001", "1.001", "1.01", "1.05", "1.5", "2.067"]:
        val = D1(mp.mpf(s))
        print(f"  s={s:<10} D1={mp.nstr(val, 40)}")

    csv_path = Path(args.csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["j", "s", "D1"])
        for row in result["rows"]:
            writer.writerow([row["j"], mp.nstr(row["s"], 30), mp.nstr(row["D1"], 50)])

    print(f"wrote {csv_path}")
    print("=" * 88)

if __name__ == "__main__":
    main()
