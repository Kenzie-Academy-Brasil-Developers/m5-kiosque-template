from management.product_handler import get_product_price_by_id


def calculate_tab(table):
    subtotal = 0
    for item in table:
        price = get_product_price_by_id(item['_id'])
        subtotal += price * item['amount'] 
    formatted_subtotal = f'${subtotal:.2f}'
    if formatted_subtotal.endswith('0'):
        formatted_subtotal = formatted_subtotal[:-1]

    return {'subtotal': formatted_subtotal}
