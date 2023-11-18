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

   