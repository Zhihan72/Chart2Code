import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Web Dev', 'Data Science', 'Mobile Dev', 'Embedded Systems', 'Game Dev']
N = len(categories)

values = {
    'Python': [8, 10, 5, 5, 6],
    'JavaScript': [10, 5, 7, 3, 6],
    'C++': [4, 7, 7, 10, 9],
    'Swift': [5, 3, 10, 6, 7]
}

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)

# Manually shuffled colors
colors = ['#32CD32', '#8A2BE2', '#FF6347', '#4682B4']  # Changed the order here

for (language, proficiency), color in zip(values.items(), colors):
    data = proficiency + proficiency[:1]
    ax.plot(angles, data, linewidth=2, linestyle='-', label=language, color=color, marker='o')
    ax.fill(angles, data, alpha=0.25, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkblue')

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', fontsize=10)

plt.title('Programming Language Proficiency Radar\nComparative Analysis Across Domains - 2023', size=15, color='navy', pad=40)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, frameon=True, framealpha=0.5)

for language, proficiency in values.items():
    for i, (angle, score) in enumerate(zip(angles, proficiency + proficiency[:1])):
        if score == max(proficiency) or score == min(proficiency):
            ax.text(angle, score + 0.5, f"{score}", color='black', fontsize=9, ha='center')

plt.tight_layout()
plt.show()