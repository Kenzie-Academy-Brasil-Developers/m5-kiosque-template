from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(product_type):
    if type(product_type) != str:
        raise TypeError("product type must be a str")
    products_list = []
    for product in products:
        if product["type"] == product_type:
            products_list.append(product)
    return products_list


def add_product(menu, **new_product):
    all_ids = []

    if len(menu) == 0:
        added_product = {"_id": 1, **new_product}
        menu.append(added_product)
        return added_product

    for product_id in menu:
        all_ids.append(product_id["_id"])

    max_id = max(all_ids)

    if len(menu) > 0:
        added_product = {"_id": max_id + 1, **new_product}
        menu.append(added_product)
        return added_product


def menu_report():
    products_count = len(products)
    products_sum = 0
    products_type = []

    for product in products:
        products_sum += product["price"]
        products_type.append(product["type"])   
    most_common_type = 0
    most_common_type_name = ""

    for product_type in products_type:
        if products_type.count(product_type) > most_common_type:
            most_common_type = products_type.count(product_type)
            most_common_type_name = product_type

    average_price = round(products_sum/products_count, 2)

    return f"Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: {most_common_type_name}"
