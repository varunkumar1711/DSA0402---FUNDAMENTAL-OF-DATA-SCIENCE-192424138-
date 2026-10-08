import numpy as np

marks = np.array([
    [80, 70, 90, 60],
    [75, 80, 85, 70],
    [90, 85, 95, 80],
    [70, 75, 80, 65]
])

avg = np.mean(marks, axis=0)

print("Math Average:", avg[0])
print("Science Average:", avg[1])
print("English Average:", avg[2])
print("History Average:", avg[3])

print("Highest Average:", np.max(avg))
