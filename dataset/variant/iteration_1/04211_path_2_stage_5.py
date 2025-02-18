import matplotlib.pyplot as plt
import numpy as np

fruit_types = ['Cherry', 'Banana', 'Elderberry', 'Apple', 'Date']

usage_data = np.array([
    [60, 35, 40, 45, 30],
    [65, 50, 60, 55, 80],
    [190, 150, 180, 170, 160],
    [70, 40, 50, 55, 45],
    [160, 150, 135, 140, 155]
])

total_usage = usage_data.sum(axis=1)
sorted_indices = np.argsort(total_usage)
sorted_fruit_types = [fruit_types[i] for i in sorted_indices]
sorted_total_usage = total_usage[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

# Randomly altered colors for bars
colors = ['#e74c3c', '#8e44ad', '#16a085', '#f39c12', '#2ecc71']

# Plot sorted bar chart with different colors
ax.bar(sorted_fruit_types, sorted_total_usage, color=[colors[i] for i in sorted_indices])

# Randomly altered chart labels and styles
ax.set_xlabel('Fruit Varieties', fontsize=14, fontstyle='italic')
ax.set_ylabel('Total Usage Instances', fontsize=14, fontstyle='italic')
ax.set_title('Five-Year Aggregated Fruit Usage', fontsize=18, fontweight='bold', pad=30)

# Add grid
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Add a border by setting the spine color and width
for spine in ax.spines.values():
    spine.set_edgecolor('#34495e')
    spine.set_linewidth(1.2)

# Add legend after bars with colorful markers
ax.legend(['Usage Data'], loc='upper left', frameon=True, fontsize=12, markerfirst=True)

plt.tight_layout()
plt.show()