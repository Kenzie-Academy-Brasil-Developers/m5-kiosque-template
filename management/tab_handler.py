from builtins import round 
from management import product_handler

def calculate_tab(consumptions):
    subtotal = 0.0

    for consumption in consumptions:
        
        product_id = consumption["_id"]
        quantity = consumption["amount"]

        unit_price = product_handler.get_product_by_id(product_id)["price"]
        
        subtotal += quantity * unit_price
  
    rounded_subtotal = round(subtotal, 2)

    formatted_subtotal = f"${rounded_subtotal}"

    result = {"subtotal": formatted_subtotal}

    return result

        