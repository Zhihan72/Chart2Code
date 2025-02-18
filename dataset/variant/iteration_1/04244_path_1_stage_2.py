import matplotlib.pyplot as plt
import numpy as np

attributes = ['Sweetness', 'Sourness', 'Saltiness', 'Bitterness', 'Umami', 'Aroma']
num_vars = len(attributes)

cuisine_italian = [6, 2, 9, 7, 3, 8]
cuisine_japanese = [4, 9, 5, 7, 3, 8]
cuisine_indian = [5, 8, 9, 4, 7, 7]
cuisine_french = [5, 6, 3, 7, 9, 3]

cuisine_italian += cuisine_italian[:1]
cuisine_japanese += cuisine_japanese[:1]
cuisine_indian += cuisine_indian[:1]
cuisine_french += cuisine_french[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], attributes, color='darkslategray', size=12)
ax.set_yticklabels(["1", "3", "5", "7", "9"], color='grey', size=10)
ax.set_ylim(0, 10)

colors = ['#FF6347', '#4682B4', '#8FBC8B', '#DB7093']
cuisines = [cuisine_italian, cuisine_japanese, cuisine_indian, cuisine_french]
cuisine_names = ['Italian', 'Japanese', 'Indian', 'French']

for data, name, color in zip(cuisines, cuisine_names, colors):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, linewidth=1, linestyle='-', label=name, color=color)

plt.title('Sensory Attributes of Various Cuisines', size=20, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)
plt.tight_layout()
plt.show()