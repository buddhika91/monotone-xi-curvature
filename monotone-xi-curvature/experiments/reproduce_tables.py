#!/usr/bin/env python3
import csv
from pathlib import Path
import mpmath as mp
from monotone_xi_curvature.compact_strip import K4
from monotone_xi_curvature.euler_region import D1

mp.mp.dps = 80

def main():
    Path("data").mkdir(exist_ok=True)
    k4_points = ["0", "0.1", "0.3", "0.49"]
    d1_points = ["1.000001", "1.5", "2.067"]

    print("=" * 80)
    print("K4 table")
    print("=" * 80)
    with open("data/K4_table.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["r", "K4"])
        for r in k4_points:
            val = K4(mp.mpf(r))
            writer.writerow([r, mp.nstr(val, 50)])
            print(f"r={r:<8} K4={mp.nstr(val, 40)}")

    print("=" * 80)
    print("D1 table")
    print("=" * 80)
    with open("data/D1_table.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["s", "D1"])
        for s in d1_points:
            val = D1(mp.mpf(s))
            writer.writerow([s, mp.nstr(val, 50)])
            print(f"s={s:<10} D1={mp.nstr(val, 40)}")

    print("wrote data/K4_table.csv and data/D1_table.csv")

if __name__ == "__main__":
    main()
