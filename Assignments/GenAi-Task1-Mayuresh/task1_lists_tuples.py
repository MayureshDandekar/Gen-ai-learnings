products = ["mobile", "laptop", "Sofa", "camera", "headphones", "smartwatch"]
sample_product = ("TV", 100000, "electronic")

print(products[1],products[5])
products.append("printer")
products.append("Keyboard")
print(products)

sample_product = list(sample_product)
sample_product[1] = 11000
sample_product = tuple(sample_product)
print(sample_product)