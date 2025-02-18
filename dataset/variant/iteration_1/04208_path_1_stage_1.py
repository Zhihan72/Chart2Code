import matplotlib.pyplot as plt
import numpy as np

planets = ['Earth', 'Mars', 'Jupiter', 'Neptune']
food_categories = ['Fruits', 'Vegetables', 'Meat', 'Dairy', 'Grains']
preferences = [
    [30, 25, 20, 15, 10],
    [10, 10, 40, 30, 10],
    [15, 20, 30, 20, 15],
    [20, 30, 20, 10, 20],
]
colors = ['#FFD700', '#32CD32', '#FF6347', '#87CEFA', '#D2B48C']

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
fig.suptitle('Galactic Food Preferences Survey:\nA Study Across Different Planets', fontsize=16, fontweight='bold', y=0.92)

for i, ax in enumerate(axes.flat):
    wedges, _, autotexts = ax.pie(
        preferences[i], autopct='%1.1f%%', startangle=140,
        colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3),
        explode=[0.05 if j == 0 else 0 for j in range(len(food_categories))]
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
        autotext.set_weight('bold')

    ax.set_title(planets[i], fontsize=14, pad=15)

plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()