from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from menu import products
from management.tab_handler import calculate_tab
from management.product_handler import menu_report


if __name__ == "__main__":
    new_product: dict = {
        "title": "Suco de React",
        "price": 5.0,
        "rating": 4,
        "description": "Suco de React com Limao",
        "type": "drink",
    }
    
    print(add_product(products, **new_product))

    print(menu_report())
    
    print(get_products_by_type([1, 1, 3, 5]))
    ...
