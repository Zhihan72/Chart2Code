import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Visualize the Sales Performance of Different Product Categories in an E-commerce Store
# across the first two quarters of 2023. This visualization aims to help the management
# identify the categories with the highest and lowest sales and plan strategies for the future.

# Define product categories
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Beauty', 'Toys']

# Sales data for Q1 and Q2 in 2023 (in thousands of units)
sales_q1 = np.array([150, 200, 130, 120, 170, 90])
sales_q2 = np.array([180, 210, 140, 130, 160, 100])

# Create a bar chart to compare sales
fig, ax = plt.subplots(figsize=(14, 8))

width = 0.35  # width of the bars
x = np.arange(len(categories))

# Bar plots
bars1 = ax.bar(x - width/2, sales_q1, width, label='Q1 2023', color='skyblue', edgecolor='black')
bars2 = ax.bar(x + width/2, sales_q2, width, label='Q2 2023', color='lightcoral', edgecolor='black')

# Adding data labels
for bar in bars1 + bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

# Adding some text for labels, title, and axes ticks
ax.set_xlabel('Product Categories', fontsize=12)
ax.set_ylabel('Sales (in thousands)', fontsize=12)
ax.set_title('E-commerce Sales Performance\n(Q1 vs. Q2 2023)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend(title='Quarters', fontsize=12, title_fontsize=13)

# Grid settings
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()