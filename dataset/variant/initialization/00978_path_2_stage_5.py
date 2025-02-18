import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([5, 6, 7, 9, 11, 13, 15, 17, 20, 22, 25])
walking = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
car_sharing = np.array([1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9])
scooters = np.array([0, 1, 1, 2, 3, 5, 6, 7, 8, 9, 10])
conventional_vehicles = np.array([53, 48, 43, 38, 33, 26, 19, 12, 2, 1, 0])

# Arrays for sustainable and non-sustainable transports
sustainable_transport = public_transport + cycling + walking + electric_vehicles + car_sharing + scooters

fig, ax = plt.subplots(figsize=(14, 9))

# Plot positive (sustainable) transport modes
ax.bar(years, public_transport, color='darkcyan', label='Public Transport', bottom=0)
ax.bar(years, cycling, color='gold', bottom=public_transport)
ax.bar(years, walking, color='lightgreen', bottom=public_transport + cycling)
ax.bar(years, electric_vehicles, color='mediumorchid', bottom=public_transport + cycling + walking)
ax.bar(years, car_sharing, color='cornflowerblue', bottom=public_transport + cycling + walking + electric_vehicles)
ax.bar(years, scooters, color='orange', bottom=public_transport + cycling + walking + electric_vehicles + car_sharing)

# Plot negative (conventional vehicles) transport
ax.bar(years, -conventional_vehicles, color='firebrick', label='Conventional Vehicles')

ax.axhline(0, color='grey', linewidth=1)

ax.grid(axis='y', linestyle='-', alpha=0.7)

ax.legend(loc='upper left', frameon=False)

plt.tight_layout()

plt.show()