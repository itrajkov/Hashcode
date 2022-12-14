from entity import warehouse
import numpy as np

class Map:
    def __init__(self, r, c) -> None:
        self._warehouses = {}
        self.r = r # number of rows
        self.c = c # number of columns

    def add_warehouse(self, w: warehouse.Warehouse) -> None:
        if f"{w.r},{w.c}" in self._warehouses.keys():
            raise Exception(f"Warehouse already exists at ({w.r},{w.c})")
        else:
            self._warehouses[f"{w.r},{w.c}"] = w

    def get_warehouse(self, id) -> warehouse.Warehouse:
        return self._warehouses[list(self._warehouses.keys())[id]]
