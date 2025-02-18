import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
solar_energy = np.array([10, 20, 35, 55, 85, 130])
solar_cost_reduction = np.array([200, 160, 130, 100, 75, 50])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Swapped the colors between the two plots
ax1.plot(years, solar_energy, color='magenta', marker='x', linestyle='-.', linewidth=2.5)

ax2 = ax1.twinx()
ax2.plot(years, solar_cost_reduction, color='darkorange', marker='p', linestyle='--', linewidth=3)

ax1.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()