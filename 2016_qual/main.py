import entity
import simulation
import time

def main():

    with open('input/busy_day.in', 'r') as f:

        lines = f.readlines()
        rows, columns, d, deadline, max_payload = list(map(int, lines[0].split(' ')))
        product_types = int(lines[1])
        weights = list(map(int, lines[2].split(' ')))
        warehouses_num = int(lines[3])

        # Create world map from input taken above
        world_map = entity.Map(rows, columns)
        orders = []
        drones = []

        i = 0

        # Create warehouses from input
        for i in range(4, 4 + warehouses_num*2 , 2):
            location = list(map(int, lines[i].split(' ')))
            capacities = list(map(int, lines[i+1].split(' ')))
            w = entity.Warehouse(i - 4, location[0], location[1], capacities)
            world_map.add_warehouse(w)
        print(f"[+] Warehouses generated")

        i = i+2

        # Create orders from input
        o = lines[i]
        for i in range(i+1, int(o), 3):
            r, c = list(map(int, lines[i].split()))
            items = int(lines[i+1])
            products = list(map(int, lines[i+2].split()))
            o = entity.Order(r, c, products)
            orders.append(o)
        print(f"[+] Orders generated")

        # Create drones
        for i in range(d):
            w0 = world_map.get_warehouse(0)
            d = entity.Drone(i, w0.r, w0.c, max_payload)
            drones.append(d)
        print(f"[+] Drones created")

    s = simulation.Simulation(world_map, orders, drones, deadline)
    while True:
        if s.step() == 0: break
        time.sleep(0.1)
        # print(s.drones[0].r, s.drones[0].c)



if __name__ == "__main__":
    main()
