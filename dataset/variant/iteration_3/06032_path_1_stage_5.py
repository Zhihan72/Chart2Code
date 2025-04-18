import matplotlib.pyplot as plt
import numpy as np

# Define cities
cities = ["Flame Town", "Chillburgh", "Neutral Nook", "Breeze Borough"]

# Define temperature data for summer
summer_temperatures = [
    [35, 36, 38, 40, 39, 34, 37, 35, 38, 36],  # Inferno City
    [5, 6, 7, 4, 6, 5, 4, 7, 6, 5],  # Frostville
    [25, 26, 24, 27, 28, 26, 25, 27, 28, 26],  # Temperate Town
    [22, 23, 25, 24, 23, 22, 21, 24, 25, 23]   # Zephyr Zone
]

fig, ax = plt.subplots(figsize=(9, 8))

# Horizontal boxplot for summer temperatures
bp = ax.boxplot(summer_temperatures, vert=False, patch_artist=True, showmeans=True, notch=True,
                boxprops=dict(facecolor="skyblue", color="navy"),
                medianprops=dict(color="orange", linewidth=1.5),
                meanprops=dict(marker='D', markeredgecolor='red', markerfacecolor='lime'),
                whiskerprops=dict(color="navy"), capprops=dict(color="navy"))

ax.set_yticklabels(cities, fontsize=11)
ax.set_title("Heatwave Variations Throughout Enclaves", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Enclaves", fontsize=12)
ax.set_xlabel("Heat Levels (°C)", fontsize=12)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()