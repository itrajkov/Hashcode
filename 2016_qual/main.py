import entity

def main():

    with open('input/busy_day.in', 'r') as f:

        lines = f.readlines()
        rows, columns, drones, turns, max_payload = list(map(int, lines[0].split(' ')))
        product_types = int(lines[1])
        weights = list(map(int, lines[2].split(' ')))
        warehouses_num = int(lines[3])

        # Create world map from input taken above
        world_map = entity.Map(rows, columns)
        orders = []

        i = 0

        print()
        print("Generating warehouses..")
        # Create warehouses from input
        for i in range(4, 4 + warehouses_num*2 , 2):
            location = list(map(int, lines[i].split(' ')))
            capacities = list(map(int, lines[i+1].split(' ')))
            w = entity.Warehouse(i - 4, location[0], location[1], capacities)
            world_map.add_warehouse(w)
            print(f"Warehouse {w.r},{w.c} added!")

        i = i+2

        print()
        print("Generating orders..")
        # Create orders from input
        o = lines[i]
        for i in range(i+1, int(o), 3):
            r, c = list(map(int, lines[i].split()))
            items = int(lines[i+1])
            products = list(map(int, lines[i+2].split()))
            o = entity.Order(r, c, products)
            orders.append(o)
            print(f"Order {o.to} added!")


if __name__ == "__main__":
    main()
