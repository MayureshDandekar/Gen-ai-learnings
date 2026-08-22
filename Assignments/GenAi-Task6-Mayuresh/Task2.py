prices = [120,350,'abc','xyz', 500,-200,800]


total_price = 0 
for i in prices:
    try:
        if i < 0 :  # condition for positive integer 
            raise ValueError    # add a custom error 
        total_price += i
    except TypeError:   # error for string
        continue
    except ValueError as e :    # cstch the error which we raised
        print(e)
        continue

        
print(total_price)


