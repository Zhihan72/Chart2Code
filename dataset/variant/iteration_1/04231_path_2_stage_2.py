import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

apples = np.array([25, 24, 23, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 12, 12, 12, 13, 14, 15])
bananas = np.array([20, 21, 22, 23, 24, 24, 25, 25, 25, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14])
oranges = np.array([15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10])
grapes = np.array([10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 25, 25, 24, 23, 22])
strawberries = 100 - (apples + bananas + oranges + grapes)

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, apples, bananas, oranges, grapes, strawberries, 
             colors=['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3'], alpha=0.8)

ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 100)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()