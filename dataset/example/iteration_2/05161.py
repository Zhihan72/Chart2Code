import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# "A weekly analysis of soft drink sales in a retail store."

# Define the weeks and soft drink types
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
soft_drinks = ['Cola', 'Lemon-Lime', 'Ginger Ale', 'Root Beer']

# Sales data in liters
cola_sales = [150, 160, 170, 180]
lemon_lime_sales = [90, 100, 120, 130]
ginger_ale_sales = [70, 80, 95, 110]
root_beer_sales = [50, 55, 60, 65]

# Total sales list for stacked bar chart
total_sales = [cola_sales, lemon_lime_sales, ginger_ale_sales, root_beer_sales]

# Initialize subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for different soft drinks
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Bottom values for stacking bars
bottom_values = np.zeros(len(weeks))

# Plotting stacked bar chart
for sales, color, drink in zip(total_sales, colors, soft_drinks):
    ax.bar(weeks, sales, bottom=bottom_values, color=color, edgecolor='black', label=drink, alpha=0.85)
    bottom_values += np.array(sales)

# Adding title and labels
ax.set_title('Weekly Soft Drink Sales Analysis', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Week', fontsize=12, fontweight='bold')
ax.set_ylabel('Liters Sold', fontsize=12, fontweight='bold')

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Soft Drink Type')

# Adding gridlines for readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()