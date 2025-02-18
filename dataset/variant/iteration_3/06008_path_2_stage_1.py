import matplotlib.pyplot as plt
import numpy as np

# Monthly sales for different smoothie flavors (in units)
flavors = ['Strawberry', 'Banana', 'Mango', 'Kiwi']
sales_data = {
    'Strawberry': [150, 120, 130, 200, 180, 240, 250, 220, 210, 190, 160, 180],
    'Banana': [100, 80, 75, 95, 85, 105, 115, 110, 108, 102, 92, 104],
    'Mango': [90, 70, 65, 85, 75, 95, 100, 98, 94, 88, 72, 90],
    'Kiwi': [60, 55, 52, 60, 58, 65, 68, 64, 61, 59, 55, 62]
}

# Calculate total sales for each flavor
total_sales = {flavor: sum(sales) for flavor, sales in sales_data.items()}

# Sort flavors by total sales in descending order
sorted_flavors = sorted(total_sales, key=total_sales.get, reverse=True)
sorted_sales_data = [sales_data[flavor] for flavor in sorted_flavors]

# Define the months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months_idx = np.arange(len(months))

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Set bar width
bar_width = 0.2

# Plot bar chart for each sorted smoothie flavor
for i, flavor in enumerate(sorted_flavors):
    ax.bar(months_idx + (i - 1.5) * bar_width, sorted_sales_data[i], 
           width=bar_width, label=flavor, alpha=0.8)

# Titles and labels
ax.set_title('Monthly Sales of Smoothie Flavors at Local Cafe', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Number of Smoothies Sold', fontsize=14)
ax.set_xticks(months_idx)
ax.set_xticklabels(months, fontsize=12)
ax.legend(title='Smoothie Flavors', fontsize=12, title_fontsize='13')

# Grid and limits
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(0, 300)

# Add data labels above each bar
for i, sales in enumerate(sorted_sales_data):
    for j, value in enumerate(sales):
        ax.text(j + (i - 1.5) * bar_width, value + 5, str(value),
                ha='center', va='bottom', fontsize=9, color='black', fontweight='bold')

# Tight layout to adjust padding
plt.tight_layout()

# Show the plot
plt.show()