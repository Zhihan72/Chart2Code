import numpy as np
import matplotlib.pyplot as plt

# Define the data for the 3D bar chart
months = ['Jun', 'Jan', 'Apr', 'Mar', 'May', 'Feb']
coffee_varieties = ['Mocha', 'Espresso', 'Americano', 'Latte', 'Cappuccino']

# Sales data in units sold (rows: months, columns: coffee varieties)
sales_data = np.array([
    [240, 150, 180, 200, 250],  # June
    [150, 240, 180, 270, 330],  # January
    [210, 200, 230, 250, 270],  # April
    [200, 180, 220, 230, 260],  # March
    [220, 210, 250, 260, 320],  # May
    [180, 220, 190, 230, 260]   # February
])

# Calculate average monthly sales
average_sales = sales_data.mean(axis=1)

# Prepare the 3D plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Define colors for each coffee variety
colors = ['#CD853F', '#8B4513', '#A0522D', '#DEB887', '#D2691E']
dx = dy = 0.5

# Plot each coffee variety's sales data
for y, color in enumerate(colors):
    xs = np.arange(len(months))
    ys = sales_data[:, y]
    ax.bar3d(xs, y, np.zeros_like(xs), dx, dy, ys, color=color, alpha=0.8, label=coffee_varieties[y])

# Plot the average monthly sales line
ax.plot(np.arange(len(months)), [-0.5] * len(months), average_sales, color='navy', marker='o', linewidth=2, label='Average Sales')

# Set axis labels and ticks
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45)
ax.set_yticks(np.arange(len(coffee_varieties)))
ax.set_yticklabels(coffee_varieties)
ax.set_xlabel('Moths', labelpad=10)
ax.set_ylabel('Coffee Types', labelpad=10)
ax.set_zlabel('Sold Units', labelpad=10)

# Set a viewing angle for better visibility
ax.view_init(elev=20, azim=135)

# Add title and legend
ax.set_title('Sales Monthly Performance\nand Coffee Varieties Average Units', fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Improve layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()