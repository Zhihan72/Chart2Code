import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([5, 6, 7, 9, 11, 13, 15, 17, 20, 22, 25])
walking = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
conventional_vehicles = np.array([53, 48, 43, 38, 33, 26, 19, 12, 2, 1, 0])

sustainable_transport = cycling + walking + electric_vehicles

fig, ax = plt.subplots(figsize=(14, 9))

ax.bar(years, public_transport, color='darkcyan', label='Public Transport')  
ax.bar(years, cycling, bottom=public_transport, color='gold', label='Cycling')  
ax.bar(years, walking, bottom=public_transport + cycling, color='lightgreen', label='Walking')  
ax.bar(years, electric_vehicles, bottom=public_transport + cycling + walking, color='mediumorchid', label='Electric Vehicles')  
ax.bar(years, conventional_vehicles, bottom=public_transport + cycling + walking + electric_vehicles, color='firebrick', label='Conventional Vehicles')  

ax.plot(years, sustainable_transport, color='chocolate', linewidth=2, linestyle='-.', marker='s', markersize=6, label='Sustainable Transport')

ax.grid(axis='y', linestyle='-', alpha=0.7)

ax.legend(loc='upper left', frameon=False)

plt.tight_layout()

plt.show()