import matplotlib.pyplot as plt
import numpy as np

# Units in 1000 cubic meters
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
lake_spring = [70, 90, 150, 130]
lake_silver = [50, 80, 120, 110]
lake_blue = [40, 60, 90, 85]

# Calculate cumulative water levels for stacked plotting
lake_silver_cumulative = np.array(lake_spring) + np.array(lake_silver)
total_water_levels = lake_silver_cumulative + np.array(lake_blue)

# Plot configuration
fig, ax = plt.subplots(figsize=(14, 8))

# Plot area chart
ax.fill_between(quarters, lake_spring, color='lightblue', alpha=0.7)
ax.fill_between(quarters, lake_silver_cumulative, lake_spring, color='lightgreen', alpha=0.7)
ax.fill_between(quarters, total_water_levels, lake_silver_cumulative, color='lightcoral', alpha=0.7)

# Enhance visual details
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
ax.set_ylim(0, 400)
ax.set_yticks(range(0, 401, 50))
ax.set_xticks(np.arange(len(quarters)))
ax.set_xticklabels(quarters, rotation=45, ha='right')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()