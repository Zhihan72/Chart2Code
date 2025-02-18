import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Analysis of Monthly Sales Data in an Online Store for Different Product Categories.
# Our objective is to visualize the sales distribution and compare monthly variations.

# Define product categories
categories = ['Electronics', 'Books', 'Clothing', 'Home & Kitchen', 'Sports & Outdoors']

# Define months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Hypothetical monthly sales data for each category (in thousands of units)
sales_data = {
    'Electronics': [25, 22, 27, 20, 30, 35, 40, 38, 45, 50, 55, 60],
    'Books': [15, 18, 24, 30, 22, 20, 25, 20, 15, 10, 12, 18],
    'Clothing': [20, 25, 30, 28, 35, 40, 38, 42, 50, 55, 60, 65],
    'Home & Kitchen': [18, 22, 27, 23, 25, 30, 35, 33, 37, 40, 43, 45],
    'Sports & Outdoors': [10, 15, 20, 18, 22, 25, 27, 30, 35, 40, 45, 50]
}

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Number of categories and months
num_categories = len(categories)
num_months = len(months)
width = 0.15  # Width of each bar

# Define position for each set of bars
x = np.arange(num_months)

# Plot the bar chart
for i, (category, sales) in enumerate(sales_data.items()):
    ax.bar(x + i * width, sales, width=width, label=category)

# Set labels and title
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Sales (in thousands of units)', fontsize=12)
ax.set_title('Monthly Sales Data for Different Product Categories in 2023', fontsize=14, fontweight='bold')
ax.set_xticks(x + (num_categories - 1) * width / 2)
ax.set_xticklabels(months)

# Adding grid lines and legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(title='Product Categories')

# Annotate sales values on each bar
for i, sales in enumerate(sales_data.values()):
    for j, value in enumerate(sales):
        ax.text(j + i * width, value + 1, f'{value}', ha='center', va='bottom', fontsize=8, color='black')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()