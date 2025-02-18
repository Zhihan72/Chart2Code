import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monitoring the seasonal water level changes in three interconnected lakes over a year.
# The data represents quarterly water levels (in cubic meters) for each lake.

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
ax.fill_between(quarters, lake_spring, label='Lake Spring', color='lightblue', alpha=0.7)
ax.fill_between(quarters, lake_silver_cumulative, lake_spring, label='Lake Silver', color='lightgreen', alpha=0.7)
ax.fill_between(quarters, total_water_levels, lake_silver_cumulative, label='Lake Blue', color='lightcoral', alpha=0.7)

# Titles and labels
ax.set_title('Seasonal Water Level Fluctuations in Interconnected Lakes', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Quarter', fontsize=14)
ax.set_ylabel('Water Level (1000 cubic meters)', fontsize=14)

# Adding a legend
ax.legend(loc='upper left', title='Lakes', title_fontsize='13', fontsize=11, frameon=False)

# Enhance visual details
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
ax.set_ylim(0, 400)
ax.set_yticks(range(0, 401, 50))
ax.set_xticks(np.arange(len(quarters)))
ax.set_xticklabels(quarters, rotation=45, ha='right')

# Annotate the peak water levels
peak_quarter = 'Q3'
peak_level = total_water_levels[2]
ax.annotate(f'Peak Water Level: {peak_level}k cubic meters', xy=(2, peak_level), xytext=(0.8, peak_level + 30),
            arrowprops=dict(facecolor='darkblue', arrowstyle='->'), fontsize=11, color='darkblue')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()