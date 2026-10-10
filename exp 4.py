import numpy as np

sales = np.array([1000, 1500, 2000, 2500])

total = np.sum(sales)
increase = ((sales[3] - sales[0]) / sales[0]) * 100

print("Total Sales:", total)
print("Percentage Increase:", increase, "%")
