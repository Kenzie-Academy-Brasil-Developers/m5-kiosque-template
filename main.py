# from menu import products
# from management import product_handler
from management.tab_handler import calculate_tab


if __name__ == "__main__":
    # print(product_handler.get_product_by_id(25))
    # print(product_handler.get_products_by_type('vegetable'))
    # product_data = {
    #     'description': 'Teste',
    #     'price': 50.55,
    #     'rating': 1,
    #     'title': 'Testando',
    #     'type': 'vegetable',
    # }
    # print(product_handler.add_product(products, **product_data))
    # product_data = {
    #     'description': 'Testando',
    #     'price': 500.30,
    #     'rating': 2,
    #     'title': 'Outro',
    #     'type': 'vegetable',
    # }
    # print(product_handler.add_product(products, **product_data))
    table_consumption_1 = [
        {'_id': 25, 'amount': 17},
        {'_id': 8, 'amount': 12},
        {'_id': 20, 'amount': 16},
    ]
    table_consumption_2 = [
        {'_id': 32, 'amount': 27},
        {'_id': 30, 'amount': 32},
        {'_id': 44, 'amount': 45},
    ]    
    print(calculate_tab(table_consumption_1))
    print(calculate_tab(table_consumption_2))
