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


from datetime import datetime, timedelta # datetime module is used to work with dates and times
now = datetime.now() # getting current date and time
print("Current date and time:", now)
one_week_later = now + timedelta(weeks=1) # adding one week to current date and time
print("Date and time one week later:", one_week_later) 


import time # time module is used to work with time-related tasks
# print("Current time:", time.ctime()) # getting current time
# time.sleep(5) # pausing the program for 5 seconds
# print(time.ctime()) # getting current time after 5 seconds


import shutil # shutil module is used to perform high-level file operations like copying and moving files
shutil.copy("example.txt", "example_copy.txt") # copying example.txt to example_copy.txt
# shutil.move("example_copy.txt", "example_moved.txt") # moving example_copy


import json # json module is used to work with JSON data
data = {"name": "Alice", "age": 30, "city": "New York"}
json_data = json.dumps(data) # converting Python object to JSON string
print(json_data) # printing JSON string
python_data = json.loads(json_data) # converting JSON string back to Python object
print(python_data) # printing Python object

text = '{"name": "Mayuresh", "age":21}'
data = json.loads(text)
print(data["name"])
data["age"] = 20
print(data)
print(text)



import re # re module is used for regular expression operations
text = "Golden sunlight pierced the dense morning fog, A Warming the damp earth as a lone sparrow began its quiet, Melodic song of awakening."
capital_word = re.findall(r"[A-Z]\w+", text) # finding all capitalized words in the text
print(capital_word) # printing the list of capitalized words