import matplotlib.pyplot as plt
import numpy as np

strategies = ['Online Marketing', 'Field Sales', 'Refer-a-Friend', 'Retail Partnerships']
positive_sales = [40, 20, 15, 5]
negative_sales = [-30, -10, -5, -7]  # Example opposing data for illustration

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.4

# Plot positive sales bars
p1 = ax.bar(strategies, positive_sales, bar_width, color='green', edgecolor='black', label='Positive Sales')

# Plot negative sales bars, stacked with the positive
p2 = ax.bar(strategies, negative_sales, bar_width, color='red', edgecolor='black', label='Negative Sales')

ax.set_ylabel('Sales Percentage (%)', fontsize=12, labelpad=10)
ax.set_title('Diverging Bar Chart of Sales Strategies in Q1 2023', fontsize=16, fontweight='bold', pad=20)

for idx, val in enumerate(positive_sales):
    ax.text(idx, val + 2, f'{val}%', ha='center', va='bottom', fontsize=10, color='black')

for idx, val in enumerate(negative_sales):
    ax.text(idx, val - 2, f'{-val}%', ha='center', va='top', fontsize=10, color='black')

plt.axhline(y=0, color='black', linewidth=0.8)  # Add central axis line
plt.xticks(rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()