import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([5, 2, 9, 11, 14, 15, 19, 17, 13, 9, 7])
products_purchased = np.array([2, 1, 5, 6, 9, 6, 7, 4, 5, 3, 3])

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(age_groups, ads_seen, color='teal')
ax.barh(age_groups, -products_purchased, color='salmon')

plt.show()