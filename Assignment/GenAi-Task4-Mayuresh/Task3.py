add_data = [5000,2500,1700]
with open("sales_data.txt", "a") as add:
    for i in add_data:
        add.write(f"{i}\n")

with open("sales_data.txt", "r") as add:
    print(add.read())

with open("sales_data.txt", "r") as add:
    print(len(add.readlines()))
    