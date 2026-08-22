import numpy as np 

# Here, dtype=np.int32 is deciding the memory size for each elememt of array
arr_1 = np.array([1,2,3,4,5], dtype=np.int32) 
arr_2 = np.array([1,2,3,4,5], dtype=np.int64) 
arr_3 = np.array([1,2,3,4,5], dtype=np.float16) 
arr_4 = np.array([1,2,3,4,5], dtype=np.bool) 

print(arr_1)
print(arr_2)
print(arr_3)
print(arr_4)

# np.arange() ---> this function can iterate till the given number same as for loop in 1 line of code
arange_data = np.arange(1,17)
print(arange_data)

# np.reshape() ---> this help out to convert a 1D array into a matrix
print(arange_data.reshape(4,4))
print(np.arange(2,17,2).reshape(4,2))

# np.ones() ---> if we know the size of data we can create an matrix of 1 and after fill with real data
print(np.ones((4,4), dtype=int)) 

# np.zeros() ---> sames as ones
print(np.zeros((4,4), dtype=int)) 

# np.random() ---> It generate random number values from 0 to 1 inside our matrix
print(np.random.random((2,3)))

# np.identity() ---> it helps to create an identity matrix (same values in daigonal and other values are zero is identity matrix)
print(np.identity(3))

# np.linspace() ---> it makes sure that every value within the given range s going to have similar distance from ach other 
print(np.linspace(-10,10,10))


##Attributes##

# ndim ---> ndim attribute stands for n dimenstion
arr = np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
print(arr.ndim)

# shapes ---> it give the idea about rows,columns in our matrix
arrr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arrr.shape) # the third number in output is of z axis

# size ---> return the number of element present in a array
print(np.array([[1.1,2.4,3.5],[11.4,23.6,34.6]]).size)

# itemsize ---> return the memory size of each element from array
print(np.array([[4,5,6],[1,2,3]], dtype=np.int32).itemsize)
 