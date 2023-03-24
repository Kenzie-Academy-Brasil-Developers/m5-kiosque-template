from menu import products


def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(product_type):
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
