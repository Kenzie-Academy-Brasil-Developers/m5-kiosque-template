from menu import products

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]


def calculate_tab(dic_table):
    # Recupera os valores dos produtos consumidos
    prices_products = []
    for table in dic_table:
        for product in products:
            if product["_id"] == table["_id"]:
                prices_products.append(product["price"])
    # Soma os valores dos produtos consumidos
    soma_total = round(sum(prices_products), 2)
    return {"subtotal": f"${soma_total}"}
