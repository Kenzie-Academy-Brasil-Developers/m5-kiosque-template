from menu import products

def calculate_tab(list_dictionary):
    list = []
    for table in list_dictionary:
        for list_menu in products:
            if table["_id"] == list_menu["_id"]:
                list.append(list_menu["price"] * table["amount"])
    sub_total = sum(list)
    return {"subtotal": f"${round(sub_total, 2)}"}