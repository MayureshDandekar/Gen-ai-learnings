# import math          #import all functions from math library
# print(math.sqrt(16)) # we have to write math.sqrt() to use the sqrt function from math library

# from math import sqrt #import only specific functions from math library
# print(sqrt(16)) # we can directly use sqrt() without math.sqrt()

# from math import * # we can import all functions from math library 
# print(factorial(5)) # we can directly use factorial() without math.factorial()

# ##Library- Numpy##
# import numpy as np #importing numpy library as np
# ls = [1, 2, 3, 4, 5]
# arr = np.array(ls) #converting list to numpy array
# print(arr) #printing numpy array


## Creating our own Pakage
# __init__.py is the file hat has to be inside the pakage follder. 
# and __init__.py this file helps us out in definig our pakages and intialising their namespace
from Pakage_folder.mathematics import *

a = 5
b = 10

print(addition(a,b))
print(substraction(a,b))
print(multiply(a,b))
print(division(a,b))