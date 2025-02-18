import matplotlib.pyplot as plt
import numpy as np

departments = ['Health', 'Education', 'Infrastructure', 'Public Safety', 'Arts & Culture']
budget_2020 = [160, 175, 205, 180, 65]
budget_2021 = [150, 195, 215, 185, 70]
budget_2022 = [155, 185, 225, 175, 75]

x = np.arange(len(departments))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(x - width, budget_2020, width, color='skyblue')
ax.bar(x, budget_2021, width, color='lightgreen')
ax.bar(x + width, budget_2022, width, color='lightcoral')

ax.set_title('Annual Budget Allocation for City Departments (2020-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Departments', fontsize=12)
ax.set_ylabel('Budget in Millions (USD)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(departments)

def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

bars_2020 = ax.bar(x - width, budget_2020, width, color='skyblue')
bars_2021 = ax.bar(x, budget_2021, width, color='lightgreen')
bars_2022 = ax.bar(x + width, budget_2022, width, color='lightcoral')

add_labels(ax, bars_2020)
add_labels(ax, bars_2021)
add_labels(ax, bars_2022)

plt.tight_layout()
plt.show()