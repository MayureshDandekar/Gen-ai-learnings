import numpy as np 

marks = np.array([78,85,90,66,72,88,95,60])

print(np.sort(marks))
print(np.percentile(marks, 25))
print(np.percentile(marks, 50))
print(np.percentile(marks, 75))

average = np.mean(marks)
mask = marks>average
student_above_avg = np.sum(mask) # True 1 False 0 by this logic if get the sum of student above avg
above_average = marks[mask] # here mask acts as a Boolean of condition add only True one
print(student_above_avg)
print(above_average)
