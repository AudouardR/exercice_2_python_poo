from product import Product


class Client:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.purchases: list[tuple[str, int]] = []

    def __repr__(self):
        return self.first_name + " " + self.last_name + " : Achats : " + str(self.purchases)

    def add_article(self, product: Product, quantity: int):
        self.purchases.append((product.name, quantity))
