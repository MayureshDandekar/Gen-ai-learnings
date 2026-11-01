import pandas as pd

students = pd.DataFrame({
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
})

grouped_by_subjects = students.groupby('Subject')

print(grouped_by_subjects['Marks'].mean()) 
print(grouped_by_subjects['Name'].count()) 
print(grouped_by_subjects['Marks'].max())    