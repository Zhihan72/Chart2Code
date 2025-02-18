import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])
revenue_per_tourist = 1.0
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

sorted_indices = np.argsort(space_revenue)[::-1]
sorted_years = years[sorted_indices]
sorted_space_revenue = space_revenue[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 9))

# Randomly altering color, opacity, and marker type
colors = ['#FF5733', '#4287f5', '#42f54e']
fill_patterns = ['/', '\\', '|']
selected_color = colors[sorted_indices[0] % len(colors)]
selected_pattern = fill_patterns[sorted_indices[0] % len(fill_patterns)]

ax1.bar(sorted_years, sorted_space_revenue, color=selected_color, hatch=selected_pattern, alpha=0.75, label='Revenue ($M)', width=0.4)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Revenue (in millions)", fontsize=14, color=selected_color)
ax1.tick_params(axis='y', labelcolor=selected_color)

plt.title("Sorted Space Tourism Revenue\nfrom 2020 to 2030", fontsize=18, fontweight='bold', pad=15)

# Random location for legend
legend_locations = ['upper right', 'upper left', 'lower left', 'lower right']
ax1.legend(loc=legend_locations[sorted_indices[0] % len(legend_locations)])

# Randomly alter grid styles
grid_styles = ['-', '--', '-.', ':']
ax1.grid(True, linestyle=grid_styles[sorted_indices[0] % len(grid_styles)], alpha=0.7)

fig.tight_layout()
plt.show()