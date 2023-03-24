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
    x = filter_products(id, "_id")

    if x: 
        return x[0]
    else:
        return {}


def get_products_by_type(type: str):
    x = filter_products(type, "type")

    if x: 
        return x
    else:
        return []
    ...