from management.tab_handler import calculate_tab
from menu import products
from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product

if __name__ == "__main__":
    # Seus prints de teste aqui

    print(get_product_by_id(15))

    print(get_products_by_type("drink"))

    product = {
        "description": "Healthy breakfast",
        "price": 15.10,
        "rating": 9999,
        "title": "Breakfast with cottage",
        "type": "fruit",
    }

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]

    print(add_product(products, **product))

    print(calculate_tab(table_1))
