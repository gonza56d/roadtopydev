"""From Two Scoops of Django:
1 The base view classes provided by Django always go to the right.
2 Mixins go to the left of the base view.
3 Mixins should not inherit from any other class. Keep your inheritance chain simple!
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    model = 'Vehicle with default model'

    @abstractmethod
    def travel(self):
        pass


class RadioMixin:

    def play_station(station: int) -> str:
        return f'Radio {int} is being played!'


class TvMixin:

    def play_tv(movie: str) -> str:
        return f'Now playing {movie}'


class Motorcycle(Vehicle):

    def __init__(self, model: str) -> None:
        super().__init__()
        self.model = model

    def travel(self):
        return f'{self.model} is traveling'


class Car(RadioMixin, Vehicle):

    def __init__(self, model: str) -> None:
        super().__init__()
        self.model = model


class Bus(RadioMixin,
          TvMixin,
          Vehicle):

    def __init__(self, model: str) -> None:
        super().__init__()
        self.model = model
