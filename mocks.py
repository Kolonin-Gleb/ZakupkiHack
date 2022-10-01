# mock

category_a = {
    "name": "category_a",
    "okpd2_code": "category_a_okpd2_code",
    "characteristics": ["description", "width", "heigth"]
}

product_a = {
    "id":   1,
    "name":   "product_a name",
    "okpd2_name":   "category_a",
    "saler_inn":   12345678,
    "characteristics":   {"description": "product_a description",
                          "width": 10,
                          "heigth": 20
                          }
}

product_b = {
    "id": 31,
    "name": "product_a name",
    "okpd2_name": "category_a",
    "saler_inn": 12345678,
    "characteristics": {"description": "product_a description",
                        "width": 123,
                        "heigth": 4121
                        }
}

product_c = {
    "id": 23,
    "name": "product_a name",
    "okpd2_name": "category_a",
    "saler_inn": 87654321,
    "characteristics": {"description": "product_a description",
                        "width": 443,
                        "heigth": 35
                        }
}

product_list = [
    product_a, product_b, product_c
]

product_list_saler_a = [
    product_a, product_b
]

saler_a = {
    "inn": 12345678,
    "product_list": product_list_saler_a,
    "sales": 120,
    "products_count": len(product_list)
}
# mock-end