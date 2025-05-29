#!/usr/bin/env python3
"""VerboseList – subclass de list qui notifie chaque action d'ajout/suppression."""

class VerboseList(list):
    """Liste bruyante : affiche un message à chaque modification."""

    # --- Ajouts --------------------------------------------------------------
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    # --- Suppressions --------------------------------------------------------
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index: int = -1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
