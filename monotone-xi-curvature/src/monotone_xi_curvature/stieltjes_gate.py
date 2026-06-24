from __future__ import annotations
import mpmath as mp
from .xi import K
from .derivatives import derivative

def H(u):
    """H(u)=K1(sqrt(u))/sqrt(u), where K1 is the first derivative of K."""
    u = mp.mpf(u)
    r = mp.sqrt(u)
    return derivative(K, r, 1) / r

def H_derivative(u, n: int):
    """Derivative of H with respect to u."""
    return mp.diff(H, mp.mpf(u), int(n))

def first_gate_margin(u):
    """First gate margin: -H1(u), expected positive."""
    return -H_derivative(u, 1)
