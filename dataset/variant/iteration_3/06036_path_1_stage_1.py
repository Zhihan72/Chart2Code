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

# Changed colors and added different hatches for visual differentiation
colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
hatches = ['/', 'x', '.', '\\', '*']

# Plot bars with new styles
for idx, year in enumerate(years):
    ax.bar(bar_positions + idx * bar_width, data[idx], bar_width, 
           label=f'{year}', color=colors[idx], hatch=hatches[idx])

# Modified labels, title, and grid style
ax.set_xlabel('High Schools', fontsize=12, fontstyle='italic')
ax.set_ylabel('Budget (in thousand USD)', fontsize=12, fontstyle='italic')
ax.set_title('Drama Production Budgets (2018-2022)', fontsize=14, fontweight='regular', pad=15)
ax.set_xticks(bar_positions + bar_width * 2)
ax.set_xticklabels(schools, rotation=30, ha="right", fontsize=10)

# Changed legend styling
ax.legend(title='Year', fontsize=10, loc='upper left', frameon=True, shadow=True)

# Toggled grid lines style
ax.grid(True, linestyle=':', linewidth=0.7, alpha=0.7, color='gray')
ax.set_axisbelow(True)  # Ensures grid is below the plot elements

fig.tight_layout()

plt.show()