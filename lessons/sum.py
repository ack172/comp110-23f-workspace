"""Summing the elements of a list using different loops."""

__author__ = "730385079"


def w_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum of all elements."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum of all elements, using a for loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum of all elements, using a for loop and range."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
