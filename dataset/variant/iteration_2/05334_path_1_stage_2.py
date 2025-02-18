import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
categories = ['Salaries', 'Marketing', 'Research & Development', 'Operational Costs', 'Miscellaneous']

salaries = np.array([50, 55, 60, 65, 70])
marketing = np.array([20, 25, 30, 35, 40])
research = np.array([15, 20, 25, 30, 35])
operational = np.array([10, 15, 20, 25, 30])
miscellaneous = np.array([5, 6, 7, 8, 9])

data = np.vstack([salaries, marketing, research, operational, miscellaneous])

total_per_year = data.sum(axis=0)
sorted_indices = np.argsort(total_per_year)

sorted_years = years[sorted_indices]
sorted_data = data[:, sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bottom = np.zeros(len(sorted_years))
# Manually shuffled colors
colors = ['#ff7f00', '#4daf4a', '#e41a1c', '#377eb8', '#984ea3']

for i, (datum, color) in enumerate(zip(sorted_data, colors)):
    ax.bar(sorted_years, datum, bottom=bottom, label=categories[i], color=color, edgecolor='k', linewidth=0.6)
    bottom += datum

ax.set_title("Sorted Company Budget Allocation Over Five Years (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Budget Allocation (in millions)", fontsize=14)
ax.legend(title="Departments", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_ylim(0, 200)

for year_index, year in enumerate(sorted_years):
    y_offset = 0
    for value_index, category in enumerate(categories):
        val = sorted_data[value_index, year_index]
        ax.text(year, y_offset + val / 2, f'{val}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
        y_offset += val

plt.tight_layout()
plt.show()