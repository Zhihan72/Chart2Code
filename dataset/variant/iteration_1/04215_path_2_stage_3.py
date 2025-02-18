import matplotlib.pyplot as plt
import numpy as np

regions = ['Desert', 'Tropical', 'Temperate', 'Arctic']
panel_types = ['Monocrystalline', 'Polycrystalline', 'Thin-Film', 'Hybrid']

power_output = np.array([
    [70, 55, 35, 20],
    [65, 50, 30, 18],
    [60, 45, 28, 15],
    [75, 60, 40, 25]  # New data for Hybrid panels
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#4682B4', '#32CD32', '#FF6347', '#8A2BE2']  # Updated colors to include the new panel

bar_width = 0.2  # Adjust bar width to accommodate four groups
y_pos = np.arange(len(regions))

# Plot horizontal bars
for idx, (panel_idx, color) in enumerate(zip(range(len(panel_types)), colors)):
    ax.barh(y_pos + (panel_idx - 1.5) * bar_width, power_output[panel_idx], bar_width,
            color=color, edgecolor='darkblue', linestyle='-', label=panel_types[panel_idx])

ax.set_title("Performance of Solar Panel Types by Region", fontsize=16, fontweight='bold')
ax.set_ylabel("Region", fontsize=13, fontweight='medium')
ax.set_xlabel("Power Output (MW)", fontsize=13, fontweight='medium')

ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=11)

ax.legend(title='Types of Panels', loc='upper left', fontsize=10, title_fontsize='12')

ax.grid(color='gray', linestyle='-', linewidth=0.7)

plt.tight_layout()
plt.show()