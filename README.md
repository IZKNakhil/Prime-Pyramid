# Prime Pyramid

# Prime Pyramid

A Python visualization for exploring prime numbers between consecutive squares.

For each positive integer `n`, row `n` contains the integers from

\[
n^2
\]

through

\[
(n+1)^2-1.
\]

The geometric center of each row is

\[
n^2+n,
\]

and each value \(x\) receives the horizontal coordinate

\[
k=x-(n^2+n).
\]

Therefore, every row contains exactly \(2n+1\) integers and is centered at
\(k=0\).

### Visualization

- **Red + bold:** prime number
- **Black:** non-prime number
- **Blue dashed line:** symmetry axis \(k=0\)

---

## Prime-Pair Observation

While computationally exploring the distribution of primes inside these
consecutive-square rows, I observed a recurring prime-pair pattern.

Define the required distance

\[
d(n)=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
\]

Equivalently,

\[
d(n)=2\left\lceil\frac{n}{2}\right\rceil.
\]

The computational experiments search, in every row, for two primes

\[
p_1<p_2
\]

such that both primes lie strictly between the consecutive squares,

\[
n^2<p_1<p_2<(n+1)^2,
\]

and their difference is exactly

\[
p_2-p_1=d(n).
\]

This observation led me to formulate the following conjecture.

---

## Conjecture

**Prime-Pair Conjecture for Consecutive Squares**

For every integer

\[
n\ge 344,
\]

there exist two prime numbers \(p_1<p_2\) satisfying

\[
n^2<p_1<p_2<(n+1)^2
\]

and

\[
p_2-p_1=
\begin{cases}
n, & n\text{ even},\\
n+1, & n\text{ odd}.
\end{cases}
\]

In compact form,

\[
\boxed{
\forall n\ge344,\quad
\exists\,p_1,p_2\in\mathbb P:
\quad
n^2<p_1<p_2<(n+1)^2,
\quad
p_2-p_1=2\left\lceil\frac n2\right\rceil
}
\]

In other words:

- for every **even** row \(n\), the conjecture predicts a prime pair
  separated by exactly \(n\);
- for every **odd** row \(n\), it predicts a prime pair
  separated by exactly \(n+1\).

---

## Computational Status

This conjecture arose from computational experiments with the Prime Pyramid.

The calculations provide **computational evidence only**. They do not
constitute a mathematical proof that the statement holds for every
\(n\ge344\).

The repository contains the code used to search for such prime pairs and
to test the conjecture over finite ranges of \(n\).

The verified range should always be stated explicitly, for example:

> No counterexample was found for \(344 \le n \le N\).

where \(N\) is the largest value completely verified by the current
computation.

---

## Originality Note

I arrived at this conjecture independently while experimenting with the
Prime Pyramid construction.

At the time of publication, I am not aware of an earlier source stating
this exact parity-dependent prime-pair conjecture for intervals between
consecutive squares.

If an earlier reference exists, I would be grateful to learn about it so
that it can be properly acknowledged and cited.

The purpose of this repository is to document the construction,
computational experiments, data, and conjecture in a reproducible form.


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
