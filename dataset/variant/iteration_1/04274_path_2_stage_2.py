import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_panels = [50, 55, 60, 70, 85, 100, 120, 140, 160, 180, 210]
electric_cars = [20, 25, 30, 45, 60, 90, 130, 175, 220, 280, 350]
wind_turbines = [5, 7, 10, 15, 20, 30, 45, 65, 85, 110, 150]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_panels, marker='o', linestyle='-', color='crimson', linewidth=2.5, markersize=8, label='Solar')
ax.plot(years, electric_cars, marker='^', linestyle='--', color='teal', linewidth=2.5, markersize=8, label='Cars')
ax.plot(years, wind_turbines, marker='s', linestyle='-.', color='purple', linewidth=2.5, markersize=8, label='Wind')

ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title('Renewable Growth\n(2010-20)', fontsize=18, fontweight='bold')
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('Installations', fontsize=14)
ax.legend(loc='upper left', fontsize=12)

ax.annotate('Incentives', xy=(2014, 85), xytext=(2012, 140),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, ha='center', fontweight='bold')
ax.annotate('Campaign', xy=(2017, 140), xytext=(2019, 100),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, ha='center', fontweight='bold')

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()