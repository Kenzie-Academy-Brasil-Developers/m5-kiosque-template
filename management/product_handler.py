from menu import products

def get_product_by_id(int_id):
    for list_id in products:
        if list_id["_id"] == int_id:
            return dict(list_id)
    return {}

def get_products_by_type(str_type):
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