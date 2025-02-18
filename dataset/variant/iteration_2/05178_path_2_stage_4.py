import matplotlib.pyplot as plt
import numpy as np

years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
solar_energy = np.array([5, 10, 25, 50, 90, 200, 350])
hydro_energy = np.array([500, 520, 550, 580, 600, 630, 650])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_energy, label='Sunny', color='dodgerblue', linewidth=2.5, linestyle='-', marker='>', markersize=8)
ax.plot(years, hydro_energy, label='Water Power', color='darkred', linewidth=2, linestyle='-.', marker='D', markersize=7)

ax.set_title('Trends in Sustainable Power Generation', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Timeline', fontsize=13)
ax.set_ylabel('Output (Terawatt-hours)', fontsize=13)
ax.grid(True, linestyle=':', alpha=0.4)
ax.legend(loc='lower right', fontsize=11, title="Energy Type")

for year, s, h in zip(years, solar_energy, hydro_energy):
    ax.annotate(f'{s}', xy=(year, s), xytext=(year, s+15), textcoords='offset points', ha='center', fontsize=9, color='dodgerblue')
    ax.annotate(f'{h}', xy=(year, h), xytext=(year, h+15), textcoords='offset points', ha='center', fontsize=9, color='darkred')

plt.tight_layout()
plt.show()