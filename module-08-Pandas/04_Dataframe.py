import numpy as np 
import pandas as pd

# A DataFrame is a 2D table — think of it as multiple 'Series' glued together sharing one common index.

# Three methods to create DataFrame:

# Method 1 : Dictionary of lists (Most used method)
df = pd.DataFrame({
    'chunk_id' : [1,2,3],
    'source_doc' : ['policy.pdf', 'policy.pdf', 'faq.pdf'],
    'um_tokens' : [42,38,5]
})
print(df) 
print(df.dtypes)

# Method 2 : List of Dictionar 
rows = [
    {'chunk_id' : 1, 'source_doc': 'policy.pdf', 'num_tokens': 42},
    {'chunk_id': 2, 'source_doc': 'faq.pdf', 'num_tokens': 38, 'flagged': True},
]
df = pd.DataFrame(rows)
print(df)
print(df.dtypes)

# Method 3 : 2D array/list + explicit column names
arr = np.array([[1, 42], [2, 38], [3, 55]])
df_2 = pd.DataFrame(arr, columns=['chunk_id','num_tokens'])
print(df_2)
print(df_2.dtypes)

# Reading from real files

df = pd.read_csv('file_name')       # by far the most common in practice
df = pd.read_excel('file_name')     # needs openpyxl installed
df = pd.read_json('file_name')
df = pd.read_sql('file_name')       # needs a DB connection object
