import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
hydropower_energy = np.array([30, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44])
cumulative_energy = solar_energy + wind_energy + hydropower_energy
percentage_growth = np.zeros(len(years))
percentage_growth[1:] = 100 * (cumulative_energy[1:] - cumulative_energy[:-1]) / cumulative_energy[:-1]

fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# First subplot: Stacked bar chart
axs[0].bar(years, solar_energy, label='Solar', color='orange', edgecolor='gray', hatch='/')
axs[0].bar(years, wind_energy, bottom=solar_energy, label='Wind', color='skyblue', edgecolor='gray', hatch='\\')
axs[0].bar(years, hydropower_energy, bottom=solar_energy + wind_energy, label='Hydro', color='green', edgecolor='gray', hatch='|')

axs[0].set_title('Energy Growth (2010-2020)', fontsize=18, fontweight='light')
axs[0].set_xlabel('Year Published', fontsize=14)
axs[0].set_ylabel('Output (TWh)', fontsize=14)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 250, 50))
axs[0].legend(loc='lower right', fontsize=10)
axs[0].grid(True, which='both', linestyle='-', linewidth=0.8, alpha=0.5)

# Second subplot: Line plot for percentage growth
axs[1].plot(years, percentage_growth, marker='s', linestyle='--', color='purple', linewidth=2, label='Rate of Growth')
axs[1].set_title('Annual Growth Rates', fontsize=18, fontweight='light')
axs[1].set_xlabel('Publication Year', fontsize=14)
axs[1].set_ylabel('Growth Rate (%)', fontsize=14)
axs[1].set_xticks(years)
axs[1].axhline(0, color='black', linewidth=0.8)
axs[1].grid(True, which='both', linestyle=':', linewidth=0.7, alpha=0.8)
axs[1].legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()