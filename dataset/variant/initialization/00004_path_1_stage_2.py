import numpy as np
import matplotlib.pyplot as plt

categories = ['Plant\nIdentification', 'Soil\nPreparation', 'Pest\nControl',
              'Watering\nEfficiency', 'Plant\nArrangement', 'Harvest\nYield']
N = len(categories)

values = [8, 7, 6, 9, 5, 8]
values += values[:1]
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Updated color scheme
ax.yaxis.grid(True, color='skyblue', linestyle='dotted')
ax.xaxis.grid(True, color='darkorange', linestyle='dashdot', linewidth=0.9)
ax.spines['polar'].set_color('green')
ax.spines['polar'].set_linewidth(1.5)

plt.xticks(angles[:-1], categories, color='darkorange', size=9, rotation=35)

ax.set_rscale('linear')
plt.yticks([2, 5, 7], ["2", "5", "7"], color="navy", size=9)
plt.ylim(0, 10)

ax.plot(angles, values, linewidth=1.5, linestyle='--', color='green', 
        marker='o', markersize=7, label="Green Thumb")
ax.fill(angles, values, 'green', alpha=0.2)

plt.title('Gardening Skills Radar', size=15, color='navy', loc='right', y=1.15)
plt.legend(loc='lower left', bbox_to_anchor=(0.1, -0.1), fontsize='medium',
           title="Gardener Profile", title_fontsize='small')

plt.tight_layout()

plt.show()