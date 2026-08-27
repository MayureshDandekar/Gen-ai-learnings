import pandas as pd 
import numpy as np

df = pd.DataFrame({
    'chunk_id': [1,2,3,4,5,6],
    'source_doc': ['policy.pdf','policy.pdf','faq.pdf','faq.pdf','manual.pdf','manual.pdf'],
    'num_tokens': [42, 38, np.nan, 61, 45, 500],
    'retrieval_score': [0.92, 0.81, 0.75, np.nan, 0.65, 0.60]
})

print('shape:', df.shape) 
print('dtypes:')
print(df.dtypes) 
print()
print('info:')
df.info() 
print()
print('describe:')
print(df.describe())
print() 


# Functions: head/tail/sample
print('head(3):') # return last n num of rows
print(df.head(3))
print() 
print('tail(2)') # return last n num of rows
print(df.tail(2))
print()
print('sample:')
print(df.sample(2)) # return random n num of rows
print() 

# Renaming columns
df_renamed = df.rename(columns={'num_tokens':'token_counts'}) 
print(df_renamed.columns.tolist()) 

# Setting the index
print('set_index:')
df_indexed = df.set_index('chunk_id') # turn a column as a indexed of the table 
print(df_indexed.head(3))

print('isnull().sum() per column:')
print(df.isnull().sum()) # here sum() return total NaN count present in each column

print('dropna() on DataFrame -- drops ANY row with a NaN anywhere:')
print(df.dropna()) 