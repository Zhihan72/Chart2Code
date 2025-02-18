import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
stores = ["Store A", "Store B", "Store C", "Store D", "Store E"]

# Altered Revenue data
revenue = np.array([
    [12, 11, 13, 16, 15],  # Store A
    [9, 11, 8, 13, 12],    # Store B
    [16, 14, 17, 19, 21],  # Store C
    [14, 13, 15, 16, 17],  # Store D
    [10, 12, 9, 13, 14],   # Store E
])

# Create subplots
fig, ax1 = plt.subplots(figsize=(14, 8))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']
bar_height = 0.15

for idx, store in enumerate(stores):
    ax1.barh(years + np.array(range(idx, idx+1))*bar_height, revenue[:, idx], height=bar_height, color=colors, alpha=0.7)

# Set the title and labels
ax1.set_title('Retail Chain Performance Analysis:\nRevenue per Year (2018-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Revenue (in millions)', fontsize=12)
ax1.set_ylabel('Stores', fontsize=12)
ax1.set_yticks(years + bar_height*(len(years)-1)/2)
ax1.set_yticklabels(years)

# Move the legend to the lower center
bars = [store + " Revenue" for store in stores]
ax1.legend(bars, title='Revenue Years', loc='lower right', fontsize=10, frameon=True)

ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()
plt.show()