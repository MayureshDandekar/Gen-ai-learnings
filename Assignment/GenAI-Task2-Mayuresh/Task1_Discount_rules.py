try:
    order_amount = int(input("Enter the order amount: "))

    if order_amount >= 2000:
        final_price = order_amount * 0.85
    elif order_amount >= 1500:
        final_price = order_amount * 0.90
    elif order_amount >= 1000:
        final_price = order_amount * 0.93

    else:
        final_price = order_amount
        print("No discount applied")
    # print(f"after discount the final price is : {final_price}")

    tax_amount = final_price*0.05 
    print(f"Subtotal:{final_price}, Tax:{tax_amount}, Total:{final_price+tax_amount}")


except ValueError:
    print(f"Please enter a valid amount")
    exit()
