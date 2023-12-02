from menu import products


def calculate_tab(consumos: list) -> dict:
    subtotal = 0.0

    for product in products:
        product['_id']
        for consumo in consumos:
            if consumo['_id'] == product['_id']:
                print(product)
                price = product['price']
                consumo_mult = consumo['amount']
                subtotal += price * consumo_mult
    print(subtotal)
    result_finally = round(subtotal, 2)

    return {"subtotal": f'${result_finally}'}
