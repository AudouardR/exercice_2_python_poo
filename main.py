from typing import Any

from product import Product
from client import Client


def choose_product(p):
    product_name_is_valid = False
    product_to_buy = None
    while not product_name_is_valid:
        product_name = input("\nQuel produit le client souhaite acheter ? ")
        for product in Product.products:
            if product_name == product.name:
                product_to_buy = product
                product_name_is_valid = True
    return product_to_buy


def choose_quantity(product_to_buy: Product | None) -> int:
    quantity_is_valid = False
    quantity = None
    while not quantity_is_valid:
        quantity = input(f"\nquel quantité de {product_to_buy.name} le client souhaite-t-il acheter (en {product_to_buy.unit}) ?")
        if not quantity.isdigit():
            continue
        quantity = int(quantity)
        if product_to_buy.quantity >= quantity:
            quantity_is_valid = True
    return quantity


def init():
    f1 = Product("Clémentine", "Fruit", 2.90, 6, "kg")
    f2 = Product("Datte", "Fruit", 7.00, 4, "kg")
    f3 = Product("Grenade", "Fruit", 3.50, 3, "kg")
    f4 = Product("Kaki", "Fruit", 4.50, 3, "kg")
    f5 = Product("Kiwi", "Fruit", 3.50, 5, "kg")
    f6 = Product("Mandarine", "Fruit", 2.80, 6, "kg")
    f7 = Product("Orange", "Fruit", 1.50, 8, "kg")
    f8 = Product("Pamplemousse", "Fruit", 2.00, 8, "pièces")
    f9 = Product("Poire", "Fruit", 2.50, 5, "kg")
    f10 = Product("Pomme", "Fruit", 1.50, 8, "kg")

    l1 = Product("Carotte", "Légume", 1.3, 7, "kg")
    l2 = Product("Choux de Bruxelles", "Légume", 4.0, 4, "kg")
    l3 = Product("Chou vert", "Légume", 2.5, 12, "pièce")
    l4 = Product("Courge butternut", "Légume", 2.5, 6, "pièce")
    l5 = Product("Endive", "Légume", 2.5, 5, "kg")
    l6 = Product("Epinard", "Légume", 2.6, 4, "kg")
    l7 = Product("Poireau", "Légume", 1.2, 5, "kg")
    l8 = Product("Potiron", "Légume", 2.5, 6, "pièces")
    l9 = Product("Radis noir", "Légume", 5.0, 10, "pièces")
    l10 = Product("Salsifis", "Légume", 2.5, 3, "kg")

    day_over = False

    while not day_over:
        print("\nUn client arrive")

        client_first_name = input("Prénom du client : ")
        client_last_name = input("Nom du client : ")

        client_actuel = Client(client_first_name, client_last_name)

        keep_purchasing = True
        while keep_purchasing:

            for p in Product.products:
                print(p)

            product_to_buy = choose_product(p)

            quantity = choose_quantity(product_to_buy)

            if quantity > 0:
                client_actuel.add_article(product_to_buy, quantity)
                product_to_buy.remove_quantity(quantity)

            print(f"\nPanier actuel : {client_actuel.purchases}")
            keep_purchasing = False if input("\nLe client souhaite-t-il acheter un autre article ? (o/n)") == "n" \
                else True

        print(client_actuel)

        day_over = True if input("Voulez-vous continuer la journée ? (appuyez sur Entrée pour continuer, tapez n pour "
                                 "ne pas continuer) : ") == 'n' else False

    print("\nFin de la journée\n"
          f"Stock restant : {Product.products}\n"
          f"Bilan des achats de la journée : {Client.clients}")


if __name__ == '__main__':
    init()