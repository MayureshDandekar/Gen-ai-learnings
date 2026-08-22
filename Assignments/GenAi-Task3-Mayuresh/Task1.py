def apply_discount(price, discount_percent=5):

    if discount_percent>60:
        print("Discount cant exceed then 60%")
        discount_percent = 60

    discount = discount_percent/100
    final_price = price - (price*discount)
    return final_price


discount_61= apply_discount(1000,61)
print(discount_61)

discount_default = apply_discount(1000)
print(discount_default)


