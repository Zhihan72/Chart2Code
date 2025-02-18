import matplotlib.pyplot as plt
import numpy as np

regions = ['Desert', 'Tropical', 'Temperate', 'Arctic']
panel_types = ['Mono', 'Poly', 'Thin', 'Hybrid']

power_output = np.array([
    [70, 55, 35, 20],
    [65, 50, 30, 18],
    [60, 45, 28, 15],
    [75, 60, 40, 25]
])

fig, ax = plt.subplots(figsize=(12, 8))

single_color = '#4682B4'
bar_width = 0.2
y_pos = np.arange(len(regions))

for idx, panel_idx in enumerate(range(len(panel_types))):
    ax.barh(y_pos + (panel_idx - 1.5) * bar_width, power_output[panel_idx], bar_width,
            color=single_color, edgecolor='darkblue', linestyle='-', label=panel_types[panel_idx])

ax.set_title("Solar Panel Output by Region", fontsize=16, fontweight='bold')
ax.set_ylabel("Region", fontsize=13, fontweight='medium')
ax.set_xlabel("Power (MW)", fontsize=13, fontweight='medium')

ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=11)

ax.legend(title='Panel Type', loc='upper left', fontsize=10, title_fontsize='12')

ax.grid(color='gray', linestyle='-', linewidth=0.7)

plt.tight_layout()
plt.show()