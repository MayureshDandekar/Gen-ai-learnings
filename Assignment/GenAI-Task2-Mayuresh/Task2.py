total_revenue = 0

orders = [1200, 2500, 800, 1750, 3000]

for order_amount in orders:
    if order_amount >= 2000:
        discount = 15
        final_price = order_amount * 0.85
        # print(f"{order_amount} -> {discount} -> {final_price}")

    elif order_amount >= 1500:
        discount = 10
        final_price = order_amount * 0.90
        # print(f"{order_amount} -> {discount} -> {final_price}")

    elif order_amount >= 1000:
        discount = 7
        final_price = order_amount * 0.93
        # print(f"{order_amount} -> {discount} -> {final_price}")

    else:
        discount=0
        final_price = order_amount
        # print(f"{order_amount} -> {discount} -> {final_price}")

    print(f"{order_amount} -> {discount} -> {final_price}")
    total_revenue+= final_price
print(f"Your Total Revenue is :{total_revenue}")

