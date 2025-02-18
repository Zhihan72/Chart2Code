import matplotlib.pyplot as plt
import numpy as np

sedans = [8.5, 9.2, 9.5, 7.4, 5.7, 6.8, 8.0, 7.6, 5.3, 9.0, 6.3, 6.1, 8.9, 7.8, 5.0, 8.3, 7.0, 6.5, 7.2, 5.5, 5.9]

fig, ax = plt.subplots(figsize=(7, 9))

# Alter stylistic elements
box_colors = ['lemonchiffon', 'palegreen', 'lightcoral', 'skyblue']
line_styles = ['-.', ':', '--', '-']
marker_styles = ['v', '^', 's', 'o']

box = ax.boxplot(sedans, vert=True, patch_artist=True, notch=False,
                 boxprops=dict(facecolor=box_colors[2], color='darkviolet'),
                 whiskerprops=dict(color='darkviolet', linestyle=line_styles[1]),
                 capprops=dict(color='darkviolet'),
                 medianprops=dict(color='limegreen', linewidth=3),
                 flierprops=dict(markerfacecolor='red', marker=marker_styles[2], markersize=10, linestyle='none'))

mean = np.mean(sedans)
ax.scatter(1, mean, color='darkred', marker=marker_styles[0])

# Alter grid style
ax.set_xticks(ticks=[1])
ax.set_xticklabels([''])
ax.grid(axis='y', linestyle=line_styles[3], alpha=0.5)

# Add random styled legend
ax.legend(['Mean Value'], loc='upper right', frameon=False)

plt.tight_layout()
plt.show()