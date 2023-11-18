from menu import products


def get_product_by_id(id: int) -> dict:
    for product in products:
        if product['_id'] == id:
            return product
    return {}