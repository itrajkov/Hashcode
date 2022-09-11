import entity

def main():


    with open('input/busy_day.in', 'r') as f:
        lines = f.readlines()
        rows, columns, drones, turns, max_payload = list(map(int, lines[0].split(' ')))
        product_types = int(lines[1])
        weights = list(map(int, lines[2].split(' ')))
        warehouses_num = int(lines[3])

        m = entity.Map(rows, columns)

        for i in range(4, 4 + warehouses_num*2 , 2):
            location = list(map(int, lines[i].split(' ')))
            capacities = list(map(int, lines[i+1].split(' ')))
            w = entity.Warehouse(i - 4, location[0], location[1], capacities)
            m.add_warehouse(w)


    # Check if order location is a warehouse // Exception


if __name__ == "__main__":
    main()
