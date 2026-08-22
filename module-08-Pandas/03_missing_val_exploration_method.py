import pandas as pd

token_counts = pd.Series([42, None, 55, None, 61],
                            index=["chunk_1", "chunk_2", "chunk_3", "chunk_4", "chunk_5"])

print(token_counts.loc["chunk_1":"chunk_5"]) 
# NaN is float type that why dtype is float64

## Detecting Missing Values ##

print(token_counts.isnull()) #.isna alias # True where NaN, False elsewhere
print(token_counts.notnull()) # opposite — True where value is not empty

## Dealing with Missing Values ##

print(token_counts.dropna()) # Removes the row containing missing values

# print(token_counts.fillna(0)) # replace those NaN with fixed value
print(token_counts.fillna(token_counts.mean())) # replace with the average — common default
# Which to use depends entirely on what the missing value means in context — 
# that's a judgment call, not something Pandas decides for you.


labels = pd.Series(['policy.pdf', 'faq.pdf', 'policy.pdf', 'policy.pdf', 'faq.pdf'])

print(labels.unique()) 
print(labels.value_counts()) 
print(labels.sort_values()) 