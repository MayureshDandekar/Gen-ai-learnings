import numpy as np 
import pandas as pd

# A DataFrame is a 2D table — think of it as multiple 'Series' glued together sharing one common index.

# Two methods to create DataFrame:

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