import matplotlib.pyplot as plt
import numpy as np

# Define regions and product categories
regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Apparel", "Home Goods", "Books", "Toys", "Groceries"]

# Constructing fictional sales data for illustration
sales_data = np.array([
    [120, 140, 130, 90, 60, 150],  # North
    [180, 160, 115, 80, 110, 130], # South
    [90, 130, 140, 100, 90, 120],  # East
    [150, 110, 165, 95, 100, 140], # West
])

# Creating data for subplot to show product trends over the months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_trends = {
    "Electronics": [12, 15, 14, 16, 14, 20, 18, 17, 16, 19, 21, 22],
    "Apparel": [8, 9, 10, 12, 13, 15, 18, 17, 16, 14, 10, 9],
    "Home Goods": [5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6],
    "Books": [4, 5, 5, 5, 6, 7, 6, 7, 6, 7, 8, 9],
    "Toys": [3, 4, 5, 6, 7, 6, 8, 9, 7, 8, 9, 10],
    "Groceries": [20, 22, 25, 23, 25, 24, 26, 27, 28, 26, 25, 24]
}

# Convert product trends to a matrix for subplot
trend_data = np.array([product_trends[category] for category in categories])

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Mask upper triangle for the main heatmap
masked_data = np.tril(sales_data)

# Plot the triangle heatmap for regional sales data
cax = ax1.matshow(masked_data, cmap='viridis', aspect='auto')

# Set ticks and labels for the heatmap
ax1.set_xticks(np.arange(len(categories)))
ax1.set_yticks(np.arange(len(regions)))
ax1.set_xticklabels(categories, rotation=45, ha='left')
ax1.set_yticklabels(regions)

# Add color bar
fig.colorbar(cax, ax=ax1, orientation='vertical', fraction=0.046, pad=0.04)
ax1.set_title('Triangular Average Monthly Sales by Region and Category', pad=15)

# Annotate heatmap cells with sales values
for i in range(masked_data.shape[0]):
    for j in range(masked_data.shape[1]):
        if masked_data[i, j] != 0:  # Annotate only unmasked cells
            ax1.text(j, i, f"{masked_data[i, j]:.0f}", ha='center', va='center', color='white' if masked_data[i, j] > 100 else 'black')

# Plot the product trend over the months
ax2.plot(months, trend_data.T)
ax2.set_title('Monthly Product Sales Trends', pad=15)
ax2.set_xlabel('Months')
ax2.set_ylabel('Average Sales')
ax2.legend(categories, loc='upper left', bbox_to_anchor=(1, 1))

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()