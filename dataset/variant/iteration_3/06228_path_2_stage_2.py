import matplotlib.pyplot as plt
import numpy as np

# Altered Data: Cities with respective tree coverage (%) and AQI Levels
cities = ["City A", "City B", "City C", "City D", "City E", "City F", "City G", "City H"]
# Shuffled tree coverage and AQI levels among cities
tree_coverage = np.array([35, 10, 50, 30, 15, 40, 45, 25])
AQI_levels = np.array([85, 150, 65, 90, 130, 75, 70, 100])

# Shuffled quarterly temperature trends for evidence of random alteration
temperature_trends = {
    "City A": [10, 20, 30, 15],  # Was City C's trend
    "City B": [8, 18, 28, 12],   # Same as before to maintain some original order
    "City C": [5, 15, 25, 10],   # Was City A's trend
    "City D": [14, 24, 34, 19],  # Was City E's trend
    "City E": [12, 22, 32, 17],  # Was City D's trend
    "City F": [18, 28, 38, 23],  # Was City G's trend
    "City G": [16, 26, 36, 21],  # Was City F's trend
    "City H": [20, 30, 40, 25]   # Same as before
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Scatter plot for tree coverage vs AQI
scatter = ax1.scatter(tree_coverage, AQI_levels, color='green', s=100, alpha=0.8,
                      edgecolors='black', linewidth=1.5)

ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 55)
ax1.set_ylim(50, 160)

# Subplot for quarterly temperature trends
for city in cities:
    temperatures = temperature_trends[city]
    quarters = ['Winter', 'Spring', 'Summer', 'Autumn']
    ax2.plot(quarters, temperatures, marker='o')

ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()