import matplotlib.pyplot as plt
import numpy as np

# Define cities
cities = ["Inferno City", "Frostville", "Temperate Town", "Zephyr Zone", "Aqua Haven"]

# Define temperature data for each city during summer and winter
summer_temperatures = [
    [35, 36, 38, 40, 39, 34, 37, 35, 38, 36],
    [5, 6, 7, 4, 6, 5, 4, 7, 6, 5],
    [25, 26, 24, 27, 28, 26, 25, 27, 28, 26],
    [22, 23, 25, 24, 23, 22, 21, 24, 25, 23],
    [30, 32, 33, 31, 35, 34, 33, 32, 31, 30]
]

winter_temperatures = [
    [5, 6, 8, 10, 7, 6, 5, 6, 7, 8],
    [-10, -8, -9, -11, -7, -12, -10, -9, -8, -11],
    [12, 14, 13, 15, 11, 13, 14, 12, 13, 14],
    [10, 11, 13, 12, 9, 11, 10, 12, 12, 11],
    [17, 18, 20, 21, 19, 18, 17, 18, 19, 20]
]

# Set up the plot with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Boxplot for winter temperatures (swapped position)
ax1 = axes[0]
bp1 = ax1.boxplot(winter_temperatures, vert=True, patch_artist=True, showmeans=True, notch=True,
                  boxprops=dict(facecolor="lightblue", color="navy"),
                  medianprops=dict(color="blue", linewidth=1.5),
                  meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='gold'),
                  whiskerprops=dict(color="navy"), capprops=dict(color="navy"))

ax1.set_xticklabels(cities, fontsize=11, rotation=30)
ax1.set_title("Winter Temperatures Across Cities in Elementia", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Cities", fontsize=12)
ax1.set_ylabel("Temperature (°C)", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Boxplot for summer temperatures (swapped position)
ax2 = axes[1]
bp2 = ax2.boxplot(summer_temperatures, vert=True, patch_artist=True, showmeans=True, notch=True,
                  boxprops=dict(facecolor="lightcoral", color="firebrick"),
                  medianprops=dict(color="darkred", linewidth=1.5),
                  meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='gold'),
                  whiskerprops=dict(color="firebrick"), capprops=dict(color="firebrick"))

ax2.set_xticklabels(cities, fontsize=11, rotation=30)
ax2.set_title("Summer Temperatures Across Cities in Elementia", fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel("Cities", fontsize=12)
ax2.set_ylabel("Temperature (°C)", fontsize=12)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better fit
plt.tight_layout()

# Display the plots
plt.show()