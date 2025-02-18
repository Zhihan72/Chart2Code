import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2026)

solar_energy = [5, 10, 20, 30, 45, 60, 80, 100, 130, 170, 210, 260, 320, 390, 470, 550]
wind_energy = [8, 12, 18, 25, 35, 50, 70, 95, 125, 160, 200, 245, 295, 350, 410, 480]
hydro_energy = [15, 20, 25, 30, 35, 40, 50, 60, 75, 90, 110, 130, 150, 180, 210, 250]
coal_energy = [180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30]
oil_energy = [120, 115, 110, 105, 100, 95, 90, 85, 75, 65, 55, 45, 35, 25, 20, 15]

stacked_data = np.vstack([solar_energy, wind_energy, hydro_energy, coal_energy, oil_energy])

colors = ['#FFD700', '#87CEEB', '#228B22', '#A9A9A9', '#FF4500']

plt.figure(figsize=(14, 9))

plt.stackplot(years, stacked_data, labels=['Sunshine', 'Breeze', 'Water Power', 'Fossil', 'Petroleum'], colors=colors, alpha=0.8)

plt.title('Power Surge:\nA Greener Path Ahead (2010-2025)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Power Generation (TWh)', fontsize=14)
plt.legend(loc='upper left', title='Power Sources', fontsize=12, frameon=False)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1000, 100))

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)

plt.annotate('Renewable Era Peaks', xy=(2021, 560), xytext=(2015, 800),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, weight='bold', color='darkgreen')

plt.tight_layout()
plt.show()