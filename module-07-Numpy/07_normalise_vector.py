import numpy as np 

# steps to a normalise a vector :
# 1. take the magnitude(norm) of vector
# 2. divide each element of vector wiht vectors magnitude
# 3. now take magnitude of this new vector (if it magnitude returns as 1)
# 4. get the dot product of it
v = np.array([3,4])
norm_v = v / np.linalg.norm(v)
new_v = np.linalg.norm(norm_v)

# example of cosine similarity with normalising method
a = (3, 4, 0)
b = (0, 3, 4)

norm_a = a /np.linalg.norm(a)
norm_b = b /np.linalg.norm(b)
print(norm_a,norm_b) # get new normalised vector

mag_norm_a = np.linalg.norm(norm_a)
mag_norm_b = np.linalg.norm(norm_b)
print(mag_norm_a,mag_norm_b) # checked that new vector magnitude is scaled 1

dot = np.dot(norm_a,norm_b)
print(dot)
