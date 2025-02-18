import matplotlib.pyplot as plt
import numpy as np

superheroes = [
    "Iron Avenger", "Dark Knight", "Scarlet Witch", 
    "Green Guardian", "Fastest Man", "Blue Thunder", "Crimson Defender"
]
categories = ["Strength", "Tech Savvy", "Magic", "Durability", "Speed"]

capabilities = np.array([
    [8, 9, 2, 8, 7],
    [7, 9, 1, 7, 6],
    [5, 4, 10, 6, 4],
    [6, 4, 4, 10, 5],
    [3, 2, 3, 3, 10],
    [7, 6, 1, 7, 6],  # Blue Thunder
    [4, 5, 2, 9, 7]   # Crimson Defender
])

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ["#FF0000", "#000000", "#800080", "#008000", "#FFD700", "#0000FF", "#DC143C"]

for idx, (data, color) in enumerate(zip(capabilities, colors)):
    data = np.concatenate((data, [data[0]]))
    ax.fill(angles, data, color=color, alpha=0.3)
    ax.plot(angles, data, linewidth=2, linestyle='solid', marker='o', color=color)
    for angle, val in zip(angles, data):
        ax.text(angle, val + 0.5, f'{val:.1f}', horizontalalignment='center', verticalalignment='center', fontsize=8, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

ax.set_yticks(range(1, 11))
ax.set_yticklabels([])
ax.yaxis.grid(False)
ax.xaxis.grid(False)

ax.set_frame_on(False)
ax.set_title("League of Heroes: Capabilities Comparison", fontsize=16, fontweight='bold', va='bottom')

ax.set_facecolor('#f0f0f0')

plt.tight_layout()
plt.show()