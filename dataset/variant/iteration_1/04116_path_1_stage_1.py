import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
lake_spring = [70, 90, 150, 130]
lake_silver = [50, 80, 120, 110]
lake_blue = [40, 60, 90, 85]

lake_silver_cumulative = np.array(lake_spring) + np.array(lake_silver)
total_water_levels = lake_silver_cumulative + np.array(lake_blue)

fig, ax = plt.subplots(figsize=(14, 8))

# Use a single color for all data groups
single_color = 'cornflowerblue'
alpha_value = 0.7

ax.fill_between(quarters, lake_spring, label='Lake Spring', color=single_color, alpha=alpha_value)
ax.fill_between(quarters, lake_silver_cumulative, lake_spring, label='Lake Silver', color=single_color, alpha=alpha_value)
ax.fill_between(quarters, total_water_levels, lake_silver_cumulative, label='Lake Blue', color=single_color, alpha=alpha_value)

ax.set_title('Seasonal Water Level Fluctuations in Interconnected Lakes', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Quarter', fontsize=14)
ax.set_ylabel('Water Level (1000 cubic meters)', fontsize=14)

ax.legend(loc='upper left', title='Lakes', title_fontsize='13', fontsize=11, frameon=False)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
ax.set_ylim(0, 400)
ax.set_yticks(range(0, 401, 50))
ax.set_xticks(np.arange(len(quarters)))
ax.set_xticklabels(quarters, rotation=45, ha='right')

peak_quarter = 'Q3'
peak_level = total_water_levels[2]
ax.annotate(f'Peak Water Level: {peak_level}k cubic meters', xy=(2, peak_level), xytext=(0.8, peak_level + 30),
            arrowprops=dict(facecolor='darkblue', arrowstyle='->'), fontsize=11, color='darkblue')

plt.tight_layout()
plt.show()