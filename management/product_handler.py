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


