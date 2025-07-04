from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def describe(self):
        pass

class Fish(Animal):
    def __init__(self, species, weight, bait):
        self.species = species
        self.weight = weight
        self.bait = bait

    def describe(self):
        return f"{self.species} ({self.weight} kg), umpan: {self.bait}"
