import matplotlib.pyplot as plt
import numpy as np

superheroes = ["Iron Avenger", "Dark Knight", "Scarlet Witch", "Green Guardian", "Fastest Man"]
categories = ["Strength", "Tech Savvy", "Magic", "Durability", "Speed"]

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
colors = ["#00BFFF", "#DC143C", "#9400D3", "#3CB371", "#FFA500"]

for idx, (data, color) in enumerate(zip(capabilities, colors)):
    data = np.concatenate((data, [data[0]]))
    line_style = '-' if idx % 2 == 0 else '--'
    marker_style = 'o' if idx % 3 == 0 else 's'
    ax.plot(angles, data, linestyle=line_style, color=color, marker=marker_style, markersize=5, linewidth=2)
    ax.fill(angles, data, color=color, alpha=0.2, label=superheroes[idx])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, style='italic')

ax.set_yticks(range(1, 11, 2))
ax.set_yticklabels([str(i) for i in range(1, 11, 2)], color='blue')

# Removed the Y-axis grid and changed the style of the X-axis grid
ax.xaxis.grid(True, color='blue', linestyle='-.', linewidth=1)

ax.set_title("League of Heroes: Capabilities Comparison", fontsize=18, color='purple', loc='left')
ax.legend(loc='lower left', bbox_to_anchor=(-0.1, 0), title="Superheroes", fontsize=9, frameon=False)

ax.set_facecolor('#e6f7ff')

plt.tight_layout()
plt.show()