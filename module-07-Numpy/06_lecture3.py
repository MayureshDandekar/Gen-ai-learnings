import numpy as np
# ## Imp Function

# # astype() ---> to convert dtype of dataset or to shrink size of dataset
# #Rep-1
# data = np.array([10, 20, 30])
# data_float = data.astype(float)
# print(data_float, data_float.dtype)
# print(data.dtype)
# #Rep-2
# values = np.array([3.9, 4.1, -2.7])
# values = np.round(values) # convert float to round otherwise astype chops off from decimal
# print(values.astype(int))
# #Rep-3
# arr = np.array([1,0,-5]).astype(bool) # in boolean conversion every non-Zero number is True and zero is consider as False
# print(arr)

# ## Mathematical Functions

# # Scaler operations --> applying a operation on an matrix or array with a single value
# array = np.round(np.random.random((4,4))*100).astype(np.int32)
# # print(array) 
# print(array/2)

# # Vectorise Operations

# arr_1 = np.arange(1,10).reshape(3,3)
# arr_2 = np.arange(10,19).reshape(3,3)
# print(arr_1)
# print(arr_2) 
# print(arr_1-arr_2)

# # Important function for Machine learning and Data Science

# arr_3 = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]], dtype="int32")

# print(arr_3.mean(axis=1))     
# print(arr_3.max(axis=1))     
# print(arr_3.min(axis=1))     


# # Dot Product ---> for dot product of two matrix Condition is 
# # the num. of column of first matrix and num. of row of second matrix must same
# # 1D array->Vector, 2D array->Matrix
# arrr = np.array([[1,2,3],
#                  [4,56,6],
#                  [7,8,9],
#                  [11,23,45]])
# arrrr = np.array([[1,2,3],
#                  [4,56,6],
#                  [7,8,9]])

# arra = np.array([1,2,3]) #1D vector dot product with matrix
# print(np.dot(arrrr,arra))
# print(np.dot(arrr,arrrr)) 

# # log() --> gives the log value of each element of matrix
# matrix = np.round(np.random.random((3,4))*100).astype('int32')
# print(matrix)
# print(np.log(matrix))

# # exp() --> gives exponential of each elements in matrix
# print(np.exp(matrix))

# # round() --> 1.6-->2, 1.3-->1
# # ceil() --> 1.6-->2, 1.3-->2 because if their is a decimal value it gonna convert it into next num
# # floor() --> 1.6-->1 because its opp. of ceil no matter decimal is how clo se to next num it cut off the 

# # tanspose() or arr.T --> it convert row in column and column in row of matrix
# print(matrix.T)

# # ravel() ---> it converts the ndim arrays to 1D aaray
# print(np.ravel(matrix)) 

# Indexing & Sclicing

# print(matrix[1:,1:3])  
# print(matrix[:,1])

# Iterating over an array

# array_1 = np.arange(1,28).reshape(3,3,3)
# print(array_1)
# # for i in array_1:
# #     print(i)
# # nditer() --> it help us to iterate on each element as seperate values in ndimesion array
# for i in np.nditer(array_1):
#     print(i)

## 1DArray ---> value by value on iteration
## 2DArray ---> Row by Row on iteration
## 3DArray ---> 2d Array by 2D Array

# Stacking and Splitting

# a_1 = np.array([1,2,3,4])
# a_2 = np.array([11,22,33,44])
# a_3 = np.array([12,13,14,15])

# # print(np.vstack([a_1,a_2,a_3]).shape ) 
# # print(np.hstack([a_1,a_2,a_3])) 
# s_matrix = np.vstack([a_1,a_2,a_3])
# print(s_matrix,s_matrix.shape)
# split_matrix = np.hsplit(s_matrix, 4)
# print(split_matrix) 

grid = np.array([[1,2,3,4],
                 [5,6,7,8]])
print(np.vsplit(grid, 2))   # splits by ROW  -- same as np.split(grid, 2, axis=0)
print(np.hsplit(grid, 2))  