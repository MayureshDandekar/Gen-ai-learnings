order_list = []
while True:
    choice = input("Enter your Choice(1-Add order  2-Show orders  q-Quit): ")

    if choice == "1":
        amount = int(input("enter your amount: "))
        order_list.append(amount)

    elif choice == "2":
        total_amount = 0
        for amount in order_list:
            if amount >= 2000:
                final_price = amount * 0.85
                print(f"{amount} -> {final_price}")
            elif amount >= 1500:
                final_price = amount * 0.90
                print(f"{amount} -> {final_price}")
            elif amount >= 1000:
                final_price = amount * 0.93
                print(f"{amount} -> {final_price}")
            else:
                final_price = amount
                print("No discount applied")
            total_amount += final_price
        print(f"Total Amount: {total_amount}")

    elif choice == "q":
        break

    else:
        continue

