from __future__ import annotations
import mpmath as mp
from .xi import K
from .derivatives import derivative

def K_derivative(r, n: int):
    return derivative(K, mp.mpf(r), int(n))

def K3(r):
    return K_derivative(r, 3)

def K4(r):
    return K_derivative(r, 4)

def K5(r):
    return K_derivative(r, 5)

def certify_K4_strip(h="0.01", guard="1.25", dps=80):
    """Sample/Lipschitz certificate scaffold for K4(r)<0 on [0,1/2]."""
    mp.mp.dps = int(dps)
    h = mp.mpf(h)
    guard = mp.mpf(guard)
    a = mp.mpf("0")
    b = mp.mpf("0.5")
    n = int(mp.ceil((b - a) / h))

    rows = []
    worst_upper = -mp.inf
    worst = None
    failures = []

    for j in range(n):
        left = a + j * h
        right = min(a + (j + 1) * h, b)
        mid = (left + right) / 2
        radius = (right - left) / 2

        k4_mid = K4(mid)
        k5_bound = guard * max(abs(K5(left)), abs(K5(mid)), abs(K5(right)))
        upper = k4_mid + radius * k5_bound

        row = {
            "j": j,
            "left": left,
            "right": right,
            "mid": mid,
            "K4_mid": k4_mid,
            "K5_bound": k5_bound,
            "upper": upper,
            "certified": upper < 0,
        }
        rows.append(row)
        if upper > worst_upper:
            worst_upper = upper
            worst = row
        if upper >= 0:
            failures.append(row)

    return {
        "rows": rows,
        "worst_upper": worst_upper,
        "worst": worst,
        "failures": failures,
        "certified": len(failures) == 0,
    }
