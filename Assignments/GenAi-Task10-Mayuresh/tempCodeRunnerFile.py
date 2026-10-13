import pandas as pd

marks = pd.Series([78, 85, 90, 66, 72]) 

print(marks.max()) 
print(marks.min()) 
print(marks.sum()) 
print(marks.mean()) 

student_passed = marks.apply(lambda x: 'passed' if x>=70 else 'failed')
print(student_passed) 

print(student_passed.value_counts())