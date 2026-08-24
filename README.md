# Prime Pyramid

A Python visualization and computational experiment for exploring the
distribution of prime numbers between consecutive squares.

The construction arranges the positive integers into centered rows.
Each row corresponds exactly to the integers lying between two
consecutive squares.

The geometric representation led to a computational observation about
prime pairs, which is formulated below as the **AE Conjecture**.

---

## 1. Construction of the Prime Pyramid

For every positive integer \(n\), row \(n\) contains the integers

$$
n^2,\; n^2+1,\; n^2+2,\;\ldots,\;(n+1)^2-1.
$$

Since

$$
(n+1)^2-n^2=2n+1,
$$

row \(n\) contains exactly

$$
2n+1
$$

integers.

The central value of the row is

$$
n^2+n=n(n+1).
$$

This value defines the vertical symmetry axis of the pyramid.

---

## 2. Coordinate System

Let \(k\) denote the horizontal column relative to the central axis.

The integer located in row \(n\) and column \(k\) is

$$
P(n,k)=n(n+1)+k,
\qquad -n\le k\le n.
$$

Thus:

- \(k=0\) is the central column,
- \(k=1\) is one column to the right,
- \(k=2\) is two columns to the right,
- \(k=-1\) is one column to the left,
- \(k=-2\) is two columns to the left.

For example,

$$
P(n,0)=n(n+1),
$$

$$
P(n,1)=n(n+1)+1,
$$

$$
P(n,-1)=n(n+1)-1.
$$

The two outer positions of row \(n\) are

$$
P(n,-n)=n^2
$$

and

$$
P(n,n)=(n+1)^2-1.
$$

Therefore the entire interval between two consecutive squares is represented
by the simple coordinate formula

$$
P(n,k)=n(n+1)+k,
\qquad -n\le k\le n.
$$

---

## 3. Visualization

The Python program plots the integers according to their coordinates
\((k,n)\).

The visualization uses:

- **Red + bold:** prime number
- **Black:** non-prime number
- **Blue dashed line:** central axis \(k=0\)

The central axis therefore represents the sequence

$$
n(n+1)=n^2+n.
$$

The resulting triangular arrangement is referred to in this repository as
the **Prime Pyramid**.

---

## 4. Prime-Pair Observation

While computationally exploring the distribution of primes inside the
Prime Pyramid, I observed a recurring pattern involving pairs of primes
within the same row.

For each row \(n\), define the prescribed distance

$$
d(n)=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
$$

Since this is always the smallest even integer greater than or equal to
\(n\), the same function can be written compactly as

$$
d(n)=2\left\lceil\frac{n}{2}\right\rceil.
$$

The computational observation concerns prime numbers \(p_1<p_2\) belonging
to the same row and satisfying

$$
p_2-p_1=d(n).
$$

In terms of the Prime Pyramid coordinates, if

$$
p_1=P(n,k_1)
$$

and

$$
p_2=P(n,k_2),
$$

then

$$
p_2-p_1
=
P(n,k_2)-P(n,k_1)
=
k_2-k_1.
$$

Therefore the observation can also be expressed geometrically as

$$
k_2-k_1=d(n).
$$

This means that the arithmetic distance between the two primes is exactly
their horizontal column distance inside the Prime Pyramid.

This recurring computational pattern led me to formulate the following
conjecture.

---

# 5. AE Conjecture

## Prime Pairs Between Consecutive Squares

For every integer

$$
n\ge344,
$$

there exist two prime numbers

$$
p_1 < p_2
$$

lying strictly between the consecutive squares \(n^2\) and \((n+1)^2-1\),

$$

n^2< p_1 < p_2 < (n+1)^2-1,

$$

such that

$$
p_2-p_1=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
$$

Equivalently,

$$
p_2-p_1
=
2\left\lceil\frac{n}{2}\right\rceil.
$$

A compact formulation of the **AE Conjecture** is therefore

$$
\forall n\ge344,\quad
\exists\,p_1,p_2\in\mathbb{P}:
\quad
n^2<p_1<p_2<(n+1)^2,
\qquad
p_2-p_1=
2\left\lceil\frac{n}{2}\right\rceil.
$$

In words:

> **AE Conjecture.**
> For every integer \(n\ge344\), the interval between the consecutive
> squares \(n^2\) and \((n+1)^2\) contains at least one pair of primes
> whose difference is exactly \(n\) when \(n\) is even and exactly
> \(n+1\) when \(n\) is odd.

---

## 6. Geometric Form of the AE Conjecture

Using the Prime Pyramid coordinate system

$$
P(n,k)=n(n+1)+k,
$$

the conjecture can also be formulated entirely in terms of columns.

There exist two columns \(k_1<k_2\) such that

$$
P(n,k_1)\in\mathbb{P}
$$

and

$$
P(n,k_2)\in\mathbb{P},
$$

with

$$
k_2-k_1=
2\left\lceil\frac{n}{2}\right\rceil.
$$

Therefore the AE Conjecture has the equivalent geometric form

$$
\forall n\ge344,\quad
\exists\,k_1,k_2\in\{-n,\ldots,n\}
$$

such that

$$
P(n,k_1),P(n,k_2)\in\mathbb{P}
$$

and

$$
k_2-k_1=
2\left\lceil\frac{n}{2}\right\rceil.
$$

This formulation connects the prime-pair condition directly to the
geometry of the Prime Pyramid.

---

## 7. Even and Odd Rows

The conjecture alternates between two cases.

### Even rows

If \(n\) is even, then

$$
d(n)=n.
$$

The conjecture predicts primes \(p_1,p_2\) in row \(n\) satisfying

$$
p_2-p_1=n.
$$

In pyramid coordinates,

$$
k_2-k_1=n.
$$

### Odd rows

If \(n\) is odd, then

$$
d(n)=n+1.
$$

The conjecture predicts primes \(p_1,p_2\) in row \(n\) satisfying

$$
p_2-p_1=n+1.
$$

In pyramid coordinates,

$$
k_2-k_1=n+1.
$$

Thus in both cases the required distance is always even:

$$
d(n)=2\left\lceil\frac n2\right\rceil.
$$

---

## 8. Computational Test

For every tested row \(n\), the program examines the interval

$$
(n^2,(n+1)^2)
$$

and computes

$$
d(n)=2\left\lceil\frac n2\right\rceil.
$$

It then searches for a prime \(p_1\) such that

$$
p_2=p_1+d(n)
$$

is also prime and remains inside the same interval.

A row passes the test when

$$
p_1\in\mathbb{P},
$$

$$
p_1+d(n)\in\mathbb{P},
$$

and

$$
n^2<p_1<p_1+d(n)<(n+1)^2.
$$

If no such pair exists, that row is a counterexample to the conjecture.

---

## 9. Computational Evidence

The AE Conjecture originated from computational experiments with the
Prime Pyramid.

The threshold used in the conjecture is

$$
n\ge344.
$$

Computational verification over a finite interval does **not** constitute
a proof that the conjecture holds for every \(n\ge344\).

The mathematically appropriate statement for a completed computation is:

> **No counterexample was found in the tested range.**

The repository should record the exact tested range, program version,
parameters, and relevant output so that the computation can be independently
reproduced.

---

## 10. Status

**Status:** Open conjecture / computational investigation.

The project currently consists of:

- the Prime Pyramid construction,
- the coordinate formula \(P(n,k)=n(n+1)+k\),
- visualization of primes between consecutive squares,
- the parity-dependent distance \(d(n)\),
- the AE Conjecture,
- computational searches for counterexamples,
- and experimental investigation of related prime patterns.

---

## 11. Origin and Prior-Art Note

The AE Conjecture was formulated independently while experimenting with
the Prime Pyramid and studying the distribution of primes between
consecutive squares.

The geometric construction first led to the coordinate system

$$
P(n,k)=n(n+1)+k.
$$

Computational exploration of prime positions in these rows then led to the
observation of prime pairs separated by

$$
d(n)=
\begin{cases}
n, & n\text{ even},\\
n+1, & n\text{ odd}.
\end{cases}
$$

This observation motivated the formulation of the **AE Conjecture**.

At the time of publication, I am not aware of an earlier source stating
this exact conjecture in the form presented here.

This statement should not be interpreted as a claim that no equivalent
formulation exists in the mathematical literature.

If an earlier reference or equivalent formulation is identified, it will
be acknowledged and cited in this repository.

---

## 12. Reproducibility

The purpose of this repository is to make the experiments reproducible.

The source code used for the Prime Pyramid is included in the repository.

Future updates may include:

- larger verified ranges,
- optimized prime sieves,
- complete lists of exceptional small values,
- statistical analysis of the number of valid pairs per row,
- visualization of valid prime pairs,
- downloadable computational data,
- and mathematical analysis of the conjecture.

---

## Disclaimer

The AE Conjecture is currently a conjecture supported by computational
experiments.

No proof for all \(n\ge344\) is claimed.

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
