import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2027)

north_america = [0.02, 0.05, 0.1, 0.2, 0.4, 0.7, 1.1, 1.5, 2, 2.7, 3.5, 4.5, 5.8, 7, 8.5, 10, 12]
europe = [0.01, 0.03, 0.06, 0.1, 0.2, 0.4, 0.7, 1.1, 1.8, 2.5, 3.3, 4.2, 5.4, 6.8, 8.2, 9.9, 11.5]
asia = [0.02, 0.04, 0.08, 0.15, 0.25, 0.45, 0.75, 1.2, 2, 3.2, 4.5, 6, 8, 10.5, 13, 15.5, 18]
south_america = [0.001, 0.002, 0.005, 0.01, 0.02, 0.04, 0.07, 0.1, 0.2, 0.4, 0.7, 1, 1.5, 2, 2.7, 3.5, 4.5]
africa = [0.0005, 0.001, 0.002, 0.004, 0.01, 0.015, 0.03, 0.05, 0.08, 0.12, 0.2, 0.3, 0.5, 0.7, 1, 1.3, 1.7]
oceania = [0.0002, 0.0005, 0.001, 0.002, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12, 0.18, 0.25, 0.35, 0.5, 0.7]
atlantis = [0.001, 0.002, 0.004, 0.006, 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1, 1.2]
lemuria = [0.001, 0.003, 0.007, 0.012, 0.02, 0.035, 0.06, 0.10, 0.17, 0.25, 0.35, 0.48, 0.6, 0.8, 1.1, 1.5, 1.9]

ev_adoption = np.vstack([north_america, europe, asia, south_america, africa, oceania, atlantis, lemuria])

def calculate_percentage(data):
    return (data / np.sum(data, axis=0)) * 100

percentage_shares = calculate_percentage(ev_adoption)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

ax1.stackplot(years, ev_adoption, labels=['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania', 'Atlantis', 'Lemuria'],
              colors=['#1f78b4'], alpha=0.8)

ax1.set_title('Global Electric Vehicle Adoption by Continent (2010-2025)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of EVs (in millions)', fontsize=14)
ax1.legend(loc='upper left', fontsize=12, title='Continents', bbox_to_anchor=(1, 1))
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 20 + 1, 2))
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for i, continent in enumerate(['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania', 'Atlantis', 'Lemuria']):
    ax2.plot(years, percentage_shares[i], label=continent, color='#1f78b4', marker='o')

ax2.set_title('Percentage Share of Global EV Adoption by Continent (2010-2025)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Percentage (%)', fontsize=14)
ax2.legend(loc='upper right', fontsize=12, title='Continents')
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 100 + 1, 10))
ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()