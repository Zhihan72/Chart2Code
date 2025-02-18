import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2026)

# Data points for each energy type
solar_energy = [5, 20, 10, 45, 30, 60, 80, 100, 170, 130, 210, 320, 260, 390, 550, 470]
wind_energy = [8, 18, 12, 25, 35, 70, 50, 125, 95, 160, 245, 200, 295, 410, 350, 480]
hydro_energy = [15, 25, 20, 35, 30, 50, 40, 75, 60, 110, 90, 130, 180, 150, 210, 250]
coal_energy = [180, 160, 170, 140, 150, 110, 130, 100, 120, 80, 90, 60, 70, 40, 50, 30]
oil_energy = [120, 110, 115, 100, 105, 85, 95, 75, 90, 55, 65, 35, 45, 20, 25, 15]

stacked_data = np.vstack([solar_energy, wind_energy, hydro_energy, coal_energy, oil_energy])

single_color = '#87CEEB'  # Sky Blue

plt.figure(figsize=(14, 9))

# Use a single color for all data groups
plt.stackplot(years, stacked_data, labels=['Solarium', 'Zephyros', 'Aquaflow', 'CarbonCore', 'PetrolPeak'], 
              colors=[single_color] * stacked_data.shape[0], alpha=0.8, linestyle='-.')

plt.title('Renewed Vibrancy of Powerland:\nA Shift from Ancient Fuels', fontsize=16, weight='bold', pad=20)
plt.xlabel('Chronicles of Years', fontsize=14)
plt.ylabel('Output in Terawatt Hours', fontsize=14)
plt.legend(loc='lower right', title='Energy Varieties', fontsize=11, frameon=True, shadow=True)

plt.xticks(years, rotation=30)
plt.yticks(np.arange(0, 1000, 100))

plt.grid(axis='y', linestyle='-', color='navy', linewidth=0.7)

plt.annotate('Renewable Surge', xy=(2022, 560), xytext=(2016, 800),
             arrowprops=dict(arrowstyle='-|>', color='purple', lw=2), fontsize=10, weight='bold', color='darkblue')

plt.tight_layout()

plt.show()