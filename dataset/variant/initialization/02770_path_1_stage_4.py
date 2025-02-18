import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2026)
solar_energy = [5, 10, 20, 30, 45, 60, 80, 100, 130, 170, 210, 260, 320, 390, 470, 550]
wind_energy = [8, 12, 18, 25, 35, 50, 70, 95, 125, 160, 200, 245, 295, 350, 410, 480]
hydro_energy = [15, 20, 25, 30, 35, 40, 50, 60, 75, 90, 110, 130, 150, 180, 210, 250]

stacked_data = np.vstack([solar_energy, wind_energy, hydro_energy])

single_color = '#228B22'

plt.figure(figsize=(14, 9))
plt.stackplot(years, stacked_data, colors=[single_color]*3, alpha=0.8)

plt.title('Power Surge:\nA Greener Path Ahead (2010-2025)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Power Generation (TWh)', fontsize=14)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1000, 100))

plt.tight_layout()
plt.show()