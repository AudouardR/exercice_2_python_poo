from product import Product
from client import Client

if __name__ == '__main__':
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

    for p in Product.products:
        print(p)

    day_over = False

    while not day_over:
        print("\nUn client arrive")

        client_first_name = input("Prénom du client : ")
        client_last_name = input("Nom du client : ")

        client_actuel = Client(client_first_name, client_last_name)

        client_actuel.add_article(f8, 4)
        print(client_actuel)

        day_over = True if input("Voulez-vous continuer la journée ? (appuyez sur Entrée pour continuer, tapez n pour ne pas continuer) : ") == 'n' else False