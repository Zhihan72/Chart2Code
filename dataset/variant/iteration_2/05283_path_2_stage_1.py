import matplotlib.pyplot as plt
import numpy as np

# Weeks numbering for the x-axis (total 52 weeks in a year)
weeks = np.arange(1, 53)

# Manually altered weekly sales data for each fruit (in kilograms)
sales_apples = [2, 3, 5, 7, 7, 9, 8, 11, 13, 14, 14, 17, 19, 18, 20, 22, 24, 26, 30, 37, 39, 43, 44, 47, 51, 46, 41, 39, 33, 29, 24, 21, 19, 17, 16, 14, 11, 9, 7, 6, 5, 6, 4, 3, 2, 3, 2.5, 3, 1.5, 2, 1.5, 1]
sales_bananas = [3, 3, 3, 4, 4, 4, 5, 5, 4.5, 4.5, 4.5, 4, 5, 5, 5, 5, 4.5, 5.5, 5.5, 6, 6.5, 6, 7, 7, 6.5, 7, 7, 7, 7.5, 7, 6.5, 7, 7.5, 7, 7, 7, 6.5, 7, 7, 7, 7, 7, 7, 7, 7, 6.5, 7, 7, 7, 7, 7, 7]
sales_cherries = [2, 2, 2, 3, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2, 3, 4, 5, 8, 9, 14, 18, 28, 30, 38, 44, 43, 35, 30, 29, 27, 24, 21, 20, 18, 16, 14, 11, 10, 9, 7, 5, 5, 4, 2, 3, 2, 2, 2, 3, 2, 1.5, 2]
sales_dates = [1.5, 1, 1, 1.5, 1, 1, 2, 1.5, 1, 1, 1, 1, 1, 1, 2, 42, 50, 62, 75, 78, 61, 41, 12, 6, 5, 5, 5, 6, 5, 5, 3.5, 3, 3, 2.5, 2.5, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1.5]

# Combined data for Stacked Area Plot
sales_data = np.vstack([sales_apples, sales_bananas, sales_cherries, sales_dates])

# Define the colors for each fruit
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(weeks, sales_data, labels=['Apples', 'Bananas', 'Cherries', 'Dates'], colors=colors, alpha=0.8)

# Titles and labels
ax.set_title('Seasonal Sales Trends of Different Fruits at a Local Market Over a Year', fontsize=16, fontweight='bold')
ax.set_xlabel('Week', fontsize=12)
ax.set_ylabel('Sales (kilograms)', fontsize=12)

# Add a legend
ax.legend(loc='upper left', title='Fruits')

# Customize grid and layout
ax.grid(linestyle='--', alpha=0.6)
ax.set_xticks(np.arange(1, 53, 4))  # Setting less frequent Xticks for readability
ax.set_xlim(1, 52)
ax.set_ylim(0, 100)

# Enhance readability of x-axis labels
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()