import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solarance_production = [20, 25, 30, 40, 55, 60, 80, 85, 90, 95, 100]
hydroflow_production = [10, 12, 15, 18, 25, 35, 50, 55, 60, 65, 70]

plt.figure(figsize=(14, 8))

# Use a single color for both data groups
common_color = '#1f77b4'
plt.plot(years, solarance_production, marker='o', linestyle='-', color=common_color,
         label='Solarance (Solar Energy)', linewidth=2)
plt.plot(years, hydroflow_production, marker='s', linestyle='-', color=common_color,
         label='HydroFlow (Hydropower)', linewidth=2)

plt.title('Renewable Energy Production Trends in EcoVille (2010-2020)', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Production (GWh)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 111, step=10))
plt.legend(loc='upper left', fontsize=12, title='Energy Companies', title_fontsize='14')
plt.tight_layout()

plt.show()