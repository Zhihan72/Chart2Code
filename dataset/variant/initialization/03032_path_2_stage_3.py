import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
solar_energy = np.array([5, 10, 18, 30, 50, 75, 100, 130, 165, 200, 240])
wind_energy = np.array([8, 12, 25, 35, 55, 80, 110, 150, 190, 230, 270])
hydro_energy = np.array([15, 15, 15, 18, 22, 30, 40, 55, 70, 85, 100])
total_renewable_energy = solar_energy + wind_energy + hydro_energy
percentage_growth = np.zeros(len(total_renewable_energy))
percentage_growth[1:] = ((total_renewable_energy[1:] - total_renewable_energy[:-1]) / total_renewable_energy[:-1]) * 100

fig, axes = plt.subplots(1, 2, figsize=(14, 8))

axes[0].bar(years, solar_energy, label='Sol', color='#ff9999', alpha=0.85, edgecolor='grey', linestyle='-')
axes[0].bar(years, wind_energy, bottom=solar_energy, label='Wind', color='#66b3ff', alpha=0.85, edgecolor='grey', hatch='/')
axes[0].bar(years, hydro_energy, bottom=solar_energy + wind_energy, label='Hydro', color='#99ff99', alpha=0.85, edgecolor='grey', hatch='\\')
axes[0].set_title('Growth 2020-30', fontsize=14)
axes[0].set_xlabel('Yr', fontsize=11)
axes[0].set_ylabel('Energy', fontsize=11)
axes[0].set_xticks(years, labels=years, rotation=45)
axes[0].set_ylim(0, 620)
axes[0].grid(axis='y', linestyle='-.', linewidth=0.5, alpha=0.6)
axes[0].legend(loc='lower left', fontsize=10, title='Type', title_fontsize='11')

for i, (s, w, h) in enumerate(zip(solar_energy, wind_energy, hydro_energy)):
    axes[0].text(years[i], s / 2, f'{s}', ha='center', va='center', color='black', fontsize=8)
    axes[0].text(years[i], s + w / 2, f'{w}', ha='center', va='center', color='black', fontsize=8)
    axes[0].text(years[i], s + w + h / 2, f'{h}', ha='center', va='center', color='black', fontsize=8)

axes[1].plot(years, total_renewable_energy, label='Total', color='#ffa64d', marker='s', linewidth=2.5, linestyle='-.')
axes[1].plot(years, percentage_growth, label='Growth %', color='#c45959', linestyle=':', marker='^', linewidth=1.5)
axes[1].set_title('Total & Growth %', fontsize=14)
axes[1].set_xlabel('Yr', fontsize=11)
axes[1].set_ylabel('TWh / %', fontsize=11)
axes[1].set_xticks(years, labels=years, rotation=45)
axes[1].set_ylim(0, max(total_renewable_energy) * 1.2)
axes[1].legend(loc='lower right', fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()