import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1975, 2030, 10)
residential_solar = [1, 4, 15, 30, 50, 70]
commercial_solar = [2, 8, 20, 35, 55, 75]
industrial_solar = [0, 2, 8, 20, 40, 65]
agricultural_solar = [0, 1, 3, 10, 20, 35]

area_data = np.vstack([residential_solar, commercial_solar, industrial_solar, agricultural_solar])
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Growth of Solar Energy Adoption in the U.S. (1975-2025)', fontsize=16, fontweight='bold', y=1.05)

ax1 = axes[0]
ax1.stackplot(decades, area_data, colors=colors, alpha=0.8)
ax1.set_title('Percentage of Total Energy Usage (%)', fontsize=14)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.set_xticks(decades)
ax1.set_yticks(np.arange(0, 101, 20))
ax1.tick_params(axis='x', rotation=45)

categories = ['Residential', 'Commercial', 'Industrial', 'Agricultural']
usage_perc_2025 = [70, 75, 65, 35]

# Sort the data in descending order for the bar chart
sorted_indices = np.argsort(usage_perc_2025)[::-1]
sorted_categories = [categories[i] for i in sorted_indices]
sorted_usage_perc_2025 = [usage_perc_2025[i] for i in sorted_indices]

ax2 = axes[1]
bars = ax2.bar(sorted_categories, sorted_usage_perc_2025, color=colors, alpha=0.8)
ax2.set_title('Projected Solar Energy Usage in 2025', fontsize=14)
ax2.set_xlabel('Sector', fontsize=12)
ax2.set_ylabel('Projected Percentage (%)', fontsize=12)
ax2.set_yticks(np.arange(0, 101, 20))
ax2.bar_label(bars, padding=3)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()