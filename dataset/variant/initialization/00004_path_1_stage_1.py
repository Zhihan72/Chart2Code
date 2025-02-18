import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Plant\nIdentification', 'Soil\nPreparation', 'Pest\nControl',
              'Watering\nEfficiency', 'Plant\nArrangement', 'Harvest\nYield']
N = len(categories)

values = [8, 7, 6, 9, 5, 8]
values += values[:1]

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Randomly altered stylistic elements
ax.yaxis.grid(True, color='lightblue', linestyle='dotted')
ax.xaxis.grid(True, color='brown', linestyle='dashdot', linewidth=0.9)
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('purple')
ax.spines['polar'].set_linewidth(1.5)

plt.xticks(angles[:-1], categories, color='brown', size=9, rotation=35)

ax.set_rscale('linear')
plt.yticks([2, 5, 7], ["2", "5", "7"], color="darkblue", size=9)
plt.ylim(0, 10)

ax.plot(angles, values, linewidth=1.5, linestyle='--', color='purple', marker='s', markersize=7, label="Green Thumb")
ax.fill(angles, values, 'purple', alpha=0.2)

plt.title('Gardening Skills Radar', size=15, color='darkblue', loc='right', y=1.15)
plt.legend(loc='lower left', bbox_to_anchor=(0.1, -0.1), fontsize='medium', title="Gardener Profile", title_fontsize='small')

plt.tight_layout()

plt.show()