# Monotone Curvature Decay of the Completed Riemann Function

This repository supports the one-page note:

**Monotone Curvature Decay of the Completed Riemann Function**

The completed Riemann function is

$$
\Xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
$$

and the real-axis logarithmic landscape is

$$
K(r)=\log \Xi(1/2+r).
$$

The supported monotonicity target is

$$
K'''(r)<0,\qquad r>0.
$$

Equivalently,

$$
\frac{d^3}{ds^3}\log \Xi(s)<0,\qquad s>1/2.
$$

## Install

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate     # Windows

pip install -r requirements.txt
pip install -e .
```

## Reproduce checks

Compact strip:

```bash
python experiments/verify_K4_strip.py --h 0.01 --dps 80
```

Euler interval:

```bash
python experiments/verify_D1_euler.py --h 0.001 --dps 80
```

Scan `K'''`:

```bash
python experiments/scan_K3.py --a 0.001 --b 10 --h 0.01 --dps 80
```

Reproduce quoted tables:

```bash
python experiments/reproduce_tables.py
```

## Status

This code provides high-precision numerical verification and certificate scaffolding. It is not a proof assistant certificate and does not prove the Riemann Hypothesis.

For publication-grade certification, replace sampled derivative/Lipschitz estimates with outward-rounded interval or ball arithmetic.
