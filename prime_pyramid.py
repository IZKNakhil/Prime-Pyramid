"""Prime Pyramid visualization."""

from math import isqrt
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

LIMIT = 2024
SCALE_X = 4
SCALE_Y = 4
FONT_SIZE = 10
FIGURE_SIZE = (40, 18)
DPI = 250


def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def plot_prime_pyramid(limit: int) -> None:
    """Plot rows n^2 through (n+1)^2-1, centered at n^2+n."""
    if limit < 1:
        raise ValueError("limit must be at least 1.")

    max_n = isqrt(limit)
    fig, ax = plt.subplots(figsize=FIGURE_SIZE, dpi=DPI)

    for n in range(1, max_n + 1):
        row_start = n * n
        row_end = min((n + 1) ** 2 - 1, limit)
        row_center = n * n + n
        y = n * SCALE_Y

        for value in range(row_start, row_end + 1):
            x = (value - row_center) * SCALE_X
            prime = is_prime(value)

            ax.text(
                x, y, str(value),
                fontsize=FONT_SIZE,
                ha="center",
                va="center",
                color="red" if prime else "black",
                fontweight="bold" if prime else "normal",
            )

    ax.axvline(0, color="blue", linestyle="--", linewidth=1)

    max_x = max_n * SCALE_X
    ax.set_xlim(-max_x - 2 * SCALE_X, max_x + 2 * SCALE_X)
    ax.set_ylim((max_n + 2) * SCALE_Y, 0)

    ticks = range(-max_n, max_n + 1, 2)
    ax.set_xticks([k * SCALE_X for k in ticks])
    ax.set_xticklabels([str(k) for k in ticks])
    ax.set_yticks([n * SCALE_Y for n in range(1, max_n + 1)])
    ax.set_yticklabels([str(n) for n in range(1, max_n + 1)])

    ax.set_xlabel("Column coordinate k", fontsize=13)
    ax.set_ylabel("Row n", fontsize=13)
    ax.set_title(f"Prime Pyramid — Numbers up to {limit:,}", fontsize=18)

    ax.legend(
        handles=[
            Line2D([0], [0], marker="o", linestyle="None",
                   markerfacecolor="red", markeredgecolor="red",
                   markersize=9, label="Prime number"),
            Line2D([0], [0], marker="o", linestyle="None",
                   markerfacecolor="black", markeredgecolor="black",
                   markersize=9, label="Non-prime number"),
        ],
        loc="upper right",
        fontsize=12,
        frameon=True,
    )

    ax.grid(alpha=0.25)
    fig.tight_layout()
    plt.show()


def main() -> None:
    plot_prime_pyramid(LIMIT)


if __name__ == "__main__":
    main()
