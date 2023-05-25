from menu import products


def get_product_by_id(id):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

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


def menu_report():
    all_prices = len(products)
    sum_of_all_prices = 0

    for product in products:
        price = product["price"]
        sum_of_all_prices += price

    media = sum_of_all_prices / all_prices

    media_arredondada = round(media, 2)

    contagem_types = {}

    for product in products:
        typee = product["type"]

        if typee in contagem_types:
            contagem_types[typee] += 1
        else:
            contagem_types[typee] = 1

    type_more_common = max(contagem_types, key=contagem_types.get)

    return f"Products Count: {len(products)} - Average Price: ${media_arredondada} - Most Common Type: {type_more_common}"
