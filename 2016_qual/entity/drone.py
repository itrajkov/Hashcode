class Drone:
    def __init__(self, id, r, c, max_payload) -> None:
        self.r = r
        self.c = c
        self._inventory = []
        self._orders = []
        self._max_payload = max_payload

    def deliver(self, order_id):
        o = self._orders[order_id]
        print(o.to)

    def assign_order(self, order):
        self._orders.append(order)

    def get_current_order(self):
        return self._orders[0]
