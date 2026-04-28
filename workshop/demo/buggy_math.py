"""Intentionally buggy module for the Copilot Agent demo.

Bug: `average` divides by len(values) without handling the empty case
and uses integer division, which truncates results.
"""

from typing import Sequence


def average(values: Sequence[float]) -> float:
    total = 0
    for v in values:
        total += v
    return total // len(values)
