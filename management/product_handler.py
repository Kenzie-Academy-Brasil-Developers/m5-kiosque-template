from menu import products

def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return product
    return {}

def get_products_by_type(product_type):
    matching_products = []
    for product in products:
        if product["type"] == product_type:
            matching_products.append(product)
    return matching_products

def add_product(product_list, new_product):
    if product_list:
        max_id = max(product_list, key = lambda x: x["_id"])
        new_id = max_id["_id"] + 1
    else:
        new_id = 1
    product = {"_id": new_id, **new_product}
    product_list.append(product)
    return product

def calculate_tab(consumptions):
    subtotal = 0.0
    for consumption in consumptions:
        product_id = consumption["_id"]
        amount = consumption["amount"]

        product = get_product_by_id(product_id)
        
        if product:
            price = product["price"]
            subtotal += price * amount
    return {"subtotal": "${:.2f}".format(subtotal)}