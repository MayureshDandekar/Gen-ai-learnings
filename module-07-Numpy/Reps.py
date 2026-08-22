import numpy as np

arr_1 = np.zeros((4,4))
arr_2 = np.ones((4,4))

print(arr_1.shape, arr_1.dtype)
print(arr_2.shape, arr_2.dtype)


real_data = np.array([1, 2, 3, 4, 5, 6])
real_data_copy = np.zeros_like(real_data)
print(real_data_copy.dtype)

arr_3 = np.ones((3,2), dtype=int)
print(arr_3) 


a = np.array([1,23,4])
print(np.linalg.norm(a)) 