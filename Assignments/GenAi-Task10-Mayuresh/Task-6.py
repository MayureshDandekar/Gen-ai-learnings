import pandas as pd

students = pd.DataFrame({
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
})

scored_above_75 = students['Marks']>75 
print(students[scored_above_75]) 

math_students = students['Subject']=='Math'
print(f'students belonging to math subject\n {students[math_students]}')

average_marks = students['Marks'].mean() 
scored_more_than_average = students['Marks']>average_marks
print(f'student scored more than average\n {students[scored_more_than_average]}') 

failed_students = students['Marks']<70
print(f'Failed Student\n {students[failed_students]}') 