from menu import products
from main import menu


def verify_id(id) -> int:
    typeId = type(id)
    if typeId != int:
        raise TypeError('product id must be an int')
    return id


def verify_str(type: str) -> str:
    if type != str:
        raise TypeError('product type must be a str')
    return type


def get_product_by_id(id: int) -> dict:
    if id is not int:
        raise TypeError('product id must be an int')

    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type: str):
    if type is not str:
        raise TypeError('product type must be a str')
       
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

    return kwargs


def menu_report():
    if not products:
        return 'No products avaliable.'
    product_count = len(products)

    average_price = round(sum(product['price'] for product in products) / product_count, 2)

    type_count = {}

    for product in products:
        type_count[product['type']] = type_count.get(product['type'], 0) + 1
        
    most_common_type = max(type_count, key=type_count.get)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
