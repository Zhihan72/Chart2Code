import numpy as np
import matplotlib.pyplot as plt

# Altered the data randomly within each group
sales_data = np.array([
    [150, 110, 130, 140, 120, 145, 100, 180, 160, 175, 190, 210],  # USA
    [105, 90, 120, 150, 95, 140, 100, 85, 115, 130, 160, 170],    # Canada
    [210, 120, 130, 170, 140, 220, 100, 180, 190, 200, 150, 160],   # Germany
    [150, 70, 80, 90, 60, 110, 120, 130, 140, 100, 160, 170],     # Australia
    [90, 130, 100, 170, 180, 150, 80, 120, 160, 140, 190, 110]    # India
])
average_sales = sales_data.mean(axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
index = np.arange(12)

colors = ['#32CD32', '#FF6347', '#4682B4', '#800080', '#FFD700']
hatches = ['/', '\\', '-', '|', '+']

for i in range(5):
    ax.barh(index + i * bar_height, sales_data[i], bar_height, color=colors[i], alpha=0.75, hatch=hatches[i])

ax.plot(average_sales, index + 2 * bar_height, color='black', linestyle=':', marker='s', linewidth=2, markersize=8)

ax.set_yticks(index + 2 * bar_height)

ax.xaxis.grid(True, linestyle=':', color='gray', alpha=0.7)
ax.yaxis.grid(True)

plt.tight_layout()
plt.show()