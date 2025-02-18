import matplotlib.pyplot as plt
import numpy as np

attributes = ['Sweetness', 'Sourness', 'Saltiness', 'Bitterness', 'Umami', 'Aroma']
num_vars = len(attributes)

cuisine_italian = [7, 3, 6, 2, 8, 9]
cuisine_japanese = [5, 7, 4, 3, 9, 8]
cuisine_indian = [8, 4, 9, 5, 7, 7]
cuisine_french = [6, 5, 5, 3, 7, 9]

cuisine_italian += cuisine_italian[:1]
cuisine_japanese += cuisine_japanese[:1]
cuisine_indian += cuisine_indian[:1]
cuisine_french += cuisine_french[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

plt.xticks(angles[:-1], attributes, color='darkslategray', size=12)
ax.set_yticklabels(["1", "3", "5", "7", "9"], color='grey', size=10)
ax.set_ylim(0, 10)

colors = ['#8FBC8B', '#FF6347', '#DB7093', '#4682B4']

cuisines = [cuisine_italian, cuisine_japanese, cuisine_indian, cuisine_french]
cuisine_names = ['Italian', 'Japanese', 'Indian', 'French']

for data, name, color in zip(cuisines, cuisine_names, colors):
    ax.plot(angles, data, linewidth=2, color=color)
    ax.fill(angles, data, color=color, alpha=0.3)

plt.title('Sensory Attributes of Various Cuisines', size=20, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)

plt.tight_layout()
plt.show()