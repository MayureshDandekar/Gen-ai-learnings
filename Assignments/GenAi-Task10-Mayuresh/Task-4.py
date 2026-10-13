import pandas as pd

students = {
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

students_d = pd.DataFrame(students)
print(students_d[:3])
print(students_d[-2:]) 

print(students_d.shape, students_d.columns) 