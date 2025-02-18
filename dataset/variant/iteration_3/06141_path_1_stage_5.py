import matplotlib.pyplot as plt
import numpy as np

years = ['2012', '2014', '2016', '2018', '2020', '2022']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Bio']

adoption_data = np.array([
    [5, 10, 30, 3],   
    [10, 15, 35, 5],  
    [20, 30, 40, 7],  
    [30, 40, 45, 10],
    [40, 50, 50, 12],
    [50, 60, 55, 15]
])

sorted_indices = [np.argsort(-adoption_data[:, idx]) for idx in range(len(energy_sources))]
sorted_adoption_data = np.array([adoption_data[sorted_indices[idx], idx] for idx in range(len(energy_sources))]).T

colors = ['#ff7f0e', '#2ca02c', '#9467bd', '#1f77b4']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x = np.arange(len(years))

for idx, source in enumerate(energy_sources):
    ax.bar(x + idx * bar_width, sorted_adoption_data[:, idx], width=bar_width, label=source, color=colors[idx])

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Rate (%)', fontsize=14)
ax.set_title('Sorted Energy Adoption (2012-2022)', fontsize=18, fontweight='bold')

ax.set_xticks(x + bar_width * (len(energy_sources) - 1) / 2)
ax.set_xticklabels(years)

ax.legend(title='Source', fontsize=11, title_fontsize=13, loc='upper left')

ax.grid(True, which='both', linestyle='-', linewidth=0.7, alpha=0.5)

for idx, source in enumerate(energy_sources):
    for i in range(len(years)):
        ax.text(x[i] + idx * bar_width, sorted_adoption_data[i, idx] + 1, str(sorted_adoption_data[i, idx]), 
                ha='center', va='bottom')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()