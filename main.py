from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from management.product_handler import menu_report
from management.tab_handler import calculate_tab
from menu import products

new_product1 = {
    "title": "Bolinho JS",
    "price": 1.0,
    "rating": 2,
    "description": "Bolinho de JS com cenoura",
    "type": "bakery",
}

new_product2 = {
    "title": "Suco de React",
    "price": 5.0,
    "rating": 4,
    "description": "Suco de React com Limao",
    "type": "drink",
}

empty_list = []

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
table_2 = [
    {"_id": 10, "amount": 3},
    {"_id": 20, "amount": 2},
    {"_id": 21, "amount": 5},
]

if __name__ == "__main__":
    #print(get_product_by_id(28))
    # try:
    #     print(get_product_by_id([1, 2, 3]))
    # except TypeError as error:
    #     print(error)
    # try:
    #     print(get_product_by_id("test"))
    # except TypeError:
    #     print(get_product_by_id(10))
    #print(get_products_by_type("drink"))
    #print(add_product(products, **new_product1))
    #print(add_product(empty_list, **new_product2))
    #print(calculate_tab(table_1))
    print(menu_report())