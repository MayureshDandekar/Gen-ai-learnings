import numpy as np

data = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

sum_row = np.sum(data, axis=1)
sum_column = np.sum(data, axis=0)
min_value = np.min(data)
max_value = np.max(data)
mean_value = np.mean(data)

print(sum_row)
print(sum_column)
print(min_value)
print(max_value)
print(mean_value) 