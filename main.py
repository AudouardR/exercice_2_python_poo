from product import Product
from client import Client


def choose_product():
    product_to_buy = None
    while product_to_buy is None:
        product_name = input("\nQuel produit le client souhaite acheter ? ")
        for product in Product.products:
            if product_name == product.name:
                product_to_buy = product
    return product_to_buy


def choose_quantity(product_to_buy: Product | None) -> int:
    quantity_is_valid = False
    quantity = None
    while not quantity_is_valid:
        quantity = input(
            f"\nquel quantité de {product_to_buy.name} le client souhaite-t-il acheter (en {product_to_buy.unit}) ?")
        if not quantity.isdigit():
            continue
        quantity = int(quantity)
        if product_to_buy.quantity >= quantity:
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
            day_over = True
            continue
        print("\nUn client arrive")

        client_first_name = input("Prénom du client : ")
        client_last_name = input("Nom du client : ")

        client_actuel = Client(client_first_name, client_last_name)

        purchasing(client_actuel)

        print(client_actuel)

        day_over = True if input("Voulez-vous continuer la journée ? (appuyez sur Entrée pour continuer, tapez n pour "
                                 "ne pas continuer) : ") == 'n' else False

    print("\nFin de la journée\n"
          f"Stock restant : {Product.products}\n"
          f"Bilan des achats de la journée : {Client.clients}")


def purchasing(client_actuel: Client):
    keep_purchasing = True
    while keep_purchasing:

        for p in Product.products:
            print(p)

        product_to_buy = choose_product()

        quantity = choose_quantity(product_to_buy)

        if quantity > 0:
            client_actuel.add_article(product_to_buy, quantity)
            product_to_buy.remove_quantity(quantity)

        print(f"\nPanier actuel : {client_actuel.purchases}")
        keep_purchasing = False if input("\nLe client souhaite-t-il acheter un autre article ? (o/n)") == "n" \
            else True


if __name__ == '__main__':
    init()
