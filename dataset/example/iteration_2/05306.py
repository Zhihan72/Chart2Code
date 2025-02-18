import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart illustrates the monthly sales performance of fruit juice and soda in different regions of a country in 2022.
# Comparisons between these beverages are provided, aiming to understand the consumer preferences by region.

# Define regions and data
regions = ['North', 'South', 'East', 'West']
fruit_juice_sales = [1200, 1500, 1400, 1300]  # Monthly sales (in liters) of fruit juice
soda_sales = [1800, 1600, 1700, 1500]        # Monthly sales (in liters) of soda

# Data for the percentage increase in total beverage sales compared to the previous year
percentage_increase = [10, 12, 8, 15]  # Example data

# Position of bars on x-axis
x = np.arange(len(regions))

# Width of a bar
width = 0.35

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Bar chart for sales performance (first subplot)
bars1 = ax1.bar(x - width/2, fruit_juice_sales, width, label='Fruit Juice Sales', color='#ff9999')
bars2 = ax1.bar(x + width/2, soda_sales, width, label='Soda Sales', color='#66b3ff')

# Customization
ax1.set_title('Monthly Sales Performance of Beverages by Region in 2022', fontsize=16, fontweight='bold')
ax1.set_xlabel('Region', fontsize=13)
ax1.set_ylabel('Sales (in liters)', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(regions, fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.legend(loc='upper right', fontsize=11)

# Add data labels on bars
def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 30, int(yval), va='center', ha='center', fontsize=11, fontweight='bold', color='black')

add_labels(ax1, bars1)
add_labels(ax1, bars2)

# Bar chart for percentage increase (second subplot)
bars3 = ax2.bar(x, percentage_increase, color='#ffcc99')

# Customization
ax2.set_title('Percentage Increase in Total Beverage Sales by Region\n(compared to the previous year)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Region', fontsize=13)
ax2.set_ylabel('Percentage Increase (%)', fontsize=13)
ax2.set_xticks(x)
ax2.set_xticklabels(regions, fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Add data labels on bars
for bar in bars3:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, yval + 1, f'{yval}%', va='center', ha='center', fontsize=11, fontweight='bold', color='black')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()