def process_prices(prices):
    discount = 10

    discount_applied = list(map(lambda x: x*(1-discount/100), prices))
    print(discount_applied)

    discount_condition = list(filter(lambda x: x>300, discount_applied))
    print(discount_condition)

    return discount_applied, discount_condition

a = process_prices([100,500,900,50,750])
