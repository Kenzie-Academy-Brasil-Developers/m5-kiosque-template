from menu import products


def calculate_tab(table):
    total_products = []
    for consumers_products in table:
        for product in products:
            if (consumers_products["_id"] == product["_id"]):
                total_products.append(product["price"]*consumers_products["amount"])
    subtotal = sum(total_products)
    return {"subtotal": f'${round(subtotal, 2)}'}
