import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Sales Performance among Different Fruit Categories in 2022 
# Based on hypothetical quarterly sales data measured in thousand units.

# Categories of fruits
categories = ["Apples", "Bananas", "Oranges", "Peaches", "Plums"]

# Quarterly sales data for each fruit category (in thousands)
q1_sales = [120, 80, 150, 90, 60]
q2_sales = [130, 85, 160, 95, 70]
q3_sales = [140, 95, 170, 100, 75]
q4_sales = [150, 100, 180, 110, 80]

# Average sales per quarter to plot on secondary y-axis
avg_sales_per_quarter = np.mean([q1_sales, q2_sales, q3_sales, q4_sales], axis=0)

# Setting figure size 
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the bar charts for each quarter
width = 0.2  # Width of the bars

x = np.arange(len(categories))  # The label locations

bars1 = ax1.bar(x - 1.5*width, q1_sales, width, label='Q1', color='dodgerblue')
bars2 = ax1.bar(x - 0.5*width, q2_sales, width, label='Q2', color='goldenrod')
bars3 = ax1.bar(x + 0.5*width, q3_sales, width, label='Q3', color='seagreen')
bars4 = ax1.bar(x + 1.5*width, q4_sales, width, label='Q4', color='tomato')

# Titles and labels
ax1.set_title("2022 Quarterly Sales Performance of Fruit Categories", fontsize=18, weight='bold', pad=20)
ax1.set_xlabel("Fruit Categories", fontsize=14)
ax1.set_ylabel("Quarterly Sales (Thousands)", fontsize=14, color='slategray')

# Setting the x-ticks and labels properly
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)
ax1.tick_params(axis='y', labelcolor='slategray')

# Adding grid for better readability
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Create second y-axis
ax2 = ax1.twinx()
ax2.plot(categories, avg_sales_per_quarter, color='purple', linestyle='--', marker='o', markersize=8, label='Average Quarterly Sales', alpha=0.7)
ax2.set_ylabel("Average Sales (Thousands)", fontsize=14, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Adding legend to both axes
fig.legend(loc='upper right', bbox_to_anchor=(1.1, 1), fontsize=12, frameon=False)

# Add annotations
for index, value in enumerate(q4_sales):
    ax1.text(x=index + 1.5*width, y=value + 2, s=f"{value}", ha='center', va='bottom', fontsize=10, color='black')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()