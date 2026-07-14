def apply_discount(price, percent):
    return price*(1-percent/100)


discount = apply_discount(1000, 10)
# print(discount)


def flat_discount(price):
    return price - 50


f_discount = flat_discount(1000)
# print(f_discount)