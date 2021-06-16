"""The way to deal with interfaces with python, inherit from ABC to get ABCMeta
and make your class abstract."""

from abc import ABC, abstractclassmethod, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return 'Guau!'


class Cat(Animal):

    def make_sound(self):
        return 'Miau!'


class Bird(Animal):
    """Cant be instantiated because it doesn't implement
    @abstractmethod make_sound."""
    pass


dog = Dog()
print(dog.make_sound())
print(Cat().make_sound())
birb = Bird() # error here
