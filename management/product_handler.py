from menu import products


def get_product_by_id(produt_id):
    if type(produt_id) is not int:
        raise TypeError("Product id must be integer")

    for product in products:
        if product["_id"] == produt_id:
            return product

    return {}


def get_products_by_type(product_type):
    if type(product_type) is not str:
        raise TypeError("Product id must be a str")

    results = []

    for product in products:
        if product["type"] == product_type:
            results.append(product)
    return results
