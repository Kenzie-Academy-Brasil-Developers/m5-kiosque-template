from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(1))
    print(get_products_by_type("drink"))
