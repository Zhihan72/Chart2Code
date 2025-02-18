import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are analyzing the sales data of three different product categories (Electronics, Furniture, and Clothing) over the course of a year in a retail store. We also include a pie chart to show the overall sales distribution among these categories.

# Monthly sales data (in thousands of USD)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
electronics_sales = [25, 30, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75]
furniture_sales = [20, 25, 22, 30, 35, 40, 38, 42, 45, 50, 48, 52]
clothing_sales = [15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# Overall sales distribution
overall_sales = np.array([sum(electronics_sales), sum(furniture_sales), sum(clothing_sales)])
categories = ['Electronics', 'Furniture', 'Clothing']

# Create the figure with subplots: one for the bar chart and one for the pie chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar chart with grouped bars
bar_width = 0.25
x_indices = np.arange(len(months))

# Plot monthly sales data
ax1.bar(x_indices, electronics_sales, bar_width, label='Electronics', color='royalblue')
ax1.bar(x_indices + bar_width, furniture_sales, bar_width, label='Furniture', color='limegreen')
ax1.bar(x_indices + 2 * bar_width, clothing_sales, bar_width, label='Clothing', color='tomato')

# Customizing the bar chart
ax1.set_title("Monthly Sales Data (2023)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Sales (in thousand USD)", fontsize=12)
ax1.set_xticks(x_indices + bar_width)
ax1.set_xticklabels(months)
ax1.legend(title="Product Category", fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Enhancing visual clarity and consistency
plt.setp(ax1.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=10)
plt.setp(ax1.get_yticklabels(), fontsize=10)

# Pie chart for overall sales distribution
ax2.pie(overall_sales, labels=categories, autopct='%1.1f%%', startangle=140, colors=['royalblue', 'limegreen', 'tomato'])
ax2.set_title("Overall Sales Distribution (2023)", fontsize=14, fontweight='bold')

# Annotate the maximum sales months
ax1.annotate('Highest Sales', xy=(11, 75), xytext=(8, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax1.annotate('Summer Peak', xy=(7, 55), xytext=(4, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

# Ensure the layout is tidy
plt.tight_layout(pad=3.0)

# Show the plot
plt.show()