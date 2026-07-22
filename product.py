class Product:
    products = []

    @classmethod
    def nb_products(cls):
        return len(cls.products)

    def __init__(self, name: str, type: str, price: float, quantity: int, unit: str):
        self.name = name
        self.type = type
        self.price = price
        self.quantity = quantity
        self.unit = unit
        Product.products.append(self)

    def remove_quantity(self, value):
        self.quantity -= value

