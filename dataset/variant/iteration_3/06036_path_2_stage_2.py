import matplotlib.pyplot as plt
import numpy as np

schools = ['Hogwarts High', 'Rivendell Academy', 'Narnia Unified', 'Westeros Prep', 'Middle-Earth School']
budgets_2018 = np.array([35, 40, 25, 30, 45])
budgets_2019 = np.array([40, 38, 30, 33, 50])
budgets_2020 = np.array([50, 45, 35, 38, 55])
budgets_2021 = np.array([55, 50, 40, 42, 60])
budgets_2022 = np.array([65, 55, 45, 50, 70])

years = ['2018', '2019', '2020', '2021', '2022']
data = np.array([budgets_2018, budgets_2019, budgets_2020, budgets_2021, budgets_2022])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
bar_positions = np.arange(len(schools))
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']  # Changed color set

markers = ['o', 's', '^', 'D', 'x']

for idx, year in enumerate(years):
    ax.bar(bar_positions + idx * bar_width, 
           data[idx], 
           bar_width, 
           label=f'{year}', 
           color=colors[idx],
           edgecolor='black', 
           hatch=markers[idx % len(markers)])

ax.set_xlabel('High Schools', fontsize=10)
ax.set_ylabel('Production Budget (in thousand USD)', fontsize=10, color='purple')
ax.set_title('Annual Drama Production Budgets (2018-2022)', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(bar_positions + bar_width * 2)
ax.set_xticklabels(schools, rotation=30, ha="right", fontsize=11)

ax.legend(title='Year', fontsize=11, loc='upper right', frameon=False)

ax.grid(True, axis='y', linestyle='-.', linewidth=0.7, alpha=0.4)
ax.spines['top'].set_visible(False) 
ax.spines['right'].set_visible(False)

fig.tight_layout()
plt.show()