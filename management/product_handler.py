from menu import products

def get_product_by_id( id: int ) -> dict:
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type_filter: str) -> dict:
    filtered_products = []
    for product in products:
        if product["type"] == type_filter:
            filtered_products.append(product)
    return filtered_products

def add_product(menu, **kwargs):
    if not menu:
        last_id = 0
    else:
        last_id = max(product["_id"] for product in menu)

    new_product = {"_id": last_id + 1}
    new_product.update(kwargs)
    
    menu.append(new_product)
    return new_product


