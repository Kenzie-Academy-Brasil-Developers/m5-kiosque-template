from menu import products
from statistics import mode

def get_product_by_id(product_id: int):
    if type(product_id) is not int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == product_id:
            return product
    return {}

def get_products_by_type(product_type: str):
    matching_products = []
    if type(product_type) is not str:
        raise TypeError("product type must be a str")
    for product in products:
        if product["type"] == product_type:
            matching_products.append(product)
    return matching_products

def add_product(product_list: list, **new_product: dict):
    if product_list:
        max_id = max(product_list, key = lambda x: x["_id"])
        new_id = max_id["_id"] + 1
    else:
        new_id = 1
    new_product["_id"] = new_id
    product_list.append(new_product)
    return new_product

def menu_report():
    product_count = len(products)
    average_price = round(sum(product["price"] for product in products) / product_count, 2)
    most_common_type = mode(product["type"] for product in products)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"

def add_product_extra(product_list: list, *required_keys: tuple, **new_product: dict):
    for key in required_keys:
        if key not in new_product:
            raise KeyError(f"Field {key} is required")
    new_product = {key: new_product[key] for key in required_keys}
    return add_product(product_list, **new_product)