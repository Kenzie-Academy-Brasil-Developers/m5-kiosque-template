from menu import products
def get_product_by_id(id: int):
    current_project = {}
    for product in products:
        if product["_id"] == id: 
            current_project = product
        else: current_project
    return current_project

    
def get_products_by_type(type: str):
    current_project = []
    for product in products:
        if product.get("type") == type: 
            current_project.append(product)
    return current_project


