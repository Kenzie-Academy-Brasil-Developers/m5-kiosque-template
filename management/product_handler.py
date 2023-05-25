from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    products_founded = []
    for product in products:
        if product["type"] == type:
            products_founded.append(product)
    return products_founded


def add_product(menu, **kwargs):
    # Cria id
    if len(menu) == 0:
        new_product_id = 1
    else:
        last_product = menu[-1]
        new_product_id = last_product["_id"] + 1
    # Adiciona id ao produto
    kwargs["_id"] = new_product_id
    # Adiciona o produto no menu
    menu.append(kwargs)
    # Retorna o novo produto
    return kwargs


def menu_report():
    # Contagem de produtos
    total_products = len(products)

    # Media dos preços
    prices_products = []
    for product in products:
        prices_products.append(product["price"])
    soma_prices = sum(prices_products)
    average_prices = round(soma_prices / total_products, 2)

    # Tipo mais comum
    # Faz a contagem do numero de cada tipo
    type_counts = {}
    for product in products:
        product_type = product["type"]
        if product_type in type_counts:
            type_counts[product_type] += 1
        else:
            type_counts[product_type] = 1

    # Descobre qual o tipo de maior numero
    max_count = max(type_counts.values())
    most_common_type = None
    for product_type, count in type_counts.items():
        if count == max_count:
            most_common_type = product_type
            break
    report_string = f"Products Count: {total_products} - Average Price: ${average_prices} - Most Common Type: {most_common_type}"
    return report_string


def add_product_extra(menu, *args, **kwargs):
    new_product = kwargs
    required_keys = args
    # Remove as chaves não obrigatórias do novo produto
    for key in list(new_product.keys()):
        if key not in required_keys:
            new_product.pop(key)
    # Verifica se todas as chaves obrigatórias estão presentes no novo produto
    missing_keys = [key for key in required_keys if key not in new_product]
    if missing_keys:
        raise KeyError(f"field {', '.join(missing_keys)} is required")
    # Cria id
    if len(menu) == 0:
        new_product_id = 1
    else:
        last_product = menu[-1]
        new_product_id = last_product["_id"] + 1
    # Adiciona id ao produto
    new_product["_id"] = new_product_id
    # Adiciona o produto no menu
    menu.append(new_product)
    # Retorna o novo produto
    return new_product
