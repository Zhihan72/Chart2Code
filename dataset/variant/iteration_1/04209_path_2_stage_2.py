import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories
categories = ['Vit', 'Min', 'Prot', 'Fib', 'Sug', 'Cal']
num_vars = len(categories)

# Nutritional scores for each fruit (max score: 10)
fruit_scores = {
    'Appl': [7, 6, 2, 3, 5, 4],
    'Orng': [8, 5, 2, 3, 6, 3],
    'Bnna': [6, 7, 3, 2, 4, 5],
    'Strw': [9, 6, 2, 3, 4, 2],
    'Pnp': [7, 5, 2, 3, 6, 4]
}

# Create a radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Compute angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Add data to the plot
colors = ['#FF6347', '#FFD700', '#32CD32', '#FF1493', '#FFA500']
for idx, (fruit, scores) in enumerate(fruit_scores.items()):
    scores += scores[:1]  # Close the loop
    ax.fill(angles, scores, alpha=0.25, color=colors[idx], label=fruit)

# Add labels and title
plt.xticks(angles[:-1], categories, color='grey', size=12)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Add a legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)
plt.title('Fruit Nutrition', size=20, color='darkred', ha='center')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()