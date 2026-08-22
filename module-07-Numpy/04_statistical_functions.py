import numpy as np

# sample = np.array([4, 9, 2, 9, 6]) 

# print(sample.mean())
# print(np.median(sample))
# print(sample.std())
# print(sample.var()) 
# print(sample.min())
# print(sample.max())
# print(sample.argmax()) 

#Reps
scores = np.array([0.92, 0.15, 0.61, 0.78, 0.33])
print(scores.mean())
print(scores.std()) 
print(scores.argmax()) 

grid = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(grid.shape)
print(grid.std(axis=0).shape) 
print(grid.std(axis=1).shape)
print(grid.sum(axis=1))
