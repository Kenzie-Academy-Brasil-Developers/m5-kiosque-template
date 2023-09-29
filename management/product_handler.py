from menu import products


def get_product_by_id(product_id):
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    products_list = [product for product in products if product["type"] == type]

    return products_list


def add_product(products, **new_product):
    if not products:
        new_product["_id"] = 1
    else:
        ultimo_id = products[-1]["_id"]
        new_product["_id"] = ultimo_id + 1

    products.append(new_product)
    return new_product


def menu_report():
    products_count = len(products)
    average_price = calculate_average_price(products)
    most_common_type = find_most_common_type(products)

    report = f"Products Count: {products_count} - Average Price: ${average_price:.1f} - Most Common Type: {most_common_type}"
    return report


def calculate_average_price(products):
    if not products:
        return 0.0

    total_price = sum(product["price"] for product in products)
    return total_price / len(products)


def find_most_common_type(products):
    if not products:
        return "N/A"

    type_counts = {}
    for product in products:
        product_type = product.get("type", "N/A")
        type_counts[product_type] = type_counts.get(product_type, 0) + 1

    common_type = max(type_counts, key=type_counts.get)
    return common_type
