import matplotlib.pyplot as plt
import numpy as np

categories = ['Sweetness', 'Fiber Content', 'Vitamin C', 'Water Content', 'Sugar Levels']

# Data for fruits in different regions
tropical_scores = [8, 7, 9, 6, 8]
temperate_scores = [6, 8, 7, 7, 6]
mediterranean_scores = [7, 6, 5, 8, 7]
continental_scores = [5, 6, 7, 9, 6]

tropical_scores += tropical_scores[:1]
temperate_scores += temperate_scores[:1]
mediterranean_scores += mediterranean_scores[:1]
continental_scores += continental_scores[:1]

num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Shuffled colors for each region plot
colors = ['green', 'purple', 'blue', 'red']

ax.plot(angles, tropical_scores, color=colors[0], linewidth=2, linestyle='solid', label='Tropical Fruits')
ax.fill(angles, tropical_scores, color=colors[0], alpha=0.25)

ax.plot(angles, temperate_scores, color=colors[1], linewidth=2, linestyle='solid', label='Temperate Fruits')
ax.fill(angles, temperate_scores, color=colors[1], alpha=0.25)

ax.plot(angles, mediterranean_scores, color=colors[2], linewidth=2, linestyle='solid', label='Mediterranean Fruits')
ax.fill(angles, mediterranean_scores, color=colors[2], alpha=0.25)

ax.plot(angles, continental_scores, color=colors[3], linewidth=2, linestyle='solid', label='Continental Fruits')
ax.fill(angles, continental_scores, color=colors[3], alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold', ha='center')
ax.set_yticklabels([])

plt.title("Fruit Attributes Comparison Across Different Regions", fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title='Regions')
plt.tight_layout()
plt.show()