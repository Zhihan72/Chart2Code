import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Housing', 'Food', 'Transportation', 'Utilities', 'Medical', 'Entertainment']

expenses_data = np.array([
    [1220, 1210, 1300, 1190, 1250, 1260, 1280, 1230, 1290, 1240, 1280, 1200],
    [540, 550, 530, 570, 520, 590, 600, 580, 620, 500, 610, 560],
    [260, 250, 220, 280, 210, 290, 230, 240, 310, 270, 200, 300],
    [125, 120, 110, 140, 105, 130, 150, 115, 155, 135, 145, 100],
    [155, 150, 170, 165, 145, 135, 130, 160, 140, 125, 160, 150],
    [120, 110, 200, 140, 110, 160, 170, 130, 150, 180, 90, 210]
])

# Single color for all categories
single_color = '#1f77b4'

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
index = np.arange(len(months))

for i in range(len(categories)):
    ax.bar(index + i * bar_width, expenses_data[i], bar_width, label=categories[i], color=single_color, edgecolor='grey')

ax.set_title('Average Monthly Expenses of Families in 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Expenses (USD)', fontsize=12)
ax.set_xticks(index + bar_width * (len(categories) - 1) / 2)
ax.set_xticklabels(months, rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=10)

for i in range(len(categories)):
    for j in range(len(months)):
        ax.text(index[j] + i * bar_width, expenses_data[i, j] + 10, str(expenses_data[i, j]), ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.show()