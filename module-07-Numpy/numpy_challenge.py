import numpy as np

## --> This code more effiecient and better approach to write 
## because further there will be more hundreads of chunks 
chunks_matrics = np.array([ [0.9, 0.1, 0.0],
                            [0.1, 0.9, 0.0],
                            [0.85, 0.2, 0.1], ])

query = np.array([0.88, 0.15, 0.05])

dot_products = np.dot(chunks_matrics,query)
chunks_norms = np.linalg.norm(chunks_matrics, axis=1)
query_norm = np.linalg.norm(query)

similarities = dot_products / (chunks_norms * query_norm)
print(similarities)

best_chunk_index = np.argmax(similarities)







# chunk_1 = np.array([0.9, 0.1, 0.0])   # "the cat sat on the mat"
# chunk_2 = np.array([0.1, 0.9, 0.0])   # "stock prices rose today"
# chunk_3 = np.array([0.85, 0.2, 0.1])  # "a kitten sat on the rug"

# query = np.array([0.88, 0.15, 0.05])  # "cat sitting somewhere"

# def cosine_similarity(a,b):
#     dot_product = np.dot(a,b)
#     magnitude_a = np.linalg.norm(a)
#     magnitude_b = np.linalg.norm(b)
#     return dot_product / (magnitude_a * magnitude_b)

# c_1 = cosine_similarity(query, chunk_1)
# c_2 = cosine_similarity(query, chunk_2)
# c_3 = cosine_similarity(query, chunk_3)

# similarity_score = np.array([c_1, c_2, c_3])
# print(similarity_score)

# print(np.argmax(similarity_score)) 
print(best_chunk_index)