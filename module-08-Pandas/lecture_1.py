import numpy as np
import pandas as pd

country_name = ["India", "Usa", "Israel", "Rushia"]
print(pd.Series(country_name, dtype='str')) # dtype is use to control the memory usage 

subject_name = ["Marathi", "English", "Maths", "Physics", "Chemistry"]
subject_marks = [90,92,67,60,70]
print(pd.Series(data=subject_marks, index=subject_name, name="Subject marks data")) 
# data is a conventional alias 

# Creating Series with an Numpy array
values = np.arange(10,16)
print(pd.Series(values, index=['a','b','c','d','e','f'], dtype='int32'))

# Creating Series with an Dictionary
print(pd.Series({'Maths':70, 'Marathi':90, 'English':97,'Physics':80})) 

# Custom Index 
print(pd.Series([1,2,3,4], index=['a','b','c','d']))

# Scalar value inside a Series
print(pd.Series(7, index=['a','b','c','d']))  