import matplotlib.pyplot as plt
import numpy as np

# Expanded list of regions and panel types
regions = ['Des.', 'Trop.', 'Temp.', 'Arct.', 'Subarct.']
panel_types = ['Mono', 'Poly', 'Thin', 'Amorphous']

# Expanded power output to include new region and panel type
power_output = np.array([
    [70, 55, 35, 20, 25],
    [65, 50, 30, 18, 22],
    [60, 45, 28, 15, 20],
    [58, 42, 26, 14, 18]
])

# New meshgrid and flattened arrays to accommodate expanded data
regions_index, panel_index = np.meshgrid(np.arange(len(regions)), np.arange(len(panel_types)), indexing='ij')
regions_index_flat = regions_index.flatten()
panel_index_flat = panel_index.flatten()
z_flat = np.zeros_like(regions_index_flat)
power_flat = power_output.flatten()

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#32CD32', '#FF6347', '#4682B4', '#FFD700']  # Added color for new panel type
bar_height = 0.2  # Adjusted for additional panel type

# Adjusted loop for additional panel type and data
for idx, (region_idx, panel_idx, z, power, color) in enumerate(zip(regions_index_flat, panel_index_flat, z_flat, power_flat, np.repeat(colors, len(regions)))):
    y_pos = region_idx + (panel_idx - (len(panel_types) - 2)) * bar_height
    ax.barh(y_pos, power, bar_height, color=color, edgecolor='blue', linewidth=2, label=panel_types[panel_idx] if region_idx == 0 else "")

ax.set_title("Regional Solar Panel Output", fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel("Region", fontsize=12)
ax.set_xlabel("Avg Output (MW)", fontsize=12)
ax.set_yticks(np.arange(len(regions)) + bar_height / 2)
ax.set_yticklabels(regions, fontsize=10)

ax.legend(title='Panel Type', loc='lower right', frameon=True, shadow=True, fancybox=True)
ax.grid(color='red', linestyle='-.', linewidth=1.5, alpha=0.3)

plt.tight_layout()
plt.show()