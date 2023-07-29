from management.product_handler import get_product_by_id, get_products_by_type


def main():
    print(get_product_by_id(28))
    print(get_products_by_type('drink'))

if __name__ == "__main__":
    main()