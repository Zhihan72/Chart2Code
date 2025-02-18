import matplotlib.pyplot as plt
import numpy as np

# Data for pollutants over four seasons
seasons = np.array(['Winter', 'Spring', 'Summer', 'Autumn'])
pm25_levels = np.array([15, 35, 25, 20])  # Randomly altered PM2.5 levels
co_levels = np.array([0.4, 0.7, 0.9, 0.6])  # Randomly altered CO levels
no2_levels = np.array([20, 40, 30, 25])  # Randomly altered NO2 levels

# Creating the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Using a single color for all pollutants
common_color = 'black'

ax.plot(seasons, pm25_levels, marker='o', linestyle='-', color=common_color, linewidth=2, label='PM2.5')
ax.plot(seasons, co_levels, marker='s', linestyle='--', color=common_color, linewidth=2, label='CO')
ax.plot(seasons, no2_levels, marker='^', linestyle='-.', color=common_color, linewidth=2, label='NO2')

# Title and labels
ax.set_title("Seasonal Air Quality Analysis in Greenfield (Last Decade)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Seasons", fontsize=14)
ax.set_ylabel("Pollutant Levels", fontsize=14)

# Adding a secondary y-axis for CO levels due to different units
ax_right = ax.twinx()
ax_right.set_ylabel("CO Levels (mg/m³)", fontsize=14)

# Correspondence of CO levels to secondary y-axis
ax_right.plot(seasons, co_levels, marker='s', linestyle='--', color=common_color, linewidth=2)
ax_right.tick_params(axis='y', labelcolor=common_color)

# Adding legends
ax.legend(loc='upper left', fontsize='medium')

# Grid and layout adjustments
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Display the plot
plt.show()