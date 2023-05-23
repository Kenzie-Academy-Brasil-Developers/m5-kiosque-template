from menu import products

def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return product
    return None

def get_products_by_type(product_type):
    matching_products = []
    for product in products:
        if product["type"] == product_type:
            matching_products.append(product)
    return matching_products