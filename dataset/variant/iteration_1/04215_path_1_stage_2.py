import matplotlib.pyplot as plt
import numpy as np

regions = ['Desert', 'Tropical', 'Temperate', 'Arctic']
panel_types = ['Monocrystalline', 'Polycrystalline', 'Thin-Film']
power_output = np.array([
    [70, 55, 35, 20],
    [65, 50, 30, 18],
    [60, 45, 28, 15]
])

regions_index, panel_index = np.meshgrid(np.arange(len(regions)), np.arange(len(panel_types)), indexing='ij')
regions_index_flat = regions_index.flatten()
panel_index_flat = panel_index.flatten()
z_flat = np.zeros_like(regions_index_flat)
power_flat = power_output.flatten()

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#FF6347', '#4682B4', '#32CD32']
bar_height = 0.25

for idx, (region_idx, panel_idx, z, power, color) in enumerate(zip(regions_index_flat, panel_index_flat, z_flat, power_flat, np.repeat(colors, len(regions)))):
    y_pos = region_idx + (panel_idx - 1) * bar_height
    ax.barh(y_pos, power, bar_height, color=color, edgecolor='blue', linestyle='-', linewidth=2, label=panel_types[panel_idx] if region_idx == 0 else "")

ax.set_title("Regional Performance of Different Solar Panel Types", fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel("Region", fontsize=12)
ax.set_xlabel("Average Power Output (MW)", fontsize=12)
ax.set_yticks(np.arange(len(regions)) + bar_height / 2)
ax.set_yticklabels(regions, fontsize=10)

ax.legend(title='Solar Panel Types', loc='lower right', frameon=True, shadow=True, fancybox=True)
ax.grid(color='red', linestyle='-.', linewidth=1.5, alpha=0.3)

plt.tight_layout()
plt.show()