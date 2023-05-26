from management.product_handler import get_product_by_id

def calculate_tab(consumptions: list):
    subtotal = 0.0
    for consumption in consumptions:
        product_id = consumption["_id"]
        amount = consumption["amount"]

        product = get_product_by_id(product_id)
        
        if product:
            price = product["price"]
            subtotal += price * amount
    return {"subtotal": f"${round(subtotal, 2)}"}