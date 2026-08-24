# Prime Pyramid
---
## AE Conjecture

While exploring the distribution of prime numbers in the Prime Pyramid,
I observed a recurring pattern involving pairs of primes inside the same row.

For each row \(n\), define the distance

$$
d(n)=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
$$

Equivalently,

$$
d(n)=2\left\lceil\frac{n}{2}\right\rceil.
$$

Computational experiments with the Prime Pyramid led to the following conjecture.

---

### AE Conjecture — Prime Pairs Between Consecutive Squares

For every integer

$$
n \ge 344,
$$

there exist two prime numbers \(p_1<p_2\) in the interval between
two consecutive squares,

$$
n^2 < p_1 < p_2 < (n+1)^2,
$$

such that

$$
p_2-p_1=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
$$

In compact form:

$$
\boxed{
\forall n\ge344,\;
\exists\,p_1,p_2\in\mathbb{P}
\text{ such that }
n^2<p_1<p_2<(n+1)^2
\text{ and }
p_2-p_1=2\left\lceil\frac n2\right\rceil
}
$$

In other words:

- if \(n\) is **even**, the interval contains a prime pair with distance exactly \(n\);
- if \(n\) is **odd**, the interval contains a prime pair with distance exactly \(n+1\).

---

### Computational Evidence

The AE Conjecture originated from computational experiments with the
Prime Pyramid.

For each tested row \(n\), the program searches for primes \(p_1,p_2\)
satisfying the exact distance condition above.

A successful computational test for a finite range does **not** constitute
a proof of the conjecture for all \(n\ge344\). It provides computational
evidence only.

The verified range and the source code used for the computation are
documented in this repository.

---

### Origin and Prior-Art Note

The AE Conjecture was formulated independently while experimenting with
the Prime Pyramid and studying prime pairs between consecutive squares.

At the time of publication, I am not aware of an earlier source stating
this exact conjecture. If an earlier mathematical reference is identified,
it will be acknowledged and cited here.


- ## Prime Pyramid Visualization

![Prime Pyramid Visualization](images/prime_pyramid.png)


## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python prime_pyramid.py
```

Change `LIMIT` in `prime_pyramid.py` to control the maximum displayed number.

## Mathematical note

The arrangement is geometrically symmetric around `k = 0`. No symmetry of the distribution of prime numbers itself is assumed. This project is intended for experimental mathematical exploration; computational patterns are not proofs.


## Citation

If you use this software, visualization, or the Prime Pyramid construction
in academic or scientific work, please cite this repository.

See `CITATION.cff` for citation information.

## Authors

Akenkou & Errachdi
