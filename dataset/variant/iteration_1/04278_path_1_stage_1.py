import matplotlib.pyplot as plt
import numpy as np

# Define decades and solar energy adoption data for different sectors
decades = np.arange(1975, 2030, 10)
residential_solar = [1, 4, 15, 30, 50, 70]
commercial_solar = [2, 8, 20, 35, 55, 75]
industrial_solar = [0, 2, 8, 20, 40, 65]

# Prepare data for stacked area chart
area_data = np.vstack([residential_solar, commercial_solar, industrial_solar])

# Define colors for each sector
colors = ['#ff9999','#66b3ff','#99ff99']

# Create figure and axis for the area chart
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Growth of Solar Energy Adoption in the U.S. (1975-2025)', fontsize=16, fontweight='bold', y=1.05)

# Left Subplot: Stacked Area Chart
ax1 = axes[0]
ax1.stackplot(decades, area_data, colors=colors, alpha=0.8)
ax1.set_title('Percentage of Total Energy Usage (%)', fontsize=14)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.set_xticks(decades)
ax1.set_yticks(np.arange(0, 81, 20))
ax1.tick_params(axis='x', rotation=45)

# Right Subplot: Bar Chart for 2025 Projection
bar_width = 0.35
categories = ['Residential', 'Commercial', 'Industrial']
usage_perc_2025 = [70, 75, 65]

ax2 = axes[1]
bars = ax2.bar(categories, usage_perc_2025, bar_width, color=colors, alpha=0.8)
ax2.set_title('Projected Solar Energy Usage in 2025', fontsize=14)
ax2.set_xlabel('Sector', fontsize=12)
ax2.set_ylabel('Projected Percentage (%)', fontsize=12)
ax2.set_yticks(np.arange(0, 81, 20))
ax2.bar_label(bars, padding=3)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the chart
plt.show()