import matplotlib.pyplot as plt
import numpy as np

categories = ['Sweet', 'Fiber', 'Vit C', 'Water', 'Sugar']
tropical_scores = [8, 7, 9, 6, 8]
temperate_scores = [6, 8, 7, 7, 6]
mediterranean_scores = [7, 6, 5, 8, 7]
continental_scores = [5, 6, 7, 9, 6]
exotic_scores = [9, 5, 8, 7, 9]

# Close the loop by appending the first score to the end
tropical_scores += tropical_scores[:1]
temperate_scores += temperate_scores[:1]
mediterranean_scores += mediterranean_scores[:1]
continental_scores += continental_scores[:1]
exotic_scores += exotic_scores[:1]

num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.fill(angles, tropical_scores, color='blue', alpha=0.2, label='Tropical')
ax.fill(angles, temperate_scores, color='orange', alpha=0.3, label='Temperate')
ax.fill(angles, mediterranean_scores, color='green', alpha=0.2, label='Mediterranean')
ax.fill(angles, continental_scores, color='red', alpha=0.1, label='Continental')
ax.fill(angles, exotic_scores, color='purple', alpha=0.15, label='Exotic')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13, fontweight='normal', ha='center')

ax.set_yticklabels([])

plt.title("Fruit Compare by Region", fontsize=18, fontweight='normal', pad=20)

plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0), fontsize=11, title='Types')

ax.grid(color='grey', linestyle=':', linewidth=0.5)

plt.tight_layout()

plt.show()