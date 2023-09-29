from .product_handler import get_product_by_id


def calculate_tab(order):
    total_price = 0

    for item in order:
        product_id = item['_id']
        amount = item['amount']

        product = get_product_by_id(product_id)

        if product:
            price = product['price']
            total_price += price * amount

    return {"subtotal": f"${round(total_price, 2)}"}
