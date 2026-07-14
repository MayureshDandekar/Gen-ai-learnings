#optional task
# sales = [1200,450,980,1500,3000]

# with open("sales_data.txt", "w") as data:
#         data.write(",".join(str(i) for i in sales))

# with open("sales_data.txt", "r") as data:
#         print(data.read())


sales = [1200,450,980,1500,3000]

with open("sales_data.txt", "w") as data:
        for i in sales:
            data.write(f"{i}\n")

with open("sales_data.txt", "r") as data:
        print(data.read())