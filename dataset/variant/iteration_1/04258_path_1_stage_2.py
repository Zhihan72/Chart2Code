import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = np.array([15, 35, 5, 80, 90, 70, 20, 10, 30, 55, 100])
wind_energy = np.array([95, 25, 110, 12, 30, 85, 45, 18, 58, 75, 35])
total_energy = solar_energy + wind_energy

plt.figure(figsize=(12, 7))
plt.plot(years, solar_energy, label='Solar Energy', color='coral', linestyle='--', marker='o', linewidth=2)
plt.plot(years, wind_energy, label='Wind Energy', color='navy', linestyle='-.', marker='s', linewidth=2)
plt.plot(years, total_energy, label='Total Renewable Energy', color='purple', linestyle='-', marker='d', linewidth=2)
plt.title('Rise of Renewable Energy in Solaria (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (Gigawatts)', fontsize=12)
plt.legend(title='Energy Source', loc='upper left', fontsize=10, title_fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 121, 10))
plt.tight_layout()
plt.show()