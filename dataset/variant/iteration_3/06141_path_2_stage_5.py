import matplotlib.pyplot as plt
import numpy as np

years = ['2012', '2014', '2016', '2018', '2020', '2022']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geo', 'Bio', 'Tidal', 'Nuclear']

# Added an additional column for each new energy source 'Tidal' and 'Nuclear' across the years
adoption_data = np.array([
    [5, 10, 30, 5, 3, 2, 8],
    [10, 15, 35, 6, 5, 4, 12],
    [20, 30, 40, 7, 7, 6, 15],
    [30, 40, 45, 8, 10, 8, 20],
    [40, 50, 50, 9, 12, 10, 25],
    [50, 60, 55, 10, 15, 12, 30]
])

latest_year_adoption = adoption_data[-1]
sorted_indices = np.argsort(latest_year_adoption)[::-1]
sorted_sources = [energy_sources[i] for i in sorted_indices]
sorted_data = adoption_data[:, sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))
bar_positions = np.arange(len(sorted_sources))
ax.bar(bar_positions, sorted_data[-1], color=['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#b3b3cc'])

ax.set_xlabel('Source', fontsize=12)
ax.set_ylabel('Rate (%) ' + years[-1], fontsize=12)

ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_sources)

for i in range(len(sorted_sources)):
    ax.text(bar_positions[i], sorted_data[-1, i] + 1, str(sorted_data[-1, i]), ha='center', va='bottom')

plt.tight_layout()
plt.show()