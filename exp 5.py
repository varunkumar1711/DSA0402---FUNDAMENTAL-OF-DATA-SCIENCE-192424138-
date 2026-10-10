import numpy as np

fuel = np.array([20, 25, 30, 35])

average = np.mean(fuel)
improvement = ((fuel[3] - fuel[0]) / fuel[0]) * 100

print("Average Fuel Efficiency:", average)
print("Percentage Improvement:", improvement, "%")
