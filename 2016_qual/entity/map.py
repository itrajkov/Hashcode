from entity import warehouse
import numpy as np

class Map:
    def __init__(self, r, c) -> None:
        self.r = r # number of rows
        self.c = c # number of columns
        self._cells = np.zeros((r,c), dtype=int) # numpy array of cells
        print("Cells initialized.")


    def add_warehouse(self, w: warehouse.Warehouse) -> None:
        if type(self._cells[w.r, w.c]) == warehouse.Warehouse:
            raise Exception(f"Warehouse already exists at ({w.r},{w.c})")
        else:
            self._cells[w.r,w.c] = w


    def __repr__(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self._cells[i,j], end=" ")
            print()

    def __str__(self) -> str:
        s = ""
        for i in range(self.r):
            for j in range(self.c):
                s += f"{self._cells[i,j]} "
            s += "\n"
        return s
