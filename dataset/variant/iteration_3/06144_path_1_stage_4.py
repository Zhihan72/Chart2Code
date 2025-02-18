import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

# Randomly altered the content within data groups while preserving structure
solar_energy = np.array([1, 6, 2, 34, 10, 16, 46, 4, 24, 60, 76, 94, 114, 310, 160, 186, 160, 244, 276, 136, 346])
wind_energy = np.array([3, 5, 14, 9, 20, 27, 44, 35, 54, 66, 159, 93, 178, 198, 219, 79, 241, 264, 159, 108, 124])
hydro_energy = np.array([10, 12, 15, 37, 19, 30, 24, 45, 54, 64, 75, 100, 87, 114, 240, 129, 145, 162, 199, 180, 219])
bio_energy = np.array([12, 2, 3, 8, 23, 17, 30, 38, 47, 5, 57, 68, 80, 173, 93, 107, 122, 138, 212, 155, 192])
geothermal_energy = np.array([1, 2, 1, 5, 7, 10, 3, 14, 19, 25, 32, 49, 40, 59, 70, 82, 95, 109, 124, 140, 157])

fig, ax = plt.subplots(figsize=(12, 8))

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