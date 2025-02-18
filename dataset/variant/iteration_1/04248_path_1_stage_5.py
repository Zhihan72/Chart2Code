import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Prot.', 'Carbs', 'Fats', 'Vits', 'Mins', 'Fiber']

berries = [1.5, 14.2, 0.3, 1.6, 0.5, 2.2]
citrus = [0.9, 11.8, 0.2, 1.8, 0.6, 1.4]
tropical = [1.1, 13.5, 0.4, 1.4, 0.7, 1.7]
stone_fruits = [0.8, 12.0, 0.1, 1.2, 0.4, 1.5]
exotic_fruits = [1.2, 15.0, 0.5, 2.0, 0.8, 2.5]  # New data series

N = len(categories)

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

berries += berries[:1]
citrus += citrus[:1]
tropical += tropical[:1]
stone_fruits += stone_fruits[:1]
exotic_fruits += exotic_fruits[:1]  # Ensure closure for new series

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, berries, color='purple', linewidth=2, label="Berry")
ax.plot(angles, citrus, color='yellow', linewidth=2, label="Cit.")
ax.plot(angles, tropical, color='brown', linewidth=2, label="Trop.")
ax.plot(angles, stone_fruits, color='pink', linewidth=2, label="Stone")
ax.plot(angles, exotic_fruits, color='green', linewidth=2, label="Exotic")  # Plot new series

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 10)

ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.show()