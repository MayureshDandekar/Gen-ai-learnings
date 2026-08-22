import numpy as np

sales = np.array([1200, 1500, 900, 2000,1800, 1700, 1600])

print(f"Total weekly sales is {np.sum(sales)}")
sales_average = np.round(np.mean(sales), 4)
print(f"Average of daily sales is {sales_average}")
print(f"Highest sales of a day is {np.max(sales)} and Lowest sales of day is {np.min(sales)}")
print(np.std(sales))

print(np.where(sales>sales_average))
