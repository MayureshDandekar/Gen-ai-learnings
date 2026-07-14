with open("products.txt", "w") as data:
    i = 0
    while i<3:
        product_name = input("Enter the product name: ")
        product_price = int(input("Enter the price of your product: "))
        data.write(f"{product_name} | {product_price}\n")
        i+=1


with open("products.txt", "r") as data:
    lines = data.readlines()
    for line in lines:
        name, price = line.split("|")
        price = price.strip()
        print(f"{name} - ₹{price}")
