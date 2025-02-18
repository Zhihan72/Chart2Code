import matplotlib.pyplot as plt
import numpy as np

superheroes = [
    "Starlight Warrior", "Night Phantom", "Enigma Sorceress", 
    "Emerald Protector", "Swift Whirlwind", "Azure Storm", "Scarlet Sentinel"
]
categories = ["Power", "Gadgetry", "Enchantments", "Endurance", "Agility"]

capabilities = np.array([
    [8, 9, 2, 8, 7],
    [7, 9, 1, 7, 6],
    [5, 4, 10, 6, 4],
    [6, 4, 4, 10, 5],
    [3, 2, 3, 3, 10],
    [7, 6, 1, 7, 6],
    [4, 5, 2, 9, 7]
])

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define a single consistent color for all data groups
single_color = "#1E90FF" 

for idx, data in enumerate(capabilities):
    data = np.concatenate((data, [data[0]]))
    ax.fill(angles, data, color=single_color, alpha=0.3)
    ax.plot(angles, data, linewidth=2, linestyle='solid', marker='o', color=single_color)
    for angle, val in zip(angles, data):
        ax.text(angle, val + 0.5, f'{val:.1f}', horizontalalignment='center', verticalalignment='center', fontsize=8, color=single_color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

ax.set_yticks(range(1, 11))
ax.set_yticklabels([])
ax.yaxis.grid(False)
ax.xaxis.grid(False)

ax.set_frame_on(False)
ax.set_title("Champions of Valor: Skills Showdown", fontsize=16, fontweight='bold', va='bottom')

ax.set_facecolor('#f0f0f0')

plt.tight_layout()
plt.show()