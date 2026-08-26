import pandas as pd
import matplotlib.pyplot as plt

token_counts = pd.Series([42, 38, 55, 61, 45, 50, 39, 58],
                          index=[f'chunk_{i}' for i in range(1,9)])


# This is way to plot multiple graph in one plate
# fig, axes = plt.subplots(2, 2)          # 4 separate, independent drawing areas
# token_counts.plot(kind='bar', ax=axes[0,1])   # this chart -> that specific axes
# token_counts.plot(kind='pie', ax=axes[1,1])  # this chart -> a different axes

## Always close window before printing another plate otherwise it overlaped
print(token_counts.plot(kind='bar'))
plt.savefig('bar_chart.png') # .savefig can save those chart in a file 
# print(token_counts.plot(kind='hist'))
# print(token_counts.plot(kind='line'))
# print(token_counts.plot(kind='pie'))
plt.show() 

