import matplotlib.pyplot as plt
import numpy as np

# Define product categories
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Beauty', 'Toys']

# Sales data for Q1, Q2, and Q3 in 2023 (in thousands of units)
sales_q1 = np.array([150, 200, 130, 120, 170, 90])
sales_q2 = np.array([180, 210, 140, 130, 160, 100])
sales_q3 = np.array([170, 220, 150, 110, 180, 95])

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.25  # Narrower width to accommodate three bars per group
x = np.arange(len(categories))

# Bar plots for Q1, Q2, and Q3
bars1 = ax.bar(x - width, sales_q1, width, color='skyblue', edgecolor='black')
bars2 = ax.bar(x, sales_q2, width, color='lightcoral', edgecolor='black')
bars3 = ax.bar(x + width, sales_q3, width, color='lightgreen', edgecolor='black')

# Adding data labels
for bar in bars1 + bars2 + bars3:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

# Labels and title
ax.set_xlabel('Product Categories', fontsize=12)
ax.set_ylabel('Sales (in thousands)', fontsize=12)
ax.set_title('E-commerce Sales Performance\n(Q1 vs. Q2 vs. Q3 2023)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')

# Style adjustments
ax.yaxis.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()