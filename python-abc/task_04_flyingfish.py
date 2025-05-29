#!/usr/bin/env python3
"""Multiple inheritance demo with Fish, Bird and FlyingFish."""

class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Child of Fish *and* Bird, overrides behaviour."""

    # Overrides ---------------------------------------------------------------
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
