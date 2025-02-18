import matplotlib.pyplot as plt
import numpy as np

# Define product categories with modified labels
categories = ['Tech Gadgets', 'Apparel', 'Home Essentials', 'Outdoor Gear', 'Kids Play']

# Sales data for Q1 and Q2 in 2023 (in thousands of units)
sales_q1 = np.array([150, 200, 130, 120, 90])
sales_q2 = np.array([180, 210, 140, 130, 100])

# Calculate total sales for sorting
total_sales = sales_q1 + sales_q2
sorted_indices = np.argsort(-total_sales)
categories = [categories[i] for i in sorted_indices]
sales_q1 = sales_q1[sorted_indices]
sales_q2 = sales_q2[sorted_indices]

# Create a sorted bar chart
fig, ax = plt.subplots(figsize=(14, 8))
width = 0.35
x = np.arange(len(categories))

# Bar plots
bars1 = ax.bar(x - width/2, sales_q1, width, label='Winter Quarter', color='seagreen', edgecolor='black')
bars2 = ax.bar(x + width/2, sales_q2, width, label='Spring Quarter', color='darkorange', edgecolor='black')

# Adding data labels
for bar in bars1 + bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

# Adding labels and title
ax.set_xlabel('Categories', fontsize=12)
ax.set_ylabel('Units Sold (000s)', fontsize=12)
ax.set_title('Sales Overview by Category\n(Comparison of Winter vs. Spring)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend(title='Duration', fontsize=12, title_fontsize=13)

# Grid settings
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()