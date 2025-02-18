import matplotlib.pyplot as plt
import numpy as np

# Data setup
countries = ['Region X', 'Region Y']
energy_types = ['Geothermal', 'Nuclear', 'Biomass']
percentage_distributions = np.array([
    [40, 35, 25],  # Region X
    [30, 40, 30],  # Region Y
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_positions = np.arange(len(countries))
y_positions = np.arange(len(energy_types))
xpos, ypos = np.meshgrid(x_positions, y_positions, indexing='ij')
xpos = xpos.flatten()
ypos = ypos.flatten()
z_positions = np.zeros_like(xpos)
bar_heights = percentage_distributions.flatten()

# Changed colors and positions
colors = ['#99ff99', '#66b3ff', '#ff9999']  # New order: Biomass, Nuclear, Geothermal

# Alter border color of the bars, add edge lines, and use different alpha
ax.bar3d(xpos, ypos, z_positions, dx=0.5, dy=0.5, dz=bar_heights, color=np.repeat(colors, len(countries)), edgecolor='grey', alpha=0.7)

# Modify the plot's style elements
ax.set_title('Alternative Energy Use By Region (2023)', fontsize=16, fontweight='light', pad=25)
ax.set_xlabel('Regions', fontsize=10, color='blue')
ax.set_ylabel('Energy Sources', fontsize=10, color='red')
ax.set_zlabel('Usage Percentage (%)', fontsize=10, color='green')
ax.set_xticks(x_positions + 0.25)
ax.set_yticks(y_positions + 0.25)
ax.set_xticklabels(countries, rotation=5, ha='right')
ax.set_yticklabels(energy_types)
ax.set_zlim(0, 50)

# Style the grid
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Alter legend styling
legend_elements = [plt.Line2D([0], [0], marker='^', color='w', label=energy_type, markerfacecolor=color, markersize=12) 
                   for energy_type, color in zip(energy_types, colors)]
ax.legend(handles=legend_elements, title='Energy Sources', loc='upper right', fontsize=9, title_fontsize=11, frameon=False)

plt.tight_layout()
plt.show()