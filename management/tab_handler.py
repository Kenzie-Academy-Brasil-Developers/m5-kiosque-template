from menu import products


def calculate_tab(lista_de_objetos):
    total = 0

    for product in products:
        for element in lista_de_objetos:
            if product["_id"] == element["_id"]:
                quantity = element["amount"]
                price = product["price"]
                total += price * quantity

        subtotal_str = f"${total:.2f}".rstrip("0")

    return {"subtotal": subtotal_str}
