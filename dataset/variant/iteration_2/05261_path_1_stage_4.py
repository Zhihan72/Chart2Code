import matplotlib.pyplot as plt
import numpy as np

categories = ['Sweetness', 'Fiber Content', 'Vitamin C', 'Water Content', 'Sugar Levels']

# Data for fruits in different regions
tropical_scores = [8, 7, 9, 6, 8]
temperate_scores = [6, 8, 7, 7, 6]
mediterranean_scores = [7, 6, 5, 8, 7]

# Closing the radar chart by repeating the first score
tropical_scores += tropical_scores[:1]
temperate_scores += temperate_scores[:1]
mediterranean_scores += mediterranean_scores[:1]

num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.fill(angles, tropical_scores, color='green', alpha=0.25)
ax.fill(angles, temperate_scores, color='purple', alpha=0.25)
ax.fill(angles, mediterranean_scores, color='blue', alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold', ha='center')
ax.set_yticklabels([])

plt.title("Fruit Attributes Comparison Across Different Regions", fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()