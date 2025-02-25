import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
categories = ['Salaries', 'Marketing', 'Research & Development', 'Operational Costs', 'Miscellaneous']

salaries = np.array([65, 50, 70, 60, 55])
marketing = np.array([35, 20, 40, 25, 30])
research = np.array([30, 15, 35, 25, 20])
operational = np.array([25, 10, 30, 20, 15])
miscellaneous = np.array([8, 5, 9, 6, 7])

data = np.vstack([salaries, marketing, research, operational, miscellaneous])

total_per_year = data.sum(axis=0)
sorted_indices = np.argsort(total_per_year)

sorted_years = years[sorted_indices]
sorted_data = data[:, sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bottom = np.zeros(len(sorted_years))
colors = ['#ff7f00', '#4daf4a', '#e41a1c', '#377eb8', '#984ea3']
hatches = ['/', '\\', 'x', '.', '*']  # New bar border styles (hatching)

for i, (datum, color, hatch) in enumerate(zip(sorted_data, colors, hatches)):
    ax.bar(sorted_years, datum, bottom=bottom, color=color, edgecolor='gray', linewidth=1.2, hatch=hatch)
    bottom += datum

# Modified grid properties
ax.grid(axis='y', linestyle=':', alpha=0.5, color='gray')

# Setting a custom legend
ax.legend(categories, title='Expense Categories', loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

ax.set_ylim(0, 200)

plt.tight_layout()
plt.show()