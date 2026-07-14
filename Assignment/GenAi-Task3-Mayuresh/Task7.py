def add_price(prices_list, price):
    prices_list.append(price)
    # return prices_list
    
def get_average_price(prices_list):
    average = sum(prices_list)/len(prices_list)
    print(average)

def get_max_price(prices_list):
    max_price = max(prices_list)
    print(max_price)


prices_list = []
while True:
    choice = input("1-Add price  2-Average  3-Max  q-Quit: ")
    if choice == "1":
        n = int(input("Enter your amount: "))
        add_price(prices_list, n)
        # prices_list.append(n)
    elif choice == "2":
        get_average_price(prices_list)
    elif choice == "3":
        get_max_price(prices_list)
    elif choice == "q":
        break
    else:
        continue



