from __future__ import annotations
import mpmath as mp

def set_dps(dps: int) -> None:
    mp.mp.dps = int(dps)

def xi(s):
    """Completed Riemann Xi function."""
    s = mp.mpf(s) if not isinstance(s, mp.mpc) else s
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def log_xi(s):
    """Principal logarithm of Xi(s)."""
    return mp.log(xi(s))

def K(r):
    """K(r)=log Xi(1/2+r)."""
    return log_xi(mp.mpf("0.5") + mp.mpf(r))
