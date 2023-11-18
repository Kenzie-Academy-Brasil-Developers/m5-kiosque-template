from management import product_handler
from management import tab_handler

if __name__ == "__main__":
    product_handler.get_product_by_id()
    product_handler.get_products_by_type()
    product_handler.add_product()
    tab_handler.calculate_tab()