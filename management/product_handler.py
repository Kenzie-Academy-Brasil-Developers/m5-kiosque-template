from menu import products


def get_product_by_id(id: int) -> dict:
    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type: str):
    filtered_products = []

    for product in products:
        if product['type'] == type:
            filtered_products.append(product)
    return filtered_products


def add_product(menu: list, **kwargs: dict) -> list:

    if not menu:
        new_id = 1
    else:
        max_id = max([product.get('_id', 0) for product in products], default=0)
        new_id = max_id + 1

    kwargs['_id'] = new_id
    menu.append(kwargs)
    print(menu)

    return kwargs

