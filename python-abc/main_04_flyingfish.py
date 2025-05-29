#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()

# Méthodes redéfinies
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

# 👉 Explorer la Method Resolution Order
print("MRO :", [cls.__name__ for cls in FlyingFish.mro()])
