import pandas as pd

# token_counts = pd.Series([42,38,64,28]) 
# # No index given → Pandas assigns default positional labels 0,1,2,3
# print(token_counts.dtype)

# Two ways to lablel a series : 1.Using Indexing, 2.Creating Indexing

# token_counts = pd.Series({"chunk_1":42, "chunk_2":38, "chunk_3":64, "chunk_4":28})
token_counts = pd.Series([42,38,64,28], index=["chunk_1", "chunk_2", "chunk_3", "chunk_4"], name="chunks info")

print(token_counts.values) 
print(token_counts.index) 
print(token_counts.dtype) 
print(token_counts.shape)


s = pd.Series([100,200,300,400], index=[10,20,30,40])
print(s[10])
# print(s[1]) # cant access with indexing if index(label) is define

# Slicing with series
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s["a":"d"])
print(s[0:3]) 