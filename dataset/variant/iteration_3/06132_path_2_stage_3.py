import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Updated values with the last three groups removed
values = [1000, 750, 600, 500, 400, 350, 300]
single_color = '#6baed6'

fig, ax = plt.subplots(figsize=(12, 9))

total_width = 12
width_ratios = [value / max(values) for value in values]
heights = 1.4

for i, value in enumerate(values):
    stage_width = width_ratios[i] * total_width
    x_offset = (total_width - stage_width) / 2
    y_position = -i * heights

    polygon = patches.FancyBboxPatch(
        (x_offset, y_position),
        stage_width, -heights,
        boxstyle="round,pad=0.05",
        edgecolor='black',
        facecolor=single_color,
        linewidth=1.5
    )
    ax.add_patch(polygon)

ax.set_xlim(0, total_width)
ax.set_ylim(-len(values) * heights, 0)
ax.axis('off')

plt.tight_layout()
plt.show()