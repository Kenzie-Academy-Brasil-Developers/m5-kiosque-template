from menu import products

def get_product_by_id(int_id):
    if type(int_id) != int:
        raise TypeError("product id must be an int")
    for list_id in products:
        if list_id["_id"] == int_id:
            return dict(list_id)
    return {}

def get_products_by_type(str_type):
    if type(str_type) != str:
        raise TypeError("product type must be a str")
    empty_list = []
    for list_type in products:
        if list_type["type"] == str_type:
            empty_list.append(list_type)
    return empty_list

def add_product(menu: list, **list_menu: dict):
    new_id = 0
    for list in range(0, len(menu)):
        if menu[list]["_id"] > new_id:
            new_id = menu[list]["_id"]
    list_menu.update({"_id": new_id + 1})
    menu.append(list_menu)
    return list_menu

def menu_report():
    product_count = len(products)
    average_price = 0
    most_common_type = []
    for list in products:
        average_price += list["price"]
        most_common_type.append(list["type"])
    most_common_type_count = tuple(most_common_type)
    average_price = round((average_price/product_count), 2)
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type_count[0]}"
    
