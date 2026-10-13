import pandas as pd

marks = pd.Series([78, 85, 90, 66, 72]) 

add = marks + 5
substract = marks - 2
multiply = marks * 1.05
divide = marks / 2

print(marks + 5)
print(marks - 2)
print(marks * 1.05)
print(marks / 2)

print(marks)