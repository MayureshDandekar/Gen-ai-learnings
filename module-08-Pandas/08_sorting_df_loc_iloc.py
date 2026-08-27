import pandas as pd
import numpy as np

df = pd.DataFrame({
    'chunk_id': [1,2,3,4,5,6],
    'source_doc': ['policy.pdf','policy.pdf','faq.pdf','faq.pdf','manual.pdf','manual.pdf'],
    'num_tokens': [42, 38, 40, 61, 45, 500],
    'retrieval_score': [0.92, 0.81, 0.75, 0.70, 0.65, 0.60]
})

# Coloumn selection
# print(df['num_tokens'])   # return a Series
# print(df[['num_tokens']]) # return a DataFrame [[]]
# print(df[['source_doc', 'num_tokens']]) 

# loc/iloc on DataFrames
# print(df.loc[2, 'num_tokens'])
# print(df.loc[0:2]) # here indexing goes up to 0,1,2
# print(df.iloc[0:2]) # here 2 is excluded
# print(df.loc[:,['source_doc', 'num_tokens']])

# sorting
# print(df.sort_values('num_tokens')) 
# print(df.sort_values('num_tokens', ascending=False)) # here we want sorting with desending so ascending=False
print(df.sort_values(['source_doc', 'num_tokens'])) # here sorting happen with first given column alphabetically

# apply/map on DataFrame
print(df[['num_tokens', 'retrieval_score']].apply(lambda col: col.sum())) # here dataframe gives data as a column not scalar element
print(df[['num_tokens', 'retrieval_score']].apply(lambda col: col.sum(), axis=1)) # sum row wise

print(df.map(lambda x: x*10)) # map can access each elment not columns 