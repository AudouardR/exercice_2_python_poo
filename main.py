from product import Product
from client import Client


def choose_product(current_client):
    product_to_buy = None
    while product_to_buy is None:
        product_name = input(f"\nQuel produit { current_client.first_name } { current_client.last_name } souhaite acheter ? : ")
        for product in Product.products:
            if product_name.lower() == product.name.lower():
                product_to_buy = product
                return product_to_buy
        print(f"Le produit {product_name.lower()} n'existe pas")
    return product_to_buy


def choose_quantity(product_to_buy: Product | None, current_client) -> int:
    quantity_is_valid = False
    quantity = None
    while not quantity_is_valid:
        quantity = input(
            f"\nQuelle quantité (en {product_to_buy.unit}) { current_client.first_name } { current_client.last_name } souhaite acheter ? (Entrez 0 pour annuler l'achat) : ")
        if not quantity.isdigit():
            print("Saisie invalide : Entrez un nombre entier positif")
            continue
        quantity = int(quantity)
        if product_to_buy.quantity < quantity:
            print(f"{ current_client.first_name } { current_client.last_name } ne peut pas acheter {quantity} {product_to_buy.unit} de ce produit (Quantité restante : {product_to_buy.quantity} {product_to_buy.unit})")
            continue
        quantity_is_valid = True
    return quantity


def init():
    Product("Clémentine", "Fruit", 2.90, 6, "kg")
    Product("Datte", "Fruit", 7.00, 4, "kg")
    Product("Grenade", "Fruit", 3.50, 3, "kg")
    Product("Kaki", "Fruit", 4.50, 3, "kg")
    Product("Kiwi", "Fruit", 3.50, 5, "kg")
    Product("Mandarine", "Fruit", 2.80, 6, "kg")
    Product("Orange", "Fruit", 1.50, 8, "kg")
    Product("Pamplemousse", "Fruit", 2.00, 8, "pièces")
    Product("Poire", "Fruit", 2.50, 5, "kg")
    Product("Pomme", "Fruit", 1.50, 8, "kg")

    Product("Carotte", "Légume", 1.3, 7, "kg")
    Product("Choux de Bruxelles", "Légume", 4.0, 4, "kg")
    Product("Chou vert", "Légume", 2.5, 12, "pièce")
    Product("Courge butternut", "Légume", 2.5, 6, "pièces")
    Product("Endive", "Légume", 2.5, 5, "kg")
    Product("Epinard", "Légume", 2.6, 4, "kg")
    Product("Poireau", "Légume", 1.2, 5, "kg")
    Product("Potiron", "Légume", 2.5, 6, "pièces")
    Product("Radis noir", "Légume", 5.0, 10, "pièces")
    Product("Salsifis", "Légume", 2.5, 3, "kg")

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
    print(f"Stock restant : {Product.products}\n")
    print(f"Bilan des achats de la journée : {Client.clients}")


def purchasing(current_client: Client):
    keep_purchasing = True
    while keep_purchasing:
        for p in Product.products:
            print(p)

        product_to_buy = choose_product(current_client)

        quantity = choose_quantity(product_to_buy, current_client)

        if quantity > 0:
            current_client.add_article(product_to_buy, quantity)
            product_to_buy.remove_quantity(quantity)

        if Product.nb_products() == 0:
            break

        print(f"\nPanier actuel : {current_client.purchases}")
        keep_purchasing = False if input(f"\nEst-ce que { current_client.first_name } { current_client.last_name } souhaite acheter un autre article ? (o/n) : ") == "n" \
            else True


if __name__ == '__main__':
    init()
