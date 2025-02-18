import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2051)

wheat_a = np.array([20, 21, 22, 22, 23, 24, 24, 25, 26, 27, 28])
corn_a = np.array([15, 16, 16, 17, 18, 18, 19, 20, 21, 22, 23])
rice_a = np.array([10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18])
wheat_b = np.array([18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 26])
corn_b = np.array([14, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21])
rice_b = np.array([9, 9, 10, 11, 11, 11, 12, 13, 13, 14, 15])
wheat_c = np.array([17, 18, 19, 19, 20, 20, 21, 22, 23, 24, 25])
corn_c = np.array([13, 14, 15, 15, 16, 17, 18, 18, 19, 20, 21])
rice_c = np.array([8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, wheat_a, color='lime', linestyle='-.', marker='o', label='Wheat A')
ax.plot(years, corn_a, color='navy', linestyle='--', marker='s', label='Corn A')
ax.plot(years, rice_a, color='maroon', linestyle='-', marker='^', label='Rice A')

ax.plot(years, wheat_b, color='forestgreen', linestyle='-', marker='x', label='Wheat B')
ax.plot(years, corn_b, color='royalblue', linestyle=':', marker='*', label='Corn B')
ax.plot(years, rice_b, color='firebrick', linestyle='--', marker='d', label='Rice B')

ax.plot(years, wheat_c, color='chartreuse', linestyle='--', marker='+', label='Wheat C')
ax.plot(years, corn_c, color='dodgerblue', linestyle='-', marker='p', label='Corn C')
ax.plot(years, rice_c, color='brown', linestyle='-.', marker='h', label='Rice C')

ax.grid(False)

ax.legend(loc='upper left', frameon=True, shadow=True)

plt.tight_layout()
plt.show()