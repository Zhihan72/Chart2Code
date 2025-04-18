import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['App Dev', 'Data Analysis', 'Game Programming', 'IoT', 'Web Development']
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

colors = ['#32CD32', '#8A2BE2', '#FF6347', '#4682B4']

for (language, proficiency), color in zip(values.items(), colors):
    data = proficiency + proficiency[:1]
    ax.plot(angles, data, linewidth=2, linestyle='-', color=color, marker='o')
    ax.fill(angles, data, alpha=0.25, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkblue')
ax.spines['polar'].set_visible(False)

ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['Two', 'Four', 'Six', 'Eight', 'Ten'], color='grey', fontsize=10)

plt.title('Coding Skills Radar\nDomain Assessment Comparison 2023', size=15, color='navy', pad=40)

for language, proficiency in values.items():
    for i, (angle, score) in enumerate(zip(angles, proficiency + proficiency[:1])):
        if score == max(proficiency) or score == min(proficiency):
            ax.text(angle, score + 0.5, f"{score}", color='black', fontsize=9, ha='center')

plt.tight_layout()
plt.show()