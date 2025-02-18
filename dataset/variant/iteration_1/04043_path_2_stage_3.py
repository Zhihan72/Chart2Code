import matplotlib.pyplot as plt
import numpy as np

categories = ['Beauty', 'Sports', 'Toys', 'Electronics', 'Home & Kitchen', 'Clothing']
sales_q1 = np.array([150, 200, 130, 120, 170, 90])
sales_q2 = np.array([180, 210, 140, 130, 160, 100])
sales_q3 = np.array([170, 220, 150, 110, 180, 95])

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.25
x = np.arange(len(categories))

bars1 = ax.bar(x - width, sales_q1, width, color='skyblue', edgecolor='black')
bars2 = ax.bar(x, sales_q2, width, color='lightcoral', edgecolor='black')
bars3 = ax.bar(x + width, sales_q3, width, color='lightgreen', edgecolor='black')

for bar in bars1 + bars2 + bars3:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

ax.set_xlabel('Product Segments', fontsize=12)
ax.set_ylabel('Units Sold (in thousands)', fontsize=12)
ax.set_title('Sales Overview for 2023\nComparative Analysis for Q1, Q2, and Q3', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')

ax.yaxis.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()