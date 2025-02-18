import matplotlib.pyplot as plt
import numpy as np

regions = ['Desert', 'Tropical', 'Temperate', 'Arctic']
panel_types = ['Monocrystalline', 'Polycrystalline', 'Thin-Film']

power_output = np.array([
    [70, 55, 35, 20],
    [65, 50, 30, 18],
    [60, 45, 28, 15]
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#4682B4', '#32CD32', '#FF6347']  # Changed the order of colors

bar_width = 0.3  # Changed width of the bars
y_pos = np.arange(len(regions))

# Plot horizontal bars with modified styles
for idx, (panel_idx, color) in enumerate(zip(range(len(panel_types)), colors)):
    ax.barh(y_pos + (panel_idx - 1) * bar_width, power_output[panel_idx], bar_width,
            color=color, edgecolor='darkblue', linestyle='-', label=panel_types[panel_idx])  # Changed edge color and line style

ax.set_title("Performance of Solar Panel Types by Region", fontsize=16, fontweight='bold')  # Adjusted title font size
ax.set_ylabel("Region", fontsize=13, fontweight='medium')
ax.set_xlabel("Power Output (MW)", fontsize=13, fontweight='medium')

ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=11)

# Legend style changed
ax.legend(title='Types of Panels', loc='upper left', fontsize=10, title_fontsize='12')  # Changed legend position, font size

# Grid style changed
ax.grid(color='gray', linestyle='-', linewidth=0.7)  # Modified grid line style and width

plt.tight_layout()
plt.show()