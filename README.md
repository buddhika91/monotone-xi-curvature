# monotone-xi-curvature

Numerical support package for the note:

**Monotone Curvature Decay of the Completed Riemann Function**

This repository investigates the real-axis geometry of the completed Riemann function

[
\Xi(s)
======

\frac12 s(s-1)\pi^{-s/2}\Gamma!\left(\frac{s}{2}\right)\zeta(s).
]

Define the logarithmic landscape

[
K(r)
====

\log\Xi!\left(\frac12+r\right).
]

The central quantity studied is

[
K'''(r),
]

which measures the rate of change of curvature of the logarithmic (\Xi)-landscape.

The primary conjectural property investigated is

[
K'''(r)<0,
\qquad r>0,
]

or equivalently,

[
\frac{d^3}{ds^3}\log\Xi(s)<0,
\qquad s>\frac12.
]

---

## What This Code Does

The package provides reproducible scripts for:

* Computing (\Xi(s)), (\log\Xi(s)), and their derivatives.
* Evaluating (K'''(r)), (K^{(4)}(r)), and higher derivatives.
* Testing compact-strip negativity

[
K^{(4)}(r)<0,
\qquad 0<r<\frac12.
]

* Computing the Euler-side quantity

[
D_1(s)
======

## \frac14\zeta!\left(3,1+\frac{s}{2}\right)

\frac{d^3}{ds^3}
\log!\big((s-1)\zeta(s)\big).
]

* Testing positivity of

[
D_1(s)>0,
\qquad 1<s\le2.067.
]

* Reproducing all numerical tables appearing in the accompanying note.

---

## Installation

```bash
git clone https://github.com/buddhika91/monotone-xi-curvature.git

cd monotone-xi-curvature

pip install -r requirements.txt
```

---

## Quick Start

Verify compact-strip negativity:

```bash
python experiments/verify_K4_strip.py --h 0.01 --dps 80
```

Verify Euler-side positivity:

```bash
python experiments/verify_D1_euler.py --h 0.001 --dps 80
```

Scan the third derivative directly:

```bash
python experiments/scan_K3.py --a 0.001 --b 10 --h 0.01 --dps 80
```

Run tests:

```bash
pytest -q
```

---

## Expected Numerical Values

Representative values for the Euler-side margin:

```
D1(1.000001) ≈ 2.223 × 10⁻⁴
D1(1.5)      ≈ 4.404 × 10⁻⁴
D1(2.067)    ≈ 6.773 × 10⁻⁴
```

Representative compact-strip certification:

```
h = 0.1   margin ≈ 4.45 × 10⁻⁴
h = 0.01  margin ≈ 4.46 × 10⁻⁴
h = 0.001 margin ≈ 4.46 × 10⁻⁴
```

---

## Repository Structure

```text
monotone-xi-curvature/

├── src/
│   └── monotone_xi_curvature/
│       ├── xi.py
│       ├── derivatives.py
│       ├── compact_strip.py
│       ├── euler_region.py
│       └── stieltjes_gate.py
│
├── experiments/
│   ├── verify_K4_strip.py
│   ├── verify_D1_euler.py
│   ├── scan_K3.py
│   └── reproduce_tables.py
│
├── tests/
│   ├── test_basic.py
│   └── test_signs.py
│
├── paper/
│   └── one_page_article.md
│
├── data/
├── figures/
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Scientific Status

This repository supports a focused mathematical investigation of a geometric property of the completed Riemann function.

Established computationally here:

* Negativity of (K^{(4)}(r)) throughout the tested compact strip.
* Positivity of (D_1(s)) throughout the tested Euler interval.
* Numerical support for

[
K'''(r)<0,
\qquad r>0.
]

Open mathematical problems:

* Rigorous proof of compact-strip negativity.
* Rigorous proof of Euler-side positivity.
* Global proof of

[
K'''(r)<0.
]

* Relationship, if any, between this monotonicity property and Stieltjes/Pick structures associated with (\Xi).

---

## Disclaimer

This repository does **not** claim a proof of the Riemann Hypothesis.

The monotone-curvature property is investigated as a structural feature of the completed Riemann function that appears worthy of study independently of RH.

---


**Buddhika Weerasooriya**
*Monotone Curvature Decay of the Completed Riemann Function* (2026).
