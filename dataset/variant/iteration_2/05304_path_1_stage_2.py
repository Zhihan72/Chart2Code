import matplotlib.pyplot as plt
import numpy as np

# Define regions and product categories
regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Apparel", "Home Goods", "Books", "Toys", "Groceries"]

# Modified sales data (values shuffled within the groups)
sales_data = np.array([
    [90, 150, 130, 140, 120, 60],  # North
    [80, 160, 180, 110, 130, 115], # South
    [100, 120, 130, 90, 140, 90],  # East
    [95, 140, 165, 150, 110, 100], # West
])

# Product trends data shuffled within months
product_trends = {
    "Electronics": [22, 15, 21, 16, 14, 20, 18, 17, 14, 19, 12, 16],
    "Apparel": [9, 10, 9, 8, 10, 12, 17, 16, 14, 13, 8, 18],
    "Home Goods": [9, 10, 6, 5, 6, 10, 11, 6, 8, 7, 5, 7],
    "Books": [8, 9, 7, 4, 5, 5, 6, 9, 5, 6, 7, 7],
    "Toys": [7, 8, 9, 3, 5, 9, 8, 10, 6, 6, 7, 4],
    "Groceries": [25, 22, 24, 23, 25, 24, 26, 27, 20, 28, 26, 25]
}

# Convert product trends to a matrix for subplot
trend_data = np.array([product_trends[category] for category in categories])

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Mask upper triangle for the main heatmap
masked_data = np.tril(sales_data)

# Plot the triangle heatmap for regional sales data
cax = ax1.matshow(masked_data, cmap='viridis', aspect='auto')
ax1.set_xticks(np.arange(len(categories)))
ax1.set_yticks(np.arange(len(regions)))
ax1.set_xticklabels(categories, rotation=45, ha='left')
ax1.set_yticklabels(regions)
fig.colorbar(cax, ax=ax1, orientation='vertical', fraction=0.046, pad=0.04)
ax1.set_title('Triangular Average Monthly Sales by Region and Category', pad=15)

# Annotate heatmap cells with sales values
for i in range(masked_data.shape[0]):
    for j in range(masked_data.shape[1]):
        if masked_data[i, j] != 0:
            ax1.text(j, i, f"{masked_data[i, j]:.0f}", ha='center', va='center', color='white' if masked_data[i, j] > 100 else 'black')

# Plot the product trend over the months
ax2.plot(months, trend_data.T)
ax2.set_title('Monthly Product Sales Trends', pad=15)
ax2.set_xlabel('Months')
ax2.set_ylabel('Average Sales')
ax2.legend(categories, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()