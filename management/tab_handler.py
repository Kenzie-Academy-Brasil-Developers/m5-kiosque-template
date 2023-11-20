from menu import products


def calculate_tab(table_consumption):
    prices = {}
    subtotal = 0
    for product in products:
        prices[product['_id']] = product['price']
    for item in table_consumption:
        subtotal += prices[item['_id']] * item['amount']
    subtotal = round(subtotal, 2)
    return {'subtotal': f'${subtotal}'}
