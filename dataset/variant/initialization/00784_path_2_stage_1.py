import numpy as np
import matplotlib.pyplot as plt
from math import pi

attributes = ['Aroma', 'Acidity', 'Body', 'Sweetness', 'Aftertaste']
num_attributes = len(attributes)

# Data for three coffee blends
morning_brew = [7, 5, 6, 8, 7]
evening_delight = [6, 4, 8, 5, 9]
tropical_twist = [8, 7, 5, 9, 6]

data = np.array([morning_brew, evening_delight, tropical_twist])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

labels = ["Morning Brew", "Evening Delight", "Tropical Twist"]
colors = ['#FF7F0E', '#1F77B4', '#2CA02C']
markers = ['o', 'v', '^']

# Plot each coffee blend with random changes to appearance
for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.3, label=labels[i])
    ax.plot(angles, data[i], color=color, linewidth=2, linestyle='--', marker=markers[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=11, fontstyle='italic')

ax.set_title('Flavor Profiles of Coffee Blends: Enticing Journeys', fontsize=15, fontweight='normal', pad=30)

# Randomized legend placement
ax.legend(loc='upper left', bbox_to_anchor=(0.8, 0.2))

ax.grid(color='gray', linestyle=':', linewidth=0.7)

plt.tight_layout()
plt.show()