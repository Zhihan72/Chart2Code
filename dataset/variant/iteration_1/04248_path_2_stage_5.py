import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Proteins', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals', 'Fiber']

berries = [1.5, 14.2, 0.3, 1.6, 0.5, 2.2]
citrus = [0.9, 11.8, 0.2, 1.8, 0.6, 1.4]
tropical = [1.1, 13.5, 0.4, 1.4, 0.7, 1.7]
stone_fruits = [0.8, 12.0, 0.1, 1.2, 0.4, 1.5]
melons = [0.8, 8.0, 0.2, 0.5, 0.3, 0.9]
pomaceous = [0.6, 13.8, 0.2, 1.2, 0.4, 2.0]

N = len(categories)
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

berries += berries[:1]
citrus += citrus[:1]
tropical += tropical[:1]
stone_fruits += stone_fruits[:1]
melons += melons[:1]
pomaceous += pomaceous[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, berries, color='#FF6347', linewidth=2)      # Tomato
ax.plot(angles, citrus, color='#3CB371', linewidth=2)       # MediumSeaGreen
ax.plot(angles, tropical, color='#4682B4', linewidth=2)     # SteelBlue
ax.plot(angles, stone_fruits, color='#DA70D6', linewidth=2) # Orchid
ax.plot(angles, melons, color='#FFD700', linewidth=2)       # Gold
ax.plot(angles, pomaceous, color='#8A2BE2', linewidth=2)    # BlueViolet

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_ylim(0, 10)

plt.tight_layout()
plt.show()