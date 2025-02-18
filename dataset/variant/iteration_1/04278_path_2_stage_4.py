import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1975, 2030, 10)
residential_solar = [1, 4, 15, 30, 50, 70]
commercial_solar = [2, 8, 20, 35, 55, 75]
area_data = np.vstack([residential_solar, commercial_solar])

single_color = '#99cc99'

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('U.S. Solar Energy Uptake Journey (1975-2025)', fontsize=16, fontweight='bold', y=1.05)

# Stacked Area Chart
ax1 = axes[0]
ax1.stackplot(decades, area_data, colors=[single_color]*2, alpha=0.8)
ax1.set_title('Energy Proportion Decadal Shift (%)', fontsize=14)
ax1.set_xlabel('Year Blocks', fontsize=12)
ax1.set_ylabel('Energy Share (%)', fontsize=12)
ax1.set_xticks(decades)
ax1.set_yticks(np.arange(0, 81, 20))
ax1.tick_params(axis='x', rotation=45)

# Bar Chart for 2025 Projection
bar_width = 0.35
categories = ['Home Use', 'Business Use']
usage_perc_2025 = [70, 75]

ax2 = axes[1]
bars = ax2.bar(categories, usage_perc_2025, bar_width, color=single_color, alpha=0.8)
ax2.set_title('2025 Solar Energy Use Forecast', fontsize=14)
ax2.set_xlabel('Category', fontsize=12)
ax2.set_ylabel('Expected Share (%)', fontsize=12)
ax2.set_yticks(np.arange(0, 81, 20))
ax2.bar_label(bars, padding=3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()