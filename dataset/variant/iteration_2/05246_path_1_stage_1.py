import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year
months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

# Sales data for two products (in thousands)
product_A_sales = np.array([10, 15, 14, 18, 20, 22, 24, 23, 21, 19, 17, 16])
product_B_sales = np.array([12, 14, 16, 19, 21, 23, 25, 26, 24, 22, 20, 18])

# Define positions for each month on the x-axis
x_positions = np.arange(len(months))

# Create the bar chart with subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Set bar width
bar_width = 0.25

# Plotting the sales data for each product
bars_A = ax.bar(x_positions - bar_width / 2, product_A_sales, width=bar_width, label='Product A', color='blue', edgecolor='black')
bars_B = ax.bar(x_positions + bar_width / 2, product_B_sales, width=bar_width, label='Product B', color='green', edgecolor='black')

# Add annotations to indicate significant milestones
annotations = {
    'March': ('Peak Sales for Product B', (0, 30)),
    'August': ('New Product Launch', (0, -50)),
    'December': ('Holiday Discounts', (0, 20))
}

for month, (text, offset) in annotations.items():
    index = np.where(months == month)[0][0]
    target_sales = product_B_sales[index] if month == 'March' else (product_A_sales[index] + product_B_sales[index]) / 2.0
    ax.annotate(
        text, 
        (x_positions[index], target_sales), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='grey'),
        ha='center', fontsize=10, color='darkred'
    )

# Titles and labels
ax.set_title("Monthly Sales Analysis of Products A and B in 2022", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Sales (in thousands)", fontsize=14)

# Set x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(months, fontsize=11, rotation=30, ha='right')

# Add legend and grid
ax.legend(fontsize=12, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)

# Calculate the average sales line and plot it
average_sales = (product_A_sales + product_B_sales) / 2
ax.plot(x_positions, average_sales, color='purple', linestyle='-.', marker='o', linewidth=1.5, label='Average Sales')
ax.legend(fontsize=12, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()