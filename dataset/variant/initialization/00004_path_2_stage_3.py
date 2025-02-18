import numpy as np
import matplotlib.pyplot as plt

categories = ['ID', 'Soil Prep', 'Pest Ctrl', 'Eff Water', 'Arrangement', 'Yield']
N = len(categories)

values = [8, 7, 6, 9, 5, 8]
values += values[:1]

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='forestgreen', size=10, rotation=45)

plt.ylim(0, 10)

uniform_color = 'forestgreen'

ax.plot(angles, values, linewidth=2.5, linestyle='-', color=uniform_color, marker='o', markersize=8)
ax.fill(angles, values, uniform_color, alpha=0.25)

plt.title('Gardening Skills', size=18, color=uniform_color, loc='center', y=1.1)

plt.tight_layout()
plt.show()