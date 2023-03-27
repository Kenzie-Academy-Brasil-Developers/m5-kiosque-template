from menu import products


def calculate_tab(table):
    prices = {}
    for product in products:
        prices[product["_id"]] = product["price"]
    subtotal = 0
    for item in table:
        _id, amount = item["_id"], item["amount"]
        subtotal += prices[_id] * amount
    subtotal_formatted = f"${subtotal:.2f}".rstrip('0')
    return {"subtotal": subtotal_formatted}
