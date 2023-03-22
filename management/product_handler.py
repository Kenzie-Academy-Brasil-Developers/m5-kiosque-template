from menu import products

def get_product_by_id(int_id):
    for list_id in products:
        if list_id["_id"] == int_id:
            return list_id
        else:
            return None

def get_products_by_type(str_type):
    empty_list = []
    for list_type in products:
        if list_type["type"] == str_type:
            empty_list.append(list_type)
    return empty_list