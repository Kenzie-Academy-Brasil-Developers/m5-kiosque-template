from menu import products


def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type):
    all_products = []

    for product in products:
        if product["type"] == type:
            all_products.append(product)

    if len(all_products) == 0:
        return []
    else:
        return all_products


def add_product(menu: list, **args: dict):
    # full_object = {"_id": len(menu), **args}
    max_id = 0
    for elem in menu:
        id_atual = elem["_id"]

        if id_atual > max_id:
            max_id = id_atual

    print(max_id)

    args["_id"] = max_id + 1
    menu.append(args)

    return args
