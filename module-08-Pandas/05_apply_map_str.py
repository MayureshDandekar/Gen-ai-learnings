import pandas as pd

token_count = pd.Series([42, 38, 55, 61, 45, 50, 39, 58],
                        index=[f"chunk{i}" for i in range(1,9)])

def size_category(n):
    if n<40: return "short"
    elif n<60: return "medium"
    else : return "long"

# apply()e
sizes = token_count.apply(size_category) # we can use map() func. for same output
# map()
category_map = {"short":"S", "medium":"M", "long":"L"}
short_code = sizes.map(category_map)
print(short_code) 

# .str()
sources = pd.Series(['policy.pdf', 'FAQ.pdf', 'user_manual.PDF'])
print(sources.str.lower())
print(sources.str.contains('faq', case=False)) 
# here case is about string matching f != F, and case=False tells to ignore this diffrence
print(sources.str.replace('.pdf','', case=False, regex=False))
print(sources.str.split('.').str[0])
print(sources.str.len())

