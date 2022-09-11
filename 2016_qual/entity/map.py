from entity import warehouse
import numpy as np

class Map:
    def __init__(self, r, c) -> None:
        self._warehouses = {}
        self.r = r # number of rows
        self.c = c # number of columns
        print("Cells initialized.")


    def add_warehouse(self, w: warehouse.Warehouse) -> None:
        if f"{w.r},{w.c}" in self._warehouses.keys():
            raise Exception(f"Warehouse already exists at ({w.r},{w.c})")
        else:
            self._warehouses[f"{w.r},{w.c}"] = w

    def get_warehouse(self, key):
        print(self._warehouses[key])
