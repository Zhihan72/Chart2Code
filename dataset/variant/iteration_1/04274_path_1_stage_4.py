import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_panels = [50, 55, 60, 70, 85, 100, 120, 140, 160, 180, 210]
electric_cars = [20, 25, 30, 45, 60, 90, 130, 175, 220, 280, 350]
wind_turbines = [5, 7, 10, 15, 20, 30, 45, 65, 85, 110, 150]
geothermal_plants = [2, 3, 4, 5, 6, 8, 11, 15, 20, 27, 35]
battery_storage = [10, 13, 17, 23, 30, 40, 55, 75, 100, 130, 170]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_panels, marker='o', linestyle='-', color='purple', linewidth=2.5, markersize=8)
ax.plot(years, electric_cars, marker='^', linestyle='--', color='purple', linewidth=2.5, markersize=8)
ax.plot(years, wind_turbines, marker='s', linestyle='-.', color='purple', linewidth=2.5, markersize=8)
ax.plot(years, geothermal_plants, marker='d', linestyle=':', color='purple', linewidth=2.5, markersize=8)
ax.plot(years, battery_storage, marker='*', linestyle='-', color='purple', linewidth=2.5, markersize=8)

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()