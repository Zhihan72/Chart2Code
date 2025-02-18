import matplotlib.pyplot as plt
import numpy as np

# Examples of fruit consumption and average sweetness levels
fruits = ['Apple', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Strawberry']
consumption_alpha = [15, 25, 10, 5, 30, 20]
consumption_beta = [20, 10, 15, 25, 10, 20]
consumption_gamma = [5, 20, 10, 30, 25, 10]
consumption_delta = [10, 15, 20, 25, 30, 5]
avg_sweetness_levels = [7, 5, 8, 6, 9, 7]

data = []
for fruit, count in zip(fruits * 4, consumption_alpha + consumption_beta + consumption_gamma + consumption_delta):
    data.extend([fruit] * count)

# Setup figure and axes
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot for fruit consumption on different planets
ax1 = axs[0]
ax1.hist(data, bins=len(fruits), edgecolor='darkgreen', color='lightcoral', alpha=0.8, linestyle='--')
ax1.set_xticks(np.arange(len(fruits)))
ax1.set_xticklabels([])

# Plot for average sweetness levels of fruits
ax2 = axs[1]
ax2.bar(fruits, avg_sweetness_levels, color='lightblue', edgecolor='navy', alpha=0.6, hatch='//')
ax2.set_xticklabels([])

ax1.grid(True, linestyle=':', linewidth=0.7, color='gray')
ax2.grid(False)

plt.tight_layout()
plt.show()