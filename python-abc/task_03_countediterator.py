#!/usr/bin/env python3
"""Iterator wrapper that counts how many items have been yielded."""

class CountedIterator:
    """Wrap any iterable and keep track of the number of values produced."""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)     # May raise StopIteration → propagate
        self._count += 1
        return item

    # Public helper -----------------------------------------------------------
    def get_count(self) -> int:
        """Return how many items have been iterated so far."""
        return self._count
