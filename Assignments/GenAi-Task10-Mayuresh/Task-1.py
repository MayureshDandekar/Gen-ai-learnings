import pandas as pd 

marks = [78, 85, 90, 66, 72]

marks_series = pd.Series(marks)
print(marks_series) 

print(marks_series.values)
print(marks_series.index)
print(marks_series.dtype)

print(marks_series.iloc[0])
print(marks_series.iloc[-2:])