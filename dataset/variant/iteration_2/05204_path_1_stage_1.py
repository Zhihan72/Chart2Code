import matplotlib.pyplot as plt
import numpy as np

superheroes = ["Iron Avenger", "Dark Knight", "Scarlet Witch", "Green Guardian", "Fastest Man"]
categories = ["Strength", "Tech Savvy", "Magic", "Durability", "Speed"]

capabilities = np.array([
    [8, 9, 2, 8, 7],  # Iron Avenger
    [7, 9, 1, 7, 6],  # Dark Knight
    [5, 4, 10, 6, 4], # Scarlet Witch
    [6, 4, 4, 10, 5], # Green Guardian
    [3, 2, 3, 3, 10]  # Fastest Man
])

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ["#FF0000", "#000000", "#800080", "#008000", "#FFD700"]

for idx, (data, color) in enumerate(zip(capabilities, colors)):
    data = np.concatenate((data, [data[0]]))
    ax.fill(angles, data, color=color, alpha=0.3, label=superheroes[idx])
    for angle, val in zip(angles, data):
        ax.text(angle, val + 0.5, f'{val:.1f}', horizontalalignment='center', verticalalignment='center', fontsize=8, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

ax.set_yticks(range(1, 11))
ax.set_yticklabels([])
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)
ax.xaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)

ax.set_title("League of Heroes: Capabilities Comparison", fontsize=16, fontweight='bold', va='bottom')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Superheroes", fontsize=10)

ax.set_facecolor('#f0f0f0')

plt.tight_layout()
plt.show()