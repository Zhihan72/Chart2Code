import matplotlib.pyplot as plt
import numpy as np

# Monthly sales data (in thousands of USD)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
electronics_sales = [35, 28, 55, 40, 50, 75, 25, 70, 65, 60, 30, 45]
furniture_sales = [38, 25, 52, 22, 45, 30, 48, 35, 20, 40, 42, 50]
clothing_sales = [60, 55, 18, 30, 50, 40, 20, 65, 45, 35, 15, 25]

# Overall sales distribution
overall_sales = np.array([sum(electronics_sales), sum(furniture_sales), sum(clothing_sales)])
categories = ['Electronics', 'Furniture', 'Clothing']

# Create the figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar chart with grouped bars
bar_width = 0.25
x_indices = np.arange(len(months))

ax1.bar(x_indices, electronics_sales, bar_width, label='Electronics', color='darkorange')
ax1.bar(x_indices + bar_width, furniture_sales, bar_width, label='Furniture', color='darkviolet')
ax1.bar(x_indices + 2 * bar_width, clothing_sales, bar_width, label='Clothing', color='deepskyblue')

ax1.set_title("Monthly Sales Data (2023)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Sales (in thousand USD)", fontsize=12)
ax1.set_xticks(x_indices + bar_width)
ax1.set_xticklabels(months)
ax1.legend(title="Product Category", fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.setp(ax1.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=10)
plt.setp(ax1.get_yticklabels(), fontsize=10)

# Pie chart for overall sales distribution with new colors
ax2.pie(overall_sales, labels=categories, autopct='%1.1f%%', startangle=140, colors=['darkorange', 'darkviolet', 'deepskyblue'])
ax2.set_title("Overall Sales Distribution (2023)", fontsize=14, fontweight='bold')

# Annotate maximum sales months
ax1.annotate('Highest Sales', xy=(11, 75), xytext=(8, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax1.annotate('Summer Peak', xy=(7, 55), xytext=(4, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

plt.tight_layout(pad=3.0)

# Show the plot
plt.show()