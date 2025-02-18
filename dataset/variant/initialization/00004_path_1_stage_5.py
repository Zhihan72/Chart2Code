import numpy as np
import matplotlib.pyplot as plt

random_titles = ['Botanical\nInsight', 'Terra\nTuning', 'Insect\nShield',
                 'Hydration\nMastery', 'Flora\nDesign', 'Harvest\nOutput']
N = len(random_titles)

values_set1 = [8, 7, 6, 9, 5, 8]
values_set2 = [6, 8, 7, 8, 4, 7]  # Additional data series
values_set1 += values_set1[:1]
values_set2 += values_set2[:1]
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist() + [0]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.yaxis.grid(True, color='skyblue', linestyle='dotted')
ax.xaxis.grid(True, color='darkorange', linestyle='dashdot', linewidth=0.9)
ax.spines['polar'].set_color('green')
ax.spines['polar'].set_linewidth(1.5)

plt.xticks(angles[:-1], random_titles, color='darkorange', size=9, rotation=35)
plt.yticks([2, 5, 7], ["Deux", "Cinque", "Sept"], color="navy", size=9)
plt.ylim(0, 10)

ax.fill(angles, values_set1, 'green', alpha=0.4, label="Cultivator Chart")
ax.fill(angles, values_set2, 'blue', alpha=0.4, label="Explorer Chart")  # New data series

plt.title('Botany Prowess Spectrum', size=15, color='navy', loc='right', y=1.15)

plt.legend(loc='lower left', bbox_to_anchor=(0.1, -0.1), fontsize='medium')

plt.tight_layout()

plt.show()