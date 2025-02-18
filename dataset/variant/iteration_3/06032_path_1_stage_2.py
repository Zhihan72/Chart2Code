import matplotlib.pyplot as plt
import numpy as np

# Define cities
cities = ["Flame Town", "Chillburgh", "Neutral Nook", "Breeze Borough", "Aquatic Isle"]

# Define temperature data for summer
summer_temperatures = [
    [35, 36, 38, 40, 39, 34, 37, 35, 38, 36],  # Inferno City
    [5, 6, 7, 4, 6, 5, 4, 7, 6, 5],  # Frostville
    [25, 26, 24, 27, 28, 26, 25, 27, 28, 26],  # Temperate Town
    [22, 23, 25, 24, 23, 22, 21, 24, 25, 23],  # Zephyr Zone
    [30, 32, 33, 31, 35, 34, 33, 32, 31, 30]   # Aqua Haven
]

# Set up the plot with one subplot
fig, ax = plt.subplots(figsize=(9, 8))

# Boxplot for summer temperatures
bp = ax.boxplot(summer_temperatures, vert=True, patch_artist=True, showmeans=True, notch=True,
                boxprops=dict(facecolor="lightcoral", color="firebrick"),
                medianprops=dict(color="darkred", linewidth=1.5),
                meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='gold'),
                whiskerprops=dict(color="firebrick"), capprops=dict(color="firebrick"))

ax.set_xticklabels(cities, fontsize=11, rotation=30)
ax.set_title("Heatwave Variations Throughout Enclaves", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Enclaves", fontsize=12)
ax.set_ylabel("Heat Levels (°C)", fontsize=12)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()