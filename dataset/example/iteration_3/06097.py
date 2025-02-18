import matplotlib.pyplot as plt
import numpy as np

# Define the backstory and context
# This chart represents the annual production of different types of chocolate bars in a confectionery factory, segmented by months.

# Define months and chocolate types
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
chocolate_types = ['Dark Chocolate', 'Milk Chocolate', 'White Chocolate']

# Artificially created production data for each type of chocolate (in thousands of bars)
dark_chocolate = [15, 18, 20, 22, 19, 18, 20, 24, 23, 22, 20, 21]
milk_chocolate = [25, 28, 30, 27, 26, 30, 34, 33, 31, 30, 29, 30]
white_chocolate = [10, 12, 14, 13, 12, 15, 18, 17, 16, 15, 14, 16]

# Colors for the bars
colors = ['#6A0572', '#C70039', '#FFBF00']

# Combine the data for grouped bar chart
bar_width = 0.25  # width of each bar
x = np.arange(len(months))  # positions for the groups of bars

# Create subplots: Grouped Bar Chart and Line Chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Bar Chart for chocolate production
ax1.bar(x - bar_width, dark_chocolate, width=bar_width, color=colors[0], edgecolor='black', label='Dark Chocolate')
ax1.bar(x, milk_chocolate, width=bar_width, color=colors[1], edgecolor='black', label='Milk Chocolate')
ax1.bar(x + bar_width, white_chocolate, width=bar_width, color=colors[2], edgecolor='black', label='White Chocolate')

# Set labels, title, ticks, and legend for the bar chart
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Production (in thousands of bars)', fontsize=12)
ax1.set_title('Monthly Chocolate Production in the Confectionery Factory', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(months)
ax1.legend(title='Chocolate Types', fontsize=10, title_fontsize=12)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Calculate total productions to include in the line plot
total_production = np.array(dark_chocolate) + np.array(milk_chocolate) + np.array(white_chocolate)

# Line chart for displaying the total production trend
ax2.plot(months, total_production, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6, label='Total Production')
ax2.fill_between(months, total_production, color='lightblue', alpha=0.3)

# Set labels, title, and grid for the line chart
ax2.set_xlabel('Months', fontsize=12)
ax2.set_ylabel('Total Production (in thousands of bars)', fontsize=12)
ax2.set_title('Total Chocolate Bars Production Across the Year', fontsize=16, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout for better spacing and visibility
plt.tight_layout()

# Display the plot
plt.show()