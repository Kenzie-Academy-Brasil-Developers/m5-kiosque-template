from menu import products


def get_product_by_id(id: int):
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(product_type: str):
    products_list = []
    for product in products:
        if product["type"] == product_type:
            products_list.append(product)
    return products_list
