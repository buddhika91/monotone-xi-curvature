import mpmath as mp
from monotone_xi_curvature.compact_strip import K4
from monotone_xi_curvature.euler_region import D1

def test_K4_sample_negative():
    mp.mp.dps = 50
    for r in ["0", "0.1", "0.3", "0.49"]:
        assert K4(mp.mpf(r)) < 0

def test_D1_sample_positive():
    mp.mp.dps = 50
    for s in ["1.000001", "1.5", "2.067"]:
        assert D1(mp.mpf(s)) > 0
