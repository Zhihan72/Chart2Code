import matplotlib.pyplot as plt
import numpy as np

# Define fruits and nutritional categories
fruits = ['Blueberries', 'Bananas', 'Oranges', 'Strawberries', 'Apples']
categories = ['Vitamins', 'Fiber', 'Antioxidants', 'Minerals', 'Natural Sugars']

# Nutritional scores for each fruit
nutritional_scores = {
    'Blueberries': [9, 4, 10, 6, 5],
    'Bananas': [6, 8, 4, 5, 8],
    'Oranges': [8, 5, 7, 6, 7],
    'Strawberries': [7, 6, 9, 5, 6],
    'Apples': [7, 7, 6, 7, 8]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Updated color palette
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f']

for idx, (fruit, color) in enumerate(zip(fruits, colors)):
    values = nutritional_scores[fruit]
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)
    ax.scatter(angles, values, color=color, s=50, zorder=3)

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Remove grid lines and radial axis labels/ticks
ax.yaxis.grid(False)
ax.set_yticklabels([])
ax.set_ylim(0, 10)

# Remove spines
ax.spines['polar'].set_visible(False)

# Title
plt.title("Exploring Nutritional Value: \nThe Five Fruit Diet Plan", size=18, fontweight='bold', pad=40)

# Remove layout adjustment
plt.tight_layout()

# Display the radar chart
plt.show()