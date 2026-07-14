cart =[]
while True: # for continuous loop
    user = input("Enter the prices and 'q' to quite: ")
    # To stop running code after a condition
    if user == "q":
        break
    try:
        # condition for negative value
        convert = float(user)
        if convert < 0:
            raise ValueError
        cart.append(convert)
    # exception for invalid inputs
    except ValueError:
        print("Enter a valid price")
    
print(len(cart))
print(sum(cart))
