from menu import products


def get_product_by_id(product_id: int) -> dict:
    for product in products:
        if product['_id'] == product_id:
            return product
    return {}


def get_products_by_type(product_type: str) -> dict:
    filtered_products = []
    for product in products:
        if product['type'] == product_type:
            filtered_products.append(product)
    return filtered_products


def add_product(menu: list, **product_data: dict) -> dict:
    last_id = 0
    for product in menu:
        if product['_id'] > last_id:
            last_id = product['_id']
    product_data['_id'] = last_id + 1
    menu.append(product_data)
    return product_data
