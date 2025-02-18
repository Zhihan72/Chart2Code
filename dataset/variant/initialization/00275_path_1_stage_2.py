import matplotlib.pyplot as plt
import numpy as np

languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]
orbis_popularity = [92, 72, 80, 85, 68]

bar_width = 0.25
r1 = np.arange(len(languages))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

fig, ax = plt.subplots(figsize=(12, 7))
ax.bar(r1, xenon_popularity, color='m', width=bar_width, edgecolor='black', linestyle='dashed', label='Xenon')  # Changed edge color and style
ax.bar(r2, zephyr_popularity, color='b', width=bar_width, alpha=0.7, edgecolor='navy', linewidth=2, label='Zephyr')  # Changed edge color and thickness
ax.bar(r3, orbis_popularity, color='c', width=bar_width, edgecolor='darkgreen', label='Orbis')  # Changed color and style

for rects, data in zip([r1, r2, r3], [xenon_popularity, zephyr_popularity, orbis_popularity]):
    for rect, value in zip(rects, data):
        ax.text(rect, value + 1, str(value), ha='center', va='bottom', fontsize=9.5, rotation=45)  # Changed font size and rotation

ax.set_xlabel('Programming Languages', fontweight='light', fontsize=11)  # Changed font weight and size
ax.set_ylabel('Popularity (%)', fontweight='light', fontsize=11)
ax.set_title('Programming Language Popularity\nAcross Alien Planets', fontsize=16, fontweight='light', pad=15)  # Title style change
ax.set_xticks([r + bar_width for r in range(len(languages))])
ax.set_xticklabels(languages)
ax.yaxis.grid(True, linestyle='-.', which='major', color='purple', alpha=0.5)  # Changed grid style

plt.xticks(rotation=45, ha='right')
plt.legend(title='Planets', loc='lower right')  # Changed legend location
plt.tight_layout()
plt.show()