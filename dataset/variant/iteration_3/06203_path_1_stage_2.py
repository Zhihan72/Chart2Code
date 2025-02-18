import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2027)

north_america = [0.02, 0.05, 0.1, 0.2, 0.4, 0.7, 1.1, 1.5, 2, 2.7, 3.5, 4.5, 5.8, 7, 8.5, 10, 12]
europe = [0.01, 0.03, 0.06, 0.1, 0.2, 0.4, 0.7, 1.1, 1.8, 2.5, 3.3, 4.2, 5.4, 6.8, 8.2, 9.9, 11.5]
asia = [0.02, 0.04, 0.08, 0.15, 0.25, 0.45, 0.75, 1.2, 2, 3.2, 4.5, 6, 8, 10.5, 13, 15.5, 18]
south_america = [0.001, 0.002, 0.005, 0.01, 0.02, 0.04, 0.07, 0.1, 0.2, 0.4, 0.7, 1, 1.5, 2, 2.7, 3.5, 4.5]
africa = [0.0005, 0.001, 0.002, 0.004, 0.01, 0.015, 0.03, 0.05, 0.08, 0.12, 0.2, 0.3, 0.5, 0.7, 1, 1.3, 1.7]
oceania = [0.0002, 0.0005, 0.001, 0.002, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12, 0.18, 0.25, 0.35, 0.5, 0.7]

ev_adoption = np.vstack([north_america, europe, asia, south_america, africa, oceania])

fig, ax1 = plt.subplots(figsize=(9, 9))

ax1.stackplot(years, ev_adoption, labels=['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania'],
              colors=['#b15928', '#1f78b4', '#6a3d9a', '#33a02c', '#ff7f00', '#e31a1c'], alpha=0.8)

ax1.set_title('Global Electric Vehicle Adoption by Continent (2010-2025)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of EVs (in millions)', fontsize=14)

ax1.legend(loc='upper left', fontsize=12, title='Continents', bbox_to_anchor=(1, 1))
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 20 + 1, 2))
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()