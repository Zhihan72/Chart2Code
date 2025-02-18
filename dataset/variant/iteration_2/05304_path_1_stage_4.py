import matplotlib.pyplot as plt
import numpy as np

regions = ["N", "S", "E", "W"]
categories = ["Elec", "App", "Home", "Books", "Toys", "Grocs"]

sales_data = np.array([
    [90, 150, 130, 140, 120, 60],
    [80, 160, 180, 110, 130, 115],
    [100, 120, 130, 90, 140, 90],
    [95, 140, 165, 150, 110, 100],
])

product_trends = {
    "Elec": [22, 15, 21, 16, 14, 20, 18, 17, 14, 19, 12, 16],
    "App": [9, 10, 9, 8, 10, 12, 17, 16, 14, 13, 8, 18],
    "Home": [9, 10, 6, 5, 6, 10, 11, 6, 8, 7, 5, 7],
    "Books": [8, 9, 7, 4, 5, 5, 6, 9, 5, 6, 7, 7],
    "Toys": [7, 8, 9, 3, 5, 9, 8, 10, 6, 6, 7, 4],
    "Grocs": [25, 22, 24, 23, 25, 24, 26, 27, 20, 28, 26, 25]
}

trend_data = np.array([product_trends[category] for category in categories])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

masked_data = np.tril(sales_data)

cax = ax1.matshow(masked_data, cmap='viridis', aspect='auto')
ax1.set_xticks(np.arange(len(categories)))
ax1.set_yticks(np.arange(len(regions)))
ax1.set_xticklabels(categories, rotation=45, ha='left')
ax1.set_yticklabels(regions)
fig.colorbar(cax, ax=ax1, orientation='vertical', fraction=0.046, pad=0.04)
ax1.set_title('Triangular Sales by Region/Category', pad=15)

for i in range(masked_data.shape[0]):
    for j in range(masked_data.shape[1]):
        if masked_data[i, j] != 0:
            ax1.text(j, i, f"{masked_data[i, j]:.0f}", ha='center', va='center', color='white' if masked_data[i, j] > 100 else 'black')

months = np.arange(1, 13)
colors = ['purple', 'green', 'blue', 'orange', 'red', 'brown']  # New shuffled colors
for i in range(trend_data.shape[0]):
    ax2.plot(months, trend_data[i], label=categories[i], color=colors[i])
ax2.set_title('Product Sales Trends', pad=15)
ax2.set_xlabel('Month')
ax2.set_ylabel('Avg Sales')
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()