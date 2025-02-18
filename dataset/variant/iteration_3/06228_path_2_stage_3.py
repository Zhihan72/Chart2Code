import matplotlib.pyplot as plt
import numpy as np

cities = ["City A", "City B", "City C", "City D", "City E", "City F", "City G", "City H"]
tree_coverage = np.array([35, 10, 50, 30, 15, 40, 45, 25])
AQI_levels = np.array([85, 150, 65, 90, 130, 75, 70, 100])

temperature_trends = {
    "City A": [10, 20, 30, 15],
    "City B": [8, 18, 28, 12],
    "City C": [5, 15, 25, 10],
    "City D": [14, 24, 34, 19],
    "City E": [12, 22, 32, 17],
    "City F": [18, 28, 38, 23],
    "City G": [16, 26, 36, 21],
    "City H": [20, 30, 40, 25]
}

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 8))

for city in cities:
    temperatures = temperature_trends[city]
    quarters = ['Winter', 'Spring', 'Summer', 'Autumn']
    ax2.plot(quarters, temperatures, marker='o')

ax2.grid(True, linestyle='--', alpha=0.6)

scatter = ax1.scatter(tree_coverage, AQI_levels, color='green', s=100, alpha=0.8,
                      edgecolors='black', linewidth=1.5)

ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 55)
ax1.set_ylim(50, 160)

plt.tight_layout()

plt.show()