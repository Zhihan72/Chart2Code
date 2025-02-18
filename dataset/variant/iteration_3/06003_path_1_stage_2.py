import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022']
departments = ['Health', 'Education', 'Infrastructure', 'Public Safety', 'Arts & Culture']
budget_2020 = [210, 180, 60, 150, 170]
budget_2021 = [220, 65, 155, 190, 180]
budget_2022 = [230, 70, 160, 200, 190]

x = np.arange(len(departments))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

bars_2020 = ax.bar(x - width, budget_2020, width, label='2020', color='navy', linewidth=2, edgecolor='black')
bars_2021 = ax.bar(x, budget_2021, width, label='2021', color='gold', hatch='/', linewidth=2, edgecolor='gray')
bars_2022 = ax.bar(x + width, budget_2022, width, label='2022', color='darkred', linestyle='-', linewidth=2, edgecolor='darkred')

ax.set_title('Annual Budget Allocation for City Departments (2020-2022)', fontsize=14, fontweight='medium', pad=15)
ax.set_xlabel('Departments', fontsize=11)
ax.set_ylabel('Budget in Millions (USD)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(departments)
ax.grid(axis='y', linestyle=':', color='grey', alpha=0.3)  # Altered grid style
ax.legend(title='Year', fontsize=8, loc='upper left', frameon=False)  # Moved legend and removed frame

def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}', ha='center', va='bottom', fontsize=9, fontweight='regular')

add_labels(ax, bars_2020)
add_labels(ax, bars_2021)
add_labels(ax, bars_2022)

plt.tight_layout()
plt.show()