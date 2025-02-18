import matplotlib.pyplot as plt
import numpy as np

fruits = ['Berries', 'Banana', 'Orange', 'Strawberry', 'Apple']
categories = ['Vits', 'Fiber', 'Antiox.', 'Minerals', 'Sugars']

nutritional_scores = {
    'Berries': [10, 5, 9, 4, 6],
    'Banana': [5, 8, 6, 8, 4],
    'Orange': [7, 6, 8, 7, 5],
    'Strawberry': [9, 5, 7, 6, 6],
    'Apple': [6, 7, 7, 8, 7]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

shuffled_colors = ['#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#3498db']

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

plt.title("Nutritional Value: Fruit Diet", size=18, fontweight='bold', pad=40)

plt.show()