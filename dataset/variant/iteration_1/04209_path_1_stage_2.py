import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories
categories = ['Vitamins', 'Minerals', 'Proteins', 'Fibers', 'Sugars', 'Calories']
num_vars = len(categories)

# Nutritional scores for each fruit
fruit_scores = {
    'Apple': [7, 6, 2, 3, 5, 4],
    'Orange': [8, 5, 2, 3, 6, 3],
    'Banana': [6, 7, 3, 2, 4, 5],
    'Strawberry': [9, 6, 2, 3, 4, 2],
    'Pineapple': [7, 5, 2, 3, 6, 4],
    'Mango': [8, 6, 3, 2, 5, 3],
    'Blueberry': [9, 7, 4, 3, 3, 2],
    'Kiwi': [8, 5, 3, 4, 6, 3]
}

# Create a radar chart
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))

# Compute angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Add data to the plot
colors = ['#FF6347', '#FFD700', '#32CD32', '#FF1493', '#FFA500', '#20B2AA', '#9370DB', '#FF4500']
for idx, (fruit, scores) in enumerate(fruit_scores.items()):
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

# Remove textual elements
plt.xticks([])
ax.set_yticklabels([])
ax.set_rlabel_position(0)
plt.yticks([])

plt.tight_layout()

plt.show()