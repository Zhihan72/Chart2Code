import numpy as np
import matplotlib.pyplot as plt

# Define the data
sales_data = np.array([
    [120, 100, 110, 140, 150, 130, 145, 180, 160, 175, 190, 210],  # USA
    [90, 85, 100, 95, 105, 115, 120, 130, 140, 150, 160, 170],    # Canada
    [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],   # Germany
    [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170],     # Australia
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]    # India
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