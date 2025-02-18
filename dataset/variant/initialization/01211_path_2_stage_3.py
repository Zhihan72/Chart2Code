import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
cumulative_energy = solar_energy + wind_energy
percentage_growth = np.zeros(len(years))
percentage_growth[1:] = 100 * (cumulative_energy[1:] - cumulative_energy[:-1]) / cumulative_energy[:-1]

fig, axs = plt.subplots(1, 2, figsize=(20, 8))

axs[0].plot(years, percentage_growth, marker='o', color='darkorange', linewidth=2, label='Percentage Growth')
axs[0].set_title('Yearly Growth Rate of Renewable Energy\nin Futuristan (2010-2020)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Percentage Growth (%)', fontsize=14)
axs[0].set_xticks(years)
axs[0].axhline(0, color='grey', linewidth=1)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
axs[0].legend(loc='upper left', fontsize=12)

bar_width = 0.35
x_solar = np.arange(len(years))
x_wind = x_solar + bar_width

axs[1].bar(x_solar, solar_energy, width=bar_width, label='Solar Energy', color='gold', edgecolor='black')
axs[1].bar(x_wind, wind_energy, width=bar_width, label='Wind Energy', color='lightblue', edgecolor='black')

axs[1].set_title('Adoption of Renewable Energy Sources\nin Futuristan (2010-2020)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Energy Production (TWh)', fontsize=14)
axs[1].set_xticks(x_solar + bar_width / 2)
axs[1].set_xticklabels(years)
axs[1].set_yticks(np.arange(0, 110, 10))
axs[1].legend(loc='upper left', fontsize=12)
axs[1].text(0, 90, 'Note: Significant growth post-2015', fontsize=12, style='italic',
            bbox={'facecolor': 'lightgray', 'alpha': 0.5, 'pad': 5})
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()