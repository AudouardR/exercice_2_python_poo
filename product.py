from enum import Enum


class ProductType(Enum):
    FRUIT = "Fruit"
    VEGETABLE = "Légume"


class ProductUnit(Enum):
    KG = "kg"
    PIECE = "pièce"


class Product:
    products = []

    @classmethod
    def nb_products_on_sale(cls):
        return len(list(filter(lambda x: x.quantity > 0, cls.products)))

    def __init__(self, _name: str, _type: ProductType, _price: float, _quantity: int, _unit: ProductUnit):
        """
        :param _name: Nom du produit
        :param _type: Type du produit (Fruit ou légume)
        :param _price: Prix du produit
        :param _quantity: Quantité en stock
        :param _unit: Unité pour mesurer la quantité du produit (en kg ou en pièces)
        """
        self._name = _name
        self._type = _type
        self._price = _price
        self._quantity = _quantity
        self._unit = _unit
        Product.products.append(self)

    def __repr__(self):
        """
        Affichage du produit
        :return: Attributs du produit sous forme de texte
        """
        return f"{self._name}: {self._type.value}, {self._quantity} {self._unit.value}, {self._price} € / {self._unit.value}"

    def remove_quantity(self, value):
        """
        Retire une quantité donnée au produit
        :param value: Quantité à retirer du produit
        """
        self._quantity -= value

    @property
    def name(self) -> str:
        """
        :return: Nom du produit
        """
        return self._name

    @property
    def price(self) -> float:
        """
        :return: Prix du produit
        """
        return self._price

    @property
    def quantity(self) -> int:
        """
        :return: Quantité du produit
        """
        return self._quantity

    @property
    def unit(self) -> str:
        """
        :return: Unité pour mesurer la quantité du produit (en kg ou en pièces)
        """
        return self._unit
