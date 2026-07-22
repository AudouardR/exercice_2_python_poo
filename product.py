class Product:
    products = []

    @classmethod
    def nb_products(cls):
        return len(cls.products)

    def __init__(self, _name: str, _type: str, _price: float, _quantity: int, _unit: str):
        self._name = _name
        self._type = _type
        self._price = _price
        self._quantity = _quantity
        self._unit = _unit
        Product.products.append(self)

    def __repr__(self):
        return f"{self._name}: {self._type}, {self._quantity} {self._unit}, {self._price} € / {self._unit}"

    def remove_quantity(self, value):
        self._quantity -= value

    @property
    def name(self) -> str:
        return self._name
