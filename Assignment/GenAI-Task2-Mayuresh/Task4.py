daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0
for sale in daily:
    if sale < 0:
        print("corrupted data")
        break
    elif sale != 0:
        total_sales += sale
    # else:
    #     continue
    print(f"{sale} + {total_sales}")

print(f"Total Sales is : {total_sales}")


    