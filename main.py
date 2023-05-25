from management.product_handler import (
    get_product_by_id,
    get_products_by_type,
    add_product,
    menu_report,
)
from management.tab_handler import calculate_tab
from menu import products

new_product_to_add = {
    "title": "X-Python",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de Python",
    "type": "fast-food",
}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]

if __name__ == "__main__":
    # print(get_product_by_id("vasco"))
    # print(get_products_by_type("drink"))
    # print(add_product(products, **new_product_to_add))
    # print(calculate_tab(table_1))
    # print(menu_report())
    ...
