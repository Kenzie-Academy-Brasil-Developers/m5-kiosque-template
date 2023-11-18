from menu import products


def get_product_by_id(product_id: int) -> dict:
    for product in products:
        if product['_id'] == product_id:
            return product
    return {}


