import matplotlib.pyplot as plt
import numpy as np

renewable_data = np.array([
    [40, 25, 30, 3, 2],
    [20, 35, 25, 10, 10],
    [15, 20, 50, 5, 10],
    [45, 30, 10, 10, 5]
])

new_colors = ['#FF5733', '#33FF57', '#3357FF', '#F5A623', '#8E44AD']

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(4)  # Directly use the length of continents
bar_width = 0.15

for i, color in enumerate(new_colors):
    ax.bar(x + i * bar_width, renewable_data[:, i], bar_width, color=color, edgecolor='black')

ax.set_xticks(x + bar_width * (len(new_colors) / 2 - 0.5))

ax.yaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()