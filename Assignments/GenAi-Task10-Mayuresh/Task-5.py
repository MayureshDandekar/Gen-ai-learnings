import pandas as pd

students = pd.DataFrame({
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
})

print(students.info()) 
print(students.describe()) 
print(students.head()) 
print(students.tail()) 

print(students.sort_values('Marks', ascending=False).reset_index(drop=True))
