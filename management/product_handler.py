from menu import products


def filter_products(id, key: str):

    def fiter_list(element):
        if element.get(key) == id:
            return True
        else:
            return False
        
    x = filter(fiter_list, products)
    
    for i in x:
        return (i)
    ...


def get_product_by_id(id: int):
    x = filter_products(id, "_id")

    if x: 
        return x
    else:
        return {}

