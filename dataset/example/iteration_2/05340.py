import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents a comparative study of the monthly sales volume 
# of different fruits in a local market over a year, highlighting peak seasons for each fruit.

# Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
apples_sales = np.array([120, 130, 110, 150, 180, 200, 220, 240, 200, 150, 140, 130])
bananas_sales = np.array([90, 100, 110, 120, 130, 140, 150, 160, 150, 140, 130, 110])
oranges_sales = np.array([80, 90, 100, 110, 120, 130, 140, 150, 140, 130, 120, 100])
berries_sales = np.array([70, 80, 90, 100, 110, 120, 130, 140, 130, 120, 110, 90])

# Create the figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 12))

# First subplot: Stacked bar chart for monthly sales data
bar_width = 0.7
positions = np.arange(len(months))

# Plot stacked bars for each fruit
bar1 = axs[0].bar(positions, apples_sales, width=bar_width, color='red', label='Apples', edgecolor='black', alpha=0.8)
bar2 = axs[0].bar(positions, bananas_sales, width=bar_width, bottom=apples_sales, color='yellow', label='Bananas', edgecolor='black', alpha=0.8)
bar3 = axs[0].bar(positions, oranges_sales, width=bar_width, bottom=apples_sales + bananas_sales, color='orange', label='Oranges', edgecolor='black', alpha=0.8)
bar4 = axs[0].bar(positions, berries_sales, width=bar_width, bottom=apples_sales + bananas_sales + oranges_sales, color='purple', label='Berries', edgecolor='black', alpha=0.8)

# Add labels, title, legend
axs[0].set_title('Comparative Monthly Sales Volume of Different Fruits\n(2023)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Month', fontsize=12)
axs[0].set_ylabel('Sales Volume', fontsize=12)
axs[0].set_xticks(positions)
axs[0].set_xticklabels(months, rotation=45, ha='right', fontsize=11)
axs[0].legend(title='Fruits', loc='upper right', fontsize=11, title_fontsize=12)
axs[0].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Display data values on the bars
for bar in bar1 + bar2 + bar3 + bar4:
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + height / 2,
        f'{int(height)}',
        ha='center',
        va='center',
        color='white',
        fontsize=10
    )

# Second subplot: Line chart of cumulative monthly sales
axs[1].plot(months, apples_sales + bananas_sales + oranges_sales + berries_sales, label='Total Sales', color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)

# Add labels, grid, and title
axs[1].set_title('Cumulative Monthly Sales Volume of All Fruits\n(2023)', fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Cumulative Sales Volume', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper left', fontsize=11)

# Add values above the cumulative sales line plot
cumulative_sales = apples_sales + bananas_sales + oranges_sales + berries_sales
for i, value in enumerate(cumulative_sales):
    axs[1].text(i, value + 10, f'{value}', ha='center', va='bottom', fontsize=10, color='blue')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()