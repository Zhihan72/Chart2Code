import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Web Dev', 'Data Science', 'Mobile Dev', 'Embedded Systems', 'Game Dev']
N = len(categories)

values = {
    'Python': [8, 10, 5, 5, 6],
    'JavaScript': [10, 5, 7, 3, 6],
    'Java': [6, 6, 9, 7, 6],
    'C++': [4, 7, 7, 10, 9],
    'Swift': [5, 3, 10, 6, 7]
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
ax.set_yticks([])  # Remove the y-tick labels

# Display the plot
plt.tight_layout()
plt.show()