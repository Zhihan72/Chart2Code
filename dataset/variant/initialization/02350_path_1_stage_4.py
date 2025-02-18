import matplotlib.pyplot as plt
import numpy as np

fruits = ['Blueberries', 'Bananas', 'Oranges', 'Strawberries', 'Apples']
categories = ['Vitamins', 'Fiber', 'Antioxidants', 'Minerals', 'Natural Sugars']

nutritional_scores = {
    'Blueberries': [10, 5, 9, 4, 6],
    'Bananas': [5, 8, 6, 8, 4],
    'Oranges': [7, 6, 8, 7, 5],
    'Strawberries': [9, 5, 7, 6, 6],
    'Apples': [6, 7, 7, 8, 7]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

shuffled_colors = ['#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#3498db']

# Fill-area radar chart
for idx, (fruit, color) in enumerate(zip(fruits, shuffled_colors)):
    values = nutritional_scores[fruit]
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.4)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.yaxis.grid(False)
ax.set_yticklabels([])
ax.set_ylim(0, 10)
ax.spines['polar'].set_visible(False)

plt.title("Exploring Nutritional Value: \nThe Five Fruit Diet Plan", size=18, fontweight='bold', pad=40)

plt.show()