import pandas as pd 

df = pd.DataFrame({
    'chunk_id': [1,2,3,4,5,6],
    'source_doc': ['policy.pdf','policy.pdf','faq.pdf','faq.pdf','manual.pdf','manual.pdf'],
    'num_tokens': [42, 38, 40, 61, 45, 500],
    'retrieval_score': [0.92, 0.81, 0.75, 0.70, 0.65, 0.60]
})

# # & | ~ operators
# # In Pandas & | ~ are use to apply condition on Dataframes
# # always write Condition in Parentheses 
# result_1 = df[(df['num_tokens'] > 40) & (df['retrieval_score'] > 0.7)] 
# result_2 = df[(df['num_tokens']>80) | (df['retrieval_score']>0.80)]
# result_3 = df[~(df['num_tokens']>40)]
# print(result_1) 
# print(result_2) 
# print(result_3) 

# isin
print(df[df['source_doc'].isin(['policy.pdf', 'manual.pdf'])]) 

# between
print(df[df['num_tokens'].between(50,100)]) 

# query
print(df.query('num_tokens > 40 and retrieval_score > 0.7')) 
