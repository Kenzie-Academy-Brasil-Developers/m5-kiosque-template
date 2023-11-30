from menu import products


def calculate_tab(consumos: list) -> dict:
    subtotal = 0.0

    # # price = {product['_id']: product['price'] for product in products}
    # product_price = {consumos['_id']: product['price'] for product in products}
    # print(product_price[21], 'Linha 9')
    # print(product_price[consumos['_id']], '<-- Linha10')

    # # for product in product_price:
    # #     print(product)
    # subtotal = product_price[consumos['_id']] * consumos['amount']
    # # print(product_price)
    # # print(type(subtotal))

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
