import matplotlib.pyplot as plt
import numpy as np

# Artificial Data: Cities with respective tree coverage (%) and AQI Levels
cities = ["City A", "City B", "City C", "City D", "City E", "City F", "City G", "City H"]
tree_coverage = np.array([10, 15, 25, 30, 35, 40, 45, 50])
AQI_levels = np.array([150, 130, 100, 90, 85, 75, 70, 65])

# Quarterly temperature trends for each city
temperature_trends = {
    "City A": [5, 15, 25, 10],
    "City B": [8, 18, 28, 12],
    "City C": [10, 20, 30, 15],
    "City D": [12, 22, 32, 17],
    "City E": [14, 24, 34, 19],
    "City F": [16, 26, 36, 21],
    "City G": [18, 28, 38, 23],
    "City H": [20, 30, 40, 25]
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

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()