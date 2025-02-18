import matplotlib.pyplot as plt
import numpy as np

# Define months and chocolate types
weeks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
candy_types = ['Bright Chocolate', 'Milky Chocolate', 'Light Chocolate']

# Artificially created production data for each type of chocolate (in thousands of bars)
bright_chocolate = [15, 18, 20, 22, 19, 18, 20, 24, 23, 22, 20, 21]
milky_chocolate = [25, 28, 30, 27, 26, 30, 34, 33, 31, 30, 29, 30]
light_chocolate = [10, 12, 14, 13, 12, 15, 18, 17, 16, 15, 14, 16]

# Colors for the bars
colors = ['#6A0572', '#C70039', '#FFBF00']

# Combine the data for grouped bar chart
bar_width = 0.25  # width of each bar
x = np.arange(len(weeks))  # positions for the groups of bars

# Create subplots: Grouped Bar Chart and Line Chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Bar Chart for chocolate production
ax1.bar(x - bar_width, bright_chocolate, width=bar_width, color=colors[0], edgecolor='black', label='Bright Chocolate')
ax1.bar(x, milky_chocolate, width=bar_width, color=colors[1], edgecolor='black', label='Milky Chocolate')
ax1.bar(x + bar_width, light_chocolate, width=bar_width, color=colors[2], edgecolor='black', label='Light Chocolate')

# Set labels, title, ticks, and legend for the bar chart
ax1.set_xlabel('Weeks', fontsize=12)
ax1.set_ylabel('Output (in thousands of bars)', fontsize=12)
ax1.set_title('Monthly Chocolate Output in the Candy Factory', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(weeks)
ax1.legend(title='Candy Varieties', fontsize=10, title_fontsize=12)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Calculate total productions to include in the line plot
total_output = np.array(bright_chocolate) + np.array(milky_chocolate) + np.array(light_chocolate)

# Line chart for displaying the total production trend
ax2.plot(weeks, total_output, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6, label='Aggregate Output')
ax2.fill_between(weeks, total_output, color='lightblue', alpha=0.3)

# Set labels, title, and grid for the line chart
ax2.set_xlabel('Weeks', fontsize=12)
ax2.set_ylabel('Aggregate Output (in thousands of bars)', fontsize=12)
ax2.set_title('Total Candy Bars Output Across the Year', fontsize=16, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout for better spacing and visibility
plt.tight_layout()

# Display the plot
plt.show()