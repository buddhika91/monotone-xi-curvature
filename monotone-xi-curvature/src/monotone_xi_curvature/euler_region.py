from __future__ import annotations
import mpmath as mp

def R(s):
    """Pole-cancelled zeta factor R(s)=log((s-1) zeta(s))."""
    s = mp.mpf(s)
    return mp.log((s - 1) * mp.zeta(s))

def R3(s):
    """Third derivative of R(s)."""
    return mp.diff(R, mp.mpf(s), 3)

def gamma_tail(s):
    """2 sum_{m>=1} (s+2m)^(-3) = 1/4 zeta(3,1+s/2)."""
    s = mp.mpf(s)
    return mp.mpf("0.25") * mp.zeta(3, 1 + s / 2)

def D1(s):
    """Euler-side margin D1(s)=gamma_tail(s)-R3(s)."""
    return gamma_tail(s) - R3(s)

def scan_D1(a="1.000001", b="2.067", h="0.001", dps=80):
    mp.mp.dps = int(dps)
    a = mp.mpf(a)
    b = mp.mpf(b)
    h = mp.mpf(h)
    n = int(mp.ceil((b - a) / h))

    rows = []
    best_s = None
    best_val = mp.inf

    for j in range(n + 1):
        s = min(a + j * h, b)
        val = D1(s)
        rows.append({"j": j, "s": s, "D1": val})
        if val < best_val:
            best_val = val
            best_s = s

    return {"rows": rows, "min_s": best_s, "min_D1": best_val, "positive": best_val > 0}
