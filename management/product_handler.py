from menu import products


def get_product_price_by_id(id):
    for product in products:
        if product['_id'] == id:
            return product['price']
    return 0


def get_product_by_id(id):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type):
    products_same_type = []
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    for product in products:
        if product['type'] == type:
            products_same_type.append(product)
    return products_same_type


def get_products():
    products_ids = []
    for product in products:
        products_ids.append(product['_id'])
    return products_ids

       
def add_product(products, **new_product):
    products_ids = get_products()
    if products == []:
        max_id = 0
    else:
        max_id = max(products_ids)
    max_id += 1
    new_product['_id'] = max_id
    products.append(new_product)
    return new_product


def menu_report():
    average_price = 0
    products_count = 0
    most_common_type = []
    total_price = 0    
    for product in products:
        products_count += 1
        total_price += product['price']
        most_common_type.append(product['type'])
    average_price = total_price / products_count
    average_price = round(average_price, 1)
    most_common_type = max(set(most_common_type), key=most_common_type.count)
    return f'Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}'


        

    
    
    


  
    