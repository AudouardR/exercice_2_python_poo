class Product:
    products = []

    @classmethod
    def nb_products(cls):
        return len(cls.products)

    def __init__(self, _name: str, type: str, price: float, quantity: int, unit: str):
        self._name = _name
        self.type = type
        self.price = price
        self.quantity = quantity
        self.unit = unit
        Product.products.append(self)

    def remove_quantity(self, value):
        self.quantity -= value

    @property
    def name(self) -> str:
        return self._name
