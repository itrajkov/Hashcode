import numpy as np

class Warehouse:
    def __init__(self, id, r, c, capacities: np.ndarray) -> None:
        self.id = id
        self.r = r
        self.c = c
        self.capacities = capacities

    def get_capacity(self, pt):
        return self.capacities[pt]
