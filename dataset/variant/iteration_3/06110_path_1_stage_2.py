import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
northern_hills_temp = [-2, -1, 0, 1, 2, -1, 0, -2, 1, 2]
coastal_plains_temp = [15, 16, 16, 17, 17, 18, 16, 15, 17, 18]
desert_valley_temp = [25, 26, 27, 28, 29, 28, 26, 25, 27, 28]
tropical_forest_temp = [30, 31, 30, 31, 32, 31, 30, 31, 32, 31]

fig, ax = plt.subplots(figsize=(14, 8))

# Apply a single color consistently across all plots
single_color = 'c'  # Choose a color, e.g., 'c' for cyan

ax.plot(years, northern_hills_temp, marker='o', linestyle='-', color=single_color)
ax.plot(years, coastal_plains_temp, marker='s', linestyle='--', color=single_color)
ax.plot(years, desert_valley_temp, marker='^', linestyle='-.', color=single_color)
ax.plot(years, tropical_forest_temp, marker='d', linestyle=':', color=single_color)

plt.title("Decade Temperature Trends (2013-2022) Across Major Regions", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel("Average Temperature (°C)", fontsize=14, fontweight='bold', labelpad=15)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlim(2013, 2022)
ax.set_ylim(-5, 35)

plt.tight_layout()
plt.show()