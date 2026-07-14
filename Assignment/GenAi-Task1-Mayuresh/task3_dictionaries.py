price_dict = {"Tv": 5000, "Laptop": 8000, "Mobile": 3000, "Tablet": 4000, "Headphones": 1500, "Smartwatch": 2500}

price_dict["Watch"] = 2000
print(price_dict)
price_dict["Mobile"] = 3500
print(price_dict)

price_dict.pop("Tv",None)
print(price_dict)

print(price_dict.values())

add = 0
for i in price_dict.values():
    add+=i
print(add/len(price_dict.values()))


