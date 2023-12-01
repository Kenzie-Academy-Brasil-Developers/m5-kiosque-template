from management import tab_handler, product_handler
# from management import product_handler

menu = []

if __name__ == "__main__":
    # product_handler.get_product_by_id(50)
    # print(product_handler.get_product_by_id(25))
    # print(product_handler.get_products_by_type('fruit'))
    new_product = {
        "description": "Homemade healthy caprese salad withbasil",
        "price": 16.76,
        "rating": 5,
        "title": "Caprese salad",
        "type": "vegetable"
    }

    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    product_handler.add_product(menu, **new_product)
    print(tab_handler.calculate_tab(table_2))
    print(product_handler.menu_report())
