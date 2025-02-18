import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Oni', 'Fem', 'Ram', 'Pir', 'Yam', 'Fun', 'Jul', 'Yug', 'Tep', 'Kot', 'Vun', 'Dac'])

sales_apples = np.array([4, 5, 6, 7, 5, 6, 8, 7, 6, 5, 4, 5])
sales_bananas = -np.array([6, 7, 8, 9, 8, 7, 8, 9, 6, 7, 6, 5])  # Negative to diverge
sales_cherries = np.array([2, 3, 4, 5, 4, 3, 5, 6, 5, 4, 3, 3])
sales_dates = -np.array([1, 2, 2, 3, 2, 1, 2, 2, 3, 4, 5, 4])  # Negative to diverge

data_positive = np.array([sales_apples, sales_cherries])
data_negative = np.array([sales_bananas, sales_dates])

n_months = len(months)
x = np.arange(n_months)
bar_width = 0.7

fig, ax = plt.subplots(figsize=(14, 8))

bottom_positive = np.zeros(n_months)
bottom_negative = np.zeros(n_months)

positive_colors = ['#1f77b4', '#2ca02c']
negative_colors = ['#ff7f0e', '#9467bd']

for sales, color in zip(data_positive, positive_colors):
    ax.bar(x, sales, width=bar_width, color=color, bottom=bottom_positive)
    bottom_positive += sales

for sales, color in zip(data_negative, negative_colors):
    ax.bar(x, sales, width=bar_width, color=color, bottom=bottom_negative)
    bottom_negative += sales

ax.set_xlabel('Moons', fontsize=12)
ax.set_ylabel('Units Traded (in thousands)', fontsize=12)
ax.set_title('Diverging Annual Fruity Business Dynamics\n(Oni - Dac Cycle)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(months)
plt.xticks(rotation=30, ha='right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()