from product import Product


class Client:
    """
    Représente un client et ses achats

    Attributs
    ----------
    first_name : str
        Prénom du client
    last_name : str
        Nom du client
    purchases : dict[Product, int]
        Liste des achats effectués par le client

    Méthodes
    ---------
    add_article(product, quantitity)
        Ajoute un article est la quantité achetée à la liste des achats

    """
    clients = []

    @classmethod
    def total_revenue(cls):
        return sum(client.cart_price() for client in cls.clients)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.purchases: dict[Product, int] = {}
        self.clients.append(self)

    def __repr__(self):
        display = self.first_name + " " + self.last_name + " : \n"
        for key, value in self.purchases.items():
            display += key.name + ": " + str(value) + " " + key.unit.value + " (" + str(key.price * value) + " €)" + "\n"
        display += "Total : " + str(self.cart_price()) + " €\n"
        return display

    def add_article(self, product: Product, quantity: int):
        if product in self.purchases:
            self.purchases[product] += quantity
            return
        self.purchases[product] = quantity

    def cart_price(self) -> float:
        return sum(value * key.price for key, value in self.purchases.items())