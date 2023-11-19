from menu import products

def get_product_by_id( id: int ) -> dict:
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}

def get_products_by_type(type_filter: str) -> dict:
    if not isinstance(type_filter, str):
        raise TypeError("product type must be a str")
    filtered_products = []
    for product in products:
        if product["type"] == type_filter:
            filtered_products.append(product)
    return filtered_products

def add_product(menu, **kwargs):
    if not menu:
        last_id = 0
    else:
        last_id = max(product["_id"] for product in menu)

    new_product = {"_id": last_id + 1}
    new_product.update(kwargs)
    
    menu.append(new_product)
    return new_product

def menu_report() -> str:
    if not products:
        return "Products Count: 0 - Average Price: $0.00 - Most Common Type: N/A"

    product_count = len(products)

    total_price = sum(product["price"] for product in products)
    average_price = total_price / product_count if product_count > 0 else 0
    average_price = round(average_price, 1)

    type_counts = {}
    for product in products:
        product_type = product["type"]
        type_counts[product_type] = type_counts.get(product_type, 0) + 1
    most_common_type = max(type_counts, key=type_counts.get)

    report = f"Products Count: {product_count} - Average Price: ${average_price:.1f} - Most Common Type: {most_common_type}"
    return report

