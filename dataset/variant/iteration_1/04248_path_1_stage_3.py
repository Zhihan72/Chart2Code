import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Proteins', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals', 'Fiber']
berries = [1.5, 14.2, 0.3, 1.6, 0.5, 2.2]
citrus = [0.9, 11.8, 0.2, 1.8, 0.6, 1.4]
tropical = [1.1, 13.5, 0.4, 1.4, 0.7, 1.7]
stone_fruits = [0.8, 12.0, 0.1, 1.2, 0.4, 1.5]
N = len(categories)

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]
berries += berries[:1]
citrus += citrus[:1]
tropical += tropical[:1]
stone_fruits += stone_fruits[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, berries, color='purple', linewidth=2)
ax.plot(angles, citrus, color='yellow', linewidth=2)
ax.plot(angles, tropical, color='brown', linewidth=2)
ax.plot(angles, stone_fruits, color='pink', linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 10)

plt.show()