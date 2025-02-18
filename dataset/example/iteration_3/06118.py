import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart shows the average monthly sales in units of different products for a fictional retail store Frontline Outfitters for the first half of the year.

# Categories or Products
products = ["T-Shirts", "Jeans", "Jackets", "Shoes", "Hats", "Scarves"]

# Average monthly sales
sales_jan = [150, 120, 80, 180, 50, 40]
sales_feb = [160, 130, 85, 190, 55, 45]
sales_mar = [170, 140, 90, 200, 60, 50]
sales_apr = [180, 150, 95, 210, 65, 55]
sales_may = [190, 160, 100, 220, 70, 60]
sales_jun = [200, 170, 105, 230, 75, 65]

# Creating the list of months for plotting
months = ["January", "February", "March", "April", "May", "June"]

# Creating the matplotlib figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Bar width
bar_width = 0.13

# Positions of the bars on the x-axis
r1 = np.arange(len(products))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]
r6 = [x + bar_width for x in r5]

# Plotting the bars
bar1 = ax.bar(r1, sales_jan, color='blue', width=bar_width, edgecolor='grey', label='January')
bar2 = ax.bar(r2, sales_feb, color='orange', width=bar_width, edgecolor='grey', label='February')
bar3 = ax.bar(r3, sales_mar, color='green', width=bar_width, edgecolor='grey', label='March')
bar4 = ax.bar(r4, sales_apr, color='red', width=bar_width, edgecolor='grey', label='April')
bar5 = ax.bar(r5, sales_may, color='purple', width=bar_width, edgecolor='grey', label='May')
bar6 = ax.bar(r6, sales_jun, color='brown', width=bar_width, edgecolor='grey', label='June')

# Adding grid for better readability
ax.grid(linestyle='--', alpha=0.7)

# Adding title and labels
plt.title('Average Monthly Sales of Products at Frontline Outfitters (H1)', fontsize=16, pad=20)
plt.xlabel('Product Categories', fontsize=14)
plt.ylabel('Average Monthly Sales (Units)', fontsize=14)

# Add custom x-axis labels
plt.xticks([r + 2.5 * bar_width for r in r1], products, rotation=45)

# Adding legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Months', fontsize=10, frameon=False)

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Display the plot
plt.show()