from menu import products


def get_product_by_id(product_id: int):
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")
    
    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(type_product: str) -> list:
    if not isinstance(type_product, str):
        raise TypeError("product type must be a str")  
    type_list = []
    for product in products:
        if product["type"] == type_product:
            type_list.append(product)
    return type_list


def add_product(menu, **product):
    new_id = 0
    if not menu:
        new_id = 1
    else:
        new_id = max(product['_id'] for product in menu) + 1
    product['_id'] = new_id
    menu.append(product)
    return product


def menu_report():
    count = len(products)
    avg_price = "${:,.2f}".format(sum([product['price'] for product in products]) / count)
    types = {}
    for product in products:
        type = product['type']
        if type not in types:
            types[type] = 0
        types[type] += 1
    most_common_type = max(types, key=types.get)
    report = f"Products Count: {count} - Average Price: {avg_price.rstrip('0')} - Most Common Type: {most_common_type}"
    return report







