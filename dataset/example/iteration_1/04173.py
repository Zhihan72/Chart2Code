import matplotlib.pyplot as plt
import numpy as np

# Establish the backstory: Sales Performance of Different Product Categories in a Department Store Over Four Quarters
# Product categories: Electronics, Clothing, Groceries, Household Items, Books
# Quarters: Q1, Q2, Q3, Q4

# Define categories and quarters
categories = ['Electronics', 'Clothing', 'Groceries', 'Household Items', 'Books']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Sales data (in thousands of dollars) for each category over the quarters
sales_data = np.array([
    [120, 130, 115, 140],  # Electronics
    [80, 90, 85, 100],     # Clothing
    [150, 160, 155, 170],  # Groceries
    [70, 75, 65, 80],      # Household Items
    [50, 55, 60, 65],      # Books
])

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot the bar chart for each quarter

bar_width = 0.2
bar_positions = np.arange(len(categories))

for i, quarter in enumerate(quarters):
    ax1.bar(bar_positions + i * bar_width, sales_data[:, i], width=bar_width, label=quarter)

# Set title, labels, and tick positions
ax1.set_title('Quarterly Sales Performance of Product Categories\nin Department Store (in Thousands of Dollars)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Product Categories', fontsize=12)
ax1.set_ylabel('Sales ($3)', fontsize=12)
ax1.set_xticks(bar_positions + bar_width * 1.5)
ax1.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)

# Add a legend to the bar chart
ax1.legend(title='Quarter', loc='upper left', bbox_to_anchor=(1, 1))

# Aggregate annual sales for each category
annual_sales = np.sum(sales_data, axis=1)

# Plot the bar chart for annual sales
ax2.bar(categories, annual_sales, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Annotate each bar (annual sales) with the total amount
for idx, category in enumerate(categories):
    ax2.annotate(f'{annual_sales[idx]:,}', 
                 xy=(idx, annual_sales[idx]), 
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, color='black')

# Set title, labels, and tick positions for annual sales chart
ax2.set_title('Annual Sales Performance of Product Categories\nin Department Store (in Thousands of Dollars)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Product Categories', fontsize=12)
ax2.set_ylabel('Sales ($)', fontsize=12)
ax2.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)

# Use tight layout to prevent overlapping and improve layout
plt.tight_layout()

# Display the plot
plt.show()