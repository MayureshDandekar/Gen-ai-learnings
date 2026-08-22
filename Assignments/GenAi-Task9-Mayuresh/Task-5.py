import numpy as np 

marks = np.array([78,85,90,66,72,88,95,60])

average = np.mean(marks)
median = np.median(marks)
variance = np.var(marks)
marks_std = np.std(marks)
min_marks = np.min(marks)
max_marks = np.max(marks)
range_marks = max_marks - min_marks


print(average) 
print(median)
print(variance)
print(marks_std)
print(f"Minimum marks is {min_marks} and Maximum marks is {max_marks}")
print(range_marks)
