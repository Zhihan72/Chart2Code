import matplotlib.pyplot as plt
import numpy as np

fruits = ['App', 'Ban', 'Grp', 'Org', 'Pin', 'Str']
consumption_alpha = [15, 25, 10, 5, 30, 20]
consumption_beta = [20, 10, 15, 25, 10, 20]
consumption_gamma = [5, 20, 10, 30, 25, 10]
avg_sweetness_levels = [7, 5, 8, 6, 9, 7]

data = []
for fruit, count in zip(fruits * 3, consumption_alpha + consumption_beta + consumption_gamma):
    data.extend([fruit] * count)

fig, axs = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [1, 2]})

# First subplot with stylistic changes
ax1 = axs[0]
ax1.bar(fruits, avg_sweetness_levels, color='cyan', edgecolor='blue', alpha=0.9, hatch='*')
ax1.set_title('Sweetness Levels of Fruits', fontsize=12, fontweight='light', pad=15)  # Altered title
ax1.set_xlabel('Fruit Types', fontsize=12)  # Altered xlabel
ax1.set_ylabel('Avg Sweetness Level', fontsize=12)  # Altered ylabel
ax1.set_ylim(0, 10)
ax1.grid(True, linestyle='-.', linewidth=0.5)  # Added grid

for i, sweetness in enumerate(avg_sweetness_levels):
    ax1.annotate(f'{sweetness}', xy=(i, sweetness),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=9)

# Second subplot with stylistic changes
ax2 = axs[1]
n, bins, patches = ax2.hist(data, bins=len(fruits), edgecolor='darkgreen', color='orange', alpha=0.8)
ax2.set_title('Fruit Consumption Frequency', fontsize=15, fontweight='medium', pad=18)  # Altered title
ax2.set_xlabel('Types of Fruits', fontsize=12)  # Altered xlabel
ax2.set_ylabel('Number of Fruits', fontsize=12)  # Altered ylabel
ax2.set_xticks(np.arange(len(fruits)))
ax2.set_xticklabels(fruits)
ax2.axhline(y=n.max(), color='red', linestyle='--', linewidth=0.7)  # Added horizontal line

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax2.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()