products = ["mobile", "laptop", "Sofa", "camera", "cupboard", "smartwatch"]
categories= ["electronic", "electronic","furniture","electronic","furniture","electronic"]

categories_set = set(categories)
print(categories_set)

categories_set.add("appliances") # used .add method to add new element to the set
print(categories_set)
categories_set.add("electronic") # added an existing element to the set, to show that it will not added again
print(categories_set)

print("electronic" in categories_set) # used .in function to check if the element is present in the set or not

print(len(categories_set))