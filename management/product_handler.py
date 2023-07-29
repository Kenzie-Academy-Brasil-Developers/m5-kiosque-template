from menu import products


def get_product_by_id(id: int):
    for item in products:
        if item["_id"] == id:
            return item
    
    return {}
        

def get_products_by_type(type: str):
    found_products = []
    for item in products:
        if item["type"] == type:
            found_products.append(item)
    
    return found_products