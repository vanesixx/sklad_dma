products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)


def search_product():
    search_term = input("Napiš část názvu produktu:").lower()
    found_products = []
    for product in products:
        if search_term in product['name'].lower():
            found_products.append(product)

    if len(found_products) > 0:
        for product in found_products:
            print(f"Název produktu2: {product['name']}, cena: {product['price']}$")
        else:
            print("Nebyly nalezeny žádné produkty.")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky\n")
    print("3. Vyhledat položku")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání poožky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledat položku:")
        search_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
