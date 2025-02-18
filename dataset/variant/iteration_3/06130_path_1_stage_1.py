import matplotlib.pyplot as plt
import numpy as np

# Define product categories
categories = ['Elec', 'Bks', 'Clth', 'Home', 'Sport']

# Define months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Hypothetical monthly sales data (in thousands)
sales_data = {
    'Elec': [25, 22, 27, 20, 30, 35, 40, 38, 45, 50, 55, 60],
    'Bks': [15, 18, 24, 30, 22, 20, 25, 20, 15, 10, 12, 18],
    'Clth': [20, 25, 30, 28, 35, 40, 38, 42, 50, 55, 60, 65],
    'Home': [18, 22, 27, 23, 25, 30, 35, 33, 37, 40, 43, 45],
    'Sport': [10, 15, 20, 18, 22, 25, 27, 30, 35, 40, 45, 50]
}

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.15  # Width of each bar
x = np.arange(len(months))

# Plot the bar chart
for i, (category, sales) in enumerate(sales_data.items()):
    ax.bar(x + i * width, sales, width=width, label=category)

# Set labels and title
ax.set_xlabel('Mnths', fontsize=12)
ax.set_ylabel('Sales (k units)', fontsize=12)
ax.set_title('Sales Data 2023', fontsize=14, fontweight='bold')
ax.set_xticks(x + (len(categories) - 1) * width / 2)
ax.set_xticklabels(months)

# Adding grid lines and legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(title='Categories')

# Annotate sales values on each bar
for i, sales in enumerate(sales_data.values()):
    for j, value in enumerate(sales):
        ax.text(j + i * width, value + 1, f'{value}', ha='center', va='bottom', fontsize=8, color='black')

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()