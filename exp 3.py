import numpy as np

# Columns: Bedrooms, Square Feet, Sale Price
houses = np.array([
    [3, 1200, 200000],
    [5, 1800, 300000],
    [6, 2000, 350000],
    [4, 1500, 250000],
    [7, 2200, 400000]
])

# Select houses with more than 4 bedrooms
prices = houses[houses[:, 0] > 4, 2]

# Find average sale price
average = np.mean(prices)

print("Average sale price:", average)
