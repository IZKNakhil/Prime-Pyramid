# Prime Pyramid

A Python visualization for exploring prime numbers between consecutive squares.

For each positive integer `n`, row `n` contains the integers from `n²` through `(n+1)² - 1`. The geometric center of the row is `n² + n`, and each value `x` receives the horizontal coordinate `k = x - (n² + n)`.

- **Red + bold:** prime number
- **Black:** non-prime number
- **Blue dashed line:** symmetry axis `k = 0`

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
