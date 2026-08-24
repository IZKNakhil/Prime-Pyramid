# Prime Pyramid

A Python visualization for exploring the distribution of prime numbers
between consecutive squares.

## Construction

For each positive integer \(n\), row \(n\) contains all integers from

$$
n^2
$$

through

$$
(n+1)^2-1.
$$

Since

$$
(n+1)^2-n^2=2n+1,
$$

each row contains exactly \(2n+1\) integers.

The geometric center of row \(n\) is

$$
A(n)=n^2+n=n(n+1).
$$

For every integer \(x\) in the row, its horizontal coordinate is defined by

$$
k=x-(n^2+n).
$$

Therefore:

- \(k<0\): the number lies to the left of the center,
- \(k=0\): the number lies on the central axis,
- \(k>0\): the number lies to the right of the center.

The visualization uses:

- **Red + bold:** prime number
- **Black:** non-prime number
- **Blue dashed line:** symmetry axis \(k=0\)

The resulting structure will be referred to here as the **Prime Pyramid**.

---

## Prime-Pair Observation

While exploring the Prime Pyramid computationally, I observed a recurring
pattern involving pairs of primes within the same row.

For each row \(n\), define the prescribed distance

$$
d(n)=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
$$

Because \(d(n)\) is always the smallest even integer greater than or equal
to \(n\), it can equivalently be written as

$$
d(n)=2\left\lceil\frac{n}{2}\right\rceil.
$$

The computational experiments search for two primes

$$
p_1<p_2
$$

belonging to the same row,

$$
n^2<p_1<p_2<(n+1)^2,
$$

whose difference is exactly

$$
p_2-p_1=d(n).
$$

In the experiments, this prescribed prime-pair pattern persists from
\(n=344\) onward throughout the ranges tested so far.

This observation led me to formulate the following conjecture.

---

# AE Conjecture

### Prime Pairs Between Consecutive Squares

For every integer

$$
n\ge344,
$$

there exist two prime numbers \(p_1<p_2\) such that

$$
n^2<p_1<p_2<(n+1)^2
$$

and

$$
p_2-p_1=
\begin{cases}
n, & \text{if } n \text{ is even},\\
n+1, & \text{if } n \text{ is odd}.
\end{cases}
$$

Equivalently,

$$
p_2-p_1=2\left\lceil\frac{n}{2}\right\rceil.
$$

Therefore, the AE Conjecture can be written compactly as

$$
\forall n\ge344,\quad
\exists\,p_1,p_2\in\mathbb{P}:
\quad
n^2<p_1<p_2<(n+1)^2,
\qquad
p_2-p_1=2\left\lceil\frac{n}{2}\right\rceil.
$$

In words:

> For every integer \(n\ge344\), the interval between the consecutive
> squares \(n^2\) and \((n+1)^2\) contains at least one pair of primes
> whose difference is exactly \(n\) when \(n\) is even and exactly
> \(n+1\) when \(n\) is odd.

---

## Examples

For an even row, such as

$$
n=344,
$$

the AE Conjecture requires the existence of primes \(p_1,p_2\) satisfying

$$
344^2<p_1<p_2<345^2
$$

and

$$
p_2-p_1=344.
$$

For an odd row, such as

$$
n=345,
$$

the required distance becomes

$$
d(345)=346.
$$

Thus the conjecture requires primes \(p_1,p_2\) satisfying

$$
345^2<p_1<p_2<346^2
$$

and

$$
p_2-p_1=346.
$$

---

## Computational Investigation

The AE Conjecture originated from computational experiments with the
Prime Pyramid.

For every tested value of \(n\), the program examines the interval

$$
(n^2,(n+1)^2)
$$

and searches for a prime \(p_1\) for which

$$
p_2=p_1+d(n)
$$

is also prime and remains inside the same interval.

A row is considered successful when at least one such prime pair is found.

The computational test can therefore be summarized as:

$$
p_1\in\mathbb{P},
\qquad
p_1+d(n)\in\mathbb{P},
\qquad
n^2<p_1<p_1+d(n)<(n+1)^2.
$$

---

## Computational Evidence Is Not a Proof

The results reported in this repository are computational observations.

Verifying the AE Conjecture for a finite range of \(n\), regardless of how
large that range becomes, does **not** prove that the conjecture holds for
every integer \(n\ge344\).

The correct interpretation of a completed computation is therefore:

> No counterexample was found in the tested range.

The largest completely verified value of \(n\), together with the code and
parameters used for the computation, should be recorded in this repository
so that the experiments can be independently reproduced.

---

## Origin of the Conjecture

The AE Conjecture was formulated from experiments with the Prime Pyramid.

The original motivation was geometric: integers were arranged in rows
between consecutive squares and positioned relative to the central value

$$
n^2+n.
$$

Studying the distribution of primes within these rows led to the
observation that prime pairs repeatedly appeared with the parity-dependent
distance

$$
d(n)=
\begin{cases}
n, & n\text{ even},\\
n+1, & n\text{ odd}.
\end{cases}
$$

This computational observation motivated the formulation of the
**AE Conjecture**.

---

## Originality and Prior-Art Note

I arrived at the AE Conjecture independently while experimenting with the
Prime Pyramid construction.

At the time of publication, I am not aware of an earlier source stating
this exact conjecture in the form presented here.

This is not intended as a claim that no earlier equivalent formulation
exists in the mathematical literature.

If an earlier reference or equivalent formulation is identified, it will
be acknowledged and cited in this repository.

---

## Status

**Status:** Open conjecture / computational investigation.

The repository is intended to document:

- the Prime Pyramid construction,
- the AE Conjecture,
- the algorithms used to test it,
- computational results,
- possible counterexamples,
- and future mathematical observations related to the construction.

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
