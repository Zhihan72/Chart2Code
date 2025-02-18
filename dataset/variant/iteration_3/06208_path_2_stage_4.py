import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

solarlandia_renewables = [18, 20, 22, 24, 26, 30, 32, 34, 36, 38]
windtopia_renewables = [9, 13, 15, 16, 20, 19, 24, 29, 28, 34]
hydroville_renewables = [19, 22, 21, 26, 27, 31, 33, 31, 35, 37]
geothermia_renewables = [4, 8, 11, 13, 17, 21, 20, 23, 27, 32]

plt.figure(figsize=(14, 8))

plt.plot(years, solarlandia_renewables, marker='P', linestyle=':', linewidth=2.5, color='darkgrey', label='Solarlandia')
plt.plot(years, windtopia_renewables, marker='X', linestyle='-', linewidth=1.5, color='cyan', label='Windtopia')
plt.plot(years, hydroville_renewables, marker='D', linestyle='--', linewidth=2, color='magenta', label='Hydroville')
plt.plot(years, geothermia_renewables, marker='*', linestyle='-.', linewidth=3, color='brown', label='Geothermia')

plt.title("Renewable Energy Evolution (2011-2020)\nAcross Four Nations", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Renewable Energy Contribution (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 45, 5))
plt.legend(title="Countries", loc='lower right', fontsize=10)
plt.grid(True, linestyle='-', alpha=0.4)

# Border thickness
plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['right'].set_linewidth(2)

plt.tight_layout()
plt.show()