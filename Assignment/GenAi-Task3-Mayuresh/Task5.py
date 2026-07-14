prices = [100,250,400,1200,50,2000,850]

expensive_product = filter(lambda x : x>500, prices)
cheap_product = filter(lambda x : x<=500, prices)
print(list(expensive_product))
print(list(cheap_product))