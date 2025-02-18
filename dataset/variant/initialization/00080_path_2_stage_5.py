import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Data Engineering', 'App Development', 'AI/ML', 'IoT', 'VR Tools']
N = len(categories)

values = {
    'Ruby': [7, 8, 5, 5, 8],
    'PHP': [8, 4, 6, 3, 7],
    'Flutter': [5, 7, 9, 4, 5],
    'Go': [4, 6, 8, 9, 8],
    'Rust': [6, 3, 9, 5, 6],
    'Kotlin': [7, 6, 8, 5, 7],
    'Swift': [8, 7, 6, 8, 9]
}

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)

# Using a single color for all data groups
single_color = '#4682B4'

for language, proficiency in values.items():
    data = proficiency + proficiency[:1]
    ax.plot(angles, data, linewidth=2, linestyle='-', color=single_color, marker='o')
    ax.fill(angles, data, alpha=0.25, color=single_color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkblue')

ax.set_ylim(0, 10)
ax.set_yticks([])

plt.title('Technology Proficiency Comparison', size=20, color='navy', y=1.1)

plt.tight_layout()
plt.show()