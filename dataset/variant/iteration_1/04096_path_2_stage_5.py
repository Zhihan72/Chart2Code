import matplotlib.pyplot as plt
import numpy as np

strategies = ['Online Mkt.', 'Field', 'Refer', 'Retail']
positive_sales = [40, 20, 15, 5]
negative_sales = [-30, -10, -5, -7]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.4

ax.bar(strategies, positive_sales, bar_width, color='green', edgecolor='black')
ax.bar(strategies, negative_sales, bar_width, color='red', edgecolor='black')

ax.set_ylabel('Sales (%)', fontsize=12)
ax.set_title('Sales Strategies Q1 2023', fontsize=16, fontweight='bold')

for idx, val in enumerate(positive_sales):
    ax.text(idx, val + 2, f'{val}%', ha='center', va='bottom', fontsize=10, color='black')

for idx, val in enumerate(negative_sales):
    ax.text(idx, val - 2, f'{-val}%', ha='center', va='top', fontsize=10, color='black')

plt.axhline(y=0, color='black', linewidth=0.8)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()