from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type

# from .menu import products

if __name__ == "__main__":
    print(get_product_by_id(39))
    print(get_products_by_type("vegetab"))
    ...
