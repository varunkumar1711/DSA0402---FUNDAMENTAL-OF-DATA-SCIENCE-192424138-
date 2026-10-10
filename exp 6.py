import numpy as np

price = np.array([100, 200, 300])
quantity = np.array([2, 1, 1])

total = np.sum(price * quantity)
discount = total * 10 / 100
after_discount = total - discount
tax = after_discount * 5 / 100
final_cost = after_discount + tax

print("Total Cost:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Cost:", final_cost)
