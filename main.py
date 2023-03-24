from .management.product_handler import get_product_by_id, get_products_by_type
from menu import products


if __name__ == "__main__":

    print(get_product_by_id(28))
    print(get_product_by_id(300))
    print(get_products_by_type("drink"))
    print(get_products_by_type("milk"))
