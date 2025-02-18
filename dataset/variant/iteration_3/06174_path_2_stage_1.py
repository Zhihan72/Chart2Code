import matplotlib.pyplot as plt
import numpy as np

# Categories of fruits
categories = ["Apples", "Bananas", "Oranges", "Peaches", "Plums"]

# Quarterly sales data for each fruit category (in thousands)
q1_sales = [120, 80, 150, 90, 60]
q2_sales = [130, 85, 160, 95, 70]
q3_sales = [140, 95, 170, 100, 75]
q4_sales = [150, 100, 180, 110, 80]

# Average sales per quarter
avg_sales_per_quarter = np.mean([q1_sales, q2_sales, q3_sales, q4_sales], axis=0)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting horizontal bar charts for each quarter
height = 0.2  # Height of the bars

y = np.arange(len(categories))  # The label locations

bars1 = ax1.barh(y - 1.5*height, q1_sales, height, label='Q1', color='dodgerblue')
bars2 = ax1.barh(y - 0.5*height, q2_sales, height, label='Q2', color='goldenrod')
bars3 = ax1.barh(y + 0.5*height, q3_sales, height, label='Q3', color='seagreen')
bars4 = ax1.barh(y + 1.5*height, q4_sales, height, label='Q4', color='tomato')

# Titles and labels
ax1.set_title("2022 Quarterly Sales Performance of Fruit Categories", fontsize=18, weight='bold', pad=20)
ax1.set_ylabel("Fruit Categories", fontsize=14)
ax1.set_xlabel("Quarterly Sales (Thousands)", fontsize=14, color='slategray')

# Setting the y-ticks and labels properly
ax1.set_yticks(y)
ax1.set_yticklabels(categories, fontsize=12)
ax1.tick_params(axis='x', labelcolor='slategray')

# Adding grid for better readability
ax1.grid(axis='x', linestyle='--', alpha=0.6)

# Create second x-axis
ax2 = ax1.twiny()
ax2.plot(avg_sales_per_quarter, categories, color='purple', linestyle='--', marker='o', markersize=8, label='Average Quarterly Sales', alpha=0.7)
ax2.set_xlabel("Average Sales (Thousands)", fontsize=14, color='purple')
ax2.tick_params(axis='x', labelcolor='purple')

# Adding legend to both axes
fig.legend(loc='upper right', bbox_to_anchor=(1.1, 1), fontsize=12, frameon=False)

# Add annotations
for index, value in enumerate(q4_sales):
    ax1.text(value + 2, y=index + 1.5*height, s=f"{value}", va='center', ha='left', fontsize=10, color='black')

plt.tight_layout()
plt.show()