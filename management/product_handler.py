from menu import products


def get_product_by_id(id):
    
    for product in products:
        if product['_id'] == id:
            return product

    return {}


def get_products_by_type(type):
    all_products = []

    for product in products:
        if product['type'] == type:
            all_products.append(product)
        
    if len(all_products) == 0:
        return []
    else:
        return all_products