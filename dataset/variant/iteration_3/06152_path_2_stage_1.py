import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solartech_production = [15, 22, 33, 40, 45, 50, 55, 60, 65, 70, 75]
sundrive_production = [10, 16, 25, 32, 38, 48, 52, 55, 58, 63, 67]
ecowheels_production = [5, 10, 18, 28, 36, 40, 45, 50, 55, 60, 65]

fig, ax = plt.subplots(figsize=(12, 8))

# Changed marker types and line styles
ax.plot(years, solartech_production, label='SolarTech', marker='x', linestyle='-.', linewidth=2, color='gold')
ax.plot(years, sundrive_production, label='SunDrive', marker='D', linestyle=':', linewidth=2, color='darkorange')
ax.plot(years, ecowheels_production, label='EcoWheels', marker='+', linestyle='--', linewidth=2, color='forestgreen')

# Change title padding
ax.set_title("The Journey of Solar-Powered Car Production (2010-2020)", fontsize=18, weight='bold', pad=10)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Cars Produced (in thousands)", fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{i}k' for i in range(0, 101, 10)])

# Changed grid style
ax.grid(True, linestyle='-', alpha=0.5)

# Modify the legend style
ax.legend(loc='upper center', fontsize=12, frameon=True, shadow=False, ncol=3)

for i in range(len(years)):
    ax.text(years[i], solartech_production[i], f"{solartech_production[i]}k", ha='left', va='top', fontsize=10, color='gold')
    ax.text(years[i], sundrive_production[i], f"{sundrive_production[i]}k", ha='right', va='bottom', fontsize=10, color='darkorange')
    ax.text(years[i], ecowheels_production[i], f"{ecowheels_production[i]}k", ha='center', va='top', fontsize=10, color='forestgreen')

# Adjust layout
plt.tight_layout()

plt.show()