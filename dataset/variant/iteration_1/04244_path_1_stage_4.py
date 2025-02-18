import matplotlib.pyplot as plt
import numpy as np

attributes = ['Salinity', 'Sweetness', 'Umami', 'Aroma', 'Bitterness', 'Sourness']
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

plt.xticks(angles[:-1], attributes, color='darkolivegreen', size=14)
ax.set_yticklabels(["2", "4", "6", "8", "10"], color='darkred', size=11)
ax.set_ylim(0, 10)
ax.grid(color='lightgrey', linestyle='--', linewidth=0.8)

colors = ['#FFD700', '#8A2BE2', '#FF4500', '#3CB371']
cuisines = [cuisine_italian, cuisine_japanese, cuisine_indian, cuisine_french]
cuisine_names = ['Fusion', 'Eastern', 'Spicy', 'Gourmet']

for data, name, color in zip(cuisines, cuisine_names, colors):
    ax.fill(angles, data, color=color, alpha=0.3)
    ax.plot(angles, data, linewidth=2, linestyle='--', marker='o', label=name, color=color)

plt.title('Flavor Attributes of Unique Dishes', size=22, color='darkmagenta', y=1.1)
plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0.1), fontsize=13, frameon=True)
plt.tight_layout()
plt.show()