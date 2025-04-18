import matplotlib.pyplot as plt
import numpy as np

schools = ['Hogwarts', 'Rivendell', 'Narnia', 'Westeros', 'Middle-Earth', 'Gotham', 'Starfleet']

budgets_2018 = np.array([35, 40, 25, 30, 45, 20, 32])
budgets_2019 = np.array([40, 38, 30, 33, 50, 22, 34])
budgets_2020 = np.array([50, 45, 35, 38, 55, 30, 40])
budgets_2021 = np.array([55, 50, 40, 42, 60, 35, 45])
budgets_2022 = np.array([65, 55, 45, 50, 70, 40, 50])

years = ['2018', '2019', '2020', '2021', '2022']
data = np.array([budgets_2018, budgets_2019, budgets_2020, budgets_2021, budgets_2022])

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15
bar_positions = np.arange(len(schools))

colors = ['#bcbd22', '#8c564b', '#17becf', '#e377c2', '#7f7f7f']
hatches = ['/', 'x', '.', '\\', '*']

for idx, year in enumerate(years):
    ax.barh(bar_positions + idx * bar_height, data[idx], bar_height, 
           label=year, color=colors[idx], hatch=hatches[idx])

ax.set_ylabel('Schools', fontsize=12, fontstyle='italic')
ax.set_xlabel('Budget (k USD)', fontsize=12, fontstyle='italic')
ax.set_title('Budgets 2018-2022', fontsize=14, fontweight='regular', pad=15)
ax.set_yticks(bar_positions + bar_height * 2)
ax.set_yticklabels(schools, fontsize=10)

ax.legend(title='Yr', fontsize=10, loc='upper right', frameon=True, shadow=True)

ax.grid(True, linestyle=':', linewidth=0.7, alpha=0.7, color='gray')
ax.set_axisbelow(True)

fig.tight_layout()

plt.show()