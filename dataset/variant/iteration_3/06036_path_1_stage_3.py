import matplotlib.pyplot as plt
import numpy as np

# Existing schools and budgets
schools = ['Hogwarts High', 'Rivendell Academy', 'Narnia Unified', 'Westeros Prep', 'Middle-Earth School']

budgets_2018 = np.array([35, 40, 25, 30, 45])
budgets_2019 = np.array([40, 38, 30, 33, 50])
budgets_2020 = np.array([50, 45, 35, 38, 55])
budgets_2021 = np.array([55, 50, 40, 42, 60])
budgets_2022 = np.array([65, 55, 45, 50, 70])

# New additional school budgets
budgets_2018_new = np.array([20, 32])
budgets_2019_new = np.array([22, 34])
budgets_2020_new = np.array([30, 40])
budgets_2021_new = np.array([35, 45])
budgets_2022_new = np.array([40, 50])

# Incorporate additional data
schools.extend(['Gotham Central', 'Starfleet Academy'])

# Combine original and new data
budgets_2018 = np.append(budgets_2018, budgets_2018_new)
budgets_2019 = np.append(budgets_2019, budgets_2019_new)
budgets_2020 = np.append(budgets_2020, budgets_2020_new)
budgets_2021 = np.append(budgets_2021, budgets_2021_new)
budgets_2022 = np.append(budgets_2022, budgets_2022_new)

years = ['2018', '2019', '2020', '2021', '2022']
data = np.array([budgets_2018, budgets_2019, budgets_2020, budgets_2021, budgets_2022])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.1
bar_positions = np.arange(len(schools))

colors = ['#bcbd22', '#8c564b', '#17becf', '#e377c2', '#7f7f7f']
hatches = ['/', 'x', '.', '\\', '*']

for idx, year in enumerate(years):
    ax.bar(bar_positions + idx * bar_width, data[idx], bar_width, 
           label=f'{year}', color=colors[idx], hatch=hatches[idx])

ax.set_xlabel('High Schools', fontsize=12, fontstyle='italic')
ax.set_ylabel('Budget (in thousand USD)', fontsize=12, fontstyle='italic')
ax.set_title('Drama Production Budgets (2018-2022)', fontsize=14, fontweight='regular', pad=15)
ax.set_xticks(bar_positions + bar_width * 2)
ax.set_xticklabels(schools, rotation=30, ha="right", fontsize=10)

ax.legend(title='Year', fontsize=10, loc='upper left', frameon=True, shadow=True)

ax.grid(True, linestyle=':', linewidth=0.7, alpha=0.7, color='gray')
ax.set_axisbelow(True)

fig.tight_layout()

plt.show()