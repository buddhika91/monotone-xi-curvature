#!/usr/bin/env python3
import argparse, csv
from pathlib import Path
import mpmath as mp
from monotone_xi_curvature.compact_strip import certify_K4_strip

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--h", default="0.01")
    parser.add_argument("--guard", default="1.25")
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--csv", default="data/K4_strip_scan.csv")
    args = parser.parse_args()

    result = certify_K4_strip(h=args.h, guard=args.guard, dps=args.dps)

    print("=" * 88)
    print("COMPACT STRIP: VERIFY K4(r)<0 ON [0, 1/2]")
    print("=" * 88)
    print(f"dps: {args.dps}")
    print(f"h: {args.h}")
    print(f"guard: {args.guard}")
    print(f"certified by sampled/Lipschitz scaffold: {result['certified']}")
    print(f"worst upper: {mp.nstr(result['worst_upper'], 40)}")
    w = result["worst"]
    print(f"worst interval: [{mp.nstr(w['left'], 12)}, {mp.nstr(w['right'], 12)}]")
    print(f"K4(mid): {mp.nstr(w['K4_mid'], 40)}")
    print(f"K5 bound: {mp.nstr(w['K5_bound'], 40)}")
    print(f"failures: {len(result['failures'])}")

    csv_path = Path(args.csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["j", "left", "right", "mid", "K4_mid", "K5_bound", "upper", "certified"])
        for row in result["rows"]:
            writer.writerow([
                row["j"], mp.nstr(row["left"], 30), mp.nstr(row["right"], 30),
                mp.nstr(row["mid"], 30), mp.nstr(row["K4_mid"], 50),
                mp.nstr(row["K5_bound"], 50), mp.nstr(row["upper"], 50),
                row["certified"],
            ])
    print(f"wrote {csv_path}")
    print("=" * 88)

if __name__ == "__main__":
    main()
