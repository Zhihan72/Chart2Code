import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories
categories = ['Vitamins', 'Minerals', 'Proteins', 'Fibers', 'Sugars', 'Calories']
num_vars = len(categories)

# Nutritional scores for each fruit (max score: 10)
fruit_scores = {
    'Apple': [7, 6, 2, 3, 5, 4],
    'Orange': [8, 5, 2, 3, 6, 3],
    'Banana': [6, 7, 3, 2, 4, 5],
    'Strawberry': [9, 6, 2, 3, 4, 2],
    'Pineapple': [7, 5, 2, 3, 6, 4],
    # Added new fruits
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
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=fruit, color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

# Add labels and title
plt.xticks(angles[:-1], categories, color='grey', size=12)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Add a legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)
plt.title('Comparative Nutritional Analysis of Fruits', size=20, color='darkred', ha='center')

plt.tight_layout()

plt.show()