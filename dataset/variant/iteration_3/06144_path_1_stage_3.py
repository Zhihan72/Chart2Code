import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

solar_energy = np.array([1, 2, 4, 6, 10, 16, 24, 34, 46, 60, 76, 94, 114, 136, 160, 186, 214, 244, 276, 310, 346])
wind_energy = np.array([3, 5, 9, 14, 20, 27, 35, 44, 54, 66, 79, 93, 108, 124, 141, 159, 178, 198, 219, 241, 264])
hydro_energy = np.array([10, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114, 129, 145, 162, 180, 199, 219, 240])
bio_energy = np.array([2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212])
geothermal_energy = np.array([1, 1, 2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157])

fig, ax = plt.subplots(figsize=(12, 8))

# Updated colors for the stacked area chart
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, bio_energy, geothermal_energy,
             labels=['Sun Power', 'Breeze', 'Water Flow', 'Organics', 'Earth Heat'],
             colors=['#ffcc00', '#2E8B57', '#4682B4', '#DC143C', '#8A2BE2'], alpha=0.6)

ax.set_title("Growth of Eco-friendly Energy in Greenlands (2010-2030)", fontsize=16, fontweight='bold')
ax.set_xlabel("Timeline", fontsize=12, fontstyle='italic')
ax.set_ylabel("Generation (TWh)", fontsize=12, fontstyle='italic')

ax.legend(loc='upper right', fontsize=10, frameon=True, title="Varieties")
ax.grid(True, linestyle='-', color='grey', alpha=0.8, linewidth=0.7)

ax.annotate('Significant Solar Project', xy=(2014, 10), xytext=(2016, 80),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='purple')

ax.annotate('Wind Boost', xy=(2020, 96), xytext=(2022, 170),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='red')

ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()