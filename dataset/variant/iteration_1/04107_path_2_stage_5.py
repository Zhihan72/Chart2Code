import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apple', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Strawberry']
# Manually shuffled consumption data while preserving dimensions
consumption_alpha = [10, 15, 5, 30, 20, 25]  # Original: [15, 25, 10, 5, 30, 20]
consumption_beta = [15, 20, 10, 10, 25, 20]  # Original: [20, 10, 15, 25, 10, 20]
consumption_gamma = [10, 5, 20, 25, 30, 10]  # Original: [5, 20, 10, 30, 25, 10]
consumption_delta = [20, 10, 15, 5, 25, 30]  # Original: [10, 15, 20, 25, 30, 5]
avg_sweetness_levels = [7, 5, 8, 6, 9, 7]

data = []
for fruit, count in zip(fruits * 4, consumption_alpha + consumption_beta + consumption_gamma + consumption_delta):
    data.extend([fruit] * count)

fig, axs = plt.subplots(1, 2, figsize=(16, 6))

single_color = 'mediumseagreen'

ax1 = axs[0]
ax1.hist(data, bins=len(fruits), edgecolor='darkgreen', color=single_color, alpha=0.8)
ax1.set_xticks(np.arange(len(fruits)))
ax1.set_xticklabels([])

ax2 = axs[1]
ax2.bar(fruits, avg_sweetness_levels, color=single_color, edgecolor='darkgreen', alpha=0.6)
ax2.set_xticklabels([])

ax1.grid(True, linestyle=':', linewidth=0.7, color='gray')
ax2.grid(False)

plt.tight_layout()
plt.show()