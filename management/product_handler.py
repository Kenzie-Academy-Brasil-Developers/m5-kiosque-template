from menu import products


def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product
    return []


def get_products_by_type(type):
    products_founded = []
    for product in products:
        if product["type"] == type:
            products_founded.append(product)
    return products_founded


def add_product(menu, new_product):
    # Cria id
    if len(menu) == 0:
        new_product_id = 1
    else:
        last_product = menu[-1]
        new_product_id = last_product["_id"] + 1
    # Adiciona id ao produto
    new_product["_id"] = new_product_id
    # Adiciona o produto no menu
    menu.append(new_product)
    # Retorna o novo produto
    return new_product
