import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

# Randomly altered content within each data group while preserving the original dimensional structure
solarlandia_renewables = [28, 19, 22, 15, 40, 34, 17, 37, 31, 25]  # shuffled
windtopia_renewables = [11, 30, 22, 13, 10, 35, 15, 28, 25, 18]  # shuffled
hydroville_renewables = [21, 32, 25, 30, 26, 23, 36, 20, 28, 34]  # shuffled
geothermia_renewables = [12, 9, 5, 25, 30, 28, 15, 18, 7, 22]  # shuffled

plt.figure(figsize=(14, 8))

plt.plot(years, solarlandia_renewables, marker='o', linestyle='-', linewidth=2, color='orange')
plt.plot(years, windtopia_renewables, marker='s', linestyle='--', linewidth=2, color='blue')
plt.plot(years, hydroville_renewables, marker='^', linestyle='-.', linewidth=2, color='green')
plt.plot(years, geothermia_renewables, marker='d', linestyle=':', linewidth=2, color='purple')

plt.title("Decadal Growth in Renewable Energy Adoption (2011-2020)\nAcross Four Countries", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Energy from Renewables (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 45, 5))

max_solarlandia = max(solarlandia_renewables)
max_windtopia = max(windtopia_renewables)
max_hydroville = max(hydroville_renewables)
max_geothermia = max(geothermia_renewables)

plt.annotate(f'{max_solarlandia}%', xy=(years[np.argmax(solarlandia_renewables)], max_solarlandia), 
             xytext=(years[np.argmax(solarlandia_renewables)]+0.3, max_solarlandia+1),
             arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10, color='orange')
plt.annotate(f'{max_windtopia}%', xy=(years[np.argmax(windtopia_renewables)], max_windtopia), 
             xytext=(years[np.argmax(windtopia_renewables)]-2.5, max_windtopia+2),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')
plt.annotate(f'{max_hydroville}%', xy=(years[np.argmax(hydroville_renewables)], max_hydroville), 
             xytext=(years[np.argmax(hydroville_renewables)]+0.3, max_hydroville+1),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')
plt.annotate(f'{max_geothermia}%', xy=(years[np.argmax(geothermia_renewables)], max_geothermia), 
             xytext=(years[np.argmax(geothermia_renewables)]+0.3, max_geothermia+1),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=10, color='purple')

plt.tight_layout()
plt.show()