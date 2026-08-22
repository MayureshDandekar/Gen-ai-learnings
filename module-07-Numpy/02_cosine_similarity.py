# Process Description : dot product for (query, chunk_short) and (query, chunk_long) separately, 
# magnitude of each of the three vectors, 
# divide each pair's dot product by the product of their two magnitudes, 
# land on a number between -1 and 1 that reads as direction-similarity. 
# That's the whole algorithm. Nothing missing.

import numpy as np

query   = np.array([1, 0])    
chunk_A = np.array([0.9, 0.1]) 
chunk_B = np.array([3, 2])

def cosine_similarity(a,b):
    dot_product = np.dot(a,b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    return dot_product / (magnitude_a * magnitude_b)

print(cosine_similarity(query, chunk_A))
print(cosine_similarity(query, chunk_B))

