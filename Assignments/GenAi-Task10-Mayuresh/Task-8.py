import pandas as pd
import matplotlib.pyplot as plt


students = pd.DataFrame({
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
})

marks_by_student= students.set_index('Name')
marks_by_student['Marks'].plot(kind='bar')
plt.show() 
marks_by_student['Marks'].plot(kind='line')
plt.show()  
marks_by_student['Marks'].plot(kind='hist')
plt.show() 