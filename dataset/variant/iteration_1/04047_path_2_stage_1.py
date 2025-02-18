import matplotlib.pyplot as plt
import numpy as np

# Data for pollutants (Particulate Matter: PM2.5, Carbon Monoxide: CO, Nitrogen Dioxide: NO2) over four seasons
seasons = np.array(['Winter', 'Spring', 'Summer', 'Autumn'])

# PM2.5 levels in micrograms per cubic meter
pm25_levels = np.array([35, 20, 15, 25])

# CO levels in milligrams per cubic meter
co_levels = np.array([0.9, 0.6, 0.4, 0.7])

# NO2 levels in micrograms per cubic meter
no2_levels = np.array([40, 25, 20, 30])

# Creating the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data for each pollutant with new colors
ax.plot(seasons, pm25_levels, marker='o', linestyle='-', color='purple', linewidth=2, label='PM2.5')
ax.plot(seasons, co_levels, marker='s', linestyle='--', color='orange', linewidth=2, label='CO')
ax.plot(seasons, no2_levels, marker='^', linestyle='-.', color='brown', linewidth=2, label='NO2')

# Title and labels
ax.set_title("Seasonal Air Quality Analysis in Greenfield (Last Decade)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Seasons", fontsize=14)
ax.set_ylabel("Pollutant Levels", fontsize=14)

# Adding a secondary y-axis for CO levels due to different units
ax_right = ax.twinx()
ax_right.set_ylabel("CO Levels (mg/m³)", fontsize=14)

# Ensuring the secondary y-axis corresponds to CO levels
ax_right.plot(seasons, co_levels, marker='s', linestyle='--', color='orange', linewidth=2)
ax_right.tick_params(axis='y', labelcolor='orange')

# Adding legends
ax.legend(loc='upper left', fontsize='medium')

# Grid and layout adjustments
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()