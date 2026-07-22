from product import Product


class Client:

    def __init__(self, first_name: str, last_name: str, purchases: list[tuple[str, int]]):
        self.first_name = first_name
        self.last_name = last_name
        self.purchases = purchases

    def add_article(self, product: Product, quantity: int):
        self.purchases.append((product.name, quantity))
