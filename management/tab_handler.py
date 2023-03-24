from .product_handler import filter_products


def calculate_tab(list: list):

    calc = 0

    for element in list:
        product = filter_products(element["_id"], "_id")

        calc += (product[0]["price"] * element["amount"])
        ...
    return {'subtotal': f'${round(calc, 2)}'}
