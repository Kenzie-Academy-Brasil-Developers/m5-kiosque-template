from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from menu import products

new_product1 = {
    "title": "Bolinho JS",
    "price": 1.0,
    "rating": 2,
    "description": "Bolinho de JS com cenoura",
    "type": "bakery",
}

if __name__ == "__main__":
    print(get_product_by_id(28))
    print(get_products_by_type("drink"))
    print(add_product(products, new_product1))
