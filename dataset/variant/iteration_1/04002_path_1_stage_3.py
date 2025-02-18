import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Housing', 'Food', 'Transportation', 'Utilities', 'Medical', 'Entertainment']

expenses_data = np.array([
    [120, 210, 300, -210, -250, -260, 80, 230, -290, -240, 280, 100],
    [40, -50, 130, -170, 220, -190, 100, -80, 120, -200, 110, -60],
    [60, -150, 20, -80, 10, 90, 130, -140, 110, -35, 145, 50],
    [-25, 20, 10, 40, -5, -30, 50, -15, 55, 35, 45, -10],
    [55, 50, -70, -65, 45, -35, 130, -60, 40, 25, -60, 50],
    [20, 90, -100, 40, -110, 60, 170, -30, 50, -180, 10, 110]
])

fig, ax = plt.subplots(figsize=(12, 8))

index = np.arange(len(months))
bar_width = 0.5

# Accumulate positive and negative values for stacking
bottom_positive = np.zeros(len(months))
bottom_negative = np.zeros(len(months))

for i, category in enumerate(categories):
    pos_data = np.clip(expenses_data[i], 0, None)
    neg_data = np.clip(expenses_data[i], None, 0)
    
    ax.bar(index, pos_data, bar_width, bottom=bottom_positive, label=category + ' Positive')
    ax.bar(index, neg_data, bar_width, bottom=bottom_negative, label=category + ' Negative')
    
    bottom_positive += pos_data
    bottom_negative += neg_data

ax.set_title('Diverging Monthly Expenses of Families in 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Expenses (USD)', fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(months, rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()