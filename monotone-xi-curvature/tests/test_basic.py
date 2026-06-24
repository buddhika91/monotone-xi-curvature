import mpmath as mp
from monotone_xi_curvature.xi import xi, K

def test_xi_symmetry_real():
    mp.mp.dps = 50
    s = mp.mpf("0.73")
    assert abs(xi(s) - xi(1-s)) < mp.mpf("1e-40")

def test_K_even():
    mp.mp.dps = 50
    r = mp.mpf("0.2")
    assert abs(K(r) - K(-r)) < mp.mpf("1e-40")
