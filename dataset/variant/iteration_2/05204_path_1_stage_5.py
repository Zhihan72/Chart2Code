import matplotlib.pyplot as plt
import numpy as np

# Shortened superhero names and categories
superheroes = ["Iron Av", "Knight", "Witch", "Guardian", "Fastest"]
categories = ["Str", "Tech", "Magic", "Dur", "Spd"]

capabilities = np.array([
    [7, 8, 3, 7, 6],
    [8, 8, 2, 8, 5],
    [6, 5, 9, 7, 3],
    [5, 3, 5, 9, 4],
    [4, 3, 4, 2, 9]
])

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
new_colors = ["#1E90FF", "#FF1493", "#8B008B", "#228B22", "#FFD700"]

# Iterate through each superhero's data and plot on the radar chart
for idx, (data, color) in enumerate(zip(capabilities, new_colors)):
    data = np.concatenate((data, [data[0]]))
    line_style = '-' if idx % 2 == 0 else '--'
    marker_style = 'o' if idx % 3 == 0 else 's'
    ax.plot(angles, data, linestyle=line_style, color=color, marker=marker_style, markersize=5, linewidth=2)
    ax.fill(angles, data, color=color, alpha=0.2, label=superheroes[idx])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, style='italic')

ax.set_yticks(range(1, 11, 2))
ax.set_yticklabels([str(i) for i in range(1, 11, 2)], color='blue')

ax.xaxis.grid(True, color='blue', linestyle='-.', linewidth=1)

# Simplified title and legend title
ax.set_title("Hero Skills", fontsize=18, color='purple', loc='left')
ax.legend(loc='lower left', bbox_to_anchor=(-0.1, 0), title="Heroes", fontsize=9, frameon=False)

ax.set_facecolor('#e6f7ff')

plt.tight_layout()
plt.show()