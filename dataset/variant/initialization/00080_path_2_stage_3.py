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
    'Rust': [6, 3, 9, 5, 6]
}

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

for (language, proficiency), color in zip(values.items(), colors):
    data = proficiency + proficiency[:1]
    ax.plot(angles, data, linewidth=2, linestyle='-', color=color, marker='o')
    ax.fill(angles, data, alpha=0.25, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkblue')

ax.set_ylim(0, 10)
ax.set_yticks([])

plt.title('Technology Proficiency Comparison', size=20, color='navy', y=1.1)

plt.tight_layout()
plt.show()