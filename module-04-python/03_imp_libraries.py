## Important Inbuilt Libraries in Python

import math
print(math.sqrt(16))  # Square root of 16


import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice from a list


import csv # it is used to read and write CSV files
with open("example.txt", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])

with open("example.txt", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)