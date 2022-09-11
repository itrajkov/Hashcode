class Order:
    def __init__(self, r, c, products: list) -> None:
        self._products = products
        self._isFulfilled = False
        self.to = (r, c)

    def fulfill(self):
        self._isFulfilled = True

    def deliver_item(self, pt: int):
        pass
