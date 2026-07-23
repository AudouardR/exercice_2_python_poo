from product import Product, ProductType, ProductUnit
from client import Client


def choose_product(current_client):
    product_to_buy = None
    while product_to_buy is None:
        product_name = input(f"\nQuel produit { current_client.first_name } { current_client.last_name } souhaite acheter ? : ")
        for product in filter(lambda x: x.quantity > 0, Product.products):
            if product_name.lower() == product.name.lower():
                product_to_buy = product
                return product_to_buy
        print(f"Le produit {product_name.lower()} n'est pas disponible")
    return product_to_buy


def choose_quantity(product_to_buy: Product | None, current_client) -> int:
    quantity_is_valid = False
    quantity = None
    while not quantity_is_valid:
        quantity = input(
            f"\nQuelle quantité (en {product_to_buy.unit.value}) { current_client.first_name } { current_client.last_name } souhaite acheter ? (Entrez 0 pour annuler l'achat) : ")
        if not quantity.isdigit():
            print("Saisie invalide : Entrez un nombre entier positif")
            continue
        quantity = int(quantity)
        if product_to_buy.quantity < quantity:
            print(f"{ current_client.first_name } { current_client.last_name } ne peut pas acheter {quantity} {product_to_buy.unit.value} de ce produit (Quantité restante : {product_to_buy.quantity} {product_to_buy.unit.value})")
            continue
        quantity_is_valid = True
    return quantity


def init():
    Product("Clémentine", ProductType.FRUIT, 2.90, 6, ProductUnit.KG)
    Product("Datte", ProductType.FRUIT, 7.00, 4, ProductUnit.KG)
    Product("Grenade", ProductType.FRUIT, 3.50, 3, ProductUnit.KG)
    Product("Kaki", ProductType.FRUIT, 4.50, 3, ProductUnit.KG)
    Product("Kiwi", ProductType.FRUIT, 3.50, 5, ProductUnit.KG)
    Product("Mandarine", ProductType.FRUIT, 2.80, 6, ProductUnit.KG)
    Product("Orange", ProductType.FRUIT, 1.50, 8, ProductUnit.KG)
    Product("Pamplemousse", ProductType.FRUIT, 2.00, 8, ProductUnit.PIECE)
    Product("Poire", ProductType.FRUIT, 2.50, 5, ProductUnit.KG)
    Product("Pomme", ProductType.FRUIT, 1.50, 8, ProductUnit.KG)

    Product("Carotte", ProductType.VEGETABLE, 1.3, 7, ProductUnit.KG)
    Product("Choux de Bruxelles", ProductType.VEGETABLE, 4.0, 4, ProductUnit.KG)
    Product("Chou vert", ProductType.VEGETABLE, 2.5, 12, ProductUnit.PIECE)
    Product("Courge butternut", ProductType.VEGETABLE, 2.5, 6, ProductUnit.PIECE)
    Product("Endive", ProductType.VEGETABLE, 2.5, 5, ProductUnit.KG)
    Product("Epinard", ProductType.VEGETABLE, 2.6, 4, ProductUnit.KG)
    Product("Poireau", ProductType.VEGETABLE, 1.2, 5, ProductUnit.KG)
    Product("Potiron", ProductType.VEGETABLE, 2.5, 6, ProductUnit.PIECE)
    Product("Radis noir", ProductType.VEGETABLE, 5.0, 10, ProductUnit.PIECE)
    Product("Salsifis", ProductType.VEGETABLE, 2.5, 3, ProductUnit.KG)

    work_day()


def work_day():
    day_over = False
    while not day_over:

        if Product.nb_products() == 0:
            print("Le magasin n'a rien à vendre.")
            break

        print("\nUn client arrive\n")

        client_first_name = input("Prénom du client : ")
        client_last_name = input("Nom du client : ")

        current_client = Client(client_first_name, client_last_name)
        print()

        purchasing(current_client)

        print(current_client)

        if Product.nb_products() == 0:
            print("Le magasin est en rupture de stock")
            break

        day_over = True if input("Voulez-vous continuer la journée ? (appuyez sur Entrée pour continuer, tapez n pour "
                                 "ne pas continuer) : ") == 'n' else False

    print("\nFin de la journée\n")
    print("Stock restant : ")
    for p in filter(lambda x: x.quantity > 0, Product.products):
        print(p)
    print("\nBilan des achats de la journée : ")
    for c in Client.clients:
        print(c)
    print(f"Chiffre d'affaires total : { Client.total_revenue() } €")



def purchasing(current_client: Client):
    keep_purchasing = True
    while keep_purchasing:
        for p in filter(lambda x: x.quantity > 0, Product.products):
            print(p)

        product_to_buy = choose_product(current_client)

        quantity = choose_quantity(product_to_buy, current_client)

        if quantity > 0:
            current_client.add_article(product_to_buy, quantity)
            product_to_buy.remove_quantity(quantity)

        if Product.nb_products() == 0:
            break

        print(f"\nPanier actuel : \n{current_client}")
        keep_purchasing = False if input(f"\nEst-ce que { current_client.first_name } { current_client.last_name } souhaite acheter un autre article ? (o/n) : ") == "n" \
            else True


if __name__ == '__main__':
    init()
