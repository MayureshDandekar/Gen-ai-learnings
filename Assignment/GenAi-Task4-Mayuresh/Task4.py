with open("sales_data.txt", "r") as data:
    convert_data = []
    line = data.readlines()
    for i in line:
        integer = int(i.strip())
        convert_data.append(integer)
    print(convert_data)    
        
total_sales = sum(convert_data)
print(f"Total sale is {total_sales}")

highest_sale = max(convert_data)
print(f"The Higest sale is {highest_sale}")

lowest_sale = min(convert_data)
print(f"The lowest sale is {lowest_sale}")

average_sale = total_sales/len(convert_data)
print(f"The average sale is {average_sale}")