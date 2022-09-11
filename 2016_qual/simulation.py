from math import sqrt
import random


class Simulation:

    def __init__(self, world_map, orders, drones, deadline):
        self.turns = 0
        self.score = 0
        self.deadline = deadline
        self.world_map = world_map
        self.orders = orders
        self.drones = drones

        for drone in self.drones:
            drone.assign_order(random.choice(self.orders))

    def step(self):
        if self.turns >= self.deadline:
            print(f"[+] Simulation finished with {self.score} score.")
            return 0

        # Experiment moving one drone
        drone = self.drones[0]
        o = drone.get_current_order()

        print(f"Current pos: {(drone.r, drone.c)}")
        print(f"Destination: {o.to}")

        if o.to == (drone.r, drone.c):
            print("DESTINATION REACHED")
        else:
            distance = sqrt(abs(o.to[0] - drone.r)**2 + abs(o.to[1] - drone.c)**2)
            if drone.r < o.to[0]:
                drone.r += 1
            if drone.c < o.to[1]:
                drone.c += 1
            print(distance)



        self.turns += 1
        return self.world_map, self.orders, self.drones
