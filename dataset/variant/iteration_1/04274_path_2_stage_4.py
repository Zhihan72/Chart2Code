import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_panels = [50, 55, 60, 70, 85, 100, 120, 140, 160, 180, 210]
electric_cars = [20, 25, 30, 45, 60, 90, 130, 175, 220, 280, 350]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_panels, marker='x', linestyle=':', color='darkorange', linewidth=3, markersize=10, label='Solar Panels')
ax.plot(years, electric_cars, marker='D', linestyle='-', color='darkgreen', linewidth=3, markersize=10, label='Electric Cars')

ax.grid(True, linestyle=':', linewidth=0.8, alpha=0.7)

ax.set_title('Growth of Renewable Technologies\n(2010-2020)', fontsize=20, fontweight='bold')
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Number of Installations', fontsize=16)
ax.legend(loc='upper left', fontsize=14, frameon=False)

ax.annotate('Government Incentive', xy=(2014, 85), xytext=(2012, 150),
            arrowprops=dict(facecolor='grey', shrink=0.05),
            fontsize=14, ha='center', fontweight='bold')
ax.annotate('Awareness Campaign', xy=(2017, 140), xytext=(2019, 120),
            arrowprops=dict(facecolor='grey', shrink=0.05),
            fontsize=14, ha='center', fontweight='bold')

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()