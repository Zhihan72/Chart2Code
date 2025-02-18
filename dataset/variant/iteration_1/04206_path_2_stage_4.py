import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solar_energy = [10, 20, 30, 45, 55, 70, 85, 100, 115, 130, 150]
wind_energy = [15, 25, 35, 45, 60, 75, 90, 105, 120, 140, 160]
hydro_energy = [20, 30, 40, 55, 65, 80, 95, 110, 130, 150, 170]
geothermal_energy = [5, 10, 15, 25, 35, 45, 60, 75, 90, 110, 130]
bioenergy = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 108]

color_palette = ['#FFD700', '#32CD32', '#00BFFF', '#FF4500', '#9370DB']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, solar_energy, wind_energy, hydro_energy, geothermal_energy, bioenergy, 
             colors=color_palette, alpha=0.8)

ax.set_title('Clean Energy Growth (2020-2030)', fontsize=16, fontweight='bold', ha='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Output (GW)', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Removed the legend
# Removed the grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_alpha(0.5)
ax.spines['bottom'].set_alpha(0.5)

ax.annotate('Rapid Solar Growth', xy=(2025, 70), xytext=(2023, 110),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')

ax.annotate('Rising Geo Energy', xy=(2028, 85), xytext=(2026, 130),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')

plt.tight_layout()
plt.show()