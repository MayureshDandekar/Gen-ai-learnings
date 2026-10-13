import pandas as pd 

# df = pd.DataFrame({
#     'source_doc': ['policy.pdf','policy.pdf','faq.pdf','faq.pdf','manual.pdf'],
#     'num_tokens': [42, 38, 55, 61, 45],
#     'retrieval_score': [0.92, 0.81, 0.75, 0.70, 0.65]
# })


# # # & | ~ operators
# # # In Pandas & | ~ are use to apply condition on Dataframes
# # # always write Condition in Parentheses 
# # result_1 = df[(df['num_tokens'] > 40) & (df['retrieval_score'] > 0.7)] 
# # result_2 = df[(df['num_tokens']>80) | (df['retrieval_score']>0.80)]
# # result_3 = df[~(df['num_tokens']>40)]
# # print(result_1) 
# # print(result_2) 
# # print(result_3) 

# # isin
# print(df[df['source_doc'].isin(['policy.pdf', 'manual.pdf'])]) 

# # between
# print(df[df['num_tokens'].between(50,100)]) 

# # query
# print(df.query('num_tokens > 40 and retrieval_score > 0.7')) 

# # adding a new column -- vectorized, no loop
# df['is_long'] = df['num_tokens']>50
# df.loc[df['num_tokens']>50, 'num_tokens'] = 999 
# print(df) 

# # groupby — split, apply, combine
# print(df.groupby('source_doc')['num_tokens'].mean()) 
# print(df.groupby('source_doc').agg({'num_tokens':'mean' , 'retrieval_score':'max'})) 
# print(df.groupby('source_doc').size()) 

# Concat & Merge

# # concat -- stacking rows from two separate batches
# batch1 = pd.DataFrame({'chunk_id':[1,2], 'source_doc':['policy.pdf','policy.pdf'], 'num_tokens':[42,38]})
# batch2 = pd.DataFrame({'chunk_id':[3,4], 'source_doc':['faq.pdf','faq.pdf'], 'num_tokens':[55,61]})

# chunks = pd.concat([batch1, batch2], ignore_index=True)

# # merge -- combining on a shared key, SQL-style
# doc_metadata = pd.DataFrame({
#     'source_doc': ['policy.pdf', 'faq.pdf', 'manual.pdf'],
#     'author': ['Legal Team', 'Support Team', 'Eng Team']
# })

# print(pd.merge(chunks, doc_metadata, on='source_doc', how='left')) 
# # on='source_doc' says "match rows using this shared column."
# # how='left' means: keep every row from chunks

# corr(), pivot_table, duplicated #
chunks = pd.DataFrame({
    'chunk_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'source_doc': ['policy.pdf', 'policy.pdf', 'faq.pdf', 'faq.pdf',
                    'manual.pdf', 'manual.pdf', 'guide.pdf', 'guide.pdf'],
    'num_tokens': [42, 38, 55, 61, 30, 95, 48, 52],
    'retrieval_score': [0.92, 0.81, 0.75, 0.60, 0.55, 0.88, 0.70, 0.95]
})

# corr() is correlation same as cosine similarity use to check numerical columns are moving together 
# print(chunks[['num_tokens', 'retrieval_score']].corr())

# chunk_2 = pd.DataFrame({
#     'source_doc': ['policy.pdf','policy.pdf','faq.pdf','faq.pdf','manual.pdf','manual.pdf','guide.pdf','guide.pdf'],
#     'is_high_confidence': [True, True, False, False, False, True, False, True],
#     'num_tokens': [42, 38, 55, 61, 30, 95, 48, 52]
# })
# print(chunk_2.pivot_table(values='num_tokens', index='source_doc', 
#                           columns='is_high_confidence', aggfunc='mean'))


df = pd.DataFrame({
    'name': ['Alex', 'Sam', 'Alex', 'Jordan'],
    'age': [25, 30, 25, 40]
})

print(df)
print()
print(df.duplicated())

print(df.duplicated(subset='name')) # subset tell to match only columns data not the whole row







































# Problem Solved
# import pandas as pd

# chunks = pd.DataFrame({
#     'chunk_id': [1, 2, 3, 4, 5, 6, 7, 8],
#     'source_doc': ['policy.pdf', 'policy.pdf', 'faq.pdf', 'faq.pdf',
#                     'manual.pdf', 'manual.pdf', 'guide.pdf', 'guide.pdf'],
#     'num_tokens': [42, 38, 55, 61, 30, 95, 48, 52],
#     'retrieval_score': [0.92, 0.81, 0.75, 0.60, 0.55, 0.88, 0.70, 0.95]
# })

# result = chunks[(chunks['retrieval_score']>0.75) & (chunks['num_tokens'].between(40,60))]
# result = chunks.query('retrieval_score > 0.75 and num_tokens.between(40,60)' ) 
# print(result) 
# result_2 = chunks.groupby('source_doc')['retrieval_score'].mean() 
# print(result_2.sort_values( ascending=False)) 
# chunks['is_high_confidence'] = chunks['retrieval_score']>0.8
# print(chunks.groupby('is_high_confidence').size())
# print(chunks) 

# scores_batch = pd.DataFrame({
#     'chunk_id': [1, 2, 3, 4],
#     'retrieval_score': [0.92, 0.81, 0.75, 0.60]
# })

# doc_titles = pd.DataFrame({
#     'source_doc': ['policy.pdf', 'faq.pdf', 'manual.pdf', 'guide.pdf'],
#     'title': ['Refund Policy', 'Frequently Asked Questions', 'User Manual', 'Setup Guide']
# })


# print(pd.merge(chunks, doc_titles, on='source_doc', how='left')) 
