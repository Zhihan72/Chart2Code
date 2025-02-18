import numpy as np
import matplotlib.pyplot as plt
from math import pi

attributes = ['Aroma', 'Acidity', 'Body', 'Sweetness', 'Aftertaste']
num_attributes = len(attributes)

morning_brew = [7, 5, 6, 8, 7]
evening_delight = [6, 4, 8, 5, 9]

data = np.array([morning_brew, evening_delight])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

labels = ["Morning Brew", "Evening Delight"]

# Shuffle colors for the blends
colors = ['#1F77B4', '#FF7F0E']  # Colors have been swapped

for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.25, label=labels[i])
    ax.plot(angles, data[i], color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=12, fontweight='bold')

ax.set_title('Flavor Profiles of Coffee Blends\nA Journey Through Taste', fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.tight_layout()
plt.show()