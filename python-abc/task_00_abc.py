from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class that forces subclasses to implement sound()."""

    @abstractmethod
    def sound(self) -> str:   # pragma: no cover
        """Return the animal’s sound."""
        raise NotImplementedError


class Dog(Animal):
    """Concrete Dog class."""

    def sound(self) -> str:
        return "Bark"


class Cat(Animal):
    """Concrete Cat class."""

    def sound(self) -> str:
        return "Meow"
