import pandas as pd

token_counts = pd.Series([42,38,55,61,70], index=["chunk_1", "chunk_2", "chunk_3", "chunk_4","cunk_5"])

# Same methods as Numpy
# print(token_counts.sum())
# print(token_counts.mean())
# print(token_counts.std()) 
# print(token_counts.min())
# print(token_counts.max()) 
print(token_counts.describe()) # New with whole discription of Series(count,mean,std,min,25%,max,dtype)

#Adding two arrays/series in Pandas
retrieval_score = pd.Series({'chunk_1': 0.9, 'chunk_2': 0.7, 'chunk_3': 0.85})
recency_score   = pd.Series({'chunk_2': 0.5, 'chunk_3': 0.6, 'chunk_4': 0.3})

combined = retrieval_score + recency_score # sum happens labells wise in Pandas
print(combined)

# Accessing elements with .loc & .iloc
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

print(s.loc["b"])
print(s.loc['b':'d']) # Slicing
# .loc never looks at position. .iloc never looks at labels.
print(s.iloc[1])
print(s.iloc[1:4])




