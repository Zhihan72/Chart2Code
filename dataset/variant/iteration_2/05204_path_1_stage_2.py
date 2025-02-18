import matplotlib.pyplot as plt
import numpy as np

superheroes = ["Iron Avenger", "Dark Knight", "Scarlet Witch", "Green Guardian", "Fastest Man"]
categories = ["Strength", "Tech Savvy", "Magic", "Durability", "Speed"]

# Manually altered the capabilities data within each superhero, still maintaining 5 categories.
capabilities = np.array([
    [7, 8, 3, 7, 6],  # Iron Avenger (altered)
    [8, 8, 2, 8, 5],  # Dark Knight (altered)
    [6, 5, 9, 7, 3],  # Scarlet Witch (altered)
    [5, 3, 5, 9, 4],  # Green Guardian (altered)
    [4, 3, 4, 2, 9]   # Fastest Man (altered)
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