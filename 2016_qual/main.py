import numpy as np
import entity

def main():
    map = entity.Map(10, 10)
    wh = entity.Warehouse(0, 5, 5, np.array([3, 2, 1]))
    print(wh.get_capacity(1))

    print("Simulation initialized..")

if __name__ == "__main__":
    main()
