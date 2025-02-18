import matplotlib.pyplot as plt
import numpy as np

atts = ['Sweet', 'Sour', 'Salt', 'Bitter', 'Umami', 'Aroma']
num_vars = len(atts)

italian = [3, 7, 6, 2, 8, 9]
japanese = [7, 5, 4, 3, 8, 9]
indian = [9, 4, 8, 5, 7, 7]
french = [5, 6, 5, 9, 3, 7]

italian += italian[:1]
japanese += japanese[:1]
indian += indian[:1]
french += french[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

plt.xticks(angles[:-1], atts, color='darkslategray', size=12)
ax.set_yticklabels(["1", "3", "5", "7", "9"], color='grey', size=10)
ax.set_ylim(0, 10)

colors = ['#8FBC8B', '#FF6347', '#DB7093', '#4682B4']

cuisines = [italian, japanese, indian, french]
cuisine_names = ['Ital', 'Jap', 'Ind', 'Fr']

for data, name, color in zip(cuisines, cuisine_names, colors):
    ax.plot(angles, data, linewidth=2, color=color)
    ax.fill(angles, data, color=color, alpha=0.3)

plt.title('Cuisine Sensory Chart', size=18, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

plt.tight_layout()
plt.show()