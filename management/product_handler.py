from menu import products


def filter_products(id, key: str):

    def fiter_list(element):
        if element.get(key) == id:
            return True
        else:
            return False
        
    x = filter(fiter_list, products)

    list = []
    
    for i in x:
        list.append(i)
    
    return list


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
     
    x = filter_products(id, "_id")

    if x: 
        return x[0]
    else:
        return {}


def get_products_by_type(type: str):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    x = filter_products(type, "type")

    if x:
        return x
    else:
        return []
    
    ...


def add_product(menu_list: list, **payload: dict):
    list = []

    for element in menu_list:
        list.append(element["_id"])
        ...

    print(list)

    if list:
        big = max(list)

        payload["_id"] = big + 1
    else:

        payload["_id"] = 1

    menu_list.append(payload)

    return payload


def menu_report():
    product_count = len(products)

    average_price: int = 0

    for element in products:
        average_price += element["price"]
        ...
    
    average_price = round(average_price / product_count, 1)

    list_key = [d["type"] for d in products]

    count = max(list_key, key=list_key.count)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {count}"