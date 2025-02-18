import matplotlib.pyplot as plt
import numpy as np

# Scenario: Tracking the Popularity of Different Smoothie Flavors at a Local Cafe
# over a 12-month period.

# Define the months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Monthly sales for different smoothie flavors (in units)
strawberry_sales = [150, 120, 130, 200, 180, 240, 250, 220, 210, 190, 160, 180]
banana_sales = [100, 80, 75, 95, 85, 105, 115, 110, 108, 102, 92, 104]
mango_sales = [90, 70, 65, 85, 75, 95, 100, 98, 94, 88, 72, 90]
kiwi_sales = [60, 55, 52, 60, 58, 65, 68, 64, 61, 59, 55, 62]

# Data transformation for subplots
monthly_sales = np.array([strawberry_sales, banana_sales, mango_sales, kiwi_sales])
flavors = ['Strawberry', 'Banana', 'Mango', 'Kiwi']

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Set bar width
bar_width = 0.2

# Plot bar charts for each smoothie flavor
months_idx = np.arange(len(months))
ax.bar(months_idx - 1.5 * bar_width, strawberry_sales, width=bar_width, label='Strawberry', color='#FF6347', alpha=0.8)
ax.bar(months_idx - 0.5 * bar_width, banana_sales, width=bar_width, label='Banana', color='#FFD700', alpha=0.8)
ax.bar(months_idx + 0.5 * bar_width, mango_sales, width=bar_width, label='Mango', color='#FFA500', alpha=0.8)
ax.bar(months_idx + 1.5 * bar_width, kiwi_sales, width=bar_width, label='Kiwi', color='#7FFF00', alpha=0.8)

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
for i, sales in enumerate(monthly_sales):
    for j, value in enumerate(sales):
        ax.text(j - 1.5*bar_width + i*bar_width, value + 5, str(value),
                ha='center', va='bottom', fontsize=9, color='black', fontweight='bold')

# Tight layout to adjust padding
plt.tight_layout()

# Show the plot
plt.show()