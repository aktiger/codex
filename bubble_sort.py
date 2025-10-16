"""Simple implementation of the bubble sort algorithm."""
from __future__ import annotations

from typing import Iterable, List, TypeVar


T = TypeVar("T")


def bubble_sort(values: Iterable[T]) -> List[T]:
    """Return a new list containing the items from *values* in ascending order.

    Bubble sort repeatedly steps through the list, compares adjacent items and
    swaps them when they are in the wrong order. Although it is not efficient
    for large inputs, it is a straightforward way to illustrate comparison-based
    sorting.
    """

    items = list(values)
    n = len(items)
    # Iterate over the list and bubble the largest element to the end each time.
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2]
    print("Original:", sample)
    print("Sorted:", bubble_sort(sample))
