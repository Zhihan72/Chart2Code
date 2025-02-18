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

# Alter styles and markers
ax.plot(angles, tropical_scores, linewidth=3, linestyle='dashed', marker='o', label='Tropical')
ax.fill(angles, tropical_scores, alpha=0.2)

ax.plot(angles, temperate_scores, linewidth=2, linestyle='dashdot', marker='s', label='Temperate')
ax.fill(angles, temperate_scores, alpha=0.3)

ax.plot(angles, mediterranean_scores, linewidth=1.5, linestyle='dotted', marker='^', label='Mediterranean')
ax.fill(angles, mediterranean_scores, alpha=0.2)

ax.plot(angles, continental_scores, linewidth=2.5, linestyle='solid', marker='v', label='Continental')
ax.fill(angles, continental_scores, alpha=0.1)

ax.plot(angles, exotic_scores, linewidth=3, linestyle='dashdot', marker='*', label='Exotic')
ax.fill(angles, exotic_scores, alpha=0.15)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13, fontweight='normal', ha='center')  # Changed font size and weight

ax.set_yticklabels([])

plt.title("Fruit Compare by Region", fontsize=18, fontweight='normal', pad=20)  # Changed font size and weight

plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0), fontsize=11, title='Types')  # Changed position

ax.grid(color='grey', linestyle=':', linewidth=0.5)  # Added grid with styling

plt.tight_layout()

plt.show()