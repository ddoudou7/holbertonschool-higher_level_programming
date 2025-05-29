#!/usr/bin/env python3
"""Mixins: SwimMixin, FlyMixin et la classe Dragon qui les combine."""

class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Un dragon qui sait nager ET voler grâce aux mixins."""

    def roar(self):
        print("The dragon roars!")
