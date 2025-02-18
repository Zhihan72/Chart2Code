import matplotlib.pyplot as plt
import numpy as np

# Backstory: Weekly Sales Data of Different Fruits at a Local Market Over a Year
# Topic: Analyzing the seasonal sales trends of Apples, Bananas, Cherries, and Dates

# Define weeks numbering for the x-axis (total 52 weeks in a year)
weeks = np.arange(1, 53)

# Weekly sales data for each fruit (in kilograms)
# Data explicitly created to show seasonal trends:
# - Apples peak in autumn,
# - Bananas are steady throughout the year,
# - Cherries peak in summer,
# - Dates peak during Ramadan (weeks 18-22)

sales_apples = [2, 3, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 21, 22, 23, 25, 30, 35, 40, 42, 45, 48, 50, 45, 42, 38, 32, 28, 25, 22, 20, 18, 15, 13, 12, 10, 8, 7, 6, 5, 4, 3, 3, 3, 2.5, 2.5, 2, 2, 1.5, 1.5]
sales_bananas = [3, 3, 3, 3, 4, 4, 4, 4.5, 4.5, 4.5, 4.5, 4.5, 5, 5, 5, 5, 5, 5.5, 6, 6, 6.5, 6.5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
sales_cherries = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 7, 10, 15, 20, 30, 35, 40, 45, 42, 38, 32, 30, 28, 25, 22, 21, 20, 17, 15, 12, 10, 8, 7, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
sales_dates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 40, 50, 60, 70, 80, 60, 40, 10, 5, 5, 5, 5, 5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# Combined data for Stacked Area Plot
sales_data = np.vstack([sales_apples, sales_bananas, sales_cherries, sales_dates])

# Define the colors for each fruit
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(weeks, sales_data, labels=['Apples', 'Bananas', 'Cherries', 'Dates'], colors=colors, alpha=0.8)

# Add titles and labels
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

# Enhance the readability of x-axis labels
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()