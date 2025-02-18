import numpy as np
import matplotlib.pyplot as plt

centuries = ['18th', '20th']
methods = ['Stone', 'Brick', 'Wood', 'Steel']

data = np.array([
    [20, 50, 30, 0],
    [10, 20, 30, 40]
])

method_totals = data.sum(axis=0)
sorted_indices = np.argsort(method_totals)[::-1]
sorted_methods = [methods[i] for i in sorted_indices]
sorted_data = data[:, sorted_indices]

x_pos = np.arange(len(methods))

fig, ax = plt.subplots(figsize=(10, 6))

# Randomly chosen colors, markers, and line styles replacements
colors = ['#1B9E77', '#D95F02', '#7570B3', '#E7298A']
markers = ['o', 's', '^', 'D']  # Circle, Square, Triangle, Diamond
line_styles = ['-', '--', '-.', ':']

for i in range(len(centuries)):
    ax.bar(
        x_pos + i * 0.2, sorted_data[i], width=0.2,
        color=colors[i], alpha=0.6, label=centuries[i],
        edgecolor='black', hatch=markers[i]
    )

# Randomized labels and title
ax.set_xlabel('Construction Methods', fontsize=12, fontstyle='italic')
ax.set_ylabel('Usage Percentage (%)', fontsize=12, fontweight='bold')
ax.set_title('Construction Methods Usage Over Centuries', fontsize=15, fontweight='heavy')

ax.set_xticks(x_pos + 0.3)
ax.set_xticklabels(sorted_methods, fontsize=11, rotation=15, ha='right')

# Random shuffling of the legend
ax.legend(title='Century', fontsize=9, loc='upper left', fancybox=True, shadow=True)

# Random decision to add grid
ax.grid(visible=True, linestyle='--', linewidth=0.5, color='grey')

plt.tight_layout()
plt.show()