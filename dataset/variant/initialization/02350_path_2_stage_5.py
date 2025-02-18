import matplotlib.pyplot as plt
import numpy as np

fruits = ['Blue', 'Ban', 'Oran', 'Appl']
categories = ['Vit', 'Fib', 'Antiox', 'Min', 'Sug']

nutritional_scores = {
    'Blue': [9, 4, 10, 6, 5],
    'Ban': [6, 8, 4, 5, 8],
    'Oran': [8, 5, 7, 6, 7],
    'Appl': [7, 7, 6, 7, 8]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ['#e74c3c', '#2ecc71', '#f1c40f', '#3498db']

for fruit, color in zip(fruits, colors):
    values = nutritional_scores[fruit]
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='navy')

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', size=10)
ax.set_ylim(0, 10)

plt.title("Nutrition Value: Fruit Diet", size=18, fontweight='bold', pad=40)
plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()