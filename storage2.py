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


def total_price():
    total_price = 0
    for product in products:
        total_price += product['price'] * product['price']
    print(f"Celková cena všech produktů: {total_price}$")


def cheapest_product():
    if len(products) > 0:
        min_price = min(product['price'] for product in products)
        for product in products:
            if product['price'] == min_price:
                print(f"Nejlevnější produkt: {product['name']}, cena: {product['price']}$")

    else:
        print("Žádné produkty.")

def most_expensive_product():
    if len(products) > 0:
        max_price = max(product['price'] for product in products)
        for product in products:
            if product['price'] == max_price:
                print(f"Nejdražší produkt: {product['name']}, cena: {product['price']}$")

    else:
        print("Žádné produkty.")


def avarage_price():
    if len(products) > 0:
        total_price = 0
        for product in products:
            total_price += product['price']
        avg = total_price / len(products)
        print(f"Průměrná cena: {avg}$")

    else:
        print("Žádné produkty.")

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Vyhledat položku")
    print("4. Zobrazit celkovou cenu")
    print("5. Zobrazit nejlevnější produkt")
    print("6. Zobrazit nejdražší produkt")
    print("7. Průměrná cena")

    choice = int(input("\nVolba: "))

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

    elif choice == 4:
        print("Zobrazit celkovou cenu:")
        total_price()
        print("")
        menu()

    elif choice == 5:
        print("Zobrazit nejlevnější produkt:")
        cheapest_product()
        print("")
        menu()

    elif choice == 6:
        print("Zobrazit nejdražší produkt:")
        most_expensive_product()
        print("")
        menu()

    elif choice == 7:
        print("Průměrná cena:")
        avarage_price()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
