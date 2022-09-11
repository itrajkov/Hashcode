import numpy as np

class Warehouse:
    def __init__(self, id, r, c, capacities: list) -> None:
        self.id = id
        self.r = r
        self.c = c
        self._inventory = capacities
        self.capacities = capacities

    def get_capacity(self, pt):
        return self.capacities[pt]

    def __str__(self):
        return str({'id': self.id, 'r': self.r, 'c': self.c, 'capacities': self.capacities})

    def __repr__(self):
        print(self.__str__())
