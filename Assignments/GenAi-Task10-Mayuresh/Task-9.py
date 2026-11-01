import pandas as pd
import matplotlib.pyplot as plt

sales ={
'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
'Revenue': [1200, 1500, 900, 2000, 1800]
} 

df_sales = pd.DataFrame(sales)
print(f"The sum of Revenue is {df_sales['Revenue'].sum()}") 
average_revenue = df_sales['Revenue'].mean()
print(f"The average of Revenue is {average_revenue}")
print(f"Highest Revenue Day\n {df_sales[df_sales['Revenue']==df_sales['Revenue'].max()]}")  
# print(df_sales.set_index('Day')['Revenue'].idxmax()) 
is_higher_revenue = df_sales['Revenue']> average_revenue 
print(f"Days higher than average revenue\n {df_sales[is_higher_revenue]}") 


sales_plot = df_sales.set_index('Day')
(sales_plot.plot(kind='bar'))
plt.show()
