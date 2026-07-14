prices = {"Mouse": 500, "Keyboard": 800, "Monitor": 7000, "Pendrive": 400, "Camera": 5000}

user = int(input("Enter the discount: "))

with open("discount_report.txt", "w") as data:
    discount_prices = []
    for product, price in prices.items():
        discount_price = price * (1-user/100)
        discount_prices.append(discount_price)
        data.write(f"{product} | {price} | {discount_price}\n")
        
    total_item = len(discount_prices)
    average_discount = sum(discount_prices) / total_item
    data.write(f"Total items are {total_item}\nAverage of Discount Prices is {average_discount}")

        
with open("discount_report.txt", "r") as data:
    print(data.read())









