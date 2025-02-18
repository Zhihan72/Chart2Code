import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

solarlandia_renewables = [18, 20, 22, 24, 26, 30, 32, 34, 36, 38]
windtopia_renewables = [9, 13, 15, 16, 20, 19, 24, 29, 28, 34]
hydroville_renewables = [19, 22, 21, 26, 27, 31, 33, 31, 35, 37]
geothermia_renewables = [4, 8, 11, 13, 17, 21, 20, 23, 27, 32]

plt.figure(figsize=(14, 8))

plt.plot(years, solarlandia_renewables, marker='o', linestyle='-', linewidth=2, color='green', label='Sunnyland')
plt.plot(years, windtopia_renewables, marker='s', linestyle='--', linewidth=2, color='orange', label='Breezeborough')
plt.plot(years, hydroville_renewables, marker='^', linestyle='-.', linewidth=2, color='purple', label='Watertown')
plt.plot(years, geothermia_renewables, marker='d', linestyle=':', linewidth=2, color='blue', label='Hotspotville')

plt.title("Explosive Surge in Green Energy Utilization (2011-2020)\nBy Four Imaginary Nations", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline Year', fontsize=12)
plt.ylabel('Green Energy Share (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 45, 5))
plt.legend(title="Nations", loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

max_solarlandia = max(solarlandia_renewables)
max_windtopia = max(windtopia_renewables)
max_hydroville = max(hydroville_renewables)
max_geothermia = max(geothermia_renewables)

plt.annotate(f'{max_solarlandia}%', xy=(years[-1], max_solarlandia), xytext=(years[-1]+0.3, max_solarlandia+1),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')
plt.annotate(f'{max_windtopia}%', xy=(years[-1], max_windtopia), xytext=(years[-1]-2.5, max_windtopia+2),
             arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10, color='orange')
plt.annotate(f'{max_hydroville}%', xy=(years[-1], max_hydroville), xytext=(years[-1]+0.3, max_hydroville+1),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=10, color='purple')
plt.annotate(f'{max_geothermia}%', xy=(years[-1], max_geothermia), xytext=(years[-1]+0.3, max_geothermia+1),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')

plt.tight_layout()
plt.show()