import numpy as np

# In Python if we have to apply any change on a list elements 
prices_list = [100,200,300]
discounted = [p * 0.9 for p in prices_list]
print(discounted)

## Numpy ## way --> This is fast, with no loop & comprehension
# This is called broadcasting when the shapes don't match exactly
# a scalar (0.9) gets "stretched" across every element without actually copying it in memory.
# It also works array-to-array when shapes align
prices_arr = np.array([100,200,300])
discount_percent = 0.9
discounted = prices_arr * (1-discount_percent) # applies to every element at once
print("Discount is " ,discounted)

a = np.array([1,2,3])
b = np.array([10,20,30])
print(a+b)
print(a*b) 

##Reps
temps_celsius = np.array([0, 20, 37, 100])
fahrenheit = (temps_celsius*9/5) + 32
print(f"fahrenheit is {fahrenheit}")

a = np.array([1,2,3]) 
b = np.array([4,5,6])

square_diff = (a-b)**2
print(f"The Square diff btw each element is {square_diff}")

