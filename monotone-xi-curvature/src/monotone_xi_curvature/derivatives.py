from __future__ import annotations
from typing import Callable
import mpmath as mp

def derivative(f: Callable[[mp.mpf], mp.mpf], x, n: int):
    """High-precision numerical derivative using mpmath.diff."""
    return mp.diff(f, mp.mpf(x), int(n))
