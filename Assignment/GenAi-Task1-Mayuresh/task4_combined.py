products = ["mobile", "laptop", "Sofa", "camera", "headphones", "smartwatch"]
price_dict = {"mobile": 10000, "laptop": 80000, "Sofa": 50000, "camera": 30000, "headphones": 15000, "smartwatch": 25000}
category = ["electronic", "electronic", "furniture", "electronic", "electronic", "electronic"]

catalog = list(zip(products, price_dict.values(), category))
print(catalog)


   
category_to_products = {}
for name, price, cat in catalog:
    if cat in category_to_products:
        category_to_products[cat].append((name))
    else:
        category_to_products[cat] = [(name)]    #dict[key] = value
    
    
max_count = 0
max_category = ""
max_product = ""
for cat, product_list in category_to_products.items():
    if len(product_list) > max_count:
        max_count = len(product_list)
        max_category = cat
        max_product = product_list
print(f"Category with most products: {max_category} with {max_count} products({max_product})")
